import json, urllib.request, websocket, time, base64, pathlib
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=20)
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
    call('Input.dispatchKeyEvent', kwargs); time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
def z(h=100): key('z','KeyZ',90,h)
def cancel():
    key('x','KeyX',88,100); time.sleep(0.12)
    key('Backspace','Backspace',8,100)
def arrow(d,h=80):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("""(()=>{const g=window.gameInfo||{};
      const party=(g.party||[]).map(p=>({n:p.name,l:p.level,hp:p.currentHP,max:p.maxHP,s:!!p.shiny,st:p.status||''}));
      return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome,luck:g.luck,party};})()""")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', json.dumps(st())[:500])
shot('pokerogue_faint0.jpg')

# Forced switch: Down past fainted to Yamper (index 2), Z. Do NOT cancel.
# Cursor starts on slot 0; Down, Down -> slot 2 Yamper
for _ in range(2):
    arrow('Down',90); time.sleep(0.18)
z(130); time.sleep(0.8)
print('AFTER_SWITCH', json.dumps(st())[:500])
shot('pokerogue_faint1.jpg')

# If still on choose screen, try Down more times to any Able
for attempt in range(4):
    s=st()
    # if playtime still frozen and wave same, try another mon
    t0=s.get('t')
    time.sleep(0.3)
    for _ in range(attempt+1):
        arrow('Down',90); time.sleep(0.15)
    z(130); time.sleep(0.7)
    print('TRY', attempt, st().get('t'), st().get('w'))

# Fight with whatever is out — prefer non-EQ: just Z for first move of support
for i in range(20):
    z(100); time.sleep(0.5)
    if i % 8 == 7:
        # if switch prompt again: down to living + Z
        arrow('Down',80); time.sleep(0.1); arrow('Down',80); time.sleep(0.1); z(120)
    if i % 5 == 4:
        cancel(); time.sleep(0.2)
    if i % 4 == 0:
        print('P', i, {k:st().get(k) for k in ('t','w','m')})

print('FINAL', json.dumps(st())[:800])
shot('pokerogue_faint2.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1)
ws.close()
