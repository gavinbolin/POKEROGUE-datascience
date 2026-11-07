import json, urllib.request, websocket, time, base64, pathlib
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
nid=[0]
def call(method, params=None):
    nid[0]+=1
    msg={'id':nid[0],'method':method}
    if params is not None: msg['params']=params
    ws.send(json.dumps(msg))
    while True:
        r=json.loads(ws.recv())
        if r.get('id')==nid[0]: return r
def ev(expr):
    r=call('Runtime.evaluate',{'expression':expr,'returnByValue':True})
    return ((r.get('result') or {}).get('result') or {}).get('value')
def key(key, code, kc, hold=120):
    kwargs={'type':'keyDown','windowsVirtualKeyCode':kc,'code':code,'key':key}
    if len(key)==1: kwargs['text']=key
    call('Input.dispatchKeyEvent', kwargs); time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
def space():
    call('Input.dispatchKeyEvent', {'type':'rawKeyDown','windowsVirtualKeyCode':32,'code':'Space','key':' '})
    time.sleep(0.08)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':32,'code':'Space','key':' ','text':' ','unmodifiedText':' '})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':32,'code':'Space','key':' '})
def z(h=110): key('z','KeyZ',90,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

print('BEFORE_RELOAD', ev("JSON.stringify({t:window.gameInfo&&window.gameInfo.playTime,w:window.gameInfo&&window.gameInfo.wave,m:window.gameInfo&&window.gameInfo.gameMode})"))

# Ensure settings still good before reload
ev(r'''(() => {
  const raw=localStorage.getItem('settings');
  let s={}; try{s=JSON.parse(raw||'{}')}catch(e){s={}}
  if(!s.general)s.general={};
  const g=s.general;
  Object.assign(g,{gameSpeed:5,hpBarSpeed:3,expGainsSpeed:3,partyExpNotificationMode:2,eggSkipPreference:2,battleStyle:1,enableTutorials:false,skipSeenDialogues:true,levelMoveConfirmation:false,manualMessageClear:false});
  localStorage.setItem('settings', JSON.stringify(s));
  return true;
})()''')

call('Page.reload', {'ignoreCache': False})
# wait for load
time.sleep(8)
# reconnect may be needed after reload - try eval; if fail, reconnect
try:
    mode=ev('window.gameInfo && window.gameInfo.gameMode')
    print('post-reload mode', mode, 't', ev('window.gameInfo && window.gameInfo.playTime'))
except Exception as e:
    print('eval fail after reload', e)

ws.close()
# Reconnect fresh
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
nid=[0]

# wait until gameInfo exists / title
for i in range(40):
    time.sleep(1)
    try:
        info=ev("(()=>{const g=window.gameInfo||{}; return {m:g.gameMode,w:g.wave,t:g.playTime,ready:!!g.gameMode || document.title.includes('Rogue')};})()")
        print('wait', i, info)
        if info and (info.get('m') or info.get('ready')):
            if info.get('m') in ('Title', 'Classic', None) or info.get('t')==0 or info.get('m')=='Title':
                break
    except Exception as e:
        print('wait err', e)
        # reconnect
        try: ws.close()
        except: pass
        tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
        page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
        ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
        nid=[0]

shot('pokerogue_title_reload.jpg')
call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
time.sleep(1)
# Continue is usually top option on Title — Space/Z
for _ in range(3):
    # Up to ensure top
    key('ArrowUp','ArrowUp',38,80); time.sleep(0.15)
space(); time.sleep(1.2)
z(120); time.sleep(1.2)
info=ev("(()=>{const g=window.gameInfo||{}; return {m:g.gameMode,w:g.wave,t:g.playTime,b:g.biome,luck:g.luck};})()")
print('AFTER_CONTINUE', info)
shot('pokerogue_continued.jpg')

# If still title, try again
if not info or info.get('m')=='Title' or info.get('m') is None or info.get('w') in (0, None):
    for _ in range(5):
        space(); time.sleep(0.8)
        z(120); time.sleep(0.8)
    info=ev("(()=>{const g=window.gameInfo||{}; return {m:g.gameMode,w:g.wave,t:g.playTime,b:g.biome};})()")
    print('AFTER_CONTINUE2', info)
    shot('pokerogue_continued2.jpg')

# Verify tick
if info and info.get('m')=='Classic':
    for i in range(10):
        space(); time.sleep(0.5)
        z(100); time.sleep(0.3)
    t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
    print('TICK', t0, t1, 'wave', ev('window.gameInfo.wave'))
    party=ev("""(()=>(window.gameInfo.party||[]).map(p=>({n:p.name,hp:p.currentHP,st:p.status||'',l:p.level})))()""")
    print('PARTY', party)
shot('pokerogue_after_reload_live.jpg')
ws.close()
print('RELOAD_DONE')
