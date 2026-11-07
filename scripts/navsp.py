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
        async def press(b,f=25):
            await ev(f"{H}.processInput({b})")
            for _ in range(f): await ev(STEP); await asyncio.sleep(0.02)
        await ev(HOOK)
        sp=int(sys.argv[1])
        for _ in range(3):
            idx=await ev(f"{H}.filteredStarterIds.indexOf({sp})"); a=await ev(f"{H}.cursor+{H}.scrollCursor*9")
            if idx<0: print("not found");return
            r,c=divmod(idx,9); r0,c0=divmod(a,9)
            for _ in range(abs(r-r0)): await press(1 if r>r0 else 0)
            for _ in range(abs(c-c0)): await press(3 if c>c0 else 2)
            cur=await ev(f"{H}.filteredStarterIds[{H}.cursor+{H}.scrollCursor*9]")
            if cur==sp: print("on",sp);return
        print("nav fail",cur)
asyncio.run(main())
