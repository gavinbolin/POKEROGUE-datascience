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
def bs(h=100): key('Backspace','Backspace',8,h)
def arrow(d,h=80):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':58})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
box=ev("(()=>{const c=document.querySelector('canvas');const r=c.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}})()")
call('Input.dispatchMouseEvent',{'type':'mousePressed','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
time.sleep(0.05)
call('Input.dispatchMouseEvent',{'type':'mouseReleased','x':box['x'],'y':box['y'],'button':'left','clickCount':1})
print('STATE', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode,b:window.gameInfo.biome})"))
party=ev("""(()=>{const g=window.gameInfo||{}; return (g.party||[]).map(p=>({n:p.name,l:p.level,s:p.shiny,hp:p.currentHP,f:p.isFusion}));})()""")
print('PARTY', json.dumps(party))
shot('pokerogue_now33.jpg')

# Clear softlock: BS overlays, Z messages/rewards, arrow+Z for shops
for _ in range(5):
    bs(110); time.sleep(0.2)
for i in range(25):
    z(100); time.sleep(0.5)
    if i % 6 == 5:
        arrow('Down',80); time.sleep(0.12); z(100); time.sleep(0.3)
    if i % 8 == 7:
        bs(90); time.sleep(0.2)
    if i % 4 == 0:
        st=ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})")
        print('P', i, st)
shot('pokerogue_now33b.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1, 'W', ev('window.gameInfo.wave'))
shot('pokerogue_now33c.jpg')
ws.close()
