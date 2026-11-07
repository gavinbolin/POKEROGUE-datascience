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
def z(h=120): key('z','KeyZ',90,h)
def arrow(d,h=90):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
# Select Yamper: from Zigzagoon highlight, Down past Zacian to Yamper
arrow('Down'); time.sleep(0.2)
arrow('Down'); time.sleep(0.2)
z(140); time.sleep(1.0)
print('after yamper', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))
shot('pokerogue_yamper.jpg')
# If still choose, Down once more to Nosepass/Rattata
for extra in range(3):
    t0=ev('window.gameInfo.playTime')
    time.sleep(0.8)
    t1=ev('window.gameInfo.playTime')
    if t1!=t0: break
    arrow('Down'); time.sleep(0.2); z(140); time.sleep(0.8)
    print('extra', extra, ev('window.gameInfo.playTime'), ev('window.gameInfo.wave'))
# Fight
for i in range(12):
    z(100); time.sleep(0.5)
print('FINAL', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode})"))
party=ev("""(()=> (window.gameInfo.party||[]).map(p=>({n:p.name,hp:p.currentHP,st:p.status||''})))()""")
print('PARTY', party)
shot('pokerogue_yamper2.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1)
ws.close()
