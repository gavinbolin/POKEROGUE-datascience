import json,asyncio,websockets,urllib.request
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
RD="""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());return JSON.stringify({ph:ph&&ph.constructor.name,ui:s.ui?.getHandler?.()?.constructor?.name,turn:s.currentBattle?.turn,party:s.getPlayerParty().map(p=>p.name+(p.isShiny()?'*':'')+' '+p.hp+'/'+p.getMaxHp()+(p.isOnField()?' F':'')),balls:s.pokeballCounts,wave:s.currentBattle?.waveIndex,enemy:s.getEnemyField().map(p=>p.name+' '+p.hp+'/'+p.getMaxHp()+' boss'+p.isBoss()+' seg'+p.bossSegmentIndex+' types'+p.getTypes()),t0:performance.timeOrigin})})()"""
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def ev(e):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r.get("result",{}).get("result",{}).get("value")
        await ev(HOOK)
        print(await ev(RD))
asyncio.run(main())
