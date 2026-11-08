import json,asyncio,websockets,urllib.request,sys
src=open("pr_farm17.py",encoding="utf-8").read()
HOOK=src.split('HOOK_JS = """')[1].split('"""')[0]
STEP=src.split('STEP_JS = """')[1].split('"""')[0]
H="window.__pr_cam.scene.ui.getHandler()"
ST="(()=>{const s=window.__pr_cam.scene;const h=s.ui.getHandler();const g=s.gameData;return JSON.stringify({h:h.constructor.name,c:h.cursor,o:h.config?.options?.map(o=>o.label),eggs:g.eggs?.length,z:g.starterData[890].candyCount,t:g.starterData[602].candyCount,f:g.starterData[349].candyCount,m:g.starterData[258].candyCount,v:g.voucherCounts,party:h.partyStarterIds})})()"
async def main():
    p=next(x for x in json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list")) if x.get("type")=="page" and x.get("url","").startswith("https://pokerogue.net/"))
    async with websockets.connect(p["webSocketDebuggerUrl"],max_size=50_000_000) as ws:
        n=[0]
        async def ev(e):
            n[0]+=1;await ws.send(json.dumps({"id":n[0],"method":"Runtime.evaluate","params":{"expression":e,"returnByValue":True}}))
            while True:
                r=json.loads(await ws.recv())
                if r.get("id")==n[0]:return r.get("result",{}).get("result",{}).get("value")
        async def step(k=20):
            for _ in range(k): await ev(STEP); await asyncio.sleep(0.03)
        async def st(): return json.loads(await ev(ST))
        async def pick(label):
            s=await st(); o=s["o"] or []
            i=next((j for j,x in enumerate(o) if x==label or (label.endswith('*') and x.startswith(label[:-1]))),None)
            assert i is not None,(label,s)
            await ev(f"{H}.setCursor({i})"); await step(5)
            assert (await st())["c"]==i
            await ev(f"{H}.processInput(5)"); await step(25)
        async def nav(sp):
            idx=await ev(f"{H}.filteredStarterIds.indexOf({sp})"); assert idx>=0
            for _ in range(80):
                a=await ev(f"{H}.cursor+{H}.scrollCursor*9")
                if a==idx: break
                r,c=divmod(idx,9); r0,c0=divmod(a,9)
                await ev(f"{H}.processInput({1 if r>r0 else 0 if r<r0 else 3 if c>c0 else 2})"); await step(6)
            assert await ev(f"{H}.filteredStarterIds[{H}.cursor+{H}.scrollCursor*9]")==sp
        await ev(HOOK)
        mode=sys.argv[1]
        if mode=="newgame":
            s=await st(); assert s["h"]=="TitleUiHandler",s
            await pick("New Game"); s=await st(); print(s)
            await pick("Classic"); print(await st())
        elif mode=="open":
            sp=int(sys.argv[2]); await nav(sp); await ev(f"{H}.processInput(5)"); await step(20); print(await st())
        elif mode=="pick":
            await pick(sys.argv[2]); print(await st())
        elif mode=="cancel":
            await ev(f"{H}.processInput(6)"); await step(15); print(await st())
        elif mode=="buyegg":
            s=await st(); o=s["o"] or []; i=next(j for j,x in enumerate(o) if "Buy an Egg" in x)
            await ev(f"{H}.setCursor({i})"); await step(5); assert (await st())["c"]==i
            await ev(f"{H}.processInput(5)"); await step(30); print(await st())
        elif mode=="start":
            _C=r"C:\Users\gavin\agent-tools\pokerogue_farm_config.json"; _cf=json.load(open(_C,encoding="utf-8-sig"))
            if _cf.get("pending_next_run"): _nx=_cf.pop("pending_next_run"); _cf.update(primary=_nx["primary"],secondary=_nx["secondary"]); json.dump(_cf,open(_C,"w",encoding="utf-8"),indent=2); print("applied pending_next_run",_nx)  # t232u
            _pid=_cf.get("primary",150); assert (await ev(f"{H}.partyStarterIds"))[0]==int(_pid)  # MEWABSOL: lead = config primary
            for k in [3]*12+[1]*14:
                if await ev(f"{H}.startCursorObj.visible"): break
                await ev(f"{H}.processInput({k})"); await step(6)
            assert await ev(f"{H}.startCursorObj.visible")
            await ev(f"{H}.processInput(5)"); await step(25); print(await st())
            await ev(f"{H}.processInput(5)"); await step(40)
            print(await ev(f"(()=>{{const h={H};return JSON.stringify({{n:h.constructor.name,c:h.cursor,sc:h.scrollCursor,slots:(h.sessionSlots||[]).map(s=>[s.slotId,s.hasData])}})}})()"))
        elif mode=="slot":
            sl=int(sys.argv[2]); assert await ev(f"{H}.constructor.name")=="SaveSlotSelectUiHandler"
            hd=await ev(f"{H}.sessionSlots[{sl}].hasData"); assert hd is False, ("occupied",hd)
            for _ in range(6):
                if await ev(f"{H}.cursor+{H}.scrollCursor")==sl: break
                await ev(f"{H}.processInput(1)"); await step(8)
            assert await ev(f"{H}.cursor+{H}.scrollCursor")==sl
            await ev(f"{H}.processInput(5)"); await step(40)
            nm=await ev(f"{H}.constructor.name"); print("after",nm)
            assert nm!="ConfirmUiHandler","overwrite prompt?!"
            await step(120); print(await ev("JSON.stringify([window.gameInfo.gameMode,window.gameInfo.wave,window.__pr_cam.scene.sessionSlotId,window.__pr_cam.scene.gameMode?.modeId,window.__pr_cam.scene.getPlayerParty().map(p=>p.species.speciesId)])"))
        elif mode=="key":
            for k in sys.argv[2].split(","):
                assert k!="7"
                await ev(f"{H}.processInput({k})"); await step(15)
                print(k, await ev(f"(()=>{{const h={H};return JSON.stringify([h.constructor.name,h.cursor,h.scrollCursor,h.partyCursorObj?.visible,h.partyIconsCursorIndex,h.startCursorObj?.visible,h.randomCursorObj?.visible])}})()"))
        elif mode=="eternmoves":  # t204u: Eternatus starter moveset Malignant Chain, Dragon Energy, Body Press, Poison Tail
            want=[919,820,776,342]
            print(await ev(f"""(()=>{{const s=window.__pr_cam.scene;const g=s.gameData;g.starterData[890].moveset={json.dumps(want)};const h=s.ui.getHandler();let ps=null;
            if(h.constructor.name=='StarterSelectUiHandler'&&h.partyStarterIds){{const i=h.partyStarterIds.indexOf(890);if(i>=0&&h.partyStarters&&h.partyStarters[i]){{h.partyStarters[i].moveset={json.dumps(want)};ps=h.partyStarters[i].moveset}}}}
            return JSON.stringify({{sd:g.starterData[890].moveset,eggMoves:g.starterData[890].eggMoves,partyMoveset:ps,h:h.constructor.name}})}})()"""))
        elif mode=="reduce":  # Spend candy only: reductions first, then same-species eggs.
            async def close_candy_menu():
                # Purchases return directly to starter select; failed purchases stay in options.
                for _ in range(2):
                    s=await st()
                    if s["h"]=="StarterSelectUiHandler": return
                    assert s["h"]=="OptionSelectUiHandler",s
                    await pick("Cancel")
                assert (await st())["h"]=="StarterSelectUiHandler"
            for sp in [int(x) for x in sys.argv[2].split(",")]:
                for _ in range(102):  # At most two reductions plus the 99-egg capacity.
                    assert (await st())["h"]=="StarterSelectUiHandler"
                    await nav(sp); await ev(f"{H}.processInput(5)"); await step(20)
                    s=await st(); o=s["o"] or []
                    if "Use Candies" in o:
                        await pick("Use Candies")
                        s=await st(); o=s["o"] or []
                    i=next((j for j,x in enumerate(o) if "reduce" in x.lower() and "cost" in x.lower()),None)
                    action="reduce"
                    if i is None:
                        i=next((j for j,x in enumerate(o) if "buy an egg" in x.lower()),None)
                        action="buyegg"
                    if i is None:
                        print(sp,"no candy purchase option",o)
                        await close_candy_menu(); break
                    await ev(f"{H}.setCursor({i})"); await step(5); assert (await st())["c"]==i
                    c0=await ev(f"window.__pr_cam.scene.gameData.starterData[{sp}].candyCount")
                    await ev(f"{H}.processInput(5)"); await step(25)
                    c1=await ev(f"window.__pr_cam.scene.gameData.starterData[{sp}].candyCount")
                    print(sp,action,o[i],"candy",c0,"->",c1,"vr",await ev(f"window.__pr_cam.scene.gameData.starterData[{sp}].valueReduction"))
                    await close_candy_menu()
                    if c1==c0: break  # Insufficient candy or full egg inventory: do not loop.
        elif mode=="eternverify":
            print(await ev("JSON.stringify(window.__pr_cam.scene.getPlayerParty().filter(p=>p.species.speciesId==890).map(p=>p.moveset.map(m=>m.getName())))"))
        else: print(await st())
asyncio.run(main())

