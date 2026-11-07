import json,asyncio,websockets,urllib.request
async def m():
    pg=next(p for p in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if p.get("type")=="page" and p["url"].startswith("https://pokerogue.net"))
    async with websockets.connect(pg["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        async def ev(e):
            await ws.send(json.dumps({"id":1,"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==1: return r
        r=await ev("""(()=>{const o={};o.phaser=typeof Phaser; o.games=(window.Phaser&&Phaser.GAMES)?Phaser.GAMES.length:null;
        o.keys=Object.keys(window).filter(k=>!/^(on|webkit)/.test(k)).slice(-60);
        o.gi=Object.keys(window.gameInfo||{}); o.p0=JSON.stringify((window.gameInfo||{}).party?.[0]).slice(0,600);
        o.enemy=JSON.stringify(window.gameInfo?.enemyParty||window.gameInfo?.enemy||null)?.slice(0,600);return o})()""")
        print(json.dumps(r,indent=1)[:4000])
asyncio.run(m())
