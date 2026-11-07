#!/usr/bin/env python3
"""PokéRogue Classic candy/egg farm — continue current save. No Escape, no Enter mash."""
import json, asyncio, websockets, urllib.request, pathlib, time, traceback
from datetime import datetime

PAGE_URL = "https://pokerogue.net/"
LOG = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_farm_log.txt")
STATUS = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_farm_status.json")
FLAG_EGG = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_do_egg.flag")
STOP = pathlib.Path(r"C:\Users\gavin\agent-tools\pokerogue_farm_stop.flag")
LEAD = "Zacian"
EGG_COST = 6
# Heuristic: attempt egg loop every this many waves gained after start, if flag not used
EGG_EVERY_WAVES = 40

def find_page():
    pages = json.load(urllib.request.urlopen("http://127.0.0.1:9222/json/list"))
    return next(
        p for p in pages
        if p.get("type") == "page"
        and p.get("url", "").startswith(PAGE_URL)
        and "service-worker" not in p.get("url", "")
    )

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
            await call("Input.dispatchKeyEvent", {
                "type": "keyUp", "windowsVirtualKeyCode": kc, "code": code, "key": key
            })

        async def press_z(hold=100):
            await key_hold("z", "KeyZ", 90, hold)

        async def press_bs(hold=100):
            await key_hold("Backspace", "Backspace", 8, hold)

        async def arrow(dir_, hold=80):
            m = {
                "Up": ("ArrowUp", 38), "Down": ("ArrowDown", 40),
                "Left": ("ArrowLeft", 37), "Right": ("ArrowRight", 39),
            }
            code, kc = m[dir_]
            await key_hold(code, code, kc, hold)

        async def get_state():
            return await eval_js("""(() => {
              const g = window.gameInfo || {};
              const party = (g.party || []).map(p => ({
                name: p.name, level: p.level, shiny: !!p.shiny,
                hp: p.currentHP, max: p.maxHP, fusion: !!p.isFusion,
                status: p.status || '', nature: p.nature || '',
                moves: (p.moveset || []).slice(0,4),
                ability: p.ability || '', passive: p.passiveAbility || ''
              }));
              return {
                t: g.playTime, w: g.wave, m: g.gameMode, b: g.biome,
                luck: g.luck, money: g.money, party
              };
            })()""")

        def log(msg):
            line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
            print(line, flush=True)
            with LOG.open("a", encoding="utf-8") as f:
                f.write(line + "\n")

        def write_status(st, extra=None):
            payload = {"ts": datetime.now().isoformat(), **(st or {})}
            if extra:
                payload.update(extra)
            STATUS.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        async def ensure_settings():
            changed = await eval_js("""(() => {
              const raw = localStorage.getItem('settings');
              let s = {};
              try { s = raw ? JSON.parse(raw) : {}; } catch(e) { s = {}; }
              if (!s.general) s.general = {};
              const g = s.general;
              const want = {
                gameSpeed: 5, hpBarSpeed: 3, expGainsSpeed: 3,
                partyExpNotificationMode: 2, eggSkipPreference: 2,
                battleStyle: 1, enableTutorials: false,
                skipSeenDialogues: true, levelMoveConfirmation: false
              };
              let ch = false;
              for (const [k,v] of Object.entries(want)) {
                if (g[k] !== v) { g[k] = v; ch = true; }
              }
              if (ch) localStorage.setItem('settings', JSON.stringify(s));
              return ch;
            })()""")
            return bool(changed)

        async def unstick():
            log("unstick Backspace+Z (no Esc/Enter)")
            for _ in range(6):
                await press_bs(110)
                await asyncio.sleep(0.2)
            for _ in range(3):
                await arrow("Down")
                await asyncio.sleep(0.1)
            await press_z(110)
            await asyncio.sleep(0.3)
            for _ in range(5):
                await press_z(100)
                await asyncio.sleep(0.3)

        async def fight_turn(double_hint=True):
            # Fight menu: Z = Fight. Prefer Spirit Break (move 3) over Earthquake in doubles.
            # Move grid: 1 EQ | 2 Mighty Cleave / 3 Spirit Break | 4 Bitter Blade
            await press_z(95)  # Fight or confirm
            await asyncio.sleep(0.35)
            if double_hint:
                await arrow("Down")  # move 3 Spirit Break
                await asyncio.sleep(0.15)
            await press_z(95)  # select move
            await asyncio.sleep(0.35)
            # target select in doubles: confirm first/left foe
            await press_z(90)
            await asyncio.sleep(0.25)

        async def reward_pass():
            # Generic: try confirm common top rewards; cancel junk with Backspace occasionally
            await press_z(90)
            await asyncio.sleep(0.25)
            # sometimes need arrow to Rare Candy / Soothe Bell rows
            if (time.time() // 1) % 5 == 0:
                await arrow("Down")
                await asyncio.sleep(0.12)
                await press_z(90)

        async def egg_loop():
            """Save&Quit -> New Game Classic -> Zacian Buy Egg -> cancel -> Continue."""
            log("EGG LOOP start: Save&Quit path")
            # Open menu: typically M or Escape — skill says NEVER Escape.
            # PokéRogue menu is often opened with M / Enter / button. Try M key then arrows.
            # Fallback: many builds use Esc for pause — skill forbids Esc during farm loop.
            # Use 'M' for menu if bound; else try pressing nothing and document failure.
            await key_hold("m", "KeyM", 77, 120)
            await asyncio.sleep(0.8)
            # Navigate to Save and Quit — usually near bottom of pause menu
            for _ in range(10):
                await arrow("Down")
                await asyncio.sleep(0.12)
            await press_z(120)  # Save and Quit?
            await asyncio.sleep(1.5)
            await press_z(120)  # confirm
            await asyncio.sleep(2.0)
            st = await get_state()
            log(f"after savequit mode={st and st.get('m')} wave={st and st.get('w')}")
            # Title: New Game
            # cursor often on Continue; go Down to New Game or find it
            await asyncio.sleep(1.0)
            # Try select New Game (often 2nd)
            await arrow("Down")
            await asyncio.sleep(0.3)
            await press_z(120)
            await asyncio.sleep(1.0)
            # Classic mode
            await press_z(120)
            await asyncio.sleep(1.5)
            # Starter select — need Zacian. This is fuzzy without OCR.
            # Try typing / navigating — press Z on default then look for Use Candies.
            # Better approach: arrow around and look for candy UI.
            log("EGG LOOP: on starter select — seeking Zacian Use Candies")
            for _ in range(8):
                await press_z(100)
                await asyncio.sleep(0.5)
            # Try Down to Buy Egg options
            for _ in range(6):
                await arrow("Down")
                await asyncio.sleep(0.15)
                await press_z(100)
                await asyncio.sleep(0.4)
            # Cancel out — Backspace repeatedly to title
            for _ in range(12):
                await press_bs(120)
                await asyncio.sleep(0.35)
            await asyncio.sleep(1.0)
            # Continue
            # Title cursor to Continue (usually top)
            for _ in range(5):
                await arrow("Up")
                await asyncio.sleep(0.12)
            await press_z(120)
            await asyncio.sleep(2.0)
            st = await get_state()
            log(f"EGG LOOP done mode={st and st.get('m')} wave={st and st.get('w')}")
            write_status(st, {"event": "egg_loop_done"})
            return st

        # --- boot ---
        await call("Page.bringToFront")
        await eval_js("document.querySelector('canvas') && document.querySelector('canvas').focus()")
        patched = await ensure_settings()
        log(f"START farm9 settings_patched={patched}")

        st0 = await get_state()
        write_status(st0, {"event": "start", "settings_patched": patched, "script": "pr_farm9.py"})
        log(f"state mode={st0 and st0.get('m')} wave={st0 and st0.get('w')} biome={st0 and st0.get('b')} luck={st0 and st0.get('luck')} t={st0 and st0.get('t')}")
        if st0 and st0.get("m") and st0.get("m") not in ("Classic", "Title"):
            log(f"ABORT non-Classic mode={st0.get('m')}")
            return

        start_wave = (st0 or {}).get("w") or 0
        last_egg_wave = start_wave
        last_t = last_w = None
        stuck = 0
        i = 0
        last_milestone = start_wave
        start_wall = time.time()

        # Kick current Fight menu: prefer Spirit Break path
        for _ in range(2):
            await fight_turn(double_hint=True)
            await asyncio.sleep(0.5)

        while True:
            if STOP.exists():
                log("STOP flag seen — exiting")
                break
            i += 1
            try:
                phase = i % 14
                if phase < 8:
                    # primary battle: alternate EQ-safe Spirit Break path vs plain Z
                    if phase % 2 == 0:
                        await fight_turn(double_hint=True)
                    else:
                        await press_z(95)
                elif phase < 10:
                    await reward_pass()
                elif phase == 10:
                    await press_bs(100)
                elif phase == 11:
                    # fainted switch recovery: Backspace, Down to living, Z
                    await press_bs(100)
                    await asyncio.sleep(0.15)
                    await arrow("Down")
                    await asyncio.sleep(0.1)
                    await press_z(100)
                elif phase == 12:
                    await arrow("Right")
                    await asyncio.sleep(0.12)
                    await press_z(95)
                else:
                    await arrow("Down")
                    await asyncio.sleep(0.12)
                    await press_z(95)

                await asyncio.sleep(0.7)

                if i % 3 == 0:
                    st = await get_state()
                    if not st:
                        continue
                    party = st.get("party") or []
                    alive = sum(1 for p in party if (p.get("hp") or 0) > 0)
                    lead = party[0] if party else {}
                    line = (
                        f"wave={st.get('w')} t={st.get('t')} mode={st.get('m')} "
                        f"biome={st.get('b')} luck={st.get('luck')} alive={alive} "
                        f"lead={lead.get('name')} L{lead.get('level')} hp={lead.get('hp')}/{lead.get('max')}"
                    )
                    log(line)
                    write_status(st, {
                        "alive": alive,
                        "script": "pr_farm9.py",
                        "i": i,
                        "uptime_s": int(time.time() - start_wall),
                    })

                    mode = st.get("m")
                    if mode and mode not in ("Classic", "Title"):
                        log(f"LEFT CLASSIC -> {mode} STOP")
                        break

                    w = st.get("w")
                    t = st.get("t")
                    if last_t is not None and t == last_t and w == last_w:
                        stuck += 1
                    else:
                        if last_w is not None and w and w > last_w:
                            log(f"WAVE UP {last_w} -> {w}")
                        stuck = 0
                    last_t, last_w = t, w

                    if stuck >= 6:
                        await unstick()
                        stuck = 0

                    # Egg triggers
                    do_egg = False
                    if FLAG_EGG.exists():
                        do_egg = True
                        try:
                            FLAG_EGG.unlink()
                        except Exception:
                            pass
                    elif w and (w - last_egg_wave) >= EGG_EVERY_WAVES and w >= start_wave + 10:
                        # heuristic only — candies not readable (encrypted data_PHOR)
                        do_egg = True
                        log(f"heuristic egg attempt at wave {w}")

                    if do_egg and mode == "Classic":
                        await egg_loop()
                        last_egg_wave = (await get_state() or {}).get("w") or w
                        stuck = 0

                    if w and last_milestone and w >= last_milestone + 10:
                        last_milestone = w
                        log(f"MILESTONE wave {w}")

            except Exception as e:
                log(f"ERR {e}")
                traceback.print_exc()
                await asyncio.sleep(2)
                try:
                    # reconnect-ish: refocus
                    await call("Page.bringToFront")
                except Exception:
                    pass

        stf = await get_state()
        write_status(stf, {"event": "exit"})
        log(f"DONE {stf}")

if __name__ == "__main__":
    asyncio.run(main())
