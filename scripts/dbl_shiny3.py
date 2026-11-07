import json,asyncio,websockets,urllib.request,sys
# usage: dbl_shiny.py MODE [steps] [arg]
# modes: rd | mv FIELD MOVEIDX (fight move) | tgt BATTLERIDX | sw FIELD PARTYIDX | ball SPECIES | ack
MODE=sys.argv[1]; A=sys.argv[2:]
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
PRE="const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();"
RD="(()=>{"+PRE+"""return JSON.stringify({ph:ph&&ph.constructor.name,fi:ph&&ph.fieldIndex,ui:h&&h.constructor.name,cur:h&&h.cursor,
en:s.getEnemyField().map(p=>({n:p.name,sh:p.isShiny(),lv:p.level,hp:p.hp,mx:p.getMaxHp(),boss:p.isBoss(),seg:p.bossSegments,ty:p.getTypes(),bi:p.getBattlerIndex(),f:p.isFainted(),st:p.stats,ab:p.getAbility().name})),
pl:s.getPlayerField().map(p=>({n:p.name,lv:p.level,hp:p.hp,mx:p.getMaxHp(),mv:p.getMoveset().map(m=>m.getName()+'/t'+m.getMove().type+'/p'+m.getMove().power+'/c'+m.getMove().category+'/pp'+(m.getMovePp()-m.ppUsed)),st:p.stats,bi:p.getBattlerIndex()})),
party:s.getPlayerParty().map(p=>p.name+' '+p.hp+'/'+p.getMaxHp()+' lv'+p.level+(p.isOnField()?' F':'')),balls:s.pokeballCounts})})()"""
def J(x): return json.dumps(x)
if MODE=="rd": CMD="0"
elif MODE=="mv":
    fi,mi=int(A[0]),int(A[1]); A=A[2:]
    CMD="(()=>{"+PRE+f"if(!ph||ph.constructor.name!=='CommandPhase'||ph.fieldIndex!=={fi})return 'bad phase '+(ph&&ph.constructor.name)+' '+(ph&&ph.fieldIndex);const m=s.getPlayerField()[{fi}].getMoveset()[{mi}];return 'mv '+m.getName()+' '+ph.handleCommand(0,{mi});}})()"
elif MODE=="tgt":
    bi=int(A[0]); A=A[1:]
    CMD="(()=>{"+PRE+f"if(!h||h.constructor.name!=='TargetSelectUiHandler')return 'no tsel';const e=s.getField()[{bi}];if(!e||e.isShiny())return 'target shiny/none';if(h.cursor!=={bi})h.setCursor({bi});if(h.cursor!=={bi})return 'cursor '+h.cursor;return 'ok '+e.name+' '+h.processInput(5);}})()"
elif MODE=="ball":
    sp=A[0]; A=A[1:]
    CMD="(()=>{"+PRE+f"if(!ph||ph.constructor.name!=='CommandPhase')return 'bad phase';const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());if(en.length!==1||en[0].name!=={J(sp)}||!en[0].isShiny())return 'enemy '+en.map(p=>p.name);const b=[3,2,1,0].find(k=>(s.pokeballCounts[k]||0)>0);if(b===undefined)return 'no ball';if((s.pokeballCounts[b]||0)<1)return 'no ball';return 'b'+b+' '+ph.handleCommand(1,b);}})()"
elif MODE=="sw":
    fi,pi=int(A[0]),int(A[1]); A=A[2:]
    CMD="(()=>{"+PRE+f"if(!ph||ph.constructor.name!=='CommandPhase'||ph.fieldIndex!=={fi})return 'bad phase';const en=s.getEnemyField().filter(p=>p.isOnField()&&!p.isFainted());if(!en.some(p=>p.isShiny()))return 'no shiny';const t=s.getPlayerParty()[{pi}];if(!t||t.isFainted()||t.isOnField())return 'bad target';return 'sw '+t.name+' '+ph.handleCommand(2,{pi},false);}})()"
elif MODE=="pty":
    pi=int(A[0]); A=A[1:]
    CMD="(()=>{"+PRE+f"if(!ph||ph.constructor.name!=='SwitchPhase'||!h||h.constructor.name!=='PartyUiHandler')return 'guard';const t=s.getPlayerParty()[{pi}];if(!t||t.isFainted())return 'bad';h.setCursor({pi});const r1=h.processInput(5);return 'pty '+t.name+' cur='+h.cursor+' r1='+r1+' oc='+h.optionsCursor;}})()"
elif MODE=="ok":
    CMD="(()=>{"+PRE+"if(!h||h.constructor.name!=='PartyUiHandler')return 'guard';return 'ok '+h.processInput(5);})()"
elif MODE=="ack":
    CMD="(()=>{"+PRE+"if(!h||h.constructor.name!=='BattleMessageUiHandler'||!h.awaitingActionInput||ph.constructor.name==='CommandPhase')return 'guard';return 'a '+h.processInput(5);})()"
steps=int(A[0]) if A else 0
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def ev(e):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r.get("result",{}).get("result",{}).get("value") or r.get("result",{}).get("exceptionDetails",{}).get("exception",{}).get("description")
        await ev(HOOK)
        if MODE!="rd": print(await ev(CMD))
        last=None
        for i in range(steps):
            await ev(STEP); await asyncio.sleep(0.15)
            st=await ev(RD)
            if st!=last: print(i,st); last=st
        print("FINAL",await ev(RD))
asyncio.run(main())

