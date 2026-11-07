import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"], timeout=20)
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
  res=r.get("result") or {}
  if "exceptionDetails" in res:
    return {"exc": res["exceptionDetails"].get("text")}
  return (res.get("result") or {}).get("value")
print(ev(r'''(() => {
  const out={};
  out.phaserKeys = Object.keys(Phaser||{}).slice(0,40);
  out.GAMES = Phaser.GAMES;
  // canvas
  const c=document.querySelector('canvas');
  out.canvasKeys = c ? Object.getOwnPropertyNames(c).filter(k=>k.toLowerCase().includes('phaser')||k.toLowerCase().includes('game')).slice(0,20) : null;
  // walk __proto__ soft
  try {
    const keys=[];
    for (const k in window) {
      try {
        const v=window[k];
        if (v && v.scene && v.scene.scenes) keys.push(k);
        if (v && v.game && v.game.scene) keys.push(k+'.game');
      } catch(e){}
    }
    out.foundGameLike=keys.slice(0,20);
  } catch(e){}
  return out;
})()'''))
# Runtime getProperties on Phaser
print(ev(r'''(() => {
  // Pokemon Rogue often stores battle scene on a singleton
  const names = Object.getOwnPropertyNames(window).filter(n => /scene|battle|rogue|poke|game/i.test(n));
  return names.slice(0,80);
})()'''))
ws.close()
