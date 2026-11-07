import json,asyncio,websockets,urllib.request
async def m():
    pg=next(p for p in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if p.get("type")=="page" and p["url"].startswith("https://pokerogue.net"))
    async with websockets.connect(pg["webSocketDebuggerUrl"]) as ws:
        i=0
        async def c(m,p=None):
            nonlocal i;i+=1;await ws.send(json.dumps({"id":i,"method":m,"params":p or {}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==i: return r
        print(await c("Browser.getWindowForTarget"))
        print(await c("Page.bringToFront"))
        await asyncio.sleep(1)
        print(await c("Runtime.evaluate",{"expression":"document.visibilityState","returnByValue":True}))
asyncio.run(m())
