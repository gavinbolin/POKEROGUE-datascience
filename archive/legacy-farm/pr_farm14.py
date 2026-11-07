#!/usr/bin/env python3
"""PokéRogue farm14 — Zacian-only, Fight-only (shiny catch override), PP>0 guard, no move spam,
absolute menu block, type-effectiveness, battle-start screenshots. Do not start unless asked."""
import json, asyncio, websockets, urllib.request, pathlib, time, traceback, base64, io, re
from datetime import datetime

PAGE = "https://pokerogue.net/"
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"
STATUS = OUT / "pokerogue_farm_status.json"
STOP = OUT / "pokerogue_farm_stop.flag"
SHOT = OUT / "pokerogue_farm14_ocr.jpg"
SHOT_DIR = OUT / "pokerogue_battle_shots"
PP_RE = re.compile(r"(\d+)\s*/\s*(\d+)")

# Move name -> type (extend as needed)
MOVE_TYPE = {
    "Earthquake": "Ground", "Mighty Cleave": "Rock", "Spirit Break": "Fairy",
    "Bitter Blade": "Fire", "Play Rough": "Fairy", "Iron Head": "Steel",
    "Close Combat": "Fighting", "Wild Charge": "Electric", "Crunch": "Dark",
    "Psychic Fangs": "Psychic", "Fire Fang": "Fire", "Ice Fang": "Ice",
    "Thunder Fang": "Electric", "Sacred Sword": "Fighting", "Behemoth Blade": "Steel",
    "Behemoth Bash": "Steel", "Moonblast": "Fairy", "Shadow Ball": "Ghost",
    "Flare Blitz": "Fire", "Body Press": "Fighting", "Stone Edge": "Rock",
    "Rock Slide": "Rock", "High Horsepower": "Ground", "Stomping Tantrum": "Ground",
    "Giga Impact": "Normal", "Hyper Beam": "Normal", "Tackle": "Normal",
    "Quick Attack": "Normal", "Extreme Speed": "Normal", "Bite": "Dark",
    "Nuzzle": "Electric", "Discharge": "Electric", "Earth Power": "Ground",
    "Power Gem": "Rock", "Tachyon Cutter": "Steel", "Bonemerang": "Ground",
    "Stone Axe": "Rock", "Growl": "Normal", "Harden": "Normal", "Calm Mind": "Psychic",
}

# Attacking type -> defending type -> multiplier
# Simplified chart
TYPES = ["Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground",
         "Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"]

# Chart rows = attack type, cols = defend type (same order). 0/0.5/1/2
# Built compactly for common needs
CHART = {
    "Normal": {"Rock":0.5,"Ghost":0,"Steel":0.5},
    "Fire": {"Fire":0.5,"Water":0.5,"Grass":2,"Ice":2,"Bug":2,"Rock":0.5,"Dragon":0.5,"Steel":2},
    "Water": {"Fire":2,"Water":0.5,"Grass":0.5,"Ground":2,"Rock":2,"Dragon":0.5},
    "Electric": {"Water":2,"Electric":0.5,"Grass":0.5,"Ground":0,"Flying":2,"Dragon":0.5},
    "Grass": {"Fire":0.5,"Water":2,"Grass":0.5,"Poison":0.5,"Ground":2,"Flying":0.5,"Bug":0.5,"Rock":2,"Dragon":0.5,"Steel":0.5},
    "Ice": {"Fire":0.5,"Water":0.5,"Grass":2,"Ice":0.5,"Ground":2,"Flying":2,"Dragon":2,"Steel":0.5},
    "Fighting": {"Normal":2,"Ice":2,"Poison":0.5,"Flying":0.5,"Psychic":0.5,"Bug":0.5,"Rock":2,"Ghost":0,"Dark":2,"Steel":2,"Fairy":0.5},
    "Poison": {"Grass":2,"Poison":0.5,"Ground":0.5,"Rock":0.5,"Ghost":0.5,"Steel":0,"Fairy":2},
    "Ground": {"Fire":2,"Electric":2,"Grass":0.5,"Poison":2,"Flying":0,"Bug":0.5,"Rock":2,"Steel":2},
    "Flying": {"Electric":0.5,"Grass":2,"Fighting":2,"Bug":2,"Rock":0.5,"Steel":0.5},
    "Psychic": {"Fighting":2,"Poison":2,"Psychic":0.5,"Dark":0,"Steel":0.5},
    "Bug": {"Fire":0.5,"Grass":2,"Fighting":0.5,"Poison":0.5,"Flying":0.5,"Psychic":2,"Ghost":0.5,"Dark":2,"Steel":0.5,"Fairy":0.5},
    "Rock": {"Fire":2,"Ice":2,"Fighting":0.5,"Ground":0.5,"Flying":2,"Bug":2,"Steel":0.5},
    "Ghost": {"Normal":0,"Psychic":2,"Ghost":2,"Dark":0.5},
    "Dragon": {"Dragon":2,"Steel":0.5,"Fairy":0},
    "Dark": {"Fighting":0.5,"Psychic":2,"Ghost":2,"Dark":0.5,"Fairy":0.5},
    "Steel": {"Fire":0.5,"Water":0.5,"Electric":0.5,"Ice":2,"Rock":2,"Steel":0.5,"Fairy":2},
    "Fairy": {"Fire":0.5,"Fighting":2,"Poison":0.5,"Dragon":2,"Dark":2,"Steel":0.5},
}

MENU_WORDS = re.compile(
    r"\b(bag|pokémon|pokemon|summary|pokedex|pokédex|options|settings|menu|items?|party|cancel|save and quit|save\s*&\s*quit)\b",
    re.I,
)
TYPE_WORDS = {t.lower(): t for t in TYPES}

_ocr = None
def ocr_engine():
    global _ocr
    if _ocr is None:
        from rapidocr_onnxruntime import RapidOCR
        _ocr = RapidOCR()
    return _ocr

def effectiveness(atk_type, def_types):
    if not atk_type:
        return 1.0
    if not def_types:
        return 1.0
    m = 1.0
    row = CHART.get(atk_type, {})
    for d in def_types:
        m *= row.get(d, 1.0)
    return m

def parse_types_from_text(text):
    found = []
    low = text.lower()
    for k, v in TYPE_WORDS.items():
        if re.search(rf"\b{re.escape(k)}\b", low):
            if v not in found:
                found.append(v)
    return found

def menu_detected(text):
    # Battle cues reduce false positives
    if re.search(r"\b(fight|ball|run|pokemon)\b", text, re.I) and re.search(r"\bfight\b", text, re.I):
        # Fight menu is OK (battle command menu) — not bag/party
        if not re.search(r"\b(bag|summary|pokedex|pokédex|settings|options|save)\b", text, re.I):
            # "Pokemon" on command menu is the switch command — allow
            pass
    if re.search(r"\b(bag|summary|pokedex|pokédex|settings|options|save and quit|items)\b", text, re.I):
        return True
    if re.search(r"\bmenu\b", text, re.I) and not re.search(r"\bfight\b", text, re.I):
        return True
    return bool(MENU_WORDS.search(text) and re.search(r"\b(bag|summary|pokedex|settings|options)\b", text, re.I))

def reward_ui_detected(text):
    """Post-wave / shop / transfer UI — must pick, not Fight."""
    if not text:
        return False
    return bool(re.search(
        r"\b(potion|super potion|full\s*heal|ether|elixir|revive|max\s*revive|"
        r"reroll|manage items|check team|transfer|pick (a |an )?|select (a |an )?|"
        r"nugget|poke\s*ball|great ball|ultra ball)\b",
        text, re.I))

def find_page():
    pages = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    return next(p for p in pages if p.get("type")=="page" and p.get("url","").startswith(PAGE) and "service-worker" not in p.get("url",""))

async def main():
    page = find_page()
    async with websockets.connect(page["webSocketDebuggerUrl"], max_size=50_000_000) as ws:
        n = 0
        async def call(method, params=None):
            nonlocal n
            n += 1
            msg = {"id": n, "method": method}
            if params is not None:
                msg["params"] = params
            await ws.send(json.dumps(msg))
            while True:
                raw = json.loads(await ws.recv())
                if raw.get("id") == n:
                    return raw
        async def eval_js(expr):
            r = await call("Runtime.evaluate", {"expression": expr, "returnByValue": True})
            return ((r.get("result") or {}).get("result") or {}).get("value")
        async def key_hold(key, code, kc, hold_ms=100):
            kwargs = {"type": "keyDown", "windowsVirtualKeyCode": kc, "code": code, "key": key}
            if len(key) == 1:
                kwargs["text"] = key
            await call("Input.dispatchKeyEvent", kwargs)
            await asyncio.sleep(hold_ms / 1000.0)
            await call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": kc, "code": code, "key": key})
        async def space(h=95):
            await call("Input.dispatchKeyEvent", {"type": "rawKeyDown", "windowsVirtualKeyCode": 32, "code": "Space", "key": " "})
            await asyncio.sleep(0.05)
            await call("Input.dispatchKeyEvent", {"type": "char", "windowsVirtualKeyCode": 32, "code": "Space", "key": " ", "text": " ", "unmodifiedText": " "})
            await asyncio.sleep(h / 1000.0)
            await call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 32, "code": "Space", "key": " "})
        async def press_z(h=90):
            await key_hold("z", "KeyZ", 90, h)
        async def act(h=95):
            await space(h)
            await asyncio.sleep(0.05)
            await press_z(h)
        async def back_out():
            await key_hold("x", "KeyX", 88, 90)
            await asyncio.sleep(0.06)
            await key_hold("Backspace", "Backspace", 8, 90)
        async def arrow(d, h=80):
            m = {"Up": ("ArrowUp", 38), "Down": ("ArrowDown", 40), "Left": ("ArrowLeft", 37), "Right": ("ArrowRight", 39)}
            c, k = m[d]
            await key_hold(c, c, k, h)

        async def get_state():
            return await eval_js("""(() => {
              const g = window.gameInfo || {};
              const party = (g.party || []).map(p => ({
                name: p.name, level: p.level, shiny: !!p.shiny,
                hp: p.currentHP, max: p.maxHP, fusion: !!p.isFusion,
                status: p.status || '', moves: (p.moveset||[]).slice(0,4),
                types: (p.types||[]).slice(0,2)
              }));
              return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome,luck:g.luck,party};
            })()""")

        def log(msg):
            line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
            print(line, flush=True)
            with LOG.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
        def write_status(st, extra=None):
            payload = {"ts": datetime.now().isoformat(), "script": "pr_farm14.py", **(st or {})}
            if extra:
                payload.update(extra)
            STATUS.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        async def focus():
            await call("Page.bringToFront")
            await eval_js("(()=>{const c=document.querySelector('canvas'); if(c){c.tabIndex=0;c.focus();} return 1;})()")

        async def screenshot_ocr():
            await focus()
            shot = await call("Page.captureScreenshot", {"format": "jpeg", "quality": 55})
            data = base64.b64decode(shot["result"]["data"])
            SHOT.write_bytes(data)
            try:
                engine = ocr_engine()
                result, _ = engine(str(SHOT))
                lines = []
                if result:
                    for item in result:
                        # item: [box, text, score]
                        if len(item) >= 2 and item[1]:
                            lines.append(str(item[1]))
                text = "\n".join(lines)
                return text
            except Exception as e:
                log(f"OCR err {e}")
                return ""

        async def escape_menus(max_rounds=10):
            """Absolute menu block: OCR detect bag/party/settings -> B until clear."""
            for rnd in range(max_rounds):
                text = await screenshot_ocr()
                if not text:
                    await back_out()
                    continue
                if reward_ui_detected(text):
                    return text  # let main loop pick a reward; do not B-cancel shop
                if menu_detected(text):
                    log(f"MENU DETECT -> B burst ({rnd})")
                    for _ in range(5):
                        await back_out()
                        await asyncio.sleep(0.15)
                    continue
                return text
            return await screenshot_ocr()

        def zacian(party):
            for i, p in enumerate(party or []):
                if p.get("name") == "Zacian":
                    return i, p
            return None, None

        def parse_pp_map(ocr_text, moves):
            """Map move name -> remaining PP from fight-menu OCR (e.g. Earthquake ... 0/10).
            gameInfo has no PP; this is the live guard source."""
            pp_map = {}
            if not ocr_text:
                return pp_map
            lines = [ln.strip() for ln in (ocr_text or "").splitlines() if ln.strip()]
            blob = " | ".join(lines)
            # Also flatten OCR without newlines (RapidOCR often returns space-separated)
            flat = re.sub(r"\s+", " ", ocr_text)
            for name in moves or []:
                clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                if not clean:
                    continue
                for src in (blob, flat):
                    pat = re.compile(re.escape(clean) + r".{0,60}?(\d+)\s*/\s*(\d+)", re.I)
                    m = pat.search(src)
                    if m:
                        pp_map[clean] = int(m.group(1))
                        break
                if clean in pp_map:
                    continue
                for ln in lines:
                    if clean.lower() in ln.lower():
                        m2 = PP_RE.search(ln)
                        if m2:
                            pp_map[clean] = int(m2.group(1))
                            break
                # Extra: if OCR shows "0/xx" immediately after a shortened token of the move
                if clean not in pp_map:
                    tok = clean.split()[0]
                    m3 = re.search(re.escape(tok) + r".{0,40}?0\s*/\s*\d+", flat, re.I)
                    if m3:
                        pp_map[clean] = 0
            return pp_map

        def pick_move(moves, def_types, doubles_like, stab_types=None, pp_map=None, last_move=None):
            """Return index of best move. Skip 0-PP, 0-eff, EQ in doubles, and last_move spam.
            When foe types unknown, prefer STAB (Fairy) and avoid EQ default."""
            stab_types = stab_types or ["Fairy"]
            pp_map = pp_map or {}
            scored = []
            for i, name in enumerate(moves or []):
                clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                at = MOVE_TYPE.get(clean)
                # Absolute: never select a move with 0 PP remaining
                if clean in pp_map and pp_map[clean] <= 0:
                    log(f"skip {clean} PP=0 (OCR)")
                    continue
                if clean == "Earthquake" and doubles_like:
                    log(f"skip EQ in doubles idx={i}")
                    continue
                if def_types:
                    eff = effectiveness(at, def_types) if at else 1.0
                    if eff <= 0:
                        log(f"skip {clean} eff=0 vs {def_types}")
                        continue
                    stab = 1.1 if at in stab_types else 1.0
                    score = eff * stab
                    # Soft penalty for repeating the same move last turn
                    if last_move and clean == last_move:
                        score *= 0.35
                    scored.append((score, eff, i, clean, at))
                else:
                    if clean == "Earthquake":
                        # Unknown PP: never prefer EQ (OCR miss must not spam empty EQ)
                        score = 0.05
                    elif at in stab_types:
                        score = 1.5
                    elif at in ("Rock", "Fire", "Fighting", "Steel"):
                        score = 1.1
                    else:
                        score = 1.0
                    if last_move and clean == last_move:
                        score *= 0.35
                    scored.append((score, 1.0, i, clean, at))
            if not scored:
                for i, name in enumerate(moves or []):
                    clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                    if clean in pp_map and pp_map[clean] <= 0:
                        continue
                    if clean == "Earthquake" and (doubles_like or (last_move == "Earthquake")):
                        continue
                    return i, clean, 1.0, MOVE_TYPE.get(clean)
                # Last resort: any non-zero-PP move, even EQ
                for i, name in enumerate(moves or []):
                    clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                    if clean in pp_map and pp_map[clean] <= 0:
                        continue
                    return i, clean, 1.0, MOVE_TYPE.get(clean)
                return None, None, 0.0, None
            scored.sort(key=lambda x: (-x[0], x[2]))
            best = scored[0]
            return best[2], best[3], best[1], best[4]

        async def select_move_index(idx):
            """Move grid: 0 1 / 2 3 — cursor starts on 0 after Fight."""
            # reset toward top-left
            await arrow("Up"); await asyncio.sleep(0.08)
            await arrow("Left"); await asyncio.sleep(0.08)
            await arrow("Up"); await asyncio.sleep(0.08)
            await arrow("Left"); await asyncio.sleep(0.08)
            if idx == 1:
                await arrow("Right")
            elif idx == 2:
                await arrow("Down")
            elif idx == 3:
                await arrow("Down"); await asyncio.sleep(0.08); await arrow("Right")
            await asyncio.sleep(0.12)
            await act(100)

        last_move_used = {"name": None}
        battle_shot_wave = {"w": None}

        async def save_battle_shot(tag="battle"):
            """Capture battle-start screenshot for BOREN-0 review (local file)."""
            try:
                SHOT_DIR.mkdir(parents=True, exist_ok=True)
                shot = await call("Page.captureScreenshot", {"format": "jpeg", "quality": 70})
                data = ((shot or {}).get("result") or {}).get("data")
                if not data:
                    log(f"battle shot empty resp keys={list(shot.keys()) if isinstance(shot, dict) else type(shot)}")
                    return None
                raw = base64.b64decode(data)
                ts = datetime.now().strftime("%H%M%S")
                path = SHOT_DIR / f"{tag}_{ts}.jpg"
                path.write_bytes(raw)
                log(f"battle shot saved {path.name} ({len(raw)} bytes)")
                return str(path)
            except Exception as e:
                log(f"battle shot fail: {e}")
                return None

        def shiny_detected(st, ocr_text):
            """Wild shiny overrides every other rule. Party luck-shinies do NOT count.
            Doubles-shiny KO-partner logic is a known gap (deferred)."""
            # Never treat own party shiny flags as a catch trigger (starters/luck mons are often shiny).
            # Wild/enemy shinies are not in gameInfo.party; rely on OCR / visual cues only.
            if re.search(r"\b(shiny|★|☆)\b", ocr_text or "", re.I):
                # Ignore if OCR is just reading party summary UI
                if re.search(r"\b(summary|pokedex|pokédex|bag)\b", ocr_text or "", re.I):
                    return False, None
                return True, "ocr"
            return False, None

        async def shiny_catch_flow(reason):
            """Fight menu → Ball path only when shiny. Known gap: doubles shiny (KO partner first)."""
            log(f"SHINY CATCH override reason={reason} (doubles-shiny deferred)")
            # From command menu: Fight is top-left; Ball is typically right of Fight
            await arrow("Up"); await asyncio.sleep(0.08)
            await arrow("Left"); await asyncio.sleep(0.08)
            await arrow("Right"); await asyncio.sleep(0.12)  # toward Ball
            await act(110)
            await asyncio.sleep(0.35)
            await act(110)  # confirm ball type / throw
            await asyncio.sleep(0.5)
            await act(100)

        async def smart_fight(st, ocr_text):
            nonlocal last_move_used
            party = st.get("party") or []
            zi, zmon = zacian(party)
            if not zmon:
                return
            # Shiny = top priority, overrides Fight-only / Zacian / PP / pickup
            is_shiny, shiny_why = shiny_detected(st, ocr_text)
            if is_shiny:
                await shiny_catch_flow(shiny_why)
                return
            moves = list(zmon.get("moves") or [])
            log(f"moves read: {moves}")
            def_types = parse_types_from_text(ocr_text or "")
            doubles_like = bool(re.search(r"double|2v2|ally", ocr_text or "", re.I))
            for p in party[1:]:
                n = p.get("name") or ""
                if n and re.search(rf"\b{re.escape(n)}\b", ocr_text or "", re.I):
                    doubles_like = True
            # Open Fight ONLY (never Run / Pokemon / Balls unless shiny above)
            await act(95)  # Fight / confirm
            await asyncio.sleep(0.35)
            text2 = await screenshot_ocr()
            if menu_detected(text2):
                log("MENU during fight — abort to B")
                for _ in range(6):
                    await back_out(); await asyncio.sleep(0.12)
                return
            # PP guard BEFORE selection: OCR move menu for remaining PP
            pp_map = parse_pp_map(text2, moves)
            log(f"PP map from fight UI: {pp_map or '{}'}")
            # If OCR missed PP but text clearly shows 0/ for Earthquake near name, also scan raw
            idx, name, eff, at = pick_move(
                moves, def_types, doubles_like,
                stab_types=list(zmon.get("types") or ["Fairy"]),
                pp_map=pp_map,
                last_move=last_move_used.get("name"),
            )
            if idx is None or name is None:
                log("NO eligible moves (all 0 PP?) — back out, do not spam")
                for _ in range(4):
                    await back_out(); await asyncio.sleep(0.1)
                return
            log(f"pick move[{idx}] {name} type={at} eff={eff} pp={pp_map.get(name,'?')} vs {def_types or 'unknown'} doubles={doubles_like} last={last_move_used.get('name')}")
            await select_move_index(idx)
            await asyncio.sleep(0.2)
            await act(90)  # target
            last_move_used["name"] = name

        await focus()
        st0 = await get_state()
        log(f"START farm14 FightOnly+PPguard+shinyOverride mode={st0 and st0.get('m')} wave={st0 and st0.get('w')} t={st0 and st0.get('t')}")
        write_status(st0, {"event": "start", "script": "pr_farm14.py"})
        if not st0 or st0.get("m") != "Classic":
            log(f"ABORT not Classic: {st0 and st0.get('m')}")
            return

        last_t = last_w = None
        stuck = 0
        i = 0
        wall = time.time()

        while True:
            if STOP.exists():
                log("STOP flag"); break
            i += 1
            try:
                st = await get_state()
                if not st:
                    await asyncio.sleep(0.4); continue
                if st.get("m") == "Endless":
                    log("Endless STOP"); break
                if st.get("m") and st.get("m") not in ("Classic", "Title"):
                    log(f"LEFT {st.get('m')}"); break

                party = st.get("party") or []
                zi, zmon = zacian(party)
                lead = party[0] if party else {}

                if zmon is not None and (zmon.get("hp") or 0) <= 0:
                    log("ZACIAN FAINT — stop"); write_status(st, {"event": "zacian_faint_end"}); break

                # Absolute menu guard first
                ocr_text = await escape_menus(max_rounds=4)

                # Wrong lead: switch to Zacian once if needed
                if lead.get("name") != "Zacian" and zmon and (zmon.get("hp") or 0) > 0:
                    log("lead not Zacian — back_out then one switch attempt")
                    for _ in range(5):
                        await back_out(); await asyncio.sleep(0.12)
                    # Only if still needed — navigate party carefully
                    st = await get_state() or st
                    party = st.get("party") or []
                    zi, zmon = zacian(party)
                    lead = party[0] if party else {}
                    if lead.get("name") != "Zacian" and zi is not None:
                        for _ in range(6):
                            await arrow("Up"); await asyncio.sleep(0.05)
                        for _ in range(zi):
                            await arrow("Down"); await asyncio.sleep(0.12)
                        await act(140)
                        await asyncio.sleep(0.6)
                        st2 = await get_state() or st
                        if (st2.get("party") or [{}])[0].get("name") != "Zacian":
                            for _ in range(6):
                                await back_out(); await asyncio.sleep(0.15)
                    continue

                # Ally faint while Zacian lead: confirm/back only
                if any((p.get("hp") or 0) <= 0 for p in party[1:]):
                    await act(95); await asyncio.sleep(0.1); await back_out()

                # Post-wave reward/shop: pick an item (prefer Ether/Elixir for PP), never Fight
                if reward_ui_detected(ocr_text):
                    log("REWARD UI — pick item (mandatory)")
                    # Prefer Ether/Elixir if visible (PP restore); else confirm current highlight
                    low = (ocr_text or "").lower()
                    if "elixir" in low:
                        # rough nav: reset top-left then step — shop grids vary; mash confirm after arrows
                        for _ in range(3):
                            await arrow("Up"); await asyncio.sleep(0.05)
                            await arrow("Left"); await asyncio.sleep(0.05)
                        for _ in range(6):
                            await arrow("Down"); await asyncio.sleep(0.08)
                            text_chk = await screenshot_ocr()
                            if re.search(r"\belixir\b", text_chk or "", re.I):
                                break
                    elif "ether" in low:
                        for _ in range(3):
                            await arrow("Up"); await asyncio.sleep(0.05)
                            await arrow("Left"); await asyncio.sleep(0.05)
                        for _ in range(5):
                            await arrow("Down"); await asyncio.sleep(0.08)
                    await act(120); await asyncio.sleep(0.25); await act(110)
                    await asyncio.sleep(0.3)
                    continue

                phase = i % 6
                if phase < 4:
                    await smart_fight(st, ocr_text)
                elif phase == 4:
                    # mandatory pickup / dialogue
                    await act(100); await asyncio.sleep(0.15); await act(95)
                else:
                    ocr_text = await escape_menus(max_rounds=3)
                    await act(90)

                await asyncio.sleep(0.4)

                if i % 2 == 0:
                    st = await get_state() or st
                    party = st.get("party") or []
                    alive = sum(1 for p in party if (p.get("hp") or 0) > 0)
                    lead = party[0] if party else {}
                    log(
                        f"wave={st.get('w')} t={st.get('t')} mode={st.get('m')} biome={st.get('b')} "
                        f"luck={st.get('luck')} alive={alive} lead={lead.get('name')} "
                        f"L{lead.get('level')} hp={lead.get('hp')}/{lead.get('max')}"
                    )
                    write_status(st, {"alive": alive, "i": i, "uptime_s": int(time.time()-wall)})
                    w, t = st.get("w"), st.get("t")
                    if last_t is not None and t == last_t and w == last_w:
                        stuck += 1
                    else:
                        if last_w is not None and w and w > last_w:
                            log(f"WAVE UP {last_w} -> {w}")
                            await save_battle_shot(f"wave{w}")
                            battle_shot_wave["w"] = w
                        stuck = 0
                    last_t, last_w = t, w
                    if stuck >= 3:
                        log("unstick: menu escape + act")
                        await escape_menus(max_rounds=6)
                        for _ in range(4):
                            await act(95); await asyncio.sleep(0.2)
                        stuck = 0

            except Exception as e:
                log(f"ERR {e}")
                traceback.print_exc()
                await asyncio.sleep(2)

        write_status(await get_state(), {"event": "exit"})
        log("DONE")

if __name__ == "__main__":
    SHOT_DIR.mkdir(parents=True, exist_ok=True)
    asyncio.run(main())
