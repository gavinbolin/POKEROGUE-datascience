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

call('Page.bringToFront')
# get canvas box
box=ev(r'''(() => {
  const c=document.querySelector('canvas');
  if(!c) return null;
  const r=c.getBoundingClientRect();
  return {x:r.x,y:r.y,w:r.width,h:r.height, aw:c.width, ah:c.height};
})()''')
print('box', box)
# click center of canvas
cx = box['x'] + box['w']/2
cy = box['y'] + box['h']/2
call('Input.dispatchMouseEvent', {'type':'mousePressed','x':cx,'y':cy,'button':'left','clickCount':1})
time.sleep(0.05)
call('Input.dispatchMouseEvent', {'type':'mouseReleased','x':cx,'y':cy,'button':'left','clickCount':1})
time.sleep(0.3)
ev("document.querySelector('canvas').focus()")
# try Space / Z / Enter once each carefully
for key,code,kc in [(' ','Space',32),('z','KeyZ',90)]:
    call('Input.dispatchKeyEvent', {'type':'keyDown','windowsVirtualKeyCode':kc,'code':code,'key':key, **({'text':key} if key.strip() else {})})
    time.sleep(0.12)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':kc,'code':code,'key':key})
    time.sleep(0.6)
    print(key, ev('window.gameInfo.playTime'))

# Check document visibility / paused
print('vis', ev("document.visibilityState + ' ' + document.hasFocus()"))
# Try to find Phaser game instance via webpack or scene systems
info=ev(r'''(() => {
  // scan for objects with gameData on window properties deeply? too heavy
  // check performance: are RAF callbacks running?
  return {
    hidden: document.hidden,
    visibility: document.visibilityState,
    hasFocus: document.hasFocus(),
    bodyActive: document.activeElement && document.activeElement.tagName
  };
})()''')
print('focus', info)

# Try CDP Input with commands for rawKeyDown
for i in range(6):
    call('Input.dispatchKeyEvent', {'type':'rawKeyDown','windowsVirtualKeyCode':90,'code':'KeyZ','key':'z'})
    time.sleep(0.1)
    call('Input.dispatchKeyEvent', {'type':'char','windowsVirtualKeyCode':90,'code':'KeyZ','key':'z','text':'z','unmodifiedText':'z'})
    time.sleep(0.05)
    call('Input.dispatchKeyEvent', {'type':'keyUp','windowsVirtualKeyCode':90,'code':'KeyZ','key':'z'})
    time.sleep(0.5)
print('after raw', ev('window.gameInfo.playTime'), 'wave', ev('window.gameInfo.wave'))

shot=call('Page.captureScreenshot',{'format':'jpeg','quality':65})
pathlib.Path(r'C:\Users\gavin\agent-tools\pokerogue_after_click.jpg').write_bytes(base64.b64decode(shot['result']['data']))
ws.close()
