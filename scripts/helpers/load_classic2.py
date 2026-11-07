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
def cancel():
    key('x','KeyX',88,110); time.sleep(0.15)
    key('Backspace','Backspace',8,110)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':60})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))
def st():
    return ev("(()=>{const g=window.gameInfo||{};return {m:g.gameMode,w:g.wave,t:g.playTime,b:g.biome,luck:g.luck};})()")

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('NOW', st())
shot('pokerogue_preclassic.jpg')

# Cancel submenu (Down to Cancel then Space, or Backspace/X)
for _ in range(4):
    key('ArrowDown','ArrowDown',40,80); time.sleep(0.12)
space(); time.sleep(0.5)
for _ in range(4):
    cancel(); time.sleep(0.25)
shot('pokerogue_after_cancel_sub.jpg')
print('after cancel sub', st())

# Move down to Classic slot (bottom). May need a couple Downs from top/mid.
for _ in range(3):
    key('ArrowDown','ArrowDown',40,100); time.sleep(0.35)
shot('pokerogue_classic_hilite.jpg')

# Open slot menu and Load Game (top option)
space(); time.sleep(0.7)
shot('pokerogue_classic_submenu.jpg')
# Ensure Load Game (top): Up several then Space
for _ in range(4):
    key('ArrowUp','ArrowUp',38,80); time.sleep(0.1)
space(); time.sleep(2.0)
z(120); time.sleep(1.5)
info=st()
print('LOADED', info)
shot('pokerogue_classic_live.jpg')

if info and info.get('m')=='Classic':
    # clear any prompts with Space/Z; cancel info overlays
    for i in range(15):
        space(); time.sleep(0.4)
        z(90); time.sleep(0.25)
        if i % 5 == 4:
            cancel(); time.sleep(0.2)
        if i % 3 == 0:
            print('P', i, st())
    t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
    print('TICK', t0, t1, 'wave', ev('window.gameInfo.wave'))
    party=ev("""(()=>(window.gameInfo.party||[]).map(p=>({n:p.name,hp:p.currentHP,st:p.status||'',l:p.level,s:!!p.shiny})))()""")
    print('PARTY', party)
elif info and info.get('m')=='Endless':
    print('ABORT still Endless - reload title')
    call('Page.reload', {'ignoreCache': False})
else:
    print('not classic yet', info)
    # try one more down+load
    cancel(); time.sleep(0.3)
    key('ArrowDown','ArrowDown',40,100); time.sleep(0.3)
    space(); time.sleep(0.5)
    for _ in range(3):
        key('ArrowUp','ArrowUp',38,80); time.sleep(0.1)
    space(); time.sleep(2)
    print('RETRY', st())
    shot('pokerogue_classic_retry.jpg')

shot('pokerogue_classic_final.jpg')
ws.close()
