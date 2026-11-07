import json, urllib.request, websocket, base64, pathlib
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
call('Page.bringToFront')
shot=call('Page.captureScreenshot',{'format':'jpeg','quality':70})
pathlib.Path(r'C:\Users\gavin\agent-tools\pokerogue_live_now.jpg').write_bytes(base64.b64decode(shot['result']['data']))
print('shot saved')
info=ev(r'''(() => {
  const out = {};
  out.gameInfo = window.gameInfo ? {mode:window.gameInfo.gameMode,wave:window.gameInfo.wave,biome:window.gameInfo.biome,playTime:window.gameInfo.playTime,luck:window.gameInfo.luck,money:window.gameInfo.money} : null;
  out.hasPhaser = typeof Phaser !== 'undefined';
  out.phaserGames = (typeof Phaser !== 'undefined' && Phaser.GAMES) ? Phaser.GAMES.length : 0;
  try {
    const g = (typeof Phaser !== 'undefined' && Phaser.GAMES && Phaser.GAMES[0]) ? Phaser.GAMES[0] : null;
    out.sceneKeys = g && g.scene && g.scene.scenes ? g.scene.scenes.map(s => s && s.sys && s.sys.settings && s.sys.settings.key).filter(Boolean) : [];
    const active = g && g.scene && g.scene.scenes ? g.scene.scenes.find(s => s && s.sys && s.sys.settings && s.sys.settings.active) : null;
    out.activeKey = active && active.sys && active.sys.settings && active.sys.settings.key;
    out.hasGameData = !!(active && active.gameData);
    out.hasGameMode = !!(active && active.gameMode);
    // candy from gameData.starterData
    if (active && active.gameData && active.gameData.starterData) {
      const z = active.gameData.starterData[888] || active.gameData.starterData['888'];
      out.zacianStarter = z ? {candyCount: z.candyCount, candies: z.candies, valueReduction: z.valueReduction, keys: Object.keys(z)} : null;
      // sample a few starter entries
      const sample = {};
      let n=0;
      for (const [k,v] of Object.entries(active.gameData.starterData)) {
        if (v && (v.candyCount||v.candies)) { sample[k]=v.candyCount??v.candies; n++; if(n>=5) break; }
      }
      out.starterCandySample = sample;
    }
    // ui handlers
    out.uiMode = active && active.ui && active.ui.getMode ? String(active.ui.getMode()) : null;
    out.currentBattle = !!(active && active.currentBattle);
    out.phase = active && active.currentBattle && active.currentBattle.turn ? 'battle-turn' : null;
    if (active && active.phaseManager && active.phaseManager.getCurrentPhase) {
      try { const p = active.phaseManager.getCurrentPhase(); out.phaseName = p && (p.constructor && p.constructor.name); } catch(e){}
    }
  } catch(e) { out.err = String(e); }
  return out;
})()''')
print(json.dumps(info, indent=2, default=str)[:8000])
ws.close()
