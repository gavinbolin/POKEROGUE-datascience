import json,asyncio,websockets,urllib.request
v=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/version"))
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(v["webSocketDebuggerUrl"]) as ws:
    await ws.send(json.dumps({"id":1,"method":"Browser.getWindowForTarget","params":{"targetId":p["id"]}}))
    r=json.loads(await ws.recv()); print(r)
    wid=r["result"]["windowId"]
    if r["result"]["bounds"].get("windowState")=="minimized":
      await ws.send(json.dumps({"id":2,"method":"Browser.setWindowBounds","params":{"windowId":wid,"bounds":{"windowState":"normal"}}})); print(await ws.recv())
    await ws.send(json.dumps({"id":3,"method":"Target.activateTarget","params":{"targetId":p["id"]}})); print(await ws.recv())
asyncio.run(m())
