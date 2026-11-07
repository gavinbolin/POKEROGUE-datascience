import re
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
old='''                if h == "CommandUiHandler":
                    wild_shiny = (not st.get("trainer")) and any(e["sh"] for e in st.get("enemy") or [])'''
new='''                shiny_en = [(k, e) for k, e in enumerate(st.get("enemy") or []) if e.get("sh")]
                if shiny_en and h in ("CommandUiHandler", "FightUiHandler", "TargetSelectUiHandler", "BallUiHandler"):
                    k, e = shiny_en[0]
                    log(f"SHINY ENEMY: {e['n']} wave {w} slot {k} (all={[x['n'] for _, x in shiny_en]}) -> STOP, no input")
                    sp = await shot(SHOT_DIR, f"shiny_enemy_w{w}", "png")
                    STATUS.write_text(json.dumps({"ts": datetime.now().isoformat(), "script": "pr_farm17.py", "wave": w,
                        "stopped_reason": "shiny_enemy", "shiny_species": e["n"], "shiny_slot": k,
                        "shiny_all": [x["n"] for _, x in shiny_en], "trainer": st.get("trainer"), "double": st.get("double"),
                        "screenshot": str(sp)}, indent=1), encoding="utf-8")
                    STOP.write_text(f"shiny_enemy {e['n']} wave {w}", encoding="utf-8")
                    return
                if h == "CommandUiHandler":
                    wild_shiny = (not st.get("trainer")) and any(e["sh"] for e in st.get("enemy") or [])'''
assert s.count(old)==1; s=s.replace(old,new); open(p,"w",encoding="utf-8").write(s)
