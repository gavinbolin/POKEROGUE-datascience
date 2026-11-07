import json,asyncio,websockets,urllib.request,sys,base64,pathlib
async def m():
    pg=next(p for p in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if p.get("type")=="page" and p["url"].startswith("https://pokerogue.net"))
    async with websockets.connect(pg["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        await ws.send(json.dumps({"id":1,"method":"Page.captureScreenshot","params":{"format":"png"}}))
        while True:
            r=json.loads(await ws.recv())
            if r.get("id")==1: break
        d=pathlib.Path(r"C:\Users\gavin\agent-tools\prframes"); d.mkdir(exist_ok=True)
        (d/(sys.argv[1]+".png")).write_bytes(base64.b64decode(r["result"]["data"])); print("ok")
asyncio.run(m())
