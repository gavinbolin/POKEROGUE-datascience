#!/usr/bin/env python3
"""PokéRogue farm12 — Zacian-only, no menus, pick up items, no EQ in doubles."""
import json, asyncio, websockets, urllib.request, pathlib, time, traceback
from datetime import datetime

PAGE = "https://pokerogue.net/"
OUT = pathlib.Path(r"C:\Users\gavin\agent-tools")
LOG = OUT / "pokerogue_farm_log.txt"
STATUS = OUT / "pokerogue_farm_status.json"
STOP = OUT / "pokerogue_farm_stop.flag"
FLAG_EGG = OUT / "pokerogue_do_egg.flag"

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
            # Confirm: item pickup, Fight, dialogue — never opens Menu by itself
            await space(h)
            await asyncio.sleep(0.05)
            await z(h)
        async def back_out():
            # Absolute menu abort: B/Backspace only (no Escape — Settings softlock)
            await key_hold("x", "KeyX", 88, 90)
            await asyncio.sleep(0.08)
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
            payload = {"ts": datetime.now().isoformat(), "script": "pr_farm12.py", **(st or {})}
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

        def zacian_idx(party):
            for i, p in enumerate(party or []):
                if p.get("name") == "Zacian":
                    return i
            return None

        async def no_eq_fight():
            """Fight; never pick move slot 1 (Earthquake) while partner may be out."""
            await act(95)
            await asyncio.sleep(0.28)
            if (int(time.time()) // 2) % 2 == 0:
                await arrow("Down")  # Spirit Break
            else:
                await arrow("Right")  # Mighty Cleave
            await asyncio.sleep(0.14)
            await act(95)
            await asyncio.sleep(0.2)
            await act(90)  # target if doubles

        async def switch_to_zacian_once(st):
            """Complete a faint-switch onto Zacian. Verify lead changes. No spam loop."""
            party = st.get("party") or []
            zi = zacian_idx(party)
            if zi is None:
                log("no Zacian in party")
                return False
            z = party[zi]
            if (z.get("hp") or 0) <= 0:
                log("ZACIAN FAINT — run end (no replacement)")
                write_status(st, {"event": "zacian_faint_end"})
                return "END"
            # Already party slot 0 with HP = treat as already fielded when possible
            if zi == 0 and (party[0].get("hp") or 0) > 0:
                # Ally fainted elsewhere — Zacian still lead: dismiss UI only
                await act(100)
                await asyncio.sleep(0.25)
                await back_out()
                log("ally faint; Zacian already lead — no switch")
                return True
            before = await get_state()
            before_lead = ((before or {}).get("party") or [{}])[0].get("name")
            # Navigate party UI carefully: top then Down zi times, confirm once
            for _ in range(8):
                await arrow("Up")
                await asyncio.sleep(0.06)
            for _ in range(zi):
                await arrow("Down")
                await asyncio.sleep(0.14)
            await act(140)
            await asyncio.sleep(0.7)
            after = await get_state() or {}
            after_party = after.get("party") or []
            after_lead = (after_party[0].get("name") if after_party else None)
            after_z = next((p for p in after_party if p.get("name")=="Zacian"), None)
            ok = after_lead == "Zacian" or (after_z and (after_z.get("hp") or 0) > 0 and before_lead != "Zacian" and after_lead == "Zacian")
            # Success if Zacian is slot 0 with HP, or lead name Zacian
            if after_party and after_party[0].get("name") == "Zacian" and (after_party[0].get("hp") or 0) > 0:
                log(f"switch_ok Zacian (was {before_lead})")
                return True
            log(f"switch_miss lead={after_lead} — one retry then back_out")
            # One retry only
            for _ in range(8):
                await arrow("Up")
                await asyncio.sleep(0.05)
            for _ in range(zi):
                await arrow("Down")
                await asyncio.sleep(0.14)
            await act(150)
            await asyncio.sleep(0.8)
            after2 = await get_state() or {}
            ap2 = after2.get("party") or []
            if ap2 and ap2[0].get("name") == "Zacian" and (ap2[0].get("hp") or 0) > 0:
                log("switch_ok Zacian on retry")
                return True
            # Abort thrash: back out of menus
            for _ in range(6):
                await back_out()
                await asyncio.sleep(0.2)
            return False

        await focus()
        st0 = await get_state()
        log(f"START farm12 ZacianOnly noMenu pickItems noEQ mode={st0 and st0.get('m')} wave={st0 and st0.get('w')} t={st0 and st0.get('t')}")
        write_status(st0, {"event": "start", "rules": ["zacian_only", "no_menu", "pickup_items", "no_eq_doubles"]})
        if not st0 or st0.get("m") != "Classic":
            log(f"ABORT not Classic: {st0 and st0.get('m')}")
            return

        last_t = last_w = None
        stuck = 0
        i = 0
        wall = time.time()
        last_switch_try = 0
        switch_fail_streak = 0

        while True:
            if STOP.exists():
                log("STOP flag")
                break
            i += 1
            try:
                st = await get_state()
                if not st:
                    await asyncio.sleep(0.4)
                    continue
                if st.get("m") == "Endless":
                    log("Endless STOP")
                    write_status(st, {"event": "endless_abort"})
                    break
                if st.get("m") and st.get("m") not in ("Classic", "Title"):
                    log(f"LEFT {st.get('m')}")
                    break

                party = st.get("party") or []
                zi = zacian_idx(party)
                zmon = party[zi] if zi is not None else None
                lead = party[0] if party else {}

                # Zacian faint = run end
                if zmon is not None and (zmon.get("hp") or 0) <= 0:
                    log("ZACIAN FAINT — stopping (no replacement)")
                    write_status(st, {"event": "zacian_faint_end"})
                    break

                # Hard menu abort when stuck: prefer back_out before any navigation
                # Never press M. Never open Pokemon/item menus on purpose.

                # Faint / wrong lead handling (Zacian-only)
                need_zacian = False
                if lead.get("name") != "Zacian" and zmon and (zmon.get("hp") or 0) > 0:
                    need_zacian = True
                if lead.get("name") == "Zacian" and (lead.get("hp") or 0) <= 0:
                    # should have been caught above
                    need_zacian = False

                if need_zacian:
                    now = time.time()
                    if now - last_switch_try < 2.5:
                        # cooldown — only back out / confirm, do not spam switch
                        await back_out()
                        await asyncio.sleep(0.15)
                        await act(90)
                    else:
                        last_switch_try = now
                        res = await switch_to_zacian_once(st)
                        if res == "END":
                            break
                        if res:
                            switch_fail_streak = 0
                        else:
                            switch_fail_streak += 1
                            if switch_fail_streak >= 3:
                                log("switch_fail_streak — back_out burst")
                                for _ in range(8):
                                    await back_out()
                                    await asyncio.sleep(0.18)
                                switch_fail_streak = 0
                    await asyncio.sleep(0.35)
                else:
                    # Ally faint with Zacian still lead: just confirm/back_out, never party menu
                    if any((p.get("hp") or 0) <= 0 for p in party[1:]):
                        await act(95)
                        await asyncio.sleep(0.15)
                        await back_out()

                    # Productive loop: pickup/dialogue confirm + no-EQ fight only
                    # Phase avoids menu-opening arrow+act patterns from farm11
                    phase = i % 8
                    if phase < 5:
                        await no_eq_fight()
                    elif phase == 5:
                        # Mandatory item / message clear
                        await act(100)
                        await asyncio.sleep(0.2)
                        await act(95)
                    elif phase == 6:
                        await back_out()  # leave any accidental menu
                    else:
                        await act(95)

                await asyncio.sleep(0.45)

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
                    write_status(st, {"alive": alive, "i": i, "uptime_s": int(time.time() - wall), "script": "pr_farm12.py"})

                    w, t = st.get("w"), st.get("t")
                    if last_t is not None and t == last_t and w == last_w:
                        stuck += 1
                    else:
                        if last_w is not None and w and w > last_w:
                            log(f"WAVE UP {last_w} -> {w}")
                        stuck = 0
                    last_t, last_w = t, w

                    if stuck >= 4:
                        log("unstick back_out+act (no menu nav)")
                        for _ in range(6):
                            await back_out()
                            await asyncio.sleep(0.15)
                        for _ in range(4):
                            await act(95)
                            await asyncio.sleep(0.25)
                        # only fight if Zacian lead
                        st2 = await get_state() or st
                        p2 = st2.get("party") or []
                        if p2 and p2[0].get("name") == "Zacian" and (p2[0].get("hp") or 0) > 0:
                            for _ in range(4):
                                await no_eq_fight()
                                await asyncio.sleep(0.3)
                        stuck = 0
                        await focus()

                    # Egg only via explicit flag — never auto-open menus for egg on a timer
                    if FLAG_EGG.exists():
                        log("EGG flag present but farm12 skips menu egg loop — clear flag")
                        try:
                            FLAG_EGG.unlink()
                        except Exception:
                            pass

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
