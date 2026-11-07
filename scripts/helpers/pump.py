import json,asyncio,websockets,urllib.request,pathlib
HOOK=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read().split('HOOK_JS = """')[1].split('"""')[0]
E="(()=>{const s=window.__pr_cam.scene;const ph=s.phaseManager.getCurrentPhase();return [s.ui.getHandler().constructor.name,ph.constructor.name,window.gameInfo.wave,s.getEnemyParty().map(e=>e.name+':'+e.hp)].join('|')})()"
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def call(m,pr=None):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":m,**({"params":pr} if pr else {})}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r
        await call("Runtime.evaluate",{"expression":HOOK})
        last=None
        for i in range(400):
            await call("Page.captureScreenshot",{"format":"jpeg","quality":5,"clip":{"x":0,"y":0,"width":8,"height":8,"scale":1}})
            if i%10==0:
                r=await call("Runtime.evaluate",{"expression":E,"returnByValue":True}); v=r["result"]["result"].get("value")
                if v!=last: print(i,v,flush=True); last=v
                if v and not v.split('|')[1].startswith(("AttemptCapture","BattleMessage")) and i>20 and ("Command" in v or "Confirm" in v or "Party" in v or "Option" in v or "Message" in v.split('|')[0] and False): break
asyncio.run(main())
