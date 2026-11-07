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
def space():
    call('Input.dispatchKeyEvent', {'type':'rawKeyDown','windowsVirtualKeyCode':32,'code':'Space','key':' '})
    time.sleep(0.06)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':32,'code':'Space','key':' ','text':' ','unmodifiedText':' '})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':32,'code':'Space','key':' '})
def cancel():
    key('x','KeyX',88,100); time.sleep(0.12)
    key('Backspace','Backspace',8,100)
def arrow(d,h=85):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':50})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome}})()")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', st())
# Close Info
for _ in range(8):
    cancel(); time.sleep(0.22)
shot('pokerogue_noinfo.jpg')
print('AFTER_INFO', st())
# Prefer Spirit Break path when fighting: Space(Fight) Down Space(move3) Space(target)
for i in range(18):
    space(); time.sleep(0.3)
    key('z','KeyZ',90,90); time.sleep(0.15)
    if i % 3 == 0:
        arrow('Down'); time.sleep(0.12); space(); time.sleep(0.2); space(); time.sleep(0.2)
    if i % 6 == 5:
        cancel(); time.sleep(0.2)
    if i % 4 == 0:
        print('P', i, st())
print('AFTER', st())
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1, 'W', ev('window.gameInfo.wave'))
shot('pokerogue_noeq.jpg')
ws.close()
