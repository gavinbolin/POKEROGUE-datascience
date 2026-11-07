import json, urllib.request, websocket, time, base64, pathlib
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
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
    time.sleep(0.08)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':32,'code':'Space','key':' ','text':' ','unmodifiedText':' '})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':32,'code':'Space','key':' '})
def z(h=120): key('z','KeyZ',90,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':60})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {m:g.gameMode,w:g.wave,t:g.playTime,b:g.biome,luck:g.luck};})()")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('NOW', st())
# Ensure at title top Continue, then Down Down to Load Game
for _ in range(8):
    key('ArrowUp','ArrowUp',38,80); time.sleep(0.1)
# Continue -> New Game -> Load Game
key('ArrowDown','ArrowDown',40,100); time.sleep(0.25)
key('ArrowDown','ArrowDown',40,100); time.sleep(0.35)
shot('pokerogue_loadgame_hilite.jpg')
space(); time.sleep(1.2)
z(120); time.sleep(1.0)
shot('pokerogue_loadsessions.jpg')
print('after load open', st())

# Session slots - navigate and screenshot each
for i in range(5):
    shot(f'pokerogue_slot{i}.jpg')
    print('slot', i, st())
    key('ArrowDown','ArrowDown',40,100); time.sleep(0.4)

# Go back up and try to find Classic - often shown with mode name
for _ in range(6):
    key('ArrowUp','ArrowUp',38,80); time.sleep(0.12)
shot('pokerogue_slot_top.jpg')

# Try selecting each slot until Classic
for i in range(4):
    for _ in range(i):
        key('ArrowDown','ArrowDown',40,90); time.sleep(0.15)
    space(); time.sleep(1.5)
    z(120); time.sleep(1.0)
    info=st()
    print('try slot', i, info)
    shot(f'pokerogue_loaded{i}.jpg')
    if info and info.get('m')=='Classic':
        print('GOT CLASSIC')
        break
    if info and info.get('m')=='Endless':
        print('Endless - abort reload')
        call('Page.reload', {'ignoreCache': False})
        time.sleep(8)
        ws.close()
        tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
        page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
        ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
        nid=[0]
        for _ in range(20):
            time.sleep(1)
            if (st() or {}).get('m')=='Title':
                break
        call('Page.bringToFront')
        ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
        for _ in range(8):
            key('ArrowUp','ArrowUp',38,80); time.sleep(0.1)
        key('ArrowDown','ArrowDown',40,100); time.sleep(0.2)
        key('ArrowDown','ArrowDown',40,100); time.sleep(0.3)
        space(); time.sleep(1.0)
        continue
    # if still on load UI, cancel and retry next
    key('Backspace','Backspace',8,110); time.sleep(0.4)
    key('x','KeyX',88,110); time.sleep(0.3)

print('FINAL', st())
shot('pokerogue_classic_loaded.jpg')
ws.close()
