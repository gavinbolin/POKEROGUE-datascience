p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''        if role_dead and ("revive" in r["n"].lower()''','''        if "prism scale" in r["n"].lower() and sec and (sec.get("sp") == 349 or sec.get("n") == "Feebas"):
            return -290  # PRISM SCALE: evolve Feebas, above Master tier
        if role_dead and ("revive" in r["n"].lower()''')
R('''                        if _sec and "eviolite" in (last_pick[0] or "").lower():''','''                        if _sec and "prism scale" in (last_pick[0] or "").lower():
                            tgt = party.index(_sec)
                            if same == 0: log(f"PRISM SCALE -> {_sec['n']} slot {tgt}")
                        if _sec and "eviolite" in (last_pick[0] or "").lower():''')
R('''log("PP items: rank''','''log("PRISM SCALE: rank -290 + apply to SECONDARY while Feebas"); log("PP items: rank''')
open(p,"w",encoding="utf-8").write(s); print("ok")
