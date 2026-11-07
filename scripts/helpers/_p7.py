p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''        if "prism scale" in r["n"].lower() and sec''','''        if any(k in r["n"].lower() for k in ("rusted sword", "ancient sword")) and z:
            return -290  # SWORD: Zacian Crowned form item, above Master tier
        if "prism scale" in r["n"].lower() and sec''')
R('''                        if _sec and "prism scale" in (last_pick[0] or "").lower():''','''                        if z and any(k in (last_pick[0] or "").lower() for k in ("rusted sword", "ancient sword")):
                            tgt = party.index(z)
                            if same == 0: log(f"SWORD -> {z['n']} slot {tgt}")
                        if _sec and "prism scale" in (last_pick[0] or "").lower():''')
R('''log("PRISM SCALE: rank''','''log("SWORD: Rusted/Ancient Sword rank -290 -> PRIMARY"); log("PRISM SCALE: rank''')
open(p,"w",encoding="utf-8").write(s); print("ok")
