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
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome}})()")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', st())

# U = Cancel per on-screen keybind; also Backspace
for _ in range(6):
    key('u','KeyU',85,120); time.sleep(0.3)
    bs(120); time.sleep(0.25)
print('AFTER_U', st()); shot('pokerogue_exit0.jpg')

# More cancel layers (bag -> battle)
for _ in range(8):
    key('u','KeyU',85,110); time.sleep(0.25)
    bs(110); time.sleep(0.2)
print('AFTER_U2', st()); shot('pokerogue_exit1.jpg')

# Resume fighting
for i in range(18):
    z(100); time.sleep(0.5)
    if i % 6 == 5:
        key('u','KeyU',85,100); time.sleep(0.2); bs(100); time.sleep(0.2)
    if i % 3 == 0:
        print('P', i, st())
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
w=ev('window.gameInfo.wave')
print('TICK', t0, '->', t1, 'wave', w)
print('FINAL', st()); shot('pokerogue_exit2.jpg')
# write brief status
pathlib.Path(r'C:\Users\gavin\agent-tools\pokerogue_farm_status.json').write_text(
    json.dumps({'ts':time.strftime('%Y-%m-%dT%H:%M:%S'),'event':'exit_item_menu','t':t1,'w':w,'tick':t0!=t1}, indent=2), encoding='utf-8')
ws.close()
