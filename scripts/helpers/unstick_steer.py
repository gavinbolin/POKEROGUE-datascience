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
def key(key, code, kc, hold=110):
    kwargs={'type':'keyDown','windowsVirtualKeyCode':kc,'code':code,'key':key}
    if len(key)==1: kwargs['text']=key
    call('Input.dispatchKeyEvent', kwargs)
    time.sleep(hold/1000.0)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
def shot(name):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':62})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{name}').write_bytes(base64.b64decode(s['result']['data']))

call('Page.bringToFront')
ev("(() => { const c=document.querySelector('canvas'); if(c){c.tabIndex=0;c.focus();} return true; })()")
st0=ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode,b:window.gameInfo.biome})")
print('BEFORE', st0)
shot('pokerogue_steer_before.jpg')

# Click canvas
box=ev("(() => { const c=document.querySelector('canvas'); const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}; })()")
call('Input.dispatchMouseEvent', {'type':'mousePressed','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.05)
call('Input.dispatchMouseEvent', {'type':'mouseReleased','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.25)

# Softlock fix per skill: Backspace out of overlays, then Z. No Escape.
for _ in range(8):
    key('Backspace','Backspace',8,120)
    time.sleep(0.22)
shot('pokerogue_steer_after_bs.jpg')
print('AFTER_BS', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))

# Advance move-learn / messages with Z; Down+Z for No on learn prompts
for _ in range(4):
    key('z','KeyZ',90,110)
    time.sleep(0.4)
for _ in range(3):
    key('ArrowDown','ArrowDown',40,80)
    time.sleep(0.12)
    key('z','KeyZ',90,110)
    time.sleep(0.35)
    key('Backspace','Backspace',8,110)
    time.sleep(0.25)

# Fight loop kick: Z spam (Fight / confirm)
for _ in range(15):
    key('z','KeyZ',90,100)
    time.sleep(0.55)

st1=ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode,b:window.gameInfo.biome})")
print('AFTER_Z', st1)
shot('pokerogue_steer_after_z.jpg')
t0=ev('window.gameInfo.playTime')
time.sleep(2.5)
t1=ev('window.gameInfo.playTime')
w1=ev('window.gameInfo.wave')
print('TICK', t0, '->', t1, 'wave', w1)
shot('pokerogue_steer_final.jpg')
ws.close()
