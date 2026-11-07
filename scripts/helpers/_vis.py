import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"]) as ws:
    await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"JSON.stringify({v:document.visibilityState,f:document.hasFocus(),t:document.title,gi:window.gameInfo,ph:typeof Phaser})","returnByValue":True}}))
    print(json.loads(await ws.recv())["result"]["result"].get("value"))
asyncio.run(m())
