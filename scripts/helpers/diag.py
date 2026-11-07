import json, urllib.request, websocket, time
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

# Focus canvas properly via tabIndex + click
print(ev(r'''(() => {
  const c=document.querySelector('canvas');
  c.tabIndex=0; c.focus();
  return document.activeElement===c ? 'canvas-focused' : document.activeElement.tagName;
})()'''))

# Check if RAF / game loop alive by watching a counter
print(ev(r'''(() => new Promise(resolve => {
  let n=0; const start=performance.now();
  function tick(){ n++; if(performance.now()-start>500) resolve({frames:n, dt:performance.now()-start}); else requestAnimationFrame(tick); }
  requestAnimationFrame(tick);
}))'''.replace('new Promise', '(async () => { return await new Promise') ))
# simpler:
r=call('Runtime.evaluate',{'expression':'''
new Promise(resolve => {
  let n=0; const start=performance.now();
  (function tick(){ n++; if(performance.now()-start>600) resolve({frames:n, dt:performance.now()-start}); else requestAnimationFrame(tick); })();
})
''','returnByValue':True,'awaitPromise':True})
print('raf', ((r.get('result') or {}).get('result') or {}).get('value'))

# Look for Phaser game via __PHASER or scene plugins
print(ev(r'''(() => {
  const out={};
  // Phaser 3 stores games in a private registry sometimes
  try {
    const gproto = Phaser.Game.prototype;
    out.hasGameProto = !!gproto;
  } catch(e){}
  // Search all script elements / modules - check for battle scene in closure via chrome
  // Try window['phaserGame'] variants
  for (const k of Object.getOwnPropertyNames(window)) {
    try {
      const v=window[k];
      if (v && typeof v==='object' && v.scene && v.scene.scenes) {
        out.found = k;
        out.scenes = v.scene.scenes.map(s=>s&&s.sys&&s.sys.settings&&s.sys.settings.key);
        break;
      }
    } catch(e){}
  }
  return out;
})()'''))

# Check gameInfo object for more fields / pause flag
print(ev(r'''(() => {
  const g=window.gameInfo||{};
  return {keys:Object.keys(g), full:g};
})()'''))
ws.close()
