import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
H="window.__pr_cam.scene.ui.getHandler()"
PARTY=[int(x) for x in sys.argv[1].split(",")]
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
        async def step(k=15):
            for _ in range(k): await ev(STEP); await asyncio.sleep(0.03)
        async def b(x,k=15):
            assert x!=7
            r=await ev(f"{H}.processInput({x})"); await step(k); return r
        await ev(HOOK)
        nm=await ev(f"{H}.constructor.name"); assert nm=="StarterSelectUiHandler", nm
        for sp in PARTY:
            idx=await ev(f"{H}.filteredStarterIds.indexOf({sp})"); assert idx>=0, sp
            for _ in range(60):
                a=await ev(f"{H}.cursor+{H}.scrollCursor*9")
                if a==idx: break
                r,c=divmod(idx,9); r0,c0=divmod(a,9)
                await b(1 if r>r0 else 0 if r<r0 else 3 if c>c0 else 2,6)
            cur=await ev(f"{H}.filteredStarterIds[{H}.cursor+{H}.scrollCursor*9]")
            if cur!=sp: print("nav fail",sp,cur); continue
            await b(5,20); await b(5,25)
            pl=await ev(f"{H}.partyStarterIds")
            if pl and pl[-1]==sp: print("added",sp)
            else:
                print("could not add",sp,pl, await ev(f"{H}.constructor.name"))
                for _ in range(3):
                    if await ev(f"{H}.constructor.name")=="StarterSelectUiHandler" and not await ev(f"!!{H}.starterSelectCallback===false"): break
                    await b(6,15)
        print("party",await ev(f"{H}.partyStarterIds"))
asyncio.run(main())
