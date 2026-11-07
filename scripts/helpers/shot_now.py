import json, urllib.request, websocket, base64, pathlib
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
call('Page.bringToFront')
shot=call('Page.captureScreenshot',{'format':'jpeg','quality':70})
pathlib.Path(r'C:\Users\gavin\agent-tools\pokerogue_stuck_now.jpg').write_bytes(base64.b64decode(shot['result']['data']))
print(ev("JSON.stringify({t:window.gameInfo.playTime,w:window.gameInfo.wave,m:window.gameInfo.gameMode,b:window.gameInfo.biome})"))
ws.close()
print('saved')
