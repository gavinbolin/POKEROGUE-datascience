"""Settle post-catch UI after Pansage Gotcha: party full -> storage/No, ack messages, decline learns, stop at SelectModifierPhase."""
import json, asyncio, websockets, urllib.request, os, time, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.chdir(r"C:\Users\gavin\AppData\Local\Temp\prfarm")
src = open("pr_farm17.py", encoding="utf-8").read()
HOOK = src.split('HOOK_JS = """')[1].split('"""')[0]
STEP = src.split('STEP_JS = """')[1].split('"""')[0]
PRE = "const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();"
RD = "(()=>{"+PRE+"""return JSON.stringify({ph:ph&&ph.constructor.name,fi:ph&&ph.fieldIndex,ui:h&&h.constructor.name,cur:h&&h.cursor,
await:!!(h&&h.awaitingActionInput),
party:s.getPlayerParty().map(p=>({n:p.name,sh:p.isShiny(),id:p.species.speciesId,lv:p.level})),
balls:s.pokeballCounts,wave:s.currentBattle&&s.currentBattle.waveIndex,
opts:(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})(),
txt:(()=>{try{const out=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())out.push(String(o.text).replace(/\\n/g,' ').slice(0,80));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return out.slice(0,30)}catch(e){return []}})()
})})()"""
PICK_YES = """(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/^yes$/i.test(t.trim()));if(i<0)i=opts.findIndex(t=>/yes/i.test(t));if(i<0)i=0;h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()"""
PICK_NO = """(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/no|cancel|don't|stop|storage|send/i.test(t));if(i<0)i=Math.min(1,opts.length-1);h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()"""
ACK = """(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();
if(!h||h.constructor.name!=='BattleMessageUiHandler'||!h.awaitingActionInput||(ph&&ph.constructor.name==='CommandPhase'))return 'guard';
return 'a '+h.processInput(5);})()"""

async def connect():
    tabs = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    p = next(x for x in tabs if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    return await websockets.connect(p["webSocketDebuggerUrl"], max_size=50_000_000)

async def main():
    ws = await connect()
    n=[0]
    async def call(method, params=None):
        n[0]+=1
        await ws.send(json.dumps({"id":n[0],"method":method,**({"params":params} if params else {})}))
        while True:
            r=json.loads(await ws.recv())
            if r.get("id")==n[0]: return r
    async def ev(e):
        r=await call("Runtime.evaluate",{"expression":e,"returnByValue":True})
        return ((r.get("result") or {}).get("result") or {}).get("value") or ((r.get("result") or {}).get("exceptionDetails"))
    async def key(k,code,kc,h=90):
        d={"type":"keyDown","windowsVirtualKeyCode":kc,"code":code,"key":k}
        if len(k)==1: d["text"]=k
        await call("Input.dispatchKeyEvent",d); await asyncio.sleep(h/1000)
        await call("Input.dispatchKeyEvent",{"type":"keyUp","windowsVirtualKeyCode":kc,"code":code,"key":k})
    async def X(): await key("x","KeyX",88)
    async def step(k=8):
        for _ in range(k):
            await ev(STEP); await asyncio.sleep(0.02)
    def parse(st):
        if isinstance(st, dict) and "ph" in st: return st
        return json.loads(st)

    await call("Page.bringToFront")
    await ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}})()")
    await ev(HOOK)
    await step(10)

    done = False
    for attempt in range(120):
        await step(4)
        st = parse(await ev(RD))
        ph = st.get("ph") or ""; ui = st.get("ui") or ""
        txt = " ".join(st.get("txt") or [])
        opts = st.get("opts") or []
        low = (" ".join(str(o).lower() for o in opts) + " " + txt.lower())
        t0=((st.get('txt') or [''])[0][:70]).encode('ascii','replace').decode('ascii'); print(f"---{attempt} ph={ph} ui={ui} await={st.get('await')} opts={opts} t0={t0!r}", flush=True)

        if ph == "SelectModifierPhase":
            print("DONE reward"); done=True; break
        if ph in ("TitlePhase", "GameOverPhase"):
            print("ABORT bad phase", ph); break

        if ui in ("OptionSelectUiHandler", "ConfirmUiHandler"):
            print("OPTS", opts, "lowbits", low[:120], flush=True)
            if any(x in low for x in ("add to your party", "add to party", "would you like to add")):
                print("ADD NO party full"); print(await ev(PICK_NO)); await asyncio.sleep(0.4); continue
            if any(x in low for x in ("release", "make room", "storage", "send to", "which pokemon")):
                # Prefer cancel / don't release — send to storage without releasing
                # If it's a release picker with party list, press X/cancel
                if any(x in low for x in ("release a", "make room")) or "release" in low:
                    # try find Cancel/No first
                    r = await ev(PICK_NO)
                    print("RELEASE/NO", r)
                    await asyncio.sleep(0.35)
                    # if still on party select UI, X out
                    await X(); await asyncio.sleep(0.3); continue
            if "learn" in low or "forget" in low or "stop teaching" in low:
                if "stop teaching" in low or ("stop" in low and "learn" in low):
                    await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor(0);return h.processInput(5);})()""")
                else:
                    await ev(PICK_NO)
                await asyncio.sleep(0.4); continue
            if "yes" in low and "no" in low:
                await ev(PICK_NO); await asyncio.sleep(0.35); continue
            if st.get("await"):
                await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();return 'a '+h.processInput(5);})()""")
                await asyncio.sleep(0.3); continue

        if ph == "LearnMovePhase":
            print("LEARN decline")
            if ui == "ConfirmUiHandler":
                await ev(PICK_NO); await asyncio.sleep(0.35); continue
            await X(); await asyncio.sleep(0.3); continue

        if ui == "BattleMessageUiHandler" and st.get("await"):
            await ev(ACK); await asyncio.sleep(0.2); continue

        if ui in ("PartyUiHandler", "PokemonUiHandler"):
            print("PARTY UI - cancel with X"); await X(); await asyncio.sleep(0.35); continue

        await asyncio.sleep(0.15)

    final = parse(await ev(RD))
    # storage check: scan party for Pansage shiny; also poke boxes via scene if available
    party_has = any(p.get("n")=="Pansage" and p.get("sh") for p in (final.get("party") or []))
    box_hit = await ev("""(()=>{try{const s=window.__pr_cam.scene;const sys=s.gameData||s.mysteryEncounter?.scene?.gameData;const gd=s.gameData;const boxes=(gd&&gd.pokemonBoxes)||null;if(!boxes)return JSON.stringify({err:'no boxes'});let hits=[];for(let bi=0;bi<boxes.length;bi++){const b=boxes[bi]||[];for(const p of b){if(!p)continue;if((p.species||p.speciesId)==511||(p.name==='Pansage')||(p.species?.speciesId==511)){hits.push({box:bi,n:p.name||p.species?.name,sh:!!(p.shiny||p.isShiny),lv:p.level,v:p.variant});}}}return JSON.stringify({hits:hits.slice(0,10),nboxes:boxes.length});}catch(e){return JSON.stringify({err:String(e)})}})()""")
    result = {"done": done, "party_has": party_has, "box_hit": box_hit, "final_ph": final.get("ph"), "final_ui": final.get("ui"), "party": final.get("party"), "balls": final.get("balls"), "wave": final.get("wave"), "txt": (final.get("txt") or [])[:8]}
    print("RESULT", result, flush=True)
    open("_settle_pansage_w44_result.txt","w",encoding="utf-8").write(json.dumps(result, indent=1))
    await ws.close()

asyncio.run(main())
