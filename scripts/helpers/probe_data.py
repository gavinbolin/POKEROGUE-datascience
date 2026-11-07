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
  const raw = localStorage.getItem('data_PHOR');
  if (!raw) return {empty:true};
  let data;
  try { data = JSON.parse(raw); } catch(e) { return {parseErr:String(e), len: raw.length, head: raw.slice(0,200)}; }
  const out = {topKeys: data && typeof data==='object' ? Object.keys(data) : typeof data, len: raw.length};
  // dig for candy / starter
  function findCandy(obj, path, depth) {
    if (!obj || depth>5) return null;
    if (typeof obj !== 'object') return null;
    if (obj.candyCount != null || obj.candies != null) return {path, candyCount: obj.candyCount ?? obj.candies, keys: Object.keys(obj).slice(0,20)};
    for (const [k,v] of Object.entries(obj)) {
      if (/candy|starter|dex/i.test(k)) {
        const hit = findCandy(v, path+'.'+k, depth+1);
        if (hit) return hit;
        if (v && typeof v==='object' && !Array.isArray(v)) {
          // check 888
          if (v[888] || v['888']) {
            const z = v[888]||v['888'];
            return {path: path+'.'+k+'[888]', candyCount: z.candyCount??z.candies, keys: Object.keys(z).slice(0,25), zsample: Object.fromEntries(Object.entries(z).slice(0,15))};
          }
        }
      }
    }
    return null;
  }
  out.candyHit = findCandy(data, 'root', 0);
  // also check starterData directly
  if (data.starterData) {
    const z = data.starterData[888]||data.starterData['888'];
    out.starter888 = z ? Object.fromEntries(Object.entries(z).slice(0,20)) : null;
    out.starterCount = Object.keys(data.starterData).length;
  }
  if (data.dexData) {
    const z = data.dexData[888]||data.dexData['888'];
    out.dex888 = z ? Object.fromEntries(Object.entries(z).slice(0,20)) : null;
  }
  // maybe nested under .data
  for (const k of ['data','playerData','gameData','saveData']) {
    if (data[k] && typeof data[k]==='object') {
      out['nest_'+k] = Object.keys(data[k]).slice(0,30);
      if (data[k].starterData) {
        const z = data[k].starterData[888]||data[k].starterData['888'];
        out['nest_'+k+'_888'] = z ? Object.fromEntries(Object.entries(z).slice(0,20)) : 'no888';
      }
    }
  }
  return out;
})()''')
print(json.dumps(info, indent=2, default=str)[:12000])
ws.close()
