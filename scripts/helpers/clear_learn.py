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
    time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})

call('Page.bringToFront')
ev('''(() => { const c=document.querySelector('canvas'); c.tabIndex=0; c.focus(); return true; })()''')
# Click canvas center first
box=ev('''(() => { const c=document.querySelector('canvas'); const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}; })()''')
call('Input.dispatchMouseEvent', {'type':'mousePressed','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.05)
call('Input.dispatchMouseEvent', {'type':'mouseReleased','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.3)

def shot(name):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':60})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{name}').write_bytes(base64.b64decode(s['result']['data']))

# Move-learn dismiss sequence: often Z (confirm dialogue) then Backspace (don't learn) or pick move
# Try: Z a few times to advance text, then Backspace to cancel learn
for step in range(5):
    key('z','KeyZ',90,120); time.sleep(0.45)
print('t after Z', ev('window.gameInfo.playTime'))
shot('pokerogue_learn1.jpg')

# Cancel learn
for _ in range(4):
    key('Backspace','Backspace',8,120); time.sleep(0.35)
print('t after BS', ev('window.gameInfo.playTime'))
shot('pokerogue_learn2.jpg')

# If "forget a move?" Yes/No — Down to No then Z, or Backspace
for _ in range(3):
    key('ArrowDown','ArrowDown',40,80); time.sleep(0.15)
    key('z','KeyZ',90,110); time.sleep(0.4)
    key('Backspace','Backspace',8,110); time.sleep(0.3)
print('t after no', ev('window.gameInfo.playTime'), 'w', ev('window.gameInfo.wave'))
shot('pokerogue_learn3.jpg')

# More Z to resume battle
for _ in range(10):
    key('z','KeyZ',90,100); time.sleep(0.5)
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('tick', t0, t1, 'wave', ev('window.gameInfo.wave'))
shot('pokerogue_learn4.jpg')
ws.close()
