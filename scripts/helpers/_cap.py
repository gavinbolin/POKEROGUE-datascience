import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"]) as ws:
    for i,e in enumerate([open('_hook.js',encoding='utf-8').read(), open('_cap.js',encoding='utf-8').read()]):
      await ws.send(json.dumps({"id":i+1,"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
      print(json.loads(await ws.recv())["result"])
asyncio.run(m())
