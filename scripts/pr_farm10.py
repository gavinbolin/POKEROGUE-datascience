#!/usr/bin/env python3
"""PokéRogue Classic farm10 — durable. No Escape/Enter mash. Cancel=X+Backspace."""
import json, asyncio, websockets, urllib.request, pathlib, time, traceback
from datetime import datetime

PAGE = "https://pokerogue.net/"
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"
STATUS = OUT / "pokerogue_farm_status.json"
STOP = OUT / "pokerogue_farm_stop.flag"
FLAG_EGG = OUT / "pokerogue_do_egg.flag"
EGG_EVERY = 50

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
        async def z(h=100):
            await key_hold("z", "KeyZ", 90, h)
        async def cancel():
            await key_hold("x", "KeyX", 88, 100)
            await asyncio.sleep(0.12)
            await key_hold("Backspace", "Backspace", 8, 100)
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
                status: p.status || '', moves: (p.moveset||[]).slice(0,4)
              }));
              return {t:g.playTime,w:g.wave,m:g.gameMode,b:g.biome,luck:g.luck,party};
            })()""")
        def log(msg):
            line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
            print(line, flush=True)
            with LOG.open("a", encoding="utf-8") as f:
                f.write(line + "\n")
        def write_status(st, extra=None):
            payload = {"ts": datetime.now().isoformat(), "script": "pr_farm10.py", **(st or {})}
            if extra:
                payload.update(extra)
            STATUS.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        async def focus():
            await call("Page.bringToFront")
            await eval_js("(()=>{const c=document.querySelector('canvas'); if(c){c.tabIndex=0;c.focus();} return 1;})()")
            box = await eval_js("(()=>{const c=document.querySelector('canvas'); const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2};})()")
            if box:
                await call("Input.dispatchMouseEvent", {"type": "mousePressed", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})
                await asyncio.sleep(0.05)
                await call("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})

        async def faint_switch(st):
            party = st.get("party") or []
            # index of first living
            idx = next((i for i, p in enumerate(party) if (p.get("hp") or 0) > 0), None)
            if idx is None:
                log("WIPE all fainted")
                return False
            # From top of party list, Down idx times then Z. Never cancel forced switch.
            for _ in range(idx):
                await arrow("Down")
                await asyncio.sleep(0.14)
            await z(130)
            await asyncio.sleep(0.5)
            log(f"faint_switch -> slot {idx} {party[idx].get('name')}")
            return True

        async def try_catch_shiny():
            # Fight menu: Right = Ball, Z, Z target
            await arrow("Right")
            await asyncio.sleep(0.2)
            await z(120)
            await asyncio.sleep(0.45)
            await z(120)
            await asyncio.sleep(0.4)
            await z(100)
            await asyncio.sleep(0.5)
            for _ in range(8):
                await z(95)
                await asyncio.sleep(0.4)

        async def egg_loop():
            log("EGG LOOP begin")
            # Menu via M (ALT_BUTTON_MENU), not Escape
            await key_hold("m", "KeyM", 77, 120)
            await asyncio.sleep(0.9)
            for _ in range(12):
                await arrow("Down")
                await asyncio.sleep(0.12)
            await z(120)
            await asyncio.sleep(1.2)
            await z(120)
            await asyncio.sleep(2.0)
            # Title -> New Game (Down) -> Classic -> Zacian candy buy (fuzzy)
            await arrow("Down")
            await asyncio.sleep(0.3)
            await z(120)
            await asyncio.sleep(1.0)
            await z(120)  # Classic
            await asyncio.sleep(1.5)
            for _ in range(10):
                await z(100)
                await asyncio.sleep(0.45)
            for _ in range(8):
                await arrow("Down")
                await asyncio.sleep(0.12)
                await z(100)
                await asyncio.sleep(0.35)
            for _ in range(14):
                await cancel()
                await asyncio.sleep(0.3)
            for _ in range(5):
                await arrow("Up")
                await asyncio.sleep(0.12)
            await z(120)  # Continue
            await asyncio.sleep(2.0)
            st = await get_state()
            log(f"EGG LOOP done {st and st.get('m')} w={st and st.get('w')}")
            write_status(st, {"event": "egg_loop"})
            return st

        await focus()
        st0 = await get_state()
        log(f"START farm10 mode={st0 and st0.get('m')} wave={st0 and st0.get('w')} t={st0 and st0.get('t')} luck={st0 and st0.get('luck')}")
        write_status(st0, {"event": "start"})
        if st0 and st0.get("m") and st0.get("m") not in ("Classic", "Title"):
            log(f"ABORT mode={st0.get('m')}")
            return

        start_wave = (st0 or {}).get("w") or 0
        last_egg_wave = start_wave
        last_t = last_w = None
        stuck = 0
        i = 0
        wall = time.time()
        last_milestone = start_wave

        while True:
            if STOP.exists():
                log("STOP flag")
                break
            i += 1
            try:
                st = await get_state()
                if not st:
                    await asyncio.sleep(0.5)
                    continue
                mode = st.get("m")
                if mode and mode not in ("Classic", "Title"):
                    log(f"LEFT CLASSIC {mode}")
                    write_status(st, {"event": "left_classic"})
                    break

                party = st.get("party") or []
                lead = party[0] if party else {}
                lead_hp = (lead.get("hp") or 0) if lead else 0
                # If lead fainted / 0 hp and others alive, try switch
                alive_idx = [j for j, p in enumerate(party) if (p.get("hp") or 0) > 0]
                if lead_hp <= 0 and alive_idx:
                    # likely on switch screen
                    await faint_switch(st)
                    await asyncio.sleep(0.4)

                phase = i % 16
                if phase < 9:
                    # message clear + Fight + first move (Z). Occasional Spirit Break path if Zacian lead with EQ
                    await z(95)
                    if lead.get("name") == "Zacian" and lead_hp > 0 and phase % 3 == 1:
                        await asyncio.sleep(0.25)
                        await arrow("Down")
                        await asyncio.sleep(0.12)
                        await z(95)
                        await asyncio.sleep(0.2)
                        await z(90)  # target
                elif phase == 9:
                    # shiny catch attempt periodically (Right=Ball)
                    await try_catch_shiny()
                elif phase in (10, 11):
                    await z(95)  # rewards / text
                elif phase == 12:
                    await cancel()
                elif phase == 13:
                    # faint recovery without canceling forced switch: Down+Z
                    await arrow("Down")
                    await asyncio.sleep(0.12)
                    await z(120)
                elif phase == 14:
                    await arrow("Right")
                    await asyncio.sleep(0.12)
                    await z(95)
                else:
                    await z(95)

                await asyncio.sleep(0.65)

                if i % 3 == 0:
                    st = await get_state() or st
                    party = st.get("party") or []
                    alive = sum(1 for p in party if (p.get("hp") or 0) > 0)
                    lead = party[0] if party else {}
                    line = (
                        f"wave={st.get('w')} t={st.get('t')} mode={st.get('m')} biome={st.get('b')} "
                        f"luck={st.get('luck')} alive={alive} lead={lead.get('name')} "
                        f"L{lead.get('level')} hp={lead.get('hp')}/{lead.get('max')}"
                    )
                    log(line)
                    write_status(st, {"alive": alive, "i": i, "uptime_s": int(time.time() - wall)})

                    w, t = st.get("w"), st.get("t")
                    if last_t is not None and t == last_t and w == last_w:
                        stuck += 1
                    else:
                        if last_w is not None and w and w > last_w:
                            log(f"WAVE UP {last_w} -> {w}")
                        stuck = 0
                    last_t, last_w = t, w

                    if stuck >= 5:
                        log("unstick cancel+Z+faint_switch")
                        for _ in range(4):
                            await cancel()
                            await asyncio.sleep(0.2)
                        st2 = await get_state() or st
                        party2 = st2.get("party") or []
                        if party2 and (party2[0].get("hp") or 0) <= 0:
                            await faint_switch(st2)
                        for _ in range(6):
                            await z(100)
                            await asyncio.sleep(0.3)
                        stuck = 0
                        await focus()

                    # egg triggers
                    do_egg = False
                    if FLAG_EGG.exists():
                        do_egg = True
                        try:
                            FLAG_EGG.unlink()
                        except Exception:
                            pass
                    elif w and (w - last_egg_wave) >= EGG_EVERY:
                        do_egg = True
                        log(f"heuristic egg at wave {w}")
                    if do_egg and mode == "Classic":
                        await egg_loop()
                        last_egg_wave = (await get_state() or {}).get("w") or w
                        stuck = 0

                    if w and last_milestone is not None and w >= last_milestone + 10:
                        last_milestone = w
                        log(f"MILESTONE wave {w}")

            except Exception as e:
                log(f"ERR {e}")
                traceback.print_exc()
                await asyncio.sleep(2)
                try:
                    await focus()
                except Exception:
                    pass

        write_status(await get_state(), {"event": "exit"})
        log("DONE")

if __name__ == "__main__":
    asyncio.run(main())
