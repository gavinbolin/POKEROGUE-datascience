p='pr_farm17.py'; s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert a in s, a[:60]; s=s.replace(a,b,1)
R('"""PokeRogue farm15','"""PokeRogue farm17 (from farm16: ME top option + watchdog, PP item move targeting, faint vs switch-out, Zacian HP log)\nPokeRogue farm15')
s=s.replace('log(f"START farm16','log(f"START farm17').replace('"script": "pr_farm16.py"','"script": "pr_farm17.py"').replace('log("DONE farm16")','log("DONE farm17")')
# JS: party option labels
R('PP_ITEMS = [','OPT_LABELS_JS = """(()=>{try{const h=window.__pr_cam.scene.ui.getHandler();const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type===\'Text\'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return String(e)}})()"""\nPP_ITEMS = [')
R('async def Z(): await key("z", "KeyZ", 90)','async def Z(): await key("z", "KeyZ", 90)\n        async def UP(): await key("ArrowUp", "ArrowUp", 38)')
R('me_noparty = set()\n','me_noparty = set()\n        me_sig = None; me_t0 = time.time(); last_zlog = None; zmiss = 0\n')
# faint logic
R('''                if z is None or z["hp"] <= 0:
                    faint_n += 1
                    if faint_n < 4: await asyncio.sleep(0.6); continue
                    log("ZACIAN FAINT/missing - stop"); await shot(FRAMES, "zacian_faint"); break
                faint_n = 0''','''                if z is None:
                    # not in party at all (ME / transient read) - NOT a faint; wait long before giving up
                    zmiss += 1
                    if zmiss in (1, 10): log(f"Zacian missing from party read (h={h} ph={st.get('ph')}) party={[(p['n'],p['hp']) for p in party]}")
                    if zmiss < 60: await asyncio.sleep(0.5); continue
                    log("ZACIAN MISSING 30s+ - stop"); await shot(FRAMES, "zacian_missing"); break
                zmiss = 0
                if z["hp"] <= 0:
                    faint_n += 1
                    if faint_n < 4: await asyncio.sleep(0.6); continue
                    log(f"ZACIAN FAINT hp=0/{z.get('mx')} onField={z['f']} w{st.get('wave')} ph={st.get('ph')} foes={[(e['n'],e.get('ab')) for e in st.get('enemy') or []]} lastHP={last_zlog}")
                    await shot(FRAMES, "zacian_faint"); break
                faint_n = 0
                zl = (z["hp"], z.get("mx"), z["f"])
                if zl != last_zlog:
                    if last_zlog and last_zlog[2] and not z["f"]: log("Zacian switched OUT (alive) - not a faint")
                    log(f"ZHP w{st.get('wave')} {z['hp']}/{z.get('mx')} onField={z['f']} ph={st.get('ph')}"); last_zlog = zl''')
# party PP-item targeting
R('''                            mv = [k for k, o_ in enumerate(opts) if 17 <= o_ <= 20]
                            if mv:  # ether: restore the move with most PP used
                                zm = (await ev(STATE_JS.replace("(o.fi??0)", "0"))).get("moves") or []
                                used = sorted(range(len(mv)), key=lambda k: -(zm[k]["max"] - zm[k]["left"]) if k < len(zm) else 0)
                                k = mv[used[0]]
                            else:
                                k = 0 if opts and opts[0] != -1 else None''','''                            labels = await ev(OPT_LABELS_JS)
                            labels = labels if isinstance(labels, list) else []
                            zm = (await ev(STATE_JS.replace("(o.fi??0)", "0").replace("[fi]||party[0]", "[0]&&false||party[" + str(party.index(z)) + "]"))).get("moves") or []
                            names = [m["n"].lower() for m in zm]
                            hit = [(k2, names.index(lb.strip().lower())) for k2, lb in enumerate(labels) if lb.strip().lower() in names]
                            if hit:  # PP item move menu: pick Zacian's lowest-PP-left move (by ratio)
                                k2, mi = min(hit, key=lambda km: zm[km[1]]["left"] / max(1, zm[km[1]]["max"]))
                                k = k2 if k2 < len(opts) else mi
                                log(f"PP item -> {zm[mi]['n']} {zm[mi]['left']}/{zm[mi]['max']} (labels={labels})")
                            else:
                                ap = next((k2 for k2, lb in enumerate(labels) if lb.strip().lower() in ("apply", "use")), None)
                                k = ap if ap is not None else (0 if opts and opts[0] != -1 else None)
                                if same == 0: log(f"party opts={opts} labels={labels} -> {k}")''')
# ME party pick: Zacian or slot 1
R('''                        tgt = next((p["i"] for p in party if p["hp"] > 0 and p["n"] != "Zacian"), None)
                        want_opt = None
                        if same == 0: log(f"ME party select -> slot {tgt}")
                        if tgt is None: me_noparty.add(w); await X(); await asyncio.sleep(0.3); continue''','''                        tgt = z["i"] if z else 0
                        want_opt = None
                        if same == 0: log(f"ME party select -> slot {tgt} (Zacian/slot1)")''')
# ME handler: top option
R('''                    if w in me_noparty and n_opt > 1: n_opt = 1
                    if n_opt:
                        if same == 0: log(f"mystery encounter w{w}: {n_opt} usable options -> last usable (leave)")
                        await set_cursor(n_opt - 1); await Z()
                    else:
                        await Z()''','''                    if same == 0: log(f"mystery encounter w{w}: {n_opt} options -> TOP option (0)")
                    await set_cursor(0); await Z()''')
# confirm in ME -> Yes
R('''                    if skip_yes[0] and st.get("ph") == "SelectModifierPhase":''','''                    if st.get("ph") in ("MysteryEncounterPhase", "MysteryEncounterOptionSelectedPhase", "PostMysteryEncounterPhase", "MysteryEncounterBattlePhase"):
                        await set_cursor(0); await Z()  # ME follow-up prompt: first option
                    elif skip_yes[0] and st.get("ph") == "SelectModifierPhase":''')
R('''"LearnMovePhase", "EggLapsePhase", "EncounterPhase"):''','''"LearnMovePhase", "EggLapsePhase", "EncounterPhase") or "Mystery" in str(st.get("ph")):''')
# watchdog before dispatch
R('''                if h != "PartyUiHandler": party_tries = 0''','''                if "Mystery" in str(st.get("ph")) or h == "MysteryEncounterUiHandler":
                    msig = (h, st.get("ph"), st.get("cur"), st.get("om"))
                    if msig != me_sig: me_sig = msig; me_t0 = time.time()
                    elif time.time() - me_t0 > 20:
                        log(f"ME watchdog: {msig} stuck 20s -> Up x4 + Z"); await shot(FRAMES, "me_watchdog")
                        for _ in range(4): await UP(); await asyncio.sleep(0.1)
                        await Z(); me_t0 = time.time(); await asyncio.sleep(0.4); continue
                else: me_sig = None
                if h != "PartyUiHandler": party_tries = 0''')
open(p,'w',encoding='utf-8').write(s)
