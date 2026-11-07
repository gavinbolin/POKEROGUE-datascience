import json, urllib.request, websocket
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
wsurl=[t['webSocketDebuggerUrl'] for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(wsurl, timeout=15)
def ev(expr):
    ws.send(json.dumps({'id':1,'method':'Runtime.evaluate','params':{'expression':expr,'returnByValue':True,'awaitPromise':False}}))
    while True:
        r=json.loads(ws.recv())
        if r.get('id')==1:
            return r.get('result',{}).get('result',{}).get('value')
s=ev(r'''(() => {
  const raw = localStorage.getItem('settings');
  const s = raw ? JSON.parse(raw) : {};
  const g = s.general || {};
  return {
    gameSpeed: g.gameSpeed,
    hpBarSpeed: g.hpBarSpeed,
    expGainSpeed: g.expGainSpeed,
    expGainsSpeed: g.expGainsSpeed,
    partyExpNotificationMode: g.partyExpNotificationMode,
    eggSkipPreference: g.eggSkipPreference,
    battleStyle: g.battleStyle,
    enableTutorials: g.enableTutorials,
    skipSeenDialogues: g.skipSeenDialogues,
    levelMoveConfirmation: g.levelMoveConfirmation,
    generalKeys: Object.keys(g).sort()
  };
})()''')
print('SETTINGS', json.dumps(s, indent=2))
info=ev(r'''(() => {
  const g = window.gameInfo || {};
  let candy = null;
  try {
    // try common paths for starter candy
    const scene = window.game && window.game.scene && window.game.scene.scenes
      ? window.game.scene.scenes.find(sc => sc && sc.gameData)
      : null;
    const gd = scene && scene.gameData;
    if (gd && gd.dexData) {
      // Zacian species id often 888
      const ids = [888, '888', 888001];
      for (const id of ids) {
        const d = gd.dexData[id];
        if (d && (d.candies != null || d.candyCount != null)) {
          candy = {id, candies: d.candies ?? d.candyCount, keys: Object.keys(d)};
          break;
        }
      }
      if (!candy) {
        // scan for Zacian-like
        for (const [k,v] of Object.entries(gd.dexData)) {
          if (v && typeof v === 'object' && (v.candies||v.candyCount) && String(k).includes('888')) {
            candy = {id:k, candies:v.candies??v.candyCount}; break;
          }
        }
      }
    }
    // also try starterData
    let starterCandy = null;
    if (gd && gd.starterData) {
      const z = gd.starterData[888] || gd.starterData['888'];
      if (z) starterCandy = {candies: z.candyCount ?? z.candies, keys: Object.keys(z)};
    }
    return {
      mode: g.gameMode, wave: g.wave, biome: g.biome, playTime: g.playTime, luck: g.luck,
      money: g.money, candy, starterCandy,
      hasGame: !!window.game,
      sceneNames: (window.game && window.game.scene && window.game.scene.scenes) ? window.game.scene.scenes.map(s=>s&&s.scene&&s.scene.key).filter(Boolean) : []
    };
  } catch(e) { return {err: String(e), mode:g.gameMode, wave:g.wave}; }
})()''')
print('INFO', json.dumps(info, indent=2, default=str)[:5000])
ws.close()
