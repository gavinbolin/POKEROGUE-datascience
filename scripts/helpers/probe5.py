import json, urllib.request, websocket
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
wsurl=[t['webSocketDebuggerUrl'] for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(wsurl, timeout=20)
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
    res=r.get('result') or {}
    if res.get('exceptionDetails'):
        return {'__exc': res['exceptionDetails']}
    return (res.get('result') or {}).get('value')
# Search webpack modules / poke scene
info=ev(r'''(() => {
  // Phaser.GAMES may be array-like with holes; also check Phaser.GameInstances
  const out = {};
  try {
    out.GAMES_type = typeof Phaser.GAMES;
    out.GAMES_str = String(Phaser.GAMES);
    if (Phaser.GAMES) {
      out.len = Phaser.GAMES.length;
      out.vals = [];
      for (let i=0;i<10;i++) {
        const g = Phaser.GAMES[i];
        if (g) out.vals.push({i, scenes: g.scene && g.scene.scenes && g.scene.scenes.length});
      }
    }
  } catch(e){ out.e1=String(e); }
  // walk document for __vue__ or phaser
  const canvas = document.querySelector('canvas');
  out.canvasKeys = canvas ? Object.getOwnPropertyNames(canvas).filter(k=>/game|phaser|scene/i.test(k)) : [];
  out.parentKeys = canvas && canvas.parentElement ? Object.getOwnPropertyNames(canvas.parentElement).slice(0,30) : [];
  // Check indexedDB names
  return out;
})()''')
print('A', json.dumps(info, indent=2)[:3000])
# Try Runtime.getProperties on Phaser
r=call('Runtime.evaluate',{'expression':'Phaser','returnByValue':False})
objId=((r.get('result') or {}).get('result') or {}).get('objectId')
print('Phaser objectId', objId)
if objId:
    props=call('Runtime.getProperties',{'objectId':objId,'ownProperties':True})
    names=[p['name'] for p in ((props.get('result') or {}).get('result') or [])]
    print('Phaser props sample', names[:40])
ws.close()
