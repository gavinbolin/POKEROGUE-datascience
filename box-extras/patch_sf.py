import re
p='pr_farm17.py'; s=open(p,encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:60],s.count(a)); s=s.replace(a,b)
rep('HARD_WAVES_BASE = {8, 25, 55, 95, 165, 195}\n','''HARD_WAVES_BASE = {8, 25, 55, 95, 165, 195}
# --- Gavin 10/29: live-config (control app writes CONFIG_FILE; re-read each wave) ---
CANDY_TARGET = 'secondary'    # 'secondary' | 'primary' | 'both'  (Soothe Bell / Rare Candy target)
SECONDARY_FIELD = 'auto'      # 'bench' | 'field' | 'auto'  (bring Feebas onto the field in singles for candy)
CONFIG_FILE = pathlib.Path(r"C:\\Users\\gavin\\agent-tools\\pokerogue_farm_config.json")
CFG = {"candy_target": CANDY_TARGET, "secondary_field": SECONDARY_FIELD}
def cfg_reload(logf=None):
    new = {"candy_target": CANDY_TARGET, "secondary_field": SECONDARY_FIELD}
    try:
        d = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        if str(d.get("candy_target","")).lower() in ("secondary","primary","both"): new["candy_target"] = str(d["candy_target"]).lower()
        if str(d.get("secondary_field","")).lower() in ("bench","field","auto"): new["secondary_field"] = str(d["secondary_field"]).lower()
    except Exception: pass
    for k, v in new.items():
        if CFG.get(k) != v:
            if logf: logf(f"CONFIG change {k}: {CFG.get(k)} -> {v}")
            CFG[k] = v
''')
rep('log("CANDY priority: Candy Jar/Rare Candy top (-55, below Master/Rogue tier, above vouchers)")',
 'log("CANDY priority: Candy Jar/Rare Candy top (-55, below Master/Rogue tier, above vouchers)"); cfg_reload(); log(f"CANDY_TARGET={CFG[\'candy_target\']} (Soothe Bell/Rare Candy; default {CANDY_TARGET}) file={CONFIG_FILE}"); log(f"SECONDARY_FIELD={CFG[\'secondary_field\']} (Feebas into singles; default {SECONDARY_FIELD}; auto=wild single, no boss/hard, Feebas>=40% Zacian>=50%, 1/wave, 2 faints->bench)")')
rep('title_cont = [0]\n','title_cont = [0]\n        sf = {"pend": None, "done": set(), "tries": {}, "out": None, "faints": 0, "bench_run": False, "skiplog": set(), "sec_hp": None}; candy_n = [0]\n',1)
# wave change: reload config
rep('                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")\n',
    '                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")\n                    cfg_reload(log)\n')
# secfield decision before zacian switch-in
rep('''                        # ZACIAN SWITCH-IN (Gavin OK 14:21): Zacian alive, off field, healthy -> Pokemon menu
                        do_sw = False
''','''                        # SECFIELD (Gavin OK 10/29): bring Feebas onto the field in singles for candy (participantIds)
                        do_sf = False
                        _sec = role(party, SECONDARY); _mode = CFG["secondary_field"]
                        if _sec:
                            if sf["sec_hp"] is not None and sf["sec_hp"] > 0 and _sec["hp"] <= 0 and sf["out"] == w:
                                sf["faints"] += 1; log(f"SECFIELD w{w}: Feebas fainted while fielded (#{sf['faints']})")
                                if _mode == "auto" and sf["faints"] >= 2 and not sf["bench_run"]: sf["bench_run"] = True; log("SECFIELD auto: 2 Feebas faints this run -> bench for rest of run")
                            sf["sec_hp"] = _sec["hp"]
                        if _sec and _mode != "bench" and not wild_shiny and st.get("ph") == "CommandPhase" and not st.get("double") and z["f"] and not _sec["f"] and w not in sf["done"]:
                            why = None
                            zr_ = z["hp"] / max(1, z.get("mx") or 1); sr_ = _sec["hp"] / max(1, _sec.get("mx") or 1)
                            if _mode == "auto" and sf["bench_run"]: why = "auto benched after 2 faints"
                            elif sf["tries"].get(w, 0) >= 2: why = "try cap"
                            elif w in HARD_WAVES: why = "hard wave"
                            elif _sec["hp"] <= 0: why = "Feebas fainted"
                            elif zr_ < 0.5: why = f"Zacian HP {zr_:.0%}"
                            elif sr_ < (0.4 if _mode == "auto" else 0.5): why = f"Feebas HP {sr_:.0%}"
                            elif _mode == "auto" and st.get("trainer"): why = "trainer"
                            elif any(e.get("sh") for e in st.get("enemy") or []): why = "shiny enemy"
                            if why is None:
                                sj2 = await ev(SIG_JS) or {}
                                if sj2.get("bosses"): why = "boss"
                                elif _mode == "auto" and sj2.get("fixed"): why = "fixed wave"
                                else:
                                    try: _tr = await ev("(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField()[0];return !!(f&&f.isTrapped&&f.isTrapped())}catch(e){return false}})()")
                                    except Exception: _tr = False
                                    if _tr: why = "trapped"
                            if why:
                                if (w, why) not in sf["skiplog"]: sf["skiplog"].add((w, why)); log(f"SECFIELD skip w{w} ({why}) mode={_mode}")
                                if why in ("hard wave", "boss", "trainer", "fixed wave", "try cap", "auto benched after 2 faints"): sf["done"].add(w)
                            else:
                                sf["tries"][w] = sf["tries"].get(w, 0) + 1; sf["pend"] = w; do_sf = True
                                log(f"SECFIELD w{w}: Feebas in (mode={_mode} try {sf['tries'][w]} Zacian {z['hp']}/{z.get('mx')} Feebas {_sec['hp']}/{_sec.get('mx')})")
                        if do_sf:
                            await set_cursor(2); await Z(); await asyncio.sleep(0.4); continue
                        if _sec and _sec["f"] and not z["f"] and sf["pend"] == w:
                            sf["done"].add(w); sf["out"] = w; sf["pend"] = None; log(f"SECFIELD w{w}: Feebas on field -> Zacian back next")
                        # ZACIAN SWITCH-IN (Gavin OK 14:21): Zacian alive, off field, healthy -> Pokemon menu
                        do_sw = False
''')
# party handler in CommandPhase
rep('''                    elif ph == "CommandPhase":
                        if z["hp"] > 0 and not z["f"]:''','''                    elif ph == "CommandPhase" and sf["pend"] == w and role(party, SECONDARY) and not role(party, SECONDARY)["f"] and role(party, SECONDARY)["hp"] > 0:
                        tgt = role(party, SECONDARY)["i"]; want_opt = 0
                        if party_tries == 1: log(f"SECFIELD party: Feebas slot {tgt}")
                        if party_tries >= 4: sf["pend"] = None; sf["done"].add(w); log(f"SECFIELD w{w}: switch stuck -> give up this wave"); await X(); await asyncio.sleep(0.3); continue
                    elif ph == "CommandPhase":
                        if z["hp"] > 0 and not z["f"]:''')
rep('''                            tgt = z["i"]; want_opt = 0; log(f"switch-in CommandPhase party: Zacian slot {tgt}")''',
'''                            tgt = z["i"]; want_opt = 0; log(f"switch-in CommandPhase party: Zacian slot {tgt}")
                            if sf["out"] == w and party_tries == 1: log(f"SECFIELD w{w}: Zacian back")''')
# candy target
rep('''                        if fbi is not None and (("soothe bell" in lpn and w not in fb_fall) or "rare candy" in lpn):
                            tgt = fbi
                            if same == 0: log(f"FEEBAS reward {last_pick[0]} -> Feebas slot {fbi}")''',
'''                        if ("soothe bell" in lpn or "rare candy" in lpn):
                            _ct = CFG["candy_target"]; _zi = party.index(z)
                            if _ct == "primary" or fbi is None: _pri = _zi; _alt = fbi
                            elif _ct == "both": _pri, _alt = ((fbi, _zi) if candy_n[0] % 2 == 0 else (_zi, fbi))
                            else: _pri, _alt = fbi, _zi
                            if w in fb_fall and _alt is not None: _pri = _alt
                            tgt = _pri
                            if same == 0: candy_n[0] += 1; log(f"CANDY_TARGET {_ct}: {last_pick[0]} -> slot {tgt} ({party[tgt]['n']})")''')
rep('''                            if fbi is not None and "soothe bell" in last_pick[0].lower() and w not in fb_fall:
                                fb_fall.add(w); party_tries = 0; log("FEEBAS soothe bell failed/max on Feebas -> Zacian"); await set_cursor(party.index(z)); await Z(); continue''',
'''                            if fbi is not None and any(k in last_pick[0].lower() for k in ("soothe bell", "rare candy")) and w not in fb_fall:
                                fb_fall.add(w); party_tries = 0; log("CANDY_TARGET item failed/max on first target -> other role mon"); continue''')
open(p,'w',encoding='utf-8').write(s)
