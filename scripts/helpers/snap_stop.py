import json,urllib.request,websocket
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list",timeout=5))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
ws=websocket.create_connection(pr["webSocketDebuggerUrl"],timeout=8)
ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":"JSON.stringify(window.gameInfo||null)","returnByValue":True}}))
while True:
 m=json.loads(ws.recv())
 if m.get("id")==1:
  print(m.get("result",{}).get("result",{}).get("value"))
  break
ws.close()
