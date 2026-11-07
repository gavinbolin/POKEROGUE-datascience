import json,asyncio,websockets,urllib.request,sys
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP2="""(()=>{try{const s=window.__pr_cam.scene;const L=s.game.loop;const T=s.tweens;let t=Math.max(L.lastTime||0,L.now||0);for(let k=0;k<45;k++){t+=16.7;T.prevTime=Date.now()-16.7;L.step(t)}return L.frame}catch(e){return String(e.stack||e)}})()"""
RD="""(()=>{try{const s=window.__pr_cam.scene;const ph=s.phaseManager.getCurrentPhase();const h=s.ui.getHandler();return JSON.stringify({ph:ph.constructor.name,ui:h.constructor.name,aw:h.awaitingActionInput,msg:String(s.ui.getMessageHandler?.()?.message?.text||'').slice(0,80),party:s.getPlayerParty().length,en:s.getEnemyParty().map(e=>e.name+':'+e.hp),balls:s.pokeballCounts,wave:s.currentBattle?.waveIndex})}catch(e){return String(e)}})()"""
ACT=src and """(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();if(h.constructor.name!=='BattleMessageUiHandler'||!h.awaitingActionInput)return 'guard';return h.processInput(5)})()"""
N=int(sys.argv[1]) if len(sys.argv)>1 else 60
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def ev(e):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r.get("result",{}).get("result",{}).get("value")
        await ev(HOOK); last=None
        if 'ack' in sys.argv: print('act',await ev(ACT))
        for i in range(N):
            await ev(STEP2); await asyncio.sleep(0.05)
            st=await ev(RD)
            if st!=last: print(i,st); last=st
            d=json.loads(st)
            if d['ph']!='AttemptCapturePhase' and d.get('aw'): break
            if d['ui'] in ('ConfirmUiHandler','PartyUiHandler','ModifierSelectUiHandler','CommandUiHandler','OptionSelectUiHandler'): break
asyncio.run(main())

