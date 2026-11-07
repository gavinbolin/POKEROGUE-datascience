import json,urllib.request,websocket,base64,pathlib
tabs=json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
pr=[t for t in tabs if t.get("type")=="page" and "pokerogue" in t.get("url","").lower()][0]
# Don't steal long - quick shot via new connection may kick farm; use evaluate only through farm... 
# brief connection for screenshot only
ws=websocket.create_connection(pr["webSocketDebuggerUrl"], timeout=10)
nid=[0]
def call(method,params=None):
  nid[0]+=1
  msg={"id":nid[0],"method":method}
  if params is not None: msg["params"]=params
  ws.send(json.dumps(msg))
  while True:
    r=json.loads(ws.recv())
    if r.get("id")==nid[0]: return r
r=call("Page.captureScreenshot",{"format":"jpeg","quality":60})
pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_farm12_now.jpg").write_bytes(base64.b64decode(r["result"]["data"]))
print("shot ok")
ws.close()
