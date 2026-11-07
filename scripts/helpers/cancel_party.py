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

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', st()); shot('pokerogue_cancel0.jpg')

# Cancel party submenu: Down to Cancel then Z, plus Backspace spam
for _ in range(6):
    arrow('Down',80); time.sleep(0.1)
z(120); time.sleep(0.4)
for _ in range(10):
    bs(120); time.sleep(0.25)
print('AFTER_CANCEL', st()); shot('pokerogue_cancel1.jpg')

# Resume with Z — fight / confirm rewards / clear text
for i in range(20):
    z(100); time.sleep(0.5)
    if i % 7 == 6:
        bs(100); time.sleep(0.2)
    if i % 4 == 0:
        print('P', i, st())
t0=ev('window.gameInfo.playTime'); time.sleep(2.2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, '->', t1, 'wave', ev('window.gameInfo.wave'))
print('FINAL', st()); shot('pokerogue_cancel2.jpg')
ws.close()
