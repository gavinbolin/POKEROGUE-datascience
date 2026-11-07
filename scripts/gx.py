import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
ST="""(()=>{try{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const ph=s.phaseManager?.getCurrentPhase?.();const txt=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())txt.push(String(o.text).replace(/\\n/g,' ').slice(0,50));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return {h:h?.constructor?.name,cur:h?.cursor,mode:s.ui.getMode?.(),ph:ph?.constructor?.name,txt:txt.slice(0,45)}}catch(e){return String(e)}})()"""
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
        for a in sys.argv[1:]:
            if a=="st": print(json.dumps(await ev(ST)),flush=True)
            elif a.startswith("p:"):
                b=int(a[2:]); assert b!=7, "no menu"
                print("p",b,json.dumps(await ev(f"(()=>{{try{{return window.__pr_cam.scene.ui.getHandler().processInput({b})}}catch(e){{return String(e)}}}})()")),flush=True)
            elif a.startswith("s:"):
                for _ in range(int(a[2:])): await ev(STEP); await asyncio.sleep(0.03)
            elif a.startswith("js:"): print(json.dumps(await ev(a[3:])),flush=True)
            elif a.startswith("w"): await asyncio.sleep(float(a[1:]))
asyncio.run(main())
