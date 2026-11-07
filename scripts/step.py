import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
E="(()=>{const s=window.__pr_cam.scene;const ph=s.phaseManager.getCurrentPhase();return [s.ui.getHandler().constructor.name,ph.constructor.name,window.gameInfo.wave,s.getEnemyParty().map(e=>e.name+':'+e.hp).join(','),s.getPlayerParty().length].join('|')})()"
STOPAT=sys.argv[1].split(',') if len(sys.argv)>1 else ["CommandUiHandler"]
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
        await ev(HOOK); last=None
        for i in range(150):
            await ev(STEP); await asyncio.sleep(0.05)
            v=await ev(E)
            if v!=last: print(i,v,flush=True); last=v
            if v and v.split('|')[0] in STOPAT: break
asyncio.run(main())
