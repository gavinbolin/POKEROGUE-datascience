import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"], timeout=12)
nid=[0]
def call(method,params=None):
  nid[0]+=1
  m={"id":nid[0],"method":method}
  if params is not None: m["params"]=params
  ws.send(json.dumps(m))
  while True:
    r=json.loads(ws.recv())
    if r.get("id")==nid[0]: return r
def ev(expr):
  r=call("Runtime.evaluate",{"expression":expr,"returnByValue":True,"awaitPromise":False})
  return ((r.get("result") or {}).get("result") or {}).get("value")
# Probe for enemy / battle UI / scene hooks
print(ev(r'''(() => {
  const g = window.gameInfo || {};
  const out = {gameInfoKeys: Object.keys(g), party0: (g.party||[])[0]};
  // search window for battle-ish objects
  const hits = [];
  for (const k of Object.getOwnPropertyNames(window)) {
    try {
      const v = window[k];
      if (!v || typeof v !== 'object') continue;
      const s = Object.prototype.toString.call(v);
      if (k.toLowerCase().includes('battle') || k.toLowerCase().includes('enemy') || k.toLowerCase().includes('poke')) hits.push(k);
    } catch(e) {}
  }
  out.windowHits = hits.slice(0,40);
  // Phaser games
  try {
    if (window.Phaser && Phaser.GAMES) {
      out.phaserGames = Phaser.GAMES.length;
      const game = Phaser.GAMES[0];
      if (game && game.scene && game.scene.scenes) {
        out.scenes = game.scene.scenes.map(sc => sc && sc.sys && sc.sys.settings && sc.sys.settings.key);
      }
    }
  } catch(e) { out.phaserErr = String(e); }
  return out;
})()'''))
ws.close()
