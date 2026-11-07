import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"],timeout=20)
def ev(expr,i=1):
  ws.send(json.dumps({"id":i,"method":"Runtime.evaluate","params":{"expression":expr,"returnByValue":True,"awaitPromise":False}}))
  while True:
    m=json.loads(ws.recv())
    if m.get("id")==i:
      return m
expr=r"""(() => {
  const out = {errors:[], hits:[]};
  // stringify search via toString of functions / localStorage dump size
  try {
    const ls = {};
    for (let i=0;i<localStorage.length;i++){ const k=localStorage.key(i); if(/game|save|session|pokerogue/i.test(k)) ls[k]= (localStorage.getItem(k)||'').slice(0,80); }
    out.lsKeys = Object.keys(ls);
  } catch(e){out.errors.push(String(e))}
  // Hook: look for canvas __vue / __svelte / react fiber? unlikely
  // Try accessing Phaser via canvas game
  const canvas = document.querySelector('canvas');
  out.canvasKeys = canvas ? Object.keys(canvas).filter(k=>k.startsWith('__')||/phaser|game/i.test(k)).slice(0,20) : null;
  // Search all properties on window for objects with getPlayerPokemon or similar
  const interesting = [];
  for (const k of Object.getOwnPropertyNames(window)) {
    try {
      const v = window[k];
      if (!v || typeof v !== 'object') continue;
      const ks = Object.getOwnPropertyNames(v).concat(Object.keys(v));
      if (ks.some(x=>/pokemon|battle|moveset|ppUsed|scene/i.test(x))) interesting.push({k, ks: ks.filter(x=>/pokemon|battle|move|pp|scene|party|field/i.test(x)).slice(0,15)});
    } catch(e){}
  }
  out.interesting = interesting.slice(0,30);
  // gameInfo enemy?
  const g = window.gameInfo||{};
  out.gameInfoKeys = Object.keys(g);
  out.enemies = g.enemies || g.enemyParty || g.foes || null;
  out.arena = g.arena || null;
  // try call gameInfo methods
  for (const k of Object.keys(g)) {
    if (typeof g[k]==='function') out.giFuncs=(out.giFuncs||[]).concat(k);
  }
  return out;
})()"""
r=ev(expr)
print(json.dumps(r.get("result",{}).get("result",{}).get("value"), indent=2)[:5000])
ws.close()
