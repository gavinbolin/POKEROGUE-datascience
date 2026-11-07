import json,urllib.request,websocket,time,base64
p=[t for t in json.load(urllib.request.urlopen('http://127.0.0.1:9222/json')) if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(p['webSocketDebuggerUrl'],timeout=30)
ws.send(json.dumps({'id':1,'method':'Page.captureScreenshot','params':{'format':'jpeg','quality':50}}))
while True:
  r=json.loads(ws.recv())
  if r.get('id')==1: open(r'C:\Users\gavin\agent-tools\endless_seen.jpg','wb').write(base64.b64decode(r['result']['data']));break
ws.send(json.dumps({'id':2,'method':'Page.reload'}))
