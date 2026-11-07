import json,urllib.request,websocket,time,base64,sys
p=[t for t in json.load(urllib.request.urlopen('http://127.0.0.1:9222/json')) if t.get('type')=='page' and 'pokerogue.net' in t.get('url','')][0]
ws=websocket.create_connection(p['webSocketDebuggerUrl'],timeout=30);n=[0]
def call(m,pr=None):
  n[0]+=1;ws.send(json.dumps({'id':n[0],'method':m,'params':pr or {}}))
  while True:
    r=json.loads(ws.recv())
    if r.get('id')==n[0]:return r
K={'d':('ArrowDown',40),'u':('ArrowUp',38),'z':('z',90),'r':('ArrowRight',39)}
for c in (sys.argv[1] if len(sys.argv)>1 else ''):
  k,kc=K[c];a={'type':'keyDown','key':k,'code':'KeyZ' if k=='z' else k,'windowsVirtualKeyCode':kc}
  if k=='z':a['text']='z'
  call('Input.dispatchKeyEvent',a);time.sleep(.1);call('Input.dispatchKeyEvent',{'type':'keyUp','key':k,'code':a['code'],'windowsVirtualKeyCode':kc});time.sleep(.6)
time.sleep(1)
r=call('Page.captureScreenshot',{'format':'jpeg','quality':50});open(r'C:\Users\gavin\agent-tools\st.jpg','wb').write(base64.b64decode(r['result']['data']))
print(call('Runtime.evaluate',{'expression':'JSON.stringify(window.gameInfo&&{m:gameInfo.gameMode,w:gameInfo.wave})','returnByValue':True})['result']['result'].get('value'))
