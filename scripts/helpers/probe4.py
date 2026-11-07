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
  const app = window.app;
  const out = {appType: typeof app, appKeys: app ? Object.keys(app).slice(0,60) : null};
  try {
    // common: app.getBattleScene / app.scene / app.game
    out.hasGame = !!(app && app.game);
    out.hasGetBattleScene = !!(app && app.getBattleScene);
    out.sceneKeys = app && app.game && app.game.scene && app.game.scene.scenes
      ? app.game.scene.scenes.map(s => s && s.sys && s.sys.settings && s.sys.settings.key).filter(Boolean) : [];
    let scene = null;
    if (app && typeof app.getBattleScene === 'function') {
      try { scene = app.getBattleScene(); } catch(e) { out.getBattleSceneErr = String(e); }
    }
    if (!scene && app && app.game && app.game.scene && app.game.scene.scenes) {
      scene = app.game.scene.scenes.find(s => s && s.gameData) || app.game.scene.scenes.find(s => s && s.sys && s.sys.settings && s.sys.settings.active);
    }
    if (scene) {
      out.sceneKey = scene.sys && scene.sys.settings && scene.sys.settings.key;
      out.hasGameData = !!scene.gameData;
      out.uiMode = scene.ui && scene.ui.getMode ? String(scene.ui.getMode()) : null;
      try {
        if (scene.phaseManager && scene.phaseManager.getCurrentPhase) {
          const p = scene.phaseManager.getCurrentPhase();
          out.phase = p && p.constructor && p.constructor.name;
        }
      } catch(e){}
      if (scene.gameData && scene.gameData.starterData) {
        const z = scene.gameData.starterData[888] || scene.gameData.starterData['888'];
        out.zacian = z ? Object.fromEntries(Object.entries(z).slice(0,20)) : null;
        out.zacianCandy = z ? (z.candyCount ?? z.candies ?? null) : null;
      }
      if (scene.money != null) out.money = scene.money;
      if (scene.currentBattle) {
        out.battleWave = scene.currentBattle.waveIndex;
        out.double = !!scene.currentBattle.double;
      }
    }
  } catch(e) { out.err = String(e); out.stack = e.stack && e.stack.slice(0,500); }
  return out;
})()''')
print(json.dumps(info, indent=2, default=str)[:8000])
ws.close()
