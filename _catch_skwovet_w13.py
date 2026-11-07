"""Catch wild shiny Skwovet w13 singles. Rogue>Ultra>Great>Poke. Never Master. No attack (Lv9 no shield). Party full -> No/storage."""
import json, asyncio, websockets, urllib.request, os, time
os.chdir(r"C:\Users\gavin\AppData\Local\Temp\prfarm")
src = open("pr_farm17.py", encoding="utf-8").read()
HOOK = src.split('HOOK_JS = """')[1].split('"""')[0]
STEP = src.split('STEP_JS = """')[1].split('"""')[0]
PRE = "const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();"
RD = "(()=>{"+PRE+"""return JSON.stringify({ph:ph&&ph.constructor.name,fi:ph&&ph.fieldIndex,ui:h&&h.constructor.name,cur:h&&h.cursor,
await:!!(h&&h.awaitingActionInput),
en:s.getEnemyField().map(p=>({n:p.name,sh:p.isShiny(),hp:p.hp,mx:p.getMaxHp(),f:p.isFainted(),lv:p.level,v:p.variant??null,id:p.species.speciesId})),
pl:s.getPlayerField().map(p=>({n:p.name,hp:p.hp,mx:p.getMaxHp()})),
party:s.getPlayerParty().map(p=>({n:p.name,hp:p.hp,mx:p.getMaxHp(),on:p.isOnField(),sh:p.isShiny(),id:p.species.speciesId,lv:p.level})),
balls:s.pokeballCounts,wave:s.currentBattle&&s.currentBattle.waveIndex,
opts:(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})(),
txt:(()=>{try{const out=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())out.push(String(o.text).replace(/\\n/g,' ').slice(0,60));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return out.slice(0,30)}catch(e){return []}})()
})})()"""
THROW = """(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());
if(!ph||ph.constructor.name!=='CommandPhase')return 'phase '+(ph&&ph.constructor.name);
const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());
if(en.length!==1||en[0].name!=='Skwovet'||!en[0].isShiny())return 'enemy '+JSON.stringify(en.map(p=>p.name+':'+p.isShiny()));
if(s.currentBattle.waveIndex!==13)return 'wave '+s.currentBattle.waveIndex;
const b=[3,2,1,0].find(k=>(s.pokeballCounts[k]||0)>0);
if(b===undefined)return 'no ball';
if(b===4)return 'no master';
return 'b'+b+' '+ph.handleCommand(1,b);
})()"""
PARTY_NO = """(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const n=h.constructor.name;
if(n!=='OptionSelectUiHandler'&&n!=='ConfirmUiHandler')return JSON.stringify({n});
const opts=(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();
let i=opts.findIndex(t=>/no/i.test(t));
if(i<0)i=Math.min(1,opts.length-1);
h.setCursor(i);const r=h.processInput(5);return JSON.stringify({n,opts,i,cur:h.cursor,r});
})()"""
ACK = """(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();
if(!h||h.constructor.name!=='BattleMessageUiHandler'||!h.awaitingActionInput||(ph&&ph.constructor.name==='CommandPhase'))return 'guard';
return 'a '+h.processInput(5);})()"""
WAVE=13; SHINY="Skwovet"
BALL_NAMES={0:"Poké Ball",1:"Great Ball",2:"Ultra Ball",3:"Rogue Ball",4:"Master Ball"}

async def connect():
    tabs = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    p = next(x for x in tabs if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    return await websockets.connect(p["webSocketDebuggerUrl"], max_size=50_000_000)

async def main():
    ws = await connect()
    n = [0]
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
        if isinstance(st, dict): return st
        return json.loads(st)

    await call("Page.bringToFront")
    await ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}})()")
    await ev(HOOK)
    await step(15)

    baseline = parse(await ev(RD))
    print("BASE", json.dumps(baseline, indent=1), flush=True)
    if baseline.get("wave") != WAVE:
        print("ABORT wave", baseline.get("wave")); return
    en = baseline.get("en") or []
    if not en or not en[0].get("sh") or en[0].get("n") != SHINY:
        print("ABORT shiny gone/changed", en); return
    if baseline.get("ph") != "CommandPhase" or baseline.get("ui") != "CommandUiHandler":
        print("ABORT not command menu", baseline.get("ph"), baseline.get("ui")); return
    balls0 = dict(baseline.get("balls") or {})
    hp0 = en[0].get("hp")
    party_len = len(baseline.get("party") or [])
    print("balls", balls0, "hp0", hp0, "party_len", party_len, flush=True)
    caught = False
    missed = False
    ball_used = None
    my_throws = 0

    for attempt in range(80):
        await step(6)
        st = parse(await ev(RD))
        en2 = st.get("en") or []
        print(f"---{attempt} ph={st.get('ph')} ui={st.get('ui')} en={[(e.get('n'),e.get('hp'),e.get('sh'),e.get('f')) for e in en2]} balls={st.get('balls')} t0={(st.get('txt') or [''])[0][:50]!r}", flush=True)
        if st.get("wave") != WAVE:
            if caught or (not any(e.get("sh") and e.get("n")==SHINY and not e.get("f") for e in en2)):
                caught = True; print("wave advanced after catch"); break
            print("ABORT wave changed mid-catch", st.get("wave")); return
        ph = st.get("ph") or ""
        ui = st.get("ui") or ""
        txt = " ".join(st.get("txt") or [])
        if "Gotcha" in txt or "was caught" in txt.lower():
            caught = True
            print("CAUGHT_TXT", txt[:120], flush=True)
        if ph == "LearnMovePhase":
            print("LEARN decline X/No", flush=True)
            if ui == "ConfirmUiHandler":
                await ev(PARTY_NO); await asyncio.sleep(0.35); continue
            await X(); await asyncio.sleep(0.3); continue
        if ui in ("OptionSelectUiHandler", "ConfirmUiHandler"):
            opts = st.get("opts") or []
            low = " ".join(str(o).lower() for o in opts) + " " + txt.lower()
            print("OPTS", opts, "low", low[:100], flush=True)
            if any(x in low for x in ("add","party","full","release","make room")) or (caught and ui=="OptionSelectUiHandler") or "learn" in low or "forget" in low or "stop teaching" in low:
                if "stop teaching" in low or ("stop" in low and "learn" in low):
                    await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor(0);return h.processInput(5);})()""")
                else:
                    print("PARTY_NO", await ev(PARTY_NO), flush=True)
                await asyncio.sleep(0.45); continue
            if caught:
                await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor(0);return h.processInput(5);})()""")
                await asyncio.sleep(0.4); continue
            print("UNEXPECTED confirm before catch - STOP", flush=True); return
        if ui == "BattleMessageUiHandler" and st.get("await"):
            print("ACK", await ev(ACK), flush=True)
            await asyncio.sleep(0.25); continue
        if ui in ("SummaryUiHandler", "PartyUiHandler"):
            print("UI", ui, "X"); await X(); await asyncio.sleep(0.3); continue
        shiny_alive = [e for e in en2 if e.get("sh") and e.get("n")==SHINY and not e.get("f") and (e.get("hp") or 0) > 0]
        if ph in ("SelectModifierPhase", "EggLapsePhase", "EncounterPhase", "SwitchBiomePhase", "TurnInitPhase", "PostSummonPhase", "NextEncounterPhase", "PartyHealPhase"):
            if not shiny_alive:
                caught = True; print("POST_BATTLE", ph, flush=True); break
        if ph == "CommandPhase" and ui == "CommandUiHandler":
            bnow = st.get("balls") or {}
            def bc(d,k):
                return int((d.get(str(k)) if str(k) in d else d.get(k, 0)) or 0)
            if bc(bnow,4) < bc(balls0,4):
                print("ABORT Master Ball used by someone else"); return
            if en2 and hp0 is not None and en2[0].get("hp", hp0) < hp0:
                print("ABORT HP dropped (other controller)", en2[0].get("hp"), "vs", hp0); return
            r = await ev(THROW)
            print("THROW", r, flush=True)
            if isinstance(r, str) and r.startswith("b"):
                try: ball_used = int(r[1]); my_throws += 1
                except: pass
            if r == "no ball":
                missed = True; print("OUT_OF_BALLS"); break
            if isinstance(r, str) and (r.startswith("enemy") or r.startswith("wave") or r.startswith("phase")):
                print("CHANGED", r)
                if r.startswith("wave"): return
                break
            await asyncio.sleep(0.7); continue
        if ui in ("FightUiHandler", "TargetSelectUiHandler", "BallUiHandler"):
            print("BAD_UI", ui, "backing out", flush=True)
            cancel = """(()=>{const h=window.__pr_cam.scene.ui.getHandler(); try{return h.processInput(1)}catch(e){return String(e)}})()"""
            print("CANCEL", await ev(cancel), flush=True)
            await X(); await asyncio.sleep(0.3); continue
        await ev(STEP); await asyncio.sleep(0.2)

    final = parse(await ev(RD))
    print("FINAL", json.dumps(final, indent=1), flush=True)
    en_f = final.get("en") or []
    shiny_left = [e for e in en_f if e.get("sh") and e.get("n")==SHINY and not e.get("f") and (e.get("hp") or 0)>0]
    bname = BALL_NAMES.get(ball_used, str(ball_used))
    if caught or (not shiny_left and final.get("ph") in ("SelectModifierPhase","EggLapsePhase","EncounterPhase","NextEncounterPhase","SwitchBiomePhase","PartyHealPhase")):
        print("RESULT Caught ball_used=", ball_used, bname, "throws=", my_throws, flush=True)
    elif missed or (shiny_left and final.get("ph")=="CommandPhase"):
        print("RESULT Missed ball_used=", ball_used, bname, "throws=", my_throws, flush=True)
    else:
        print("RESULT Unknown shiny_left=", shiny_left, "ph=", final.get("ph"), "ball=", ball_used, bname, flush=True)
    await ws.close()

asyncio.run(main())
