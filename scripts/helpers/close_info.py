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
def cancel():
    key('x','KeyX',88,110); time.sleep(0.15)
    key('Backspace','Backspace',8,110)
def space():
    call('Input.dispatchKeyEvent', {'type':'rawKeyDown','windowsVirtualKeyCode':32,'code':'Space','key':' '})
    time.sleep(0.08)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':32,'code':'Space','key':' ','text':' ','unmodifiedText':' '})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':32,'code':'Space','key':' '})
def z(h=110): key('z','KeyZ',90,h)
def arrow(d,h=90):
    m={'Up':('ArrowUp',38),'Down':('ArrowDown',40),'Left':('ArrowLeft',37),'Right':('ArrowRight',39)}
    c,k=m[d]; key(c,c,k,h)
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':55})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
print('BEFORE', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))

# Close Info overlay hard
for _ in range(12):
    cancel(); time.sleep(0.28)
print('AFTER_CLOSE_INFO', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave})"))
shot('pokerogue_info_closed.jpg')

# Now on Choose a Pokemon: pick living — go Up to top, Down to first able
for _ in range(6):
    arrow('Up',80); time.sleep(0.1)
# slots: try each with Space; if fainted Info might open — cancel and next
for slot in range(6):
    if slot > 0:
        arrow('Down',90); time.sleep(0.18)
    space(); time.sleep(0.7)
    t=ev('window.gameInfo.playTime')
    print('slot', slot, 't', t)
    # if info opened, cancel
    cancel(); time.sleep(0.25)
    t2=ev('window.gameInfo.playTime')
    if t2 and t and t2 > t:
        print('advanced at slot', slot)
        break
    # also try Z confirm
    z(120); time.sleep(0.5)

shot('pokerogue_after_pick.jpg')
# fight/clear
for i in range(15):
    space(); time.sleep(0.4)
    z(90); time.sleep(0.25)
    if i % 5 == 4:
        cancel(); time.sleep(0.2)
    if i % 3 == 0:
        print('P', i, ev('window.gameInfo.playTime'), ev('window.gameInfo.wave'))

print('FINAL', ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode})"))
party=ev("""(()=>(window.gameInfo.party||[]).map(p=>({n:p.name,hp:p.currentHP,st:p.status||''})))()""")
print('PARTY', party)
shot('pokerogue_live_ok.jpg')
t0=ev('window.gameInfo.playTime'); time.sleep(2); t1=ev('window.gameInfo.playTime')
print('TICK', t0, t1, 'live', t0!=t1)
ws.close()
