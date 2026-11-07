import json,asyncio,websockets,urllib.request,sys,base64,pathlib
KEYS={"z":("z","KeyZ",90),"x":("x","KeyX",88),"up":("ArrowUp","ArrowUp",38),"down":("ArrowDown","ArrowDown",40),"left":("ArrowLeft","ArrowLeft",37),"right":("ArrowRight","ArrowRight",39)}
HOOK=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read().split('HOOK_JS = """')[1].split('"""')[0]
ST="""(()=>{try{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const ph=s.phaseManager?.getCurrentPhase?.();const txt=[];const walk=(o,d)=>{if(!o||d>6)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())txt.push(String(o.text).slice(0,40));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return {h:h?.constructor?.name,cur:h?.cursor,mode:s.ui.getMode?.(),ph:ph?.constructor?.name,gm:window.gameInfo?.gameMode,wave:window.gameInfo?.wave,txt:txt.slice(0,40)}}catch(e){return String(e)}})()"""
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
            if a in ("escape","esc"): raise SystemExit("never escape")
            if a=="st": await call("Page.captureScreenshot",{"format":"jpeg","quality":5,"clip":{"x":0,"y":0,"width":8,"height":8,"scale":1}}); print(json.dumps(await ev(ST)))
            elif a.startswith("shot:"):
                r=await call("Page.captureScreenshot",{"format":"png"});pathlib.Path(a[5:]).write_bytes(base64.b64decode(r["result"]["data"]));print("saved",a[5:])
            elif a.startswith("js:"): print(json.dumps(await ev(a[3:])))
            elif a.startswith("w"): await asyncio.sleep(float(a[1:]))
            else:
                k,c,kc=KEYS[a];d={"type":"keyDown","windowsVirtualKeyCode":kc,"code":c,"key":k}
                if len(k)==1:d["text"]=k
                await call("Input.dispatchKeyEvent",d);await asyncio.sleep(.09);await call("Input.dispatchKeyEvent",{"type":"keyUp","windowsVirtualKeyCode":kc,"code":c,"key":k});await asyncio.sleep(.6)
                for _ in range(3): await call("Page.captureScreenshot",{"format":"jpeg","quality":5,"clip":{"x":0,"y":0,"width":8,"height":8,"scale":1}})
asyncio.run(main())
