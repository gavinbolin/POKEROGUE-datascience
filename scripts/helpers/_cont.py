import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
STEP=open('_step.js',encoding='utf-8').read(); n=[0]
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50000000) as ws:
    async def call(meth,par):
      n[0]+=1; await ws.send(json.dumps({"id":n[0],"method":meth,"params":par}))
      while True:
        r=json.loads(await ws.recv())
        if r.get("id")==n[0]: return r
    for d in ("keyDown","keyUp"):
      await call("Input.dispatchKeyEvent",{"type":d,"key":"z","code":"KeyZ","windowsVirtualKeyCode":90,**({"text":"z"} if d=="keyDown" else {})}); await asyncio.sleep(0.1)
    for i in range(40):
      await call("Runtime.evaluate",{"expression":STEP,"returnByValue":True}); await asyncio.sleep(0.25)
    r=await call("Runtime.evaluate",{"expression":"JSON.stringify(window.gameInfo)","returnByValue":True}); print(r["result"]["result"]["value"][:600])
asyncio.run(m())
