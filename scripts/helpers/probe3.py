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
    return ((r.get('result') or {}).get('result') or {}).get('value')
info=ev(r'''(() => {
  const keys = Object.keys(window).filter(k => /game|phaser|rogue|scene/i.test(k)).slice(0,80);
  let phaserInfo = null;
  try {
    if (typeof Phaser !== 'undefined') {
      phaserInfo = {
        version: Phaser.VERSION,
        gamesLen: Phaser.GAMES ? Phaser.GAMES.length : null,
        gameKeys: Phaser.GAMES ? Object.keys(Phaser.GAMES) : null,
        hasGame: !!Phaser.Game
      };
    }
  } catch(e){}
  // look for canvas and attached game
  const canvas = document.querySelector('canvas');
  let canvasGame = null;
  try {
    if (canvas) {
      canvasGame = {
        hasParent: !!canvas.parentElement,
        w: canvas.width, h: canvas.height,
        // Phaser often stores game on canvas
        gameOnCanvas: !!(canvas.game || (canvas.__phaser) || (canvas.parentElement && canvas.parentElement.game))
      };
    }
  } catch(e){}
  // poke common globals used by pokerogue forks
  const candidates = ['game','Game','phaserGame','pokerogue','app','currentBattleScene'];
  const found = {};
  for (const c of candidates) {
    try { found[c] = typeof window[c]; } catch(e){ found[c]='err'; }
  }
  return {keys, phaserInfo, canvasGame, found, title: document.title};
})()''')
print(json.dumps(info, indent=2, default=str)[:6000])
ws.close()
