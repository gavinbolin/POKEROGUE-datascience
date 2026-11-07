import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
H="window.__pr_cam.scene.ui.getHandler()"
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
        async def st(k=40):
            for _ in range(k): await ev(STEP); await asyncio.sleep(0.02)
        await ev(HOOK)
        assert await ev(f"{H}.constructor.name")=="TitleUiHandler"
        await ev(f"{H}.setCursor(3)"); await ev(f"{H}.processInput(5)"); await st()
        print(await ev(f"{H}.constructor.name"), await ev(f"JSON.stringify({H}.config?.options?.map(o=>o.label)||{H}.menuOptions)"))
        assert await ev(f"{H}.constructor.name")=="MenuUiHandler"
        await ev(f"{H}.setCursor(4)"); await ev(f"{H}.processInput(5)"); await st(80)
        print(await ev(f"{H}.constructor.name"))
asyncio.run(main())
