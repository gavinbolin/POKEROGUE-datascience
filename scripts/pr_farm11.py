#!/usr/bin/env python3
"""PokéRogue Classic farm11 — NEVER Earthquake in doubles. Space=Action. No Esc/Enter mash."""
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
        async def space(h=95):
            await call("Input.dispatchKeyEvent", {"type": "rawKeyDown", "windowsVirtualKeyCode": 32, "code": "Space", "key": " "})
            await asyncio.sleep(0.05)
            await call("Input.dispatchKeyEvent", {"type": "char", "windowsVirtualKeyCode": 32, "code": "Space", "key": " ", "text": " ", "unmodifiedText": " "})
            await asyncio.sleep(h / 1000.0)
            await call("Input.dispatchKeyEvent", {"type": "keyUp", "windowsVirtualKeyCode": 32, "code": "Space", "key": " "})
        async def z(h=90):
            await key_hold("z", "KeyZ", 90, h)
        async def act(h=95):
            await space(h)
            await asyncio.sleep(0.06)
            await z(h)
        async def cancel():
            await key_hold("x", "KeyX", 88, 95)
            await asyncio.sleep(0.1)
            await key_hold("Backspace", "Backspace", 8, 95)
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
            payload = {"ts": datetime.now().isoformat(), "script": "pr_farm11.py", **(st or {})}
            if extra:
                payload.update(extra)
            STATUS.write_text(json.dumps(payload, indent=2), encoding="utf-8")

        async def focus():
            await call("Page.bringToFront")
            await eval_js("(()=>{const c=document.querySelector('canvas'); if(c){c.tabIndex=0;c.focus();} return 1;})()")
            box = await eval_js("(()=>{const c=document.querySelector('canvas'); const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2};})()")
            if box:
                await call("Input.dispatchMouseEvent", {"type": "mousePressed", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})
                await asyncio.sleep(0.04)
                await call("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": box["x"], "y": box["y"], "button": "left", "clickCount": 1})

        async def no_eq_fight():
            """Fight then NEVER pick move 1 (Earthquake). Prefer Spirit Break (Down) or Mighty Cleave (Right)."""
            await act(95)  # Fight / confirm dialogue
            await asyncio.sleep(0.28)
            # Move grid: 1 EQ | 2 Mighty Cleave / 3 Spirit Break | 4 Bitter Blade
            # Always leave slot 1: alternate Down (Spirit Break) and Right (Mighty Cleave)
            if (int(time.time()) // 2) % 2 == 0:
                await arrow("Down")  # Spirit Break
            else:
                await arrow("Right")  # Mighty Cleave
            await asyncio.sleep(0.14)
            await act(95)  # select move
            await asyncio.sleep(0.22)
            await act(90)  # target in doubles

        async def faint_switch(st):
            party = st.get("party") or []
            idx = next((i for i, p in enumerate(party) if (p.get("hp") or 0) > 0), None)
            if idx is None:
                log("WIPE")
                return False
            for _ in range(6):
                await arrow("Up")
                await asyncio.sleep(0.07)
            for _ in range(idx):
                await arrow("Down")
                await asyncio.sleep(0.12)
            await act(130)
            await asyncio.sleep(0.4)
            log(f"faint_switch {idx} {party[idx].get('name')}")
            return True

        async def try_ball():
            await arrow("Right")
            await asyncio.sleep(0.18)
            await act(110)
            await asyncio.sleep(0.35)
            await act(95)
            for _ in range(5):
                await act(90)
                await asyncio.sleep(0.35)

        async def egg_loop():
            log("EGG LOOP")
            await key_hold("m", "KeyM", 77, 120)
            await asyncio.sleep(0.9)
            for _ in range(12):
                await arrow("Down")
                await asyncio.sleep(0.12)
            await act(120)
            await asyncio.sleep(1.2)
            await act(120)
            await asyncio.sleep(2.0)
            await arrow("Down")
            await asyncio.sleep(0.3)
            await act(120)
            await asyncio.sleep(1.0)
            await act(120)
            await asyncio.sleep(1.5)
            for _ in range(10):
                await act(100)
                await asyncio.sleep(0.4)
            for _ in range(8):
                await arrow("Down")
                await asyncio.sleep(0.12)
                await act(100)
                await asyncio.sleep(0.3)
            for _ in range(14):
                await cancel()
                await asyncio.sleep(0.28)
            for _ in range(5):
                await arrow("Up")
                await asyncio.sleep(0.12)
            # Load Game path safer than Continue (Continue may hit Endless)
            await arrow("Down")
            await asyncio.sleep(0.2)
            await arrow("Down")
            await asyncio.sleep(0.2)
            await act(120)
            await asyncio.sleep(1.2)
            # pick bottom Classic slot: Down past Endless slots
            for _ in range(4):
                await arrow("Down")
                await asyncio.sleep(0.25)
            await act(120)
            await asyncio.sleep(0.5)
            for _ in range(3):
                await arrow("Up")
                await asyncio.sleep(0.1)
            await act(120)
            await asyncio.sleep(2.0)
            st = await get_state()
            if st and st.get("m") == "Endless":
                log("EGG hit Endless - reload abort")
                await call("Page.reload", {"ignoreCache": False})
                await asyncio.sleep(8)
                return st
            log(f"EGG done {st and st.get('m')} w={st and st.get('w')}")
            write_status(st, {"event": "egg_loop"})
            return st

        await focus()
        st0 = await get_state()
        log(f"START farm11 noEQ mode={st0 and st0.get('m')} wave={st0 and st0.get('w')} t={st0 and st0.get('t')}")
        write_status(st0, {"event": "start", "no_earthquake_doubles": True})
        if not st0 or st0.get("m") != "Classic":
            log(f"ABORT not Classic: {st0 and st0.get('m')}")
            return

        start_wave = st0.get("w") or 0
        last_egg_wave = start_wave
        last_t = last_w = None
        stuck = 0
        i = 0
        wall = time.time()
        last_milestone = start_wave
        # Snapshot for special-event reload: track lead hp / party deaths mid-wave
        prev_lead_hp = None
        prev_alive = None

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
                if st.get("m") == "Endless":
                    log("Endless STOP")
                    write_status(st, {"event": "endless_abort"})
                    break
                if st.get("m") and st.get("m") not in ("Classic", "Title"):
                    log(f"LEFT {st.get('m')}")
                    break

                party = st.get("party") or []
                lead = party[0] if party else {}
                alive = sum(1 for p in party if (p.get("hp") or 0) > 0)
                lead_hp = lead.get("hp") or 0

                # Special-event bad outcome heuristic: sudden lead KO or forced swap
                # (alive drop + lead not Zacian / lead hp 0) mid same wave — reload Classic
                if prev_lead_hp is not None and prev_alive is not None:
                    lead_name = lead.get("name")
                    bad_event = False
                    if prev_lead_hp > 0 and lead_hp <= 0 and lead_name == "Zacian":
                        # could be normal faint — only reload if flagged via file
                        pass
                    if FLAG_EGG.exists() is False:
                        # optional: pokerogue_reload_event.flag for manual/special
                        evflag = OUT / "pokerogue_reload_event.flag"
                        if evflag.exists():
                            bad_event = True
                            try:
                                evflag.unlink()
                            except Exception:
                                pass
                    if bad_event:
                        log("special-event bad outcome -> reload Classic via Load Game")
                        await call("Page.reload", {"ignoreCache": False})
                        await asyncio.sleep(8)
                        await focus()
                        # Load Game -> Classic slot
                        for _ in range(2):
                            await arrow("Down")
                            await asyncio.sleep(0.2)
                        await act(120)
                        await asyncio.sleep(1.0)
                        for _ in range(4):
                            await arrow("Down")
                            await asyncio.sleep(0.25)
                        await act(120)
                        await asyncio.sleep(0.5)
                        for _ in range(3):
                            await arrow("Up")
                            await asyncio.sleep(0.1)
                        await act(120)
                        await asyncio.sleep(2.0)
                        stuck = 0
                        continue

                if party and lead_hp <= 0 and alive > 0:
                    await faint_switch(st)

                phase = i % 16
                if phase < 10:
                    # HARD RULE: never confirm move slot 1 (Earthquake) while partner may be out
                    await no_eq_fight()
                elif phase == 10:
                    await try_ball()  # shiny catch override path
                elif phase == 11:
                    await act(95)  # messages / rewards
                elif phase == 12:
                    await cancel()  # close Info
                elif phase == 13:
                    await arrow("Down")
                    await asyncio.sleep(0.1)
                    await act(110)
                elif phase == 14:
                    await act(95)
                else:
                    await cancel()
                    await asyncio.sleep(0.1)
                    await act(95)

                await asyncio.sleep(0.6)

                if i % 3 == 0:
                    st = await get_state() or st
                    party = st.get("party") or []
                    alive = sum(1 for p in party if (p.get("hp") or 0) > 0)
                    lead = party[0] if party else {}
                    log(
                        f"wave={st.get('w')} t={st.get('t')} mode={st.get('m')} biome={st.get('b')} "
                        f"luck={st.get('luck')} alive={alive} lead={lead.get('name')} "
                        f"L{lead.get('level')} hp={lead.get('hp')}/{lead.get('max')}"
                    )
                    write_status(st, {"alive": alive, "i": i, "uptime_s": int(time.time() - wall), "no_eq": True})
                    prev_lead_hp = lead.get("hp")
                    prev_alive = alive

                    w, t = st.get("w"), st.get("t")
                    if last_t is not None and t == last_t and w == last_w:
                        stuck += 1
                    else:
                        if last_w is not None and w and w > last_w:
                            log(f"WAVE UP {last_w} -> {w}")
                        stuck = 0
                    last_t, last_w = t, w

                    if stuck >= 5:
                        log("unstick")
                        for _ in range(5):
                            await cancel()
                            await asyncio.sleep(0.18)
                        st2 = await get_state() or st
                        party2 = st2.get("party") or []
                        if party2 and (party2[0].get("hp") or 0) <= 0:
                            await faint_switch(st2)
                        for _ in range(6):
                            await no_eq_fight()
                            await asyncio.sleep(0.35)
                        stuck = 0
                        await focus()

                    do_egg = FLAG_EGG.exists()
                    if do_egg:
                        try:
                            FLAG_EGG.unlink()
                        except Exception:
                            pass
                    elif w and (w - last_egg_wave) >= EGG_EVERY:
                        do_egg = True
                        log(f"heuristic egg wave {w}")
                    if do_egg and st.get("m") == "Classic":
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
