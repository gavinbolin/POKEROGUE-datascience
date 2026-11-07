import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50000000) as ws:
    await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"(()=>{const cb=window.__pr_cam.scene.currentBattle;return JSON.stringify({w:cb.waveIndex,bt:cb.battleType,tr:!!cb.trainer,tn:cb.trainer&&cb.trainer.config&&cb.trainer.config.name,en:cb.enemyParty.map(e=>[e.name,e.shiny])})})()","returnByValue":True}}))
    print(json.loads(await ws.recv())["result"]["result"].get("value"))
asyncio.run(m())
