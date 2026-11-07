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
    call('Input.dispatchKeyEvent', kwargs); time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
def z(h=100): key('z','KeyZ',90,h)
def bs(h=110): key('Backspace','Backspace',8,h)
def arrow(d,h=80):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome}})()")

maps=ev("localStorage.getItem('mappingConfigs')")
print('MAPS', (maps or '')[:2000])

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', st())

# Try X cancel (common), then mouse-click Cancel button area (bottom right)
key('x','KeyX',88,120); time.sleep(0.4)
key('x','KeyX',88,120); time.sleep(0.4)
bs(120); time.sleep(0.3)
key('u','KeyU',85,120); time.sleep(0.3)
print('AFTER_X', st()); shot('pokerogue_x0.jpg')

# Click bottom-right Cancel region
box=ev("(()=>{const c=document.querySelector('canvas');const r=c.getBoundingClientRect(); return {x:r.x+r.width*0.88, y:r.y+r.height*0.92, w:r.width,h:r.height};})()")
print('click cancel at', box)
for _ in range(3):
    call('Input.dispatchMouseEvent',{'type':'mousePressed','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
    time.sleep(0.05)
    call('Input.dispatchMouseEvent',{'type':'mouseReleased','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
    time.sleep(0.4)
print('AFTER_CLICK', st()); shot('pokerogue_x1.jpg')

# If still in choose: Down to Rattata (Able) and Z to apply, then cancel leftovers
for _ in range(6):
    arrow('Down',80); time.sleep(0.12)
z(120); time.sleep(0.6)
print('AFTER_RATTATA', st()); shot('pokerogue_x2.jpg')
# dismiss any follow-up
for _ in range(5):
    key('x','KeyX',88,110); time.sleep(0.25)
    bs(110); time.sleep(0.2)
    key('u','KeyU',85,110); time.sleep(0.2)
for _ in range(8):
    z(100); time.sleep(0.45)
print('FINAL', st()); shot('pokerogue_x3.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1, 'W', ev('window.gameInfo.wave'))
ws.close()
