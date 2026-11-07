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
def key(key, code, kc, hold=110, text=None):
    kwargs={'type':'keyDown','windowsVirtualKeyCode':kc,'code':code,'key':key}
    if text is not None: kwargs['text']=text
    elif len(key)==1: kwargs['text']=key
    call('Input.dispatchKeyEvent', kwargs); time.sleep(hold/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
def space(h=120):
    # Space is BUTTON_ACTION primary — use rawKeyDown+char pattern too
    call('Input.dispatchKeyEvent', {'type':'rawKeyDown','windowsVirtualKeyCode':32,'code':'Space','key':' '})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':32,'code':'Space','key':' ','text':' ','unmodifiedText':' '})
    time.sleep(h/1000)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':32,'code':'Space','key':' '})
def z(h=110): key('z','KeyZ',90,h)
def bs(h=110): key('Backspace','Backspace',8,h)
def arrow(d,h=90):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
box=ev("(()=>{const c=document.querySelector('canvas');const r=c.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}})()")
call('Input.dispatchMouseEvent',{'type':'mousePressed','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.05)
call('Input.dispatchMouseEvent',{'type':'mouseReleased','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
print('BEFORE', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))
shot('pokerogue_sp0.jpg')

# Navigate to Yamper with arrows, confirm with Space
for _ in range(3):
    arrow('Up',80); time.sleep(0.1)  # go to top
arrow('Down'); time.sleep(0.2)
arrow('Down'); time.sleep(0.2)
space(140); time.sleep(0.8)
print('AFTER_SPACE1', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))
shot('pokerogue_sp1.jpg')

# Spam Space to clear / fight
for i in range(20):
    space(100); time.sleep(0.45)
    if i % 5 == 4:
        z(100); time.sleep(0.3)
    if i % 4 == 0:
        print('P', i, ev('window.gameInfo.playTime'), ev('window.gameInfo.wave'))
print('FINAL', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode})"))
shot('pokerogue_sp2.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1)
ws.close()
