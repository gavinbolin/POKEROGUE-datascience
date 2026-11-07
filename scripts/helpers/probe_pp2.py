import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"],timeout=15)
def ev(expr,i=1):
  ws.send(json.dumps({"id":i,"method":"Runtime.evaluate","params":{"expression":expr,"returnByValue":True}}))
  while True:
    m=json.loads(ws.recv())
    if m.get("id")==i: return m.get("result",{}).get("result",{}).get("value")
expr=r"""(() => {
  // dig for PP on battle pokemon moves
  const out = {found:null, paths:[]};
  function walk(o, path, depth) {
    if (!o || depth>6 || typeof o!=='object') return;
    try {
      if (Array.isArray(o)) {
        for (let i=0;i<Math.min(o.length,8);i++) walk(o[i], path+'['+i+']', depth+1);
        return;
      }
      const keys = Object.keys(o);
      if (keys.includes('ppUsed') || keys.includes('pp') || keys.includes('movePp') || (keys.includes('moveId') && keys.includes('ppUsed'))) {
        out.paths.push({path, keys: keys.slice(0,20), sample: JSON.parse(JSON.stringify(o, (k,v)=> typeof v==='object'&&v&&(v.scene||v.parent||v.sceneUI)?undefined:v , 2).slice? undefined : o)});
        try { out.found = {path, keys, vals: Object.fromEntries(Object.entries(o).filter(([k,v])=>typeof v!=='object').slice(0,15))}; } catch(e){}
      }
      for (const k of keys) {
        if (['scene','parent','game','children','displayList','input','sys','cameras','renderer','anims','cache','textures','sound','plugins','events','time','tweens'].includes(k)) continue;
        if (k.toLowerCase().includes('pp') || k==='moveset' || k==='moves' || k==='pokemon' || k==='party' || k==='battle' || k==='field' || k==='playerPokemon' || k==='getMoveset') {
          walk(o[k], path+'.'+k, depth+1);
        }
      }
    } catch(e){}
  }
  // try common globals
  const cands = [window.Phaser, window.game, window.Game, window.__PIXI];
  for (const c of cands) walk(c, 'cand', 0);
  // Phaser.GAMES
  try {
    const G = window.Phaser && window.Phaser.GAMES;
    if (G) {
      out.phaserGames = G.length;
      for (let i=0;i<G.length;i++) walk(G[i], 'Phaser.GAMES['+i+']', 0);
    }
  } catch(e){ out.phaserErr=String(e)}
  // search all window keys lightly
  for (const k of Object.keys(window)) {
    if (/game|phaser|pokerogue|battle|scene/i.test(k)) {
      try { walk(window[k], 'window.'+k, 0); } catch(e){}
    }
  }
  return {n: out.paths.length, first: out.found, phaserGames: out.phaserGames, samplePaths: out.paths.slice(0,5).map(p=>({path:p.path, keys:p.keys}))};
})()"""
print(json.dumps(ev(expr), indent=2)[:4000])
ws.close()
