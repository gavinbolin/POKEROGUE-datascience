import json, asyncio, websockets, urllib.request, os
os.chdir(r"C:\Users\gavin\AppData\Local\Temp\prfarm")
src = open("pr_farm17.py", encoding="utf-8").read()
HOOK = src.split('HOOK_JS = """')[1].split('"""')[0]
STEP = src.split('STEP_JS = """')[1].split('"""')[0]

async def main():
    tabs = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    p = next(x for x in tabs if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    ws = await websockets.connect(p["webSocketDebuggerUrl"], max_size=50_000_000)
    n=[0]
    async def call(method, params=None):
        n[0]+=1
        await ws.send(json.dumps({"id":n[0],"method":method,**({"params":params} if params else {})}))
        while True:
            r=json.loads(await ws.recv())
            if r.get("id")==n[0]: return r
    async def ev(e):
        r=await call("Runtime.evaluate",{"expression":e,"returnByValue":True})
        return ((r.get("result") or {}).get("result") or {}).get("value")
    await call("Page.bringToFront")
    await ev(HOOK)
    for i in range(50):
        for _ in range(6):
            await ev(STEP); await asyncio.sleep(0.02)
        st = await ev("""(()=>{try{const s=window.__pr_cam.scene;const ph=s.phaseManager?.getCurrentPhase?.();const h=s.ui?.getHandler?.();const txt=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())txt.push(String(o.text).replace(/\\n/g,' ').slice(0,70));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);let opts=[];try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);opts=t.map(x=>x.t)}catch(e){}return {ph:ph&&ph.constructor.name,ui:h&&h.constructor.name,await:!!(h&&h.awaitingActionInput),wave:s.currentBattle&&s.currentBattle.waveIndex,t0:txt[0]||'',opts};}catch(e){return String(e)}})()""")
        print(i, st, flush=True)
        if not isinstance(st, dict):
            await asyncio.sleep(0.2); continue
        ph, ui = st.get("ph"), st.get("ui")
        if ph in ("SelectModifierPhase", "CommandPhase") or (ph and "Title" in ph):
            print("STOP_AT", st); break
        if ui in ("OptionSelectUiHandler", "ConfirmUiHandler"):
            r = await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();const opts=(()=>{try{const c=h.optionsContainer;const t=c.list.filter(x=>x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})();let i=opts.findIndex(t=>/no|cancel|don't|stop/i.test(t));if(i<0)i=Math.min(1,Math.max(0,opts.length-1));h.setCursor(i);return JSON.stringify({opts,i,r:h.processInput(5)});})()""")
            print("CLICK", r, flush=True); await asyncio.sleep(0.35); continue
        if ui == "BattleMessageUiHandler" and st.get("await"):
            await ev("""(()=>{const h=window.__pr_cam.scene.ui.getHandler();if(h&&h.awaitingActionInput)return 'a '+h.processInput(5);return 'no';})()""")
            await asyncio.sleep(0.2); continue
        await asyncio.sleep(0.12)
    final = await ev("""(()=>{try{const s=window.__pr_cam.scene;const party=s.getPlayerParty().map(p=>({n:p.name,id:p.species.speciesId,sh:!!p.isShiny(),lv:p.level,hp:p.hp,mx:p.getMaxHp(),ball:p.pokeball}));const d=s.gameData.dexData[947]||null;const boxes=[];try{const bs=s.gameData.boxes||s.gameData.pokemonBoxes||[];for(const box of (bs||[])){for(const p of (box||[])){if(p&&p.species&&p.species.speciesId===947)boxes.push({n:p.name||'Brambleghast',sh:!!p.shiny,lv:p.level,ball:p.pokeball})}}}catch(e){boxes.push('err:'+e)}return {ph:s.phaseManager.getCurrentPhase().constructor.name,wave:s.currentBattle&&s.currentBattle.waveIndex,party,dex947:d,boxes,balls:s.pokeballCounts};}catch(e){return String(e)}})()""")
    print("FINAL", json.dumps(final), flush=True)
    await ws.close()

asyncio.run(main())
