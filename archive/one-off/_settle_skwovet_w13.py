"""Advance UI after Skwovet w13 catch until reward / next wave."""
import json, asyncio, websockets, urllib.request, os
os.chdir(r"C:\Users\gavin\AppData\Local\Temp\prfarm")
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
PRE="const s=window.__pr_cam.scene;const ph=(s.phaseManager?.getCurrentPhase?.()||s.getCurrentPhase?.());const h=s.ui?.getHandler?.();"
RD="(()=>{"+PRE+"""return JSON.stringify({ph:ph&&ph.constructor.name,ui:h&&h.constructor.name,wave:s.currentBattle&&s.currentBattle.waveIndex,
opts:(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return []}})(),
txt:(()=>{try{const out=[];const walk=(o,d)=>{if(!o||d>7)return;if(o.visible===false)return;if(o.text!==undefined&&String(o.text).trim())out.push(String(o.text).replace(/\\n/g,' ').slice(0,80));(o.list||[]).forEach(c=>walk(c,d+1))};walk(s.ui,0);return out.slice(0,20)}catch(e){return[]}})()
})})()"""
NO="""(()=>{const h=window.__pr_cam.scene.ui.getHandler();const n=h.constructor.name;
if(n!=='OptionSelectUiHandler'&&n!=='ConfirmUiHandler')return JSON.stringify({n});
const opts=(()=>{try{const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return[]}})();
let i=opts.findIndex(t=>/no/i.test(t)); if(i<0)i=Math.min(1,opts.length-1); h.setCursor(i); return JSON.stringify({n,opts,i,r:h.processInput(5)});})()"""

async def main():
    tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    p=next(x for x in tabs if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    ws=await websockets.connect(p["webSocketDebuggerUrl"], max_size=50_000_000)
    n=[0]
    async def call(method, params=None):
        n[0]+=1
        await ws.send(json.dumps({"id":n[0],"method":method,**({"params":params} if params else {})}))
        while True:
            r=json.loads(await ws.recv())
            if r.get("id")==n[0]: return r
    async def ev(e):
        r=await call("Runtime.evaluate",{"expression":e,"returnByValue":True})
        return ((r.get("result") or {}).get("result") or {}).get("value")
    async def key(k,code,kc,h=90):
        d={"type":"keyDown","windowsVirtualKeyCode":kc,"code":code,"key":k}
        if len(k)==1: d["text"]=k
        await call("Input.dispatchKeyEvent",d); await asyncio.sleep(h/1000)
        await call("Input.dispatchKeyEvent",{"type":"keyUp","windowsVirtualKeyCode":kc,"code":code,"key":k})
    async def Z(): await key("z","KeyZ",90)
    async def X(): await key("x","KeyX",88)
    async def step(k=8):
        for _ in range(k):
            await ev(STEP); await asyncio.sleep(0.02)
    def parse(st):
        if isinstance(st,dict) and "ph" in st: return st
        return json.loads(st)
    await call("Page.bringToFront")
    await ev(HOOK)
    for i in range(45):
        await step(6)
        st=parse(await ev(RD))
        ph=st.get("ph") or ""; ui=st.get("ui") or ""; txt=" | ".join(st.get("txt") or [])[:140]
        print(f"{i} ph={ph} ui={ui} wave={st.get('wave')} opts={st.get('opts')} t={txt!r}")
        if ph=="SelectModifierPhase":
            print("SETTLED reward"); break
        if ph in ("CommandPhase","TurnInitPhase","NewBattlePhase") and st.get("wave") and st.get("wave")>13:
            print("SETTLED advanced"); break
        if ui in ("OptionSelectUiHandler","ConfirmUiHandler"):
            low=txt.lower()
            if any(x in low for x in ("full","release","make room","add","party","learn","forget","stop learning")):
                print("NO", await ev(NO)); await asyncio.sleep(0.35); continue
            await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor(0);return h.processInput(5)})()")
            await Z(); await asyncio.sleep(0.3); continue
        if ui=="SummaryUiHandler":
            await X(); await asyncio.sleep(0.3); continue
        if ui=="BattleMessageUiHandler":
            await ev("(()=>{const h=window.__pr_cam.scene.ui.getHandler();return h&&h.processInput(5)})()")
            await Z(); await asyncio.sleep(0.2); continue
        await Z(); await asyncio.sleep(0.25)
    st=parse(await ev(RD))
    print("FINAL", json.dumps({k:st.get(k) for k in ("ph","ui","wave","opts","txt")}, indent=1))

asyncio.run(main())
