import json,asyncio,websockets,urllib.request,time,sys
SPN,CMD,ARG=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
THROW="""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const f=s.getField();const e=f[2];
if(!ph||ph.constructor.name!=='CommandPhase')return 'phase '+(ph&&ph.constructor.name);
if(!e||!e.isShiny()||e.name!==SPN||f[3])return 'field mismatch';
if(CMD===1&&(s.pokeballCounts[ARG]||0)<1)return 'no ball';if(CMD===1&&ARG===4)return 'no master';if(CMD===0&&!(e.isBoss()&&e.bossSegmentIndex>0))return 'no attack needed';if(CMD!==0&&CMD!==1)return 'bad';
const r=ph.handleCommand(CMD,ARG);return 'cmd '+CMD+' '+ARG+' '+r;})()"""
RD="""(()=>{const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());return JSON.stringify({ph:ph&&ph.constructor.name,ui:s.ui?.getHandler?.()?.constructor?.name,mode:s.ui?.getMode?.(),party:s.getPlayerParty().map(p=>p.name+(p.isShiny()?'*':'')),balls:s.pokeballCounts,wave:s.currentBattle?.waveIndex,enemy:s.getEnemyField().map(p=>p.name+' '+p.hp+' seg'+p.bossSegmentIndex)})})()"""
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
        print(await ev(THROW.replace('SPN',json.dumps(SPN)).replace('CMD',str(CMD)).replace('ARG',str(ARG))))
        last=None
        for i in range(120):
            await ev(STEP); await asyncio.sleep(0.15)
            st=await ev(RD)
            if st!=last: print(i,st); last=st
            d=json.loads(st)
            if d['ui'] in ('ConfirmUiHandler','PartyUiHandler','SummaryUiHandler') : break
            if d['ph']=='CommandPhase' and i>10: break
            if d['ph'] in ('SelectModifierPhase',) : break
asyncio.run(main())


