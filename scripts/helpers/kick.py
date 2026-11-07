import json, urllib.request, websocket, time, base64, pathlib
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
wsurl=[t['webSocketDebuggerUrl'] for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(wsurl, timeout=20)
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
def key(key, code, kc, hold=100):
    kwargs={'type':'keyDown','windowsVirtualKeyCode':kc,'code':code,'key':key}
    if len(key)==1: kwargs['text']=key
    call('Input.dispatchKeyEvent', kwargs)
    time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})

# patch manualMessageClear false if set
changed=ev(r'''(() => {
  const raw=localStorage.getItem('settings');
  let s={}; try{s=JSON.parse(raw||'{}')}catch(e){s={}}
  if(!s.general)s.general={};
  const g=s.general;
  let ch=false;
  const want={gameSpeed:5,hpBarSpeed:3,expGainsSpeed:3,partyExpNotificationMode:2,eggSkipPreference:2,battleStyle:1,enableTutorials:false,skipSeenDialogues:true,levelMoveConfirmation:false,manualMessageClear:false};
  for (const [k,v] of Object.entries(want)){ if(g[k]!==v){g[k]=v;ch=true;} }
  if(ch) localStorage.setItem('settings', JSON.stringify(s));
  return {ch, manualMessageClear:g.manualMessageClear, gameSpeed:g.gameSpeed};
})()''')
print('settings', changed)

call('Page.bringToFront')
ev("document.querySelector('canvas')&&document.querySelector('canvas').focus()")
# clear messages / fight with Z spam carefully
for i in range(12):
    key('z','KeyZ',90,100)
    time.sleep(0.55)
st=ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode})")
print('after Z', st)
shot=call('Page.captureScreenshot',{'format':'jpeg','quality':65})
pathlib.Path(r'C:\Users\gavin\agent-tools\pokerogue_after_kick.jpg').write_bytes(base64.b64decode(shot['result']['data']))
# more Z+Backspace if still stuck
t0=ev('window.gameInfo.playTime')
time.sleep(2)
t1=ev('window.gameInfo.playTime')
print('tick', t0, '->', t1)
if t0==t1:
    for _ in range(4):
        key('Backspace','Backspace',8,100); time.sleep(0.25)
    for _ in range(8):
        key('z','KeyZ',90,100); time.sleep(0.5)
    print('after unstick', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))
    time.sleep(2)
    print('tick2', ev('window.gameInfo.playTime'))
ws.close()
