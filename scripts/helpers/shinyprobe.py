import json,asyncio,websockets,urllib.request,base64
p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and "pokerogue.net" in x.get("url",""))
JS=r"""(()=>{const s=window.__pr_cam&&window.__pr_cam.scene;if(!s)return 'noscene';const cb=s.currentBattle;
return JSON.stringify({h:s.ui.getHandler().constructor.name,ph:s.phaseManager.getCurrentPhase().constructor.name,wave:cb&&cb.waveIndex,dbl:cb&&cb.double,tr:!!(cb&&cb.trainer),
party:s.getPlayerParty().map(p=>[p.name,p.hp,p.getMaxHp(),!!p.shiny,p.isShiny&&p.isShiny()]),
enemy:(s.getEnemyField?s.getEnemyField():[]).map(e=>e&&[e.name,e.hp,!!e.shiny,e.isShiny&&e.isShiny()])})})()"""
HOOK=open("pr_farm17.py",encoding="utf-8").read().split('HOOK_JS = """')[1].split('"""')[0]
async def m():
  async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50000000) as ws:
    await ws.send(json.dumps({"id":9,"method":"Runtime.evaluate","params":{"expression":HOOK,"returnByValue":True}})); await ws.recv(); await asyncio.sleep(1)
    await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":JS,"returnByValue":True}}))
    print(json.loads(await ws.recv())["result"]["result"].get("value"))
    await ws.send(json.dumps({"id":2,"method":"Page.captureScreenshot","params":{"format":"png"}}))
    open(r"C:\Users\gavin\agent-tools\pokerogue_battle_shots\shinycheck_now.png","wb").write(base64.b64decode(json.loads(await ws.recv())["result"]["data"]))
asyncio.run(m())

