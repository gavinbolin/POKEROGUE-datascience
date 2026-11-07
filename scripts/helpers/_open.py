import json,asyncio,websockets,urllib.request
v=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/version"))
async def m():
  async with websockets.connect(v["webSocketDebuggerUrl"]) as ws:
    await ws.send(json.dumps({"id":1,"method":"Target.createTarget","params":{"url":"https://pokerogue.net/","background":True}}))
    print(await ws.recv())
asyncio.run(m())
