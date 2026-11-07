import json,asyncio,websockets,urllib.request,pathlib,sys
src=open(pathlib.Path(__file__).parent/"pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
E="(()=>{try{const s=window.__pr_cam.scene;const h=s.ui.getHandler();return [h.constructor.name,s.phaseManager.getCurrentPhase().constructor.name,window.gameInfo.wave,s.getPlayerField().map(p=>p.name+':'+p.hp).join(','),s.getEnemyField().map(e=>e.name+':'+e.hp).join(','),(h.message&&h.message.text||'').slice(0,60).replace(/\\n/g,' ')].join('|')}catch(e){return String(e)}})()"
K={'z':('z','KeyZ',90),'x':('x','KeyX',88),'up':('ArrowUp','ArrowUp',38),'down':('ArrowDown','ArrowDown',40),'left':('ArrowLeft','ArrowLeft',37),'right':('ArrowRight','ArrowRight',39)}
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
        for k in sys.argv[1:]:
            k,c,kc=K[k]; d={"type":"keyDown","windowsVirtualKeyCode":kc,"code":c,"key":k}
            if len(k)==1:d["text"]=k
            await call("Input.dispatchKeyEvent",d);await asyncio.sleep(.09)
            await call("Input.dispatchKeyEvent",{"type":"keyUp","windowsVirtualKeyCode":kc,"code":c,"key":k});await asyncio.sleep(1.2)
            print(k,await ev(E),flush=True)
asyncio.run(main())

