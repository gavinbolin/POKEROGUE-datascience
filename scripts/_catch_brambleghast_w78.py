"""Doubles wild shiny Brambleghast w78: KO Darmanitan partner, then Rogue>Ultra>Great>Poke. Never Master. Never hit shiny."""
import json, asyncio, websockets, urllib.request, os, time
os.chdir(r"C:\Users\gavin\AppData\Local\Temp\prfarm")
src = open("pr_farm17.py", encoding="utf-8").read()
HOOK = src.split('HOOK_JS = """')[1].split('"""')[0]
STEP = src.split('STEP_JS = """')[1].split('"""')[0]
PRE = "const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();"
RD = "(()=>{"+PRE+"""return JSON.stringify({ph:ph&&ph.constructor.name,fi:ph&&ph.fieldIndex,ui:h&&h.constructor.name,cur:h&&h.cursor,
await:!!(h&&h.awaitingActionInput),
en:s.getEnemyField().map(p=>({n:p.name,sh:p.isShiny(),hp:p.hp,mx:p.getMaxHp(),f:p.isFainted(),lv:p.level,v:p.variant??null,id:p.species.speciesId,bi:p.getBattlerIndex(),boss:p.isBoss(),seg:p.bossSegmentIndex})),
pl:s.getPlayerField().map(p=>({n:p.name,hp:p.hp,mx:p.getMaxHp(),mv:p.getMoveset().map(m=>m.getName())})),
party:s.getPlayerParty().map(p=>({n:p.name,hp:p.hp,mx:p.getMaxHp(),on:p.isOnField(),sh:p.isShiny(),id:p.species.speciesId,lv:p.level,f:p.isFainted()})),
balls:s.pokeballCounts,wave:s.currentBattle&&s.currentBattle.waveIndex,
opts:(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})(),
txt:(()=>{try{const out=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())out.push(String(o.text).replace(/\\n/g,' ').slice(0,60));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return out.slice(0,30)}catch(e){return []}})()
})})()"""
WAVE=78; SHINY="Brambleghast"; PARTNER="Darmanitan"; SID=947
BALL_NAMES={0:"Poke Ball",1:"Great Ball",2:"Ultra Ball",3:"Rogue Ball",4:"Master Ball"}

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

    st = parse(await ev(RD))
    print("BASE", json.dumps(st), flush=True)
    if st.get("wave") != WAVE:
        print("ABORT wave", st.get("wave")); return
    en = st.get("en") or []
    shiny = next((e for e in en if e.get("sh") and e.get("n")==SHINY and not e.get("f")), None)
    partner = next((e for e in en if e.get("n")==PARTNER and not e.get("f")), None)
    if not shiny:
        print("ABORT no shiny", en); return
    if shiny.get("id") != SID:
        print("ABORT sid", shiny.get("id")); return
    if st.get("ph") != "CommandPhase" or st.get("ui") != "CommandUiHandler":
        print("ABORT not command", st.get("ph"), st.get("ui")); return
    balls0 = dict(st.get("balls") or {})
    shiny_hp0 = shiny.get("hp")
    party_hp0 = [(p.get("n"), p.get("hp")) for p in (st.get("party") or [])]
    print("balls", balls0, "shiny_hp", shiny_hp0, "partner_hp", partner and partner.get("hp"), "variant_raw", shiny.get("v"), "party_hp", party_hp0, flush=True)
    my_actions = 0
    caught = False
    missed = False
    ball_used = None

    def partner_alive(s):
        return any(e.get("n")==PARTNER and not e.get("f") and e.get("hp",0)>0 for e in (s.get("en") or []))
    def shiny_alive(s):
        return any(e.get("sh") and e.get("n")==SHINY and not e.get("f") and e.get("hp",0)>0 for e in (s.get("en") or []))
    def only_shiny(s):
        alive = [e for e in (s.get("en") or []) if not e.get("f") and e.get("hp",0)>0]
        return len(alive)==1 and alive[0].get("sh") and alive[0].get("n")==SHINY

    for attempt in range(180):
        await step(6)
        st = parse(await ev(RD))
        en2 = st.get("en") or []
        ph = st.get("ph") or ""; ui = st.get("ui") or ""; fi = st.get("fi")
        txt = " ".join(st.get("txt") or [])
        print(f"---{attempt} ph={ph} fi={fi} ui={ui} en={[(e.get('n'),e.get('hp'),e.get('sh'),e.get('f')) for e in en2]} balls={st.get('balls')} cur={st.get('cur')} t0={(st.get('txt') or [''])[0][:50]!r}", flush=True)

        if st.get("wave") != WAVE:
            if caught or not shiny_alive(st):
                caught = True; print("wave advanced"); break
            print("ABORT wave changed", st.get("wave")); return

        if "Gotcha" in txt or "was caught" in txt.lower():
            caught = True; print("CAUGHT_TXT", txt[:120], flush=True)

        sh = next((e for e in en2 if e.get("n")==SHINY), None)
        if sh and sh.get("f"):
            missed = True; print("SHINY FAINTED"); break
        if sh and shiny_hp0 and sh.get("hp") is not None and sh.get("hp") < shiny_hp0:
            print("ABORT shiny HP dropped (other input or mis-target)", sh.get("hp"), "vs", shiny_hp0); return

        if ph == "LearnMovePhase":
            print("LEARN decline");
            if ui == "ConfirmUiHandler":
                await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/no|cancel|don't|stop/i.test(t));if(i<0)i=Math.min(1,opts.length-1);h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()""")
                await asyncio.sleep(0.35); continue
            await X(); await asyncio.sleep(0.3); continue

        if ui in ("OptionSelectUiHandler", "ConfirmUiHandler"):
            opts = st.get("opts") or []
            low = " ".join(str(o).lower() for o in opts) + " " + txt.lower()
            print("OPTS", opts, flush=True)
            if any(x in low for x in ("add","party","full","release","make room")) or (caught and ui=="OptionSelectUiHandler") or "learn" in low or "forget" in low:
                if "stop teaching" in low or ("stop" in low and "learn" in low):
                    await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor(0);return h.processInput(5);})()""")
                else:
                    # party full -> No (storage)
                    await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/no/i.test(t));if(i<0)i=Math.min(1,opts.length-1);h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()""")
                await asyncio.sleep(0.4); continue
            if "yes" in low and caught:
                await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/no/i.test(t));if(i<0)i=0;h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()""")
                await asyncio.sleep(0.4); continue
            if st.get("await") and caught:
                await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();return 'a '+h.processInput(5);})()""")
                await asyncio.sleep(0.3); continue

        if ui == "BattleMessageUiHandler" and st.get("await"):
            await ev("""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();if(!h||h.constructor.name!=='BattleMessageUiHandler'||!h.awaitingActionInput||(ph&&ph.constructor.name==='CommandPhase'))return 'guard';return 'a '+h.processInput(5);})()""")
            await asyncio.sleep(0.2); continue

        if ph == "SelectModifierPhase":
            if caught:
                print("REWARD after catch - done"); break
            print("unexpected reward"); break

        if ui == "TargetSelectUiHandler":
            bi = None
            for e in en2:
                if e.get("n")==PARTNER and not e.get("f"):
                    bi = e.get("bi"); break
            if bi is None:
                print("ABORT target select with no partner - cancel with X"); await X(); await asyncio.sleep(0.3); continue
            r = await ev(f"""(()=>{{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const e=s.getField()[{bi}];if(!e||e.isShiny()||e.name==='{SHINY}')return 'target shiny/bramble';if(h.cursor!=={bi})h.setCursor({bi});if(h.cursor!=={bi})return 'cursor '+h.cursor;return 'ok '+e.name+' '+h.processInput(5);}})()""")
            print("TGT", r, flush=True); my_actions += 1; await asyncio.sleep(0.35); continue

        if ph == "CommandPhase" and ui == "CommandUiHandler":
            if not shiny_alive(st):
                if caught: break
                missed = True; print("shiny gone without catch"); break

            bnow = st.get("balls") or {}
            def bc(d,k):
                return int((d.get(str(k)) if str(k) in d else d.get(k, 0)) or 0)
            if bc(bnow,4) < bc(balls0,4):
                print("ABORT Master Ball used by someone else"); return

            if partner_alive(st):
                if fi == 0:
                    # Rayquaza: Hyper Voice / Core Enforcer / Air Slash vs Darmanitan (never hit shiny)
                    r = await ev("""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());if(!ph||ph.constructor.name!=='CommandPhase'||ph.fieldIndex!==0)return 'bad phase';const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());if(!en.some(p=>p.isShiny()&&p.name==='Brambleghast'))return 'no shiny';if(!en.some(p=>p.name==='Darmanitan'&&!p.isFainted()))return 'no partner';const ms=s.getPlayerField()[0].getMoveset();const prefer=['Hyper Voice','Core Enforcer','Air Slash','V-create'];let idx=-1;for(const name of prefer){const i=ms.findIndex(m=>m&&m.getName()===name&&(m.ppUsed||0)<(m.getMovePp?.()||99));if(i>=0){idx=i;break}}if(idx<0)return 'no move '+ms.map(m=>m&&m.getName());const m=ms[idx];if(/Earthquake/i.test(m.getName()))return 'blocked '+m.getName();return 'mv '+m.getName()+' '+ph.handleCommand(0,idx);})()""")
                    print("MV0", r, flush=True); my_actions += 1; await asyncio.sleep(0.35); continue
                elif fi == 1:
                    party = st.get("party") or []
                    sw_i = None
                    for i,p in enumerate(party):
                        if not p.get("on") and not p.get("f") and p.get("hp",0)>0:
                            sw_i = i; break
                    if sw_i is None:
                        # Kadabra: no reliable status; try switch failed - use weakest? Prefer Ice Beam only if somehow alone; abort safer: switch attempt
                        r = await ev("""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());if(!ph||ph.constructor.name!=='CommandPhase'||ph.fieldIndex!==1)return 'bad phase';const ms=s.getPlayerField()[1].getMoveset();return 'no bench '+ms.map(m=>m&&m.getName());})()""")
                        print("NOBENCH1", r, flush=True); await asyncio.sleep(0.3); continue
                    r = await ev(f"""(()=>{{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());if(!ph||ph.constructor.name!=='CommandPhase'||ph.fieldIndex!==1)return 'bad phase';const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());if(!en.some(p=>p.isShiny()))return 'no shiny';const t=s.getPlayerParty()[{sw_i}];if(!t||t.isFainted()||t.isOnField())return 'bad target';return 'sw '+t.name+' '+ph.handleCommand(2,{sw_i},false);}})()""")
                    print("SW1", r, flush=True); my_actions += 1; await asyncio.sleep(0.35); continue
                else:
                    print("unexpected fi", fi); await asyncio.sleep(0.3); continue

            if only_shiny(st) or (shiny_alive(st) and not partner_alive(st)):
                r = await ev("""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());
if(!ph||ph.constructor.name!=='CommandPhase')return 'phase '+(ph&&ph.constructor.name);
const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());
if(!en.length||!en.some(p=>p.name==='Brambleghast'&&p.isShiny()))return 'enemy '+JSON.stringify(en.map(p=>p.name+':'+p.isShiny()+':'+p.hp));
if(s.currentBattle.waveIndex!==78)return 'wave '+s.currentBattle.waveIndex;
const b=[3,2,1,0].find(k=>(s.pokeballCounts[k]||0)>0);
if(b===undefined)return 'no ball';
if(b===4)return 'no master';
return 'b'+b+' '+ph.handleCommand(1,b);
})()""")
                print("BALL", r, "fi", fi, flush=True)
                if isinstance(r, str) and r.startswith("b"):
                    bi = int(r[1]); ball_used = BALL_NAMES.get(bi, str(bi)); my_actions += 1
                if r == "no ball":
                    missed = True; print("OUT_OF_BALLS"); break
                await asyncio.sleep(0.5); continue

        if ui in ("FightUiHandler", "BallUiHandler"):
            print("BAD_UI", ui, "backing out", flush=True)
            await X(); await asyncio.sleep(0.3); continue

        await asyncio.sleep(0.15)

    final = parse(await ev(RD))
    print("FINAL", json.dumps(final), flush=True)
    print("RESULT", {"caught": caught, "missed": missed, "ball": ball_used, "my_actions": my_actions, "variant_raw": (shiny or {}).get("v")}, flush=True)
    await ws.close()

asyncio.run(main())
