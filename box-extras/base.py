#!/usr/bin/env python3
"""PokeRogue farm17 (from farm16: ME top option + watchdog, PP item move targeting, faint vs switch-out, Zacian HP log)
PokeRogue farm15 - UI-state driven (reads the Phaser battle scene via a camera hook).
Zacian Classic farm. Fight only, never Escape, never Endless, stop on Zacian faint.
Fixes vs farm14: no blind Space+Z double-confirm (caused stray party/menu wandering),
real PP + foe types from game objects, reward picked by priority, move rotation."""
import json, asyncio, websockets, urllib.request, pathlib, time, base64, traceback
from datetime import datetime
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"; STATUS = OUT / "pokerogue_farm_status.json"
STOP = OUT / "pokerogue_farm_stop.flag"; SHOT_DIR = OUT / "pokerogue_battle_shots"
FRAMES = OUT / "prframes"  # stall/debug frames; battle shots -> SHOT_DIR
STATE_JS = (HERE / "state.js").read_text(encoding="utf-8")
HOOK_JS = """(()=>{const S=Phaser.GameObjects.Sprite.prototype;if(!S.__g){const so=S.setTexture;S.__g=1;S.setTexture=function(...a){if(!this.scene)return this;return so.apply(this,a)}};const P=Phaser.Cameras.Scene2D.Camera.prototype; if(!P.__hpre){const o=P.preRender;P.__hpre=1;P.preRender=function(...a){window.__pr_cam=this;return o.apply(this,a)}} return !!window.__pr_cam})()"""
GROUND = 4
STEP_JS = """(()=>{try{const L=window.__pr_cam.scene.game.loop;if(document.visibilityState!=='hidden')return {hidden:false,frame:L.frame};
let t=Math.max(L.lastTime||0,L.now||0);for(let k=0;k<45;k++){t+=16.7;L.step(t)}return {hidden:true,frame:L.frame}}catch(e){return String(e.stack||e)}})()"""
# reward priority (lower index = better). matched case-insensitively as substrings
REWARD_PRI = ["leppa berry", "rare candy", "max revive", "leftovers", "shell bell", "choice band", "life orb", "muscle band",
              "king's rock", "scope lens", "quick claw", "focus band", "soothe bell", "lucky egg", "exp. share",
              "golden", "silk scarf", "pixie plate", "fairy", "metal coat", "berry", "full restore", "max potion",
              "revive", "hyper potion", "max elixir", "elixir", "max ether", "ether", "super potion", "nugget",
              "ultra ball", "great ball", "potion", "poke ball"]
OPT_LABELS_JS = """(()=>{try{const h=window.__pr_cam.scene.ui.getHandler();const c=h.optionsContainer;if(!c)return [];const t=c.list.filter(x=>x.type==='Text'||x.text!==undefined).map(x=>({t:String(x.text),y:x.y}));t.sort((a,b)=>a.y-b.y);return t.map(x=>x.t)}catch(e){return String(e)}})()"""
PP_ITEMS = ["max elixir", "elixir", "max ether", "ether"]

def log(msg):
    line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f: f.write(line + "\n")

def find_page():
    pages = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    return next(p for p in pages if p.get("type") == "page" and p.get("url", "").startswith("https://pokerogue.net/"))

def pick_reward(st, bad=()):
    rew = [r for r in (st.get("rew") or []) if r.get("n") and r["n"] not in bad]
    if not rew: return None, None
    z = next((p for p in st["party"] if p["n"] == "Zacian"), None)
    pp_low = any(m["max"] and m["left"] / m["max"] < 0.4 for m in (st.get("zmoves") or []))
    ally_dead = any(p["hp"] <= 0 for p in st["party"])
    zhp_low = z and z.get("mx") and z["hp"] / z["mx"] < 0.5
    heal_need = z and z.get("mx") and z["hp"] / z["mx"] < 0.6 and (((st.get("wave") or 0) + 1) % 10 == 0 or st.get("trainer") or ((st.get("wave") or 0) + 1) % 10 in (5, 8))
    HEAL = ["full restore", "max potion", "hyper potion", "sitrus berry", "super potion", "potion"]
    def rank(r):
        n = r["n"].lower()
        if "leppa" in n: return -20
        if heal_need and any(k in n for k in HEAL): return -15 + [k in n for k in HEAL].index(True)
        if pp_low and any(k in n for k in PP_ITEMS): return -10 + [k in n for k in PP_ITEMS].index(True)
        if n.startswith("tm") or "memory mushroom" in n or "mint" in n or "dna splicers" in n: return 99  # opens teach/party flows
        if "lure" in n: return 85
        if n.startswith("x ") or "dire hit" in n: return 70
        if "revive" in n and not ally_dead: return 90
        if "potion" in n and not zhp_low and "full restore" not in n: return 80
        for i, k in enumerate(REWARD_PRI):
            if k in n: return i
        return 50
    best = min(rew, key=rank)
    return best["i"], f"{best['n']} (rank {rank(best)}, pp_low={pp_low}, heal_need={bool(heal_need)}) from {[r['n'] for r in rew]}"

def pick_move(st, hist, dead=()):
    moves = [m for m in (st.get("moves") or []) if m["n"] not in dead]
    doubles = st.get("double")
    cands = []
    for m in moves:
        if m["left"] <= 0 or m.get("cat") == 2: continue
        if doubles and m["type"] == GROUND and m["n"] == "Earthquake": continue
        if m["type"] == GROUND and any((e.get("ab") or "") in ("Levitate", "Lightning Rod_") for e in (st.get("enemy") or [])): continue
        effs = m.get("effs") or [1]
        if max(effs) <= 0: continue
        pw = m["pow"] if m["pow"] and m["pow"] > 0 else 40
        score = pw * max(effs) * (1.5 if m["stab"] else 1.0)
        if m["n"] == "Earthquake": score *= 0.8  # soft avoid
        if hist and hist[-1] == m["n"]: score *= 0.85
        cands.append([score, m])
    if not cands:
        # fallback (farm17 patch 09:25): any damaging move with PP, ignoring soft rules, so we never loop Fight<->back
        fb = [m for m in moves if m["left"] > 0 and m.get("cat") != 2]
        if fb:
            fb.sort(key=lambda m: -(max(m.get("effs") or [1]) > 0)); return fb[0]
        return None
    # never same move >2 in a row if any alternative exists
    if len(hist) >= 2 and hist[-1] == hist[-2]:
        alt = [c for c in cands if c[1]["n"] != hist[-1]]
        top = max(cands, key=lambda c: c[0])
        # allow a 3rd repeat only if it is >2x better than any alternative (e.g. 4x vs 0.5x)
        if alt and not (top[1]["n"] == hist[-1] and top[0] > 2 * max(a[0] for a in alt)):
            cands = alt
    cands.sort(key=lambda c: -c[0])
    return cands[0][1]

async def main():
    page = find_page()
    async with websockets.connect(page["webSocketDebuggerUrl"], max_size=50_000_000) as ws:
        n = 0
        async def call(method, params=None):
            nonlocal n; n += 1
            await ws.send(json.dumps({"id": n, "method": method, **({"params": params} if params else {})}))
            while True:
                r = json.loads(await ws.recv())
                if r.get("id") == n: return r
        async def ev(expr):
            r = await call("Runtime.evaluate", {"expression": expr, "returnByValue": True})
            return ((r.get("result") or {}).get("result") or {}).get("value")
        async def key(k, code, kc, h=90):
            d = {"type": "keyDown", "windowsVirtualKeyCode": kc, "code": code, "key": k}
            if len(k) == 1: d["text"] = k
            await call("Input.dispatchKeyEvent", d); await asyncio.sleep(h / 1000)
            await call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": kc, "code": code, "key": k})
        async def Z(): await key("z", "KeyZ", 90)
        async def UP(): await key("ArrowUp", "ArrowUp", 38)
        async def X(): await key("x", "KeyX", 88)   # cancel / back (never Escape)
        async def set_cursor(i):
            return await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setCursor({i});return h.cursor}})()")
        async def shot(dirp, tag, fmt="jpeg"):
            try:
                dirp.mkdir(parents=True, exist_ok=True)
                r = await call("Page.captureScreenshot", {"format": fmt} | ({"quality": 70} if fmt == "jpeg" else {}))
                p = dirp / f"{tag}_{datetime.now():%H%M%S}.{'jpg' if fmt=='jpeg' else 'png'}"
                p.write_bytes(base64.b64decode(r["result"]["data"])); return p.name
            except Exception as e:
                log(f"shot fail {e}")
        async def pump(k=3):
            # PC is locked/occluded -> tab hidden -> no rAF. Each captureScreenshot forces a frame.
            for _ in range(k):
                await call("Page.captureScreenshot", {"format": "jpeg", "quality": 5, "clip": {"x": 0, "y": 0, "width": 8, "height": 8, "scale": 1}})
        await call("Page.bringToFront")
        await ev("(()=>{const c=document.querySelector('canvas');if(c){c.tabIndex=0;c.focus()}})()")
        await ev(HOOK_JS); await asyncio.sleep(0.5)
        gi = await ev("window.gameInfo&&window.gameInfo.gameMode")
        log(f"START farm17 [nopp-guard] (UI-state driven) mode={gi}")
        if gi != "Classic": log("ABORT not Classic"); return
        party_tries = 0; stepping_logged = False; rew_bad = {}; last_pick = [None]; skip_yes = [False]
        hist = []; last_sig = None; same = 0; last_wave = None; framed = set(); last_rew_wave = None; shot_w = set(); lep_try = set(); faint_n = 0; me_noparty = set()
        dead_moves = {}; me_sig = None; me_t0 = time.time(); last_zlog = None; zmiss = 0
        while True:
            if STOP.exists(): log("STOP flag"); break
            try:
                if (await ev("window.gameInfo&&window.gameInfo.gameMode")) == "Endless": log("Endless STOP"); break
                # PC locked -> tab hidden -> Chrome stops rAF, Phaser freezes. Drive frames manually.
                adv = await ev(STEP_JS)
                if isinstance(adv, str): log(f"step err {adv[:160]}")
                elif adv and adv.get("hidden") and not stepping_logged:
                    log(f"tab hidden: manual frame stepping on (frame {adv.get('frame')})"); stepping_logged = True
                st = await ev(STATE_JS)
                if not st or st.get("err"):
                    await ev(HOOK_JS); await asyncio.sleep(0.5); continue
                h = st.get("h"); party = st.get("party") or []
                z = next((p for p in party if p["n"] == "Zacian"), None)
                if z is None:
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
                    log(f"ZHP w{st.get('wave')} {z['hp']}/{z.get('mx')} onField={z['f']} ph={st.get('ph')}"); last_zlog = zl
                w = st.get("wave")
                if w != last_wave:
                    if last_wave is not None: log(f"WAVE UP {last_wave} -> {w}")
                    last_wave = w
                    STATUS.write_text(json.dumps({"ts": datetime.now().isoformat(), "script": "pr_farm17.py", "wave": w,
                        "zacian": z, "party": party}, indent=1), encoding="utf-8")
                sig = json.dumps([h, st.get("cur"), st.get("om"), st.get("ph"), w, [m["left"] for m in st.get("moves") or []]])
                same = same + 1 if sig == last_sig else 0; last_sig = sig
                if same and same % 25 == 0:
                    log(f"STALL x{same} h={h} ph={st.get('ph')} cur={st.get('cur')} -> shot")
                    await shot(FRAMES, f"stall_{h}")
                if h not in framed and h in ("FightUiHandler", "ModifierSelectUiHandler", "PartyUiHandler", "CommandUiHandler"):
                    framed.add(h); await shot(FRAMES, f"frame_{h}", "png")

                if "Mystery" in str(st.get("ph")) or h == "MysteryEncounterUiHandler":
                    msig = (h, st.get("ph"), st.get("cur"), st.get("om"))
                    if msig != me_sig: me_sig = msig; me_t0 = time.time()
                    elif time.time() - me_t0 > 20:
                        log(f"ME watchdog: {msig} stuck 20s -> Up x4 + Z"); await shot(FRAMES, "me_watchdog")
                        for _ in range(4): await UP(); await asyncio.sleep(0.1)
                        await Z(); me_t0 = time.time(); await asyncio.sleep(0.4); continue
                else: me_sig = None
                if h != "PartyUiHandler": party_tries = 0
                if h == "CommandUiHandler":
                    wild_shiny = (not st.get("trainer")) and any(e["sh"] for e in st.get("enemy") or [])
                    if wild_shiny and not st.get("double"):
                        log(f"WILD SHINY {[e['n'] for e in st['enemy'] if e['sh']]} -> Ball")
                        await shot(FRAMES, "wild_shiny"); await set_cursor(1); await Z()
                    else:
                        if wild_shiny: log("wild shiny in doubles - deferred (fight)")
                        if st.get("cur") != 0: await set_cursor(0)
                        await Z()
                elif h == "FightUiHandler":
                    m = pick_move(st, hist, dead_moves.get((w, st.get('user')), ()))
                    pps = {mm["n"]: f"{mm['left']}/{mm['max']}" for mm in st.get("moves") or []}
                    foes = [(e["n"], e["t"], e.get("ab")) for e in st.get("enemy") or []]
                    if m is None:
                        log(f"no usable move {pps} foes={foes} dbl={st.get('double')} - back"); await X()
                    else:
                        log(f"w{w} {st.get('user')} -> {m['n']} eff={m['effs']} stab={m['stab']} PP={pps} foes={foes} dbl={st.get('double')}")
                        if st.get("user") == "Zacian": hist = (hist + [m["n"]])[-6:]
                        await set_cursor(m["i"]); await asyncio.sleep(0.1); await Z()
                        # no-PP guard: if fight menu still open / 'no PP' msg after ~2s, mark move dead and try others
                        dk = (w, st.get("user")); tried = {m["n"]}
                        for _ in range(5):
                            stuck = False
                            for _t in range(8):
                                await asyncio.sleep(0.25); await ev(STEP_JS)
                                s2 = await ev(STATE_JS) or {}
                                txt = str(await ev("(()=>{try{return window.__pr_cam.scene.ui.getMessageHandler?.().message?.text||''}catch(e){return ''}})()") or "")
                                if "PP" in txt and ("no" in txt.lower() or "left" in txt.lower()):
                                    stuck = True; break
                                if s2.get("h") != "FightUiHandler": break
                            else:
                                stuck = s2.get("h") == "FightUiHandler"
                            if not stuck: break
                            dead_moves.setdefault(dk, set()).update(tried)
                            log(f"NOPP stuck on {sorted(tried)} (msg={txt[:40]!r}) -> mark 0 PP, retry")
                            for _k in range(3): await Z(); await asyncio.sleep(0.2)  # clear message box
                            s2 = await ev(STATE_JS) or {}
                            if s2.get("h") != "FightUiHandler":
                                if s2.get("h") == "CommandUiHandler":
                                    if s2.get("cur") != 0: await set_cursor(0)
                                    await Z(); await asyncio.sleep(0.4); s2 = await ev(STATE_JS) or {}
                                if s2.get("h") != "FightUiHandler": break
                            m2 = pick_move(s2, hist, dead_moves[dk])
                            if m2 is None:
                                left = [mm for mm in (s2.get("moves") or []) if mm["n"] not in dead_moves[dk]]
                                if not left: log("NOPP no slots left - back"); await X(); break
                                m2 = left[0]
                            tried.add(m2["n"]); log(f"NOPP fallback -> {m2['n']} (slot {m2['i']})")
                            await set_cursor(m2["i"]); await asyncio.sleep(0.1); await Z()
                        if w not in shot_w: shot_w.add(w); await shot(SHOT_DIR, f"w{w}_{m['n'].replace(' ','')}")
                elif h == "TargetSelectUiHandler":
                    await Z()
                elif h == "BallUiHandler":
                    balls = st.get("balls") or {}
                    best = max([int(k) for k, v in balls.items() if v and int(k) <= 4] or [0])
                    await set_cursor(best); await Z()
                elif h == "ModifierSelectUiHandler":
                    st["zmoves"] = st.get("moves") if st.get("user") == "Zacian" else None
                    if st.get("zmoves") is None:
                        st["zmoves"] = (await ev(STATE_JS.replace("(o.fi??0)", "0"))).get("moves")
                    i, why = pick_reward(st, rew_bad.get(w, set()))
                    last_pick[0] = (st.get("rew") or [{}]*(i+1))[i].get("n") if i is not None else None
                    if i is None:
                        # no reward cards left (only shop) -> leave the screen; confirm the skip prompt with Yes
                        log("reward screen with no reward options - X + confirm skip"); skip_yes[0] = True
                        await X()
                    else:
                        if last_rew_wave != w: log(f"REWARD pick {why}"); last_rew_wave = w
                        await ev(f"(()=>{{const h=window.__pr_cam.scene.ui.getHandler();h.setRowCursor(1);h.setCursor({i});}})()")
                        await asyncio.sleep(0.15); await Z()
                elif h == "PartyUiHandler":
                    ph = st.get("ph")
                    party_tries += 1
                    if party_tries > 6:
                        if ph == "SelectModifierPhase" and last_pick[0]:
                            if "leppa" not in last_pick[0].lower() or w in lep_try: rew_bad.setdefault(w, set()).add(last_pick[0])
                            else: lep_try.add(w); party_tries = 0; log("leppa: retry applying to Zacian"); await set_cursor(party.index(z)); await Z(); continue
                            log(f"reward {last_pick[0]} cannot be applied - blacklist for wave {w}, back to rewards")
                            last_rew_wave = None
                        else:
                            log(f"party UI loop in {ph} - X out")
                        for _ in range(3):
                            await X(); await asyncio.sleep(0.25); await ev(STEP_JS)
                        party_tries = 0
                        continue
                    if ph in ("SwitchPhase", "SwitchSummonPhase"):
                        tgt = next((p["i"] for p in party if p["hp"] > 0 and not p["f"] and p["n"] != "Zacian"), None)
                        if tgt is None: tgt = next((p["i"] for p in party if p["hp"] > 0 and not p["f"]), None)
                        party_tries = 0 if party_tries < 3 else party_tries
                        log(f"switch-in {ph}: send slot {tgt}")
                        want_opt = 0  # SEND_OUT
                    elif ph == "SelectModifierPhase":
                        dead = next((p["i"] for p in party if p["hp"] <= 0), None)
                        tgt = party.index(z)
                        if last_pick[0] and "revive" in last_pick[0].lower() and dead is not None:
                            tgt = dead
                        want_opt = None
                    elif ph == "MysteryEncounterPhase":
                        # ME option asks for a party member: offer a non-Zacian ally (never risk Zacian)
                        tgt = z["i"] if z else 0
                        want_opt = None
                        if same == 0: log(f"ME party select -> slot {tgt} (Zacian/slot1)")
                    else:
                        log(f"stray party UI in {ph} - back"); await X(); await asyncio.sleep(0.3); continue
                    if tgt is None: await X(); continue
                    if not st.get("om"):
                        await set_cursor(tgt); await Z()
                    else:
                        opts = st.get("opts") or []
                        if ph == "SelectModifierPhase":
                            labels = await ev(OPT_LABELS_JS)
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
                                if same == 0: log(f"party opts={opts} labels={labels} -> {k}")
                        elif want_opt is None:
                            k = 0 if opts and opts[0] != -1 else None
                        else:
                            k = opts.index(want_opt) if want_opt in opts else None
                        if k is None: await X()
                        else:
                            await set_cursor(k); await Z()
                            log(f"party {ph}: slot {tgt} option {opts[k] if k < len(opts) else k}")
                elif h == "ConfirmUiHandler":
                    if st.get("ph") in ("MysteryEncounterPhase", "MysteryEncounterOptionSelectedPhase", "PostMysteryEncounterPhase", "MysteryEncounterBattlePhase"):
                        await set_cursor(0); await Z()  # ME follow-up prompt: first option
                    elif skip_yes[0] and st.get("ph") == "SelectModifierPhase":
                        skip_yes[0] = False; await set_cursor(0); await Z()
                    else:
                        await X()  # answer No (e.g. switch prompt / learn move)
                elif h == "MysteryEncounterUiHandler":
                    n_opt = await ev("(()=>{const me=window.__pr_cam.scene.currentBattle.mysteryEncounter;if(!me)return 0;let k=me.options.length;while(k>1&&me.options[k-1].meetsRequirements&&!me.options[k-1].meetsRequirements())k--;return k})()") or 0
                    if same == 0: log(f"mystery encounter w{w}: {n_opt} options -> TOP option (0)")
                    await set_cursor(0); await Z()
                elif h == "OptionSelectUiHandler" and st.get("ph") in ("SelectBiomePhase",
                           "LearnMovePhase", "EggLapsePhase", "EncounterPhase") or "Mystery" in str(st.get("ph")):
                    if same == 0: log(f"option select in {st.get('ph')} - take default")
                    await Z()
                elif h in ("MenuUiHandler", "SettingsUiHandler", "SummaryUiHandler", "PokedexPageUiHandler",
                           "OptionSelectUiHandler", "GameStatsUiHandler", "AchvsUiHandler", "SettingsDisplayUiHandler"):
                    log(f"stray menu {h} in {st.get('ph')} - back"); await X()
                else:
                    await Z()  # messages / evolution / etc.
                await asyncio.sleep(0.35)
            except Exception as e:
                log(f"ERR {e}"); traceback.print_exc(); await asyncio.sleep(2)
        log("DONE farm17")

if __name__ == "__main__":
    asyncio.run(main())

