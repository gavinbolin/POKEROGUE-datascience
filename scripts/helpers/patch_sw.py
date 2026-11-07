import re
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
rep("reroll_n = {}; reroll_log = {};","sw_try = {}; sw_turn = set(); reroll_n = {}; reroll_log = {};")
rep("""                    else:
                        if wild_shiny: log("wild shiny in doubles - deferred (fight)")
                        if st.get("cur") != 0: await set_cursor(0)
                        await Z()""","""                    else:
                        if wild_shiny: log("wild shiny in doubles - deferred (fight)")
                        # ZACIAN SWITCH-IN (Gavin OK 14:21): Zacian alive, off field, healthy -> Pokemon menu
                        do_sw = False
                        if not wild_shiny and z["hp"] > 0 and not z["f"] and st.get("ph") == "CommandPhase" and sw_try.get(w, 0) < 2:
                            fld = [p for p in party if p["f"] and p["hp"] > 0]
                            usr = next((p for p in fld if p["n"] == st.get("user")), fld[0] if fld else None)
                            zr = z["hp"] / max(1, z.get("mx") or 1)
                            ur = (usr["hp"] / max(1, usr.get("mx") or 1)) if usr else 0
                            weakest = (not usr) or len(fld) < 2 or ur <= min(p["hp"] / max(1, p.get("mx") or 1) for p in fld)
                            trapped = await ev("(()=>{try{const s=window.__pr_cam.scene;const f=s.getPlayerField();const u=f[(s.phaseManager.getCurrentPhase().fieldIndex)||0];return !!(u&&u.isTrapped&&u.isTrapped())}catch(e){return false}})()")
                            turn = await ev("window.__pr_cam.scene.currentBattle.turn")
                            tk = (w, turn, st.get("fi"))
                            if weakest and not trapped and tk not in sw_turn and (zr >= 0.5 or (zr > 0 and ur < 0.25)):
                                sw_turn.add(tk); do_sw = True
                                if any(k[0] == w and k != tk for k in sw_turn): sw_try[w] = sw_try.get(w, 0) + 1
                                log(f"ZACIAN SWITCH-IN w{w} turn {turn}: {usr and usr['n']} {usr and usr['hp']}/{usr and usr.get('mx')} -> Zacian {z['hp']}/{z.get('mx')} (try {sw_try.get(w,0)+1})")
                        if do_sw:
                            await set_cursor(2); await Z()
                        else:
                            if st.get("cur") != 0: await set_cursor(0)
                            await Z()""")
rep("""                        tgt = next((p["i"] for p in party if p["hp"] > 0 and not p["f"] and p["n"] != "Zacian"), None)""",
"""                        tgt = z["i"] if (z["hp"] > 0 and not z["f"]) else next((p["i"] for p in party if p["hp"] > 0 and not p["f"] and p["n"] != "Zacian"), None)""")
rep("""                    elif ph == "SelectModifierPhase":
                        dead =""","""                    elif ph == "CommandPhase":
                        if z["hp"] > 0 and not z["f"]:
                            tgt = z["i"]; want_opt = 0; log(f"switch-in CommandPhase party: Zacian slot {tgt}")
                        else:
                            log("party UI in CommandPhase, Zacian not switchable - back"); await X(); await asyncio.sleep(0.3); continue
                    elif ph == "SelectModifierPhase":
                        dead =""")
rep("""                    else:
                        await X()  # answer No (e.g. switch prompt / learn move)""","""                    elif st.get("ph") == "CheckSwitchPhase" and z["hp"] > 0 and not z["f"] and z["hp"] >= 0.5 * (z.get("mx") or 1):
                        log(f"CheckSwitch prompt w{w} -> Yes (send Zacian)"); await set_cursor(0); await Z()
                    else:
                        await X()  # answer No (e.g. switch prompt / learn move)""")
s=s.replace("START farm17 [reroll+vit+balls+tier]","START farm17 [reroll+vit+balls+tier+zswitch]")
open(p,"w",encoding="utf-8").write(s); print("ok")
