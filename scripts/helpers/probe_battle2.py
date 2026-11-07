import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"], timeout=15)
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
  r=call("Runtime.evaluate",{"expression":expr,"returnByValue":True})
  return ((r.get("result") or {}).get("result") or {}).get("value")
print(ev(r'''(() => {
  const out = {};
  try {
    const PG = (typeof Phaser!=='undefined' && Phaser.GAMES) ? Phaser.GAMES : null;
    out.hasPhaser = typeof Phaser!=='undefined';
    out.gamesLen = PG ? PG.length : null;
    const g = PG && PG[0];
    if (!g) return out;
    out.sceneKeys = (g.scene.scenes||[]).map(s => s?.sys?.settings?.key);
    // walk active scenes for enemy/field
    for (const sc of (g.scene.scenes||[])) {
      if (!sc || !sc.sys || !sc.sys.isActive()) continue;
      const key = sc.sys.settings.key;
      const bag = {key};
      for (const prop of Object.keys(sc)) {
        try {
          const v = sc[prop];
          if (!v) continue;
          if (prop.toLowerCase().includes('enemy') || prop.toLowerCase().includes('battle') || prop.toLowerCase().includes('field') || prop.toLowerCase().includes('arena') || prop.toLowerCase().includes('ui') || prop==='currentBattle' || prop==='battleScene') {
            bag[prop] = typeof v;
            if (v && typeof v==='object') {
              const sub = {};
              for (const k2 of Object.keys(v).slice(0,40)) {
                try { sub[k2] = typeof v[k2]; } catch(e){}
              }
              bag[prop+'_keys'] = sub;
            }
          }
        } catch(e){}
      }
      out['sc_'+key] = bag;
    }
  } catch(e) { out.err=String(e); }
  return out;
})()'''))
# Also try common pokerogue paths
print('---')
print(ev(r'''(() => {
  try {
    const g = Phaser.GAMES[0];
    const scenes = g.scene.scenes.filter(s=>s.sys.isActive());
    const battle = scenes.find(s => (s.sys.settings.key||'').toLowerCase().includes('battle')) || scenes[0];
    if (!battle) return {no:'battle'};
    // dump interesting arrays
    const cand = {};
    for (const k of ['enemies','enemyParty','field','arena','currentBattle','battleScene','uiContainer','ui','phaseQueue','phase']) {
      if (k in battle) cand[k] = true;
    }
    // recursive shallow find objects with .species or .types
    function find(obj, depth, path, acc) {
      if (depth>4 || !obj || typeof obj!=='object' || acc.length>20) return;
      try {
        if (obj.types && (obj.name || obj.species) && (obj.hp!=null || obj.currentHP!=null || obj.battleData)) {
          acc.push({path, name: obj.name||obj.species?.name, types: obj.types, hp: obj.hp||obj.currentHP});
        }
      } catch(e){}
      let keys=[];
      try { keys=Object.keys(obj).slice(0,30);} catch(e){return;}
      for (const k of keys) {
        if (['parent','scene','game','sys','input'].includes(k)) continue;
        try { find(obj[k], depth+1, path+'.'+k, acc); } catch(e){}
      }
    }
    const acc=[];
    find(battle, 0, 'battle', acc);
    return {scene: battle.sys.settings.key, cand, found: acc.slice(0,10)};
  } catch(e) { return {err:String(e)}; }
})()'''))
ws.close()
