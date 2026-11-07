import json,asyncio,websockets,urllib.request,pathlib,sys,time
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
RD="""(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();return {h:h.constructor.name,g:h.gachaCursor,c:h.cursor,v:s.gameData.voucherCounts,e:s.gameData.eggs.length,tr:!!h.transitioning}})()"""
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def call(m,pr=None):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":m,**({"params":pr} if pr else {})}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r
        async def ev(e):
            r=await call("Runtime.evaluate",{"expression":e,"returnByValue":True});return r.get("result",{}).get("result",{}).get("value")
        async def step(k):
            for _ in range(k): await ev(STEP); await asyncio.sleep(0.02)
        await ev(HOOK)
        for it in range(80):
            s=await ev(RD); print(it,json.dumps(s),flush=True)
            if s["h"]!="EggGachaUiHandler": print("not gacha, stop");break
            v=s["v"]
            if v["0"]+v["1"]+v["2"]+v["3"]==0: print("all spent");break
            if s["g"]!=2: await ev("window.__pr_cam.scene.ui.getHandler().setGachaCursor(2)"); await step(60); continue
            c=1 if v["0"]>=10 else 0 if v["0"]>=1 else 2 if v["1"]>=1 else 3 if v["2"]>=1 else 4
            await ev(f"window.__pr_cam.scene.ui.getHandler().setCursor({c})")
            r=await ev("window.__pr_cam.scene.ui.getHandler().processInput(5)"); await step(400)
            s2=await ev(RD)
            if s2["v"]==v:
                await ev("window.__pr_cam.scene.ui.getHandler().processInput(5)"); await step(400)
        print("FINAL",json.dumps(await ev(RD)),flush=True)
asyncio.run(main())
