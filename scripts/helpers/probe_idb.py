import json, urllib.request, websocket, pathlib
# dump indexedDB / localStorage keys related to candy
tabs=json.load(urllib.request.urlopen('http://127.0.0.1:9222/json'))
wsurl=[t['webSocketDebuggerUrl'] for t in tabs if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(wsurl, timeout=30)
nid=[0]
def call(method, params=None):
    nid[0]+=1
    msg={'id':nid[0],'method':method}
    if params is not None: msg['params']=params
    ws.send(json.dumps(msg))
    while True:
        r=json.loads(ws.recv())
        if r.get('id')==nid[0]: return r
def ev(expr, await_promise=False):
    r=call('Runtime.evaluate',{'expression':expr,'returnByValue':True,'awaitPromise':await_promise})
    return ((r.get('result') or {}).get('result') or {}).get('value')
keys=ev('Object.keys(localStorage)')
print('ls keys', keys)
info=ev(r'''(() => new Promise(async (resolve) => {
  try {
    const dbs = await indexedDB.databases();
    const out = {dbs};
    for (const dbinfo of dbs) {
      const name = dbinfo.name;
      const db = await new Promise((res,rej)=>{const r=indexedDB.open(name); r.onsuccess=()=>res(r.result); r.onerror=()=>rej(r.error);});
      const storeNames = Array.from(db.objectStoreNames);
      out[name] = {stores: storeNames};
      for (const sn of storeNames.slice(0,8)) {
        try {
          const tx = db.transaction(sn, 'readonly');
          const store = tx.objectStore(sn);
          const all = await new Promise((res,rej)=>{const r=store.getAll(); r.onsuccess=()=>res(r.result); r.onerror=()=>rej(r.error);});
          // summarize
          out[name][sn] = {count: all.length, sample: all.slice(0,2).map(x => {
            if (x && typeof x === 'object') {
              const o = {};
              for (const k of Object.keys(x).slice(0,30)) {
                const v = x[k];
                if (v && typeof v === 'object') o[k] = Array.isArray(v) ? `arr:${v.length}` : `obj:${Object.keys(v).slice(0,10).join(',')}`;
                else o[k] = v;
              }
              return o;
            }
            return x;
          })};
        } catch(e) { out[name][sn] = String(e); }
      }
      db.close();
    }
    resolve(out);
  } catch(e) { resolve({err:String(e)}); }
}))''', await_promise=True)
print(json.dumps(info, indent=2, default=str)[:10000])
ws.close()
