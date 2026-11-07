import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50000000) as ws:
    await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"JSON.stringify((window.gameInfo||{}).party)+(()=>{const s=window.__pr_cam&&window.__pr_cam.scene;const h=s&&s.ui.getHandler();return JSON.stringify({h:h&&h.constructor.name,ph:s&&s.phaseManager.getCurrentPhase().constructor.name,cur:h&&h.cursor,gi:window.gameInfo&&window.gameInfo.gameMode,w:window.gameInfo&&window.gameInfo.wave})})()","returnByValue":True}}))
    print(json.loads(await ws.recv())["result"]["result"].get("value"))
asyncio.run(m())

