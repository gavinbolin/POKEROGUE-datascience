import json,asyncio,websockets,urllib.request,sys
async def m():
    pg=next(p for p in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if p.get("type")=="page" and p["url"].startswith("https://pokerogue.net"))
    async with websockets.connect(pg["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        async def ev(e):
            await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==1: return r
        await ev("""(()=>{if(window.__prSM)return 1;const P=Phaser.Scenes.SceneManager.prototype;const o=P.update;P.update=function(...a){window.__prSM=this;return o.apply(this,a)};return 0})()""")
        await asyncio.sleep(1)
        r=await ev(open(sys.argv[1]).read())
        print(json.dumps(r.get("result",{}).get("result",{}).get("value"),indent=1)[:6000] if "result" in r else r)
asyncio.run(m())
