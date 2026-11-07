p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R("def shop_plan(party, z, sec, items, money, budget):", '''SIG_FILE = pathlib.Path(r"C:\\Users\\gavin\\agent-tools\\pokerogue_significant_waves.json")
SIG_JSONL = SIG_FILE.with_suffix(".jsonl")
HARD_WAVES_BASE = {8, 25, 55, 95, 165, 195}
SHOP_HARD_SPEND_FRAC = 0.75
SHOP_HARD_HURT = 0.99
def sig_load():
    try: return json.loads(SIG_FILE.read_text(encoding="utf-8"))
    except Exception: return {"learned_hard": [], "wave_tally": {}, "records": 0}
SIG = sig_load()
HARD_WAVES = HARD_WAVES_BASE | set(int(x) for x in SIG.get("learned_hard", []))
HARD_JS = """(n=>{try{const s=window.__pr_cam.scene,g=s.gameMode;let f=false,t=false;try{f=!!g.isFixedBattle(n)}catch(e){};try{t=!!g.isWaveTrainer(n,s.arena)}catch(e){};return {fixed:f,trainer:t}}catch(e){return {err:String(e)}}})"""
SIG_JS = """(()=>{try{const s=window.__pr_cam.scene,b=s.currentBattle,t=b.trainer;let fx=false;try{fx=!!s.gameMode.isFixedBattle(b.waveIndex)}catch(e){};const nm=t?(t.getName?t.getName(0,true):t.name):null;return {tr:nm,tt:t&&t.config?t.config.trainerType:null,bosses:s.getEnemyParty().filter(e=>e.isBoss&&e.isBoss()).map(e=>e.name),biome:s.arena?s.arena.biomeType:null,fixed:fx,rival:!!(t&&/rival/i.test(String(t.config&&t.config.name||'')+String(nm)))||(fx&&!!t&&[8,25,55,95,145,195].includes(b.waveIndex))}}catch(e){return {err:String(e)}}})()"""
RUN_ID = datetime.now().strftime("%Y%m%d-%H%M%S")
def shop_plan(party, z, sec, items, money, budget, hurt=None):
    SHOP_HURT_ = hurt or SHOP_HURT''')
s=s.replace("            if r < SHOP_HURT:\n","            if r < SHOP_HURT_:\n",1)
R("        if r < SHOP_HURT:\n","        if r < SHOP_HURT_:\n")
R('''                            cap = int(max(0, min(SHOP_MAX_SPEND_FRAC * m0 - spent, sh["money"] - floor)))
                            pl = shop_plan(party, z, role(party, SECONDARY), sh["items"], sh["money"], cap)''','''                            if hard_w.get("w") != w:
                                nx = (w or 0) + 1; hj = await ev(HARD_JS + f"({nx})") or {}
                                rs = [x for x, c in (("HARD_WAVES", nx in HARD_WAVES), ("fixed", hj.get("fixed")), ("trainer", hj.get("trainer")), ("x10 gym/boss", nx % 10 == 0)) if c]
                                hard_w.update(w=w, hard=bool(rs))
                                if rs: log(f"HARD WAVE NEXT {nx} ({', '.join(rs)}) -> pre-heal")
                            _hd = hard_w.get("hard")
                            cap = int(max(0, min((SHOP_HARD_SPEND_FRAC if _hd else SHOP_MAX_SPEND_FRAC) * m0 - spent, sh["money"] - floor)))
                            pl = shop_plan(party, z, role(party, SECONDARY), sh["items"], sh["money"], cap, SHOP_HARD_HURT if _hd else None)''')
R('''                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")''','''                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")
                    try:
                        if sig_pend.get("rec") and sig_pend["rec"]["wave"] == last_wave:
                            rec = sig_pend.pop("rec"); _s2 = role(party, SECONDARY)
                            rec.update(outcome="won" if z and z["hp"] > 0 else "lost", zacian_after=z and [z["hp"], z.get("mx")], secondary_after=_s2 and [_s2["hp"], _s2.get("mx")], min_role_ratio=round(sig_pend.get("minr", 1), 3))
                            with SIG_JSONL.open("a", encoding="utf-8") as fh: fh.write(json.dumps(rec) + "\\n")
                            SIG["records"] = SIG.get("records", 0) + 1; tl = SIG.setdefault("wave_tally", {}); tl[str(last_wave)] = tl.get(str(last_wave), 0) + 1
                            if rec.get("trainer") and sig_pend.get("minr", 1) < 0.5 and last_wave not in SIG.setdefault("learned_hard", []):
                                SIG["learned_hard"].append(last_wave); HARD_WAVES.add(last_wave); log(f"SIG learned hard wave {last_wave}")
                            SIG_FILE.write_text(json.dumps(SIG, indent=1), encoding="utf-8")
                    except Exception as e: log(f"SIG write error {e}")
                    sig_pend.clear()''')
R('''                h = st.get("h"); party = st.get("party") or []''','''                h = st.get("h"); party = st.get("party") or []
                try:
                    _wv = st.get("wave")
                    if sig_pend.get("probe") != _wv and st.get("ph") == "CommandPhase":
                        sig_pend["probe"] = _wv; sj = await ev(SIG_JS) or {}
                        if sj.get("tr") or sj.get("bosses"):
                            _z = role(party, PRIMARY); _s2 = role(party, SECONDARY)
                            sig_pend["rec"] = {"run_id": RUN_ID, "ts": datetime.now().isoformat(), "wave": _wv, "biome": sj.get("biome"), "trainer": sj.get("tr"), "trainer_type": sj.get("tt"), "bosses": sj.get("bosses"), "is_rival": sj.get("rival"), "fixed": sj.get("fixed"), "zacian_before": _z and [_z["hp"], _z.get("mx")], "secondary_before": _s2 and [_s2["hp"], _s2.get("mx")]}
                            log(f"SIG WAVE {_wv} {sj.get('tr') or sj.get('bosses')}")
                    if sig_pend.get("rec"):
                        for _p in (role(party, PRIMARY), role(party, SECONDARY)):
                            if _p and _p.get("mx"): sig_pend["minr"] = min(sig_pend.get("minr", 1), _p["hp"] / _p["mx"])
                except Exception as e: log(f"SIG probe error {e}")''')
R("cheap_n = {};", "cheap_n = {}; hard_w = {}; sig_pend = {};")
R('log("REROLL budget:', 'log(f"HARD_WAVES={sorted(HARD_WAVES)} sig={SIG_FILE}"); log("REROLL budget:')
if "import pathlib" not in s and "from pathlib" not in s: s="import pathlib\n"+s
open(p,"w",encoding="utf-8").write(s); print("ok")
