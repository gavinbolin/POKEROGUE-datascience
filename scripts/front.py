import json,urllib.request,asyncio,websockets
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
urllib.request.urlopen("http://127.0.0.1:9222/json/activate/"+p["id"]).read()
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"]) as ws:
    await ws.send(json.dumps({"id":1,"method":"Page.bringToFront"})); print(await ws.recv())
asyncio.run(m())
