import json,urllib.request,websocket,base64
p=[t for t in json.load(urllib.request.urlopen('http://127.0.0.1:9222/json')) if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(p['webSocketDebuggerUrl'],timeout=30)
def call(i,m,pr):
  ws.send(json.dumps({'id':i,'method':m,'params':pr}))
  while True:
    r=json.loads(ws.recv())
    if r.get('id')==i: return r
r=call(1,'Page.captureScreenshot',{'format':'jpeg','quality':50});open(r'C:\Users\gavin\agent-tools\watch_now.jpg','wb').write(base64.b64decode(r['result']['data']))
e="JSON.stringify({gi:window.gameInfo&&{m:gameInfo.gameMode,w:gameInfo.wave,party:(gameInfo.party||[]).map(p=>p.name+':'+p.hp)}})"
print(call(2,'Runtime.evaluate',{'expression':e,'returnByValue':True})['result']['result'].get('value'))
