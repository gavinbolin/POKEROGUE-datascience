import json,asyncio,websockets,urllib.request
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"]) as ws:
    await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"(()=>{const r=[];for(const k of Object.keys(window)){try{const o=window[k];if(o&&o.loop&&o.scene&&o.scene.scenes)r.push(k)}catch(e){}}return JSON.stringify({r,lp:(()=>{try{return Object.keys(Phaser.Core.TimeStep.prototype).slice(0,40)}catch(e){return String(e)}})()})})()","returnByValue":True}}))
    print(json.loads(await ws.recv())["result"]["result"].get("value"))
asyncio.run(m())

