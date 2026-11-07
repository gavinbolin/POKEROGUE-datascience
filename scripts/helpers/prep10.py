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
    key('x','KeyX',88,100); time.sleep(0.15)
    key('Backspace','Backspace',8,100)
def arrow(d,h=80):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome,luck:g.luck}})()")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('START', st()); shot('pokerogue_prefarm10.jpg')

# Clear menus
for _ in range(4):
    cancel(); time.sleep(0.25)
# Advance with Z, Spirit Break preference in doubles, cancel overlays periodically
last_t = None; stuck=0
for i in range(30):
    if i % 10 < 7:
        z(95)
        if i % 4 == 1:
            time.sleep(0.2); arrow('Down',70); time.sleep(0.1); z(90)  # Spirit Break
    elif i % 10 == 7:
        # Ball path if shiny opportunity - Right from Fight
        arrow('Right',80); time.sleep(0.15); z(100); time.sleep(0.3); z(100)
    else:
        cancel()
    time.sleep(0.55)
    if i % 3 == 0:
        s=st(); print('P', i, s)
        t=s.get('t') if s else None
        if last_t is not None and t==last_t: stuck+=1
        else: stuck=0
        last_t=t
        if stuck>=3:
            for _ in range(4): cancel(); time.sleep(0.2)
            stuck=0

s=st(); print('END', s); shot('pokerogue_prefarm10b.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1, 'live', t0!=t1)
ws.close()
