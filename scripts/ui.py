import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
H="window.__pr_cam.scene.ui.getHandler()"
CMDS=sys.argv[1:]
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
        await ev(HOOK)
        RD=f"(()=>{{const h={H};return {{n:h.constructor.name,c:h.cursor,o:h.config?.options?.map(o=>o.label),pt:h.partyStarterIds}}}})()"
        for c in CMDS:
            if c.startswith("c"): await ev(f"{H}.setCursor({int(c[1:])})")
            elif c.startswith("b"):
                k=int(c[1:]); assert k!=7; await ev(f"{H}.processInput({k})")
            elif c.startswith("e:"): print(json.dumps(await ev(c[2:])))
            for _ in range(40): await ev(STEP); await asyncio.sleep(0.02)
            print(c,json.dumps(await ev(RD)),flush=True)
asyncio.run(main())
