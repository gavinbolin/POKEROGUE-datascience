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
def shot(n):
    s=call('Page.captureScreenshot',{'format':'jpeg','quality':60})
    pathlib.Path(fr'C:\Users\gavin\agent-tools\{n}').write_bytes(base64.b64decode(s['result']['data']))

print('NOW', ev("JSON.stringify({m:window.gameInfo.gameMode,w:window.gameInfo.wave,t:window.gameInfo.playTime,b:window.gameInfo.biome})"))
# Abort Endless: reload to title WITHOUT continuing yet
call('Page.reload', {'ignoreCache': False})
time.sleep(9)
ws.close()
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
page=[t for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30)
nid=[0]
for i in range(25):
    time.sleep(1)
    info=ev("(()=>{const g=window.gameInfo||{}; return {m:g.gameMode,w:g.wave,t:g.playTime};})()")
    print('wait', i, info)
    if info and info.get('m')=='Title':
        break

call('Page.bringToFront')
ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}return 1})()")
time.sleep(1)
shot('pokerogue_title_menu.jpg')

# Inspect session saves in localStorage
sess=ev(r'''(() => {
  const keys = Object.keys(localStorage).filter(k => /session|save|data_/i.test(k));
  const out = {keys};
  for (const k of keys) {
    const v = localStorage.getItem(k);
    out[k] = {len: v ? v.length : 0, head: v ? v.slice(0,80) : null};
  }
  return out;
})()''')
print('SESS', json.dumps(sess)[:2000])

# Title menu items often: Continue, New Game, Load Game, Settings...
# Need Load Game or cycle Continue to Classic session.
# Try Down through options and screenshot each highlight via selecting Load Game
# First screenshot current title
shot('pokerogue_title0.jpg')

# Move Down once (to New Game?) and shot, etc.
for i in range(6):
    key('ArrowDown','ArrowDown',40,90); time.sleep(0.35)
    shot(f'pokerogue_title_opt{i}.jpg')
    print('opt', i)

# Go back to top
for _ in range(8):
    key('ArrowUp','ArrowUp',38,80); time.sleep(0.12)
shot('pokerogue_title_top.jpg')
ws.close()
print('TITLE_READY')
