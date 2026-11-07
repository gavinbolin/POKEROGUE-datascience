p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''        if "candy jar" in n or "rare candy" in n: return -55''','''        if "eviolite" in n and sec and (sec.get("sp") == 349 or sec.get("n") == "Feebas"): return -54  # EVIOLITE for unevolved SECONDARY
        if "candy jar" in n or "rare candy" in n: return -55''')
R('''                        _sec = role(party, SECONDARY)
''','''                        _sec = role(party, SECONDARY)
                        if _sec and "eviolite" in (last_pick[0] or "").lower():
                            tgt = party.index(_sec)
                            if same == 0: log(f"EVIOLITE -> {_sec['n']} slot {tgt}")
''')
R('''log(f"ROLES primary=''','''log("EVIOLITE rule: rank -54 + apply to SECONDARY while unevolved"); log(f"ROLES primary=''')
open(p,"w",encoding="utf-8").write(s); print("ok")
