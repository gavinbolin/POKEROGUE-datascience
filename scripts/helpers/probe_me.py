import json,asyncio,websockets,urllib.request
async def m():
    pg=next(p for p in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if p.get("type")=="page" and p["url"].startswith("https://pokerogue.net"))
    async with websockets.connect(pg["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        async def ev(e):
            await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==1: return r.get("result",{}).get("value", r)
        for i in range(8):
            r=await ev("""(()=>{const s=window.__pr_cam.scene,h=s.ui.getHandler();const me=s.currentBattle.mysteryEncounter;
            return {h:h.constructor.name,cur:h.cursor,mode:s.ui.mode,opts:(h.config&&h.config.options||[]).map(o=>o.label),
            me:me&&{type:me.encounterType,key:me.localizationKey,sel:me.selectedOption&&me.options.indexOf(me.selectedOption)},
            ph:s.phaseManager?.getCurrentPhase?.()?.constructor?.name, msg:s.ui.getMessageHandler?.()?.message?.text}})()""")
            print(json.dumps(r)); await asyncio.sleep(0.4)
asyncio.run(m())

