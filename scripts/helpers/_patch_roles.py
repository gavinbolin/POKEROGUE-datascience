p="state.js"; s=open(p,encoding="utf-8").read()
a="o.party=party.map((p,i)=>({i,n:p.name,hp:p.hp,mx:p.getMaxHp?.(),f:!!p.isOnField?.()}));"
assert s.count(a)==1; s=s.replace(a,"o.party=party.map((p,i)=>({i,n:p.name,sp:p.species?.speciesId,hp:p.hp,mx:p.getMaxHp?.(),f:!!p.isOnField?.()}));")
open(p,"w",encoding="utf-8").write(s)
p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b,c=1):
    global s
    assert s.count(a)==c,(a,s.count(a)); s=s.replace(a,b)
R('''VITAMINS = [''','''# ROLES: the two mons the farm keeps alive (match species id, else name)
PRIMARY = ("Zacian", {888})
SECONDARY = ("Feebas", {349, 350})  # Feebas + Milotic
def role(party, r):
    return next((p for p in party or [] if p.get("sp") in r[1] or p.get("n") == r[0] or (r is SECONDARY and p.get("n") == "Milotic")), None)
VITAMINS = [''')
R('''    z = next((p for p in st["party"] if p["n"] == "Zacian"), None)
    pp_low''','''    z = role(st["party"], PRIMARY)
    sec = role(st["party"], SECONDARY)
    pp_low''')
R('''    feebas = any(p.get("n") == "Feebas" for p in st.get("party") or [])''','''    feebas = sec is not None
    def _r(p): return (p["hp"] / p["mx"]) if (p and p.get("mx")) else 1.0
    role_dead = [p["n"] for p in (z, sec) if p and p["hp"] <= 0]
    role_low = [p["n"] for p in (z, sec) if p and p["hp"] > 0 and _r(p) < 0.6]''')
R('''        rank_inner = rank0(r); t = r.get("t")
''','''        rank_inner = rank0(r); t = r.get("t")
        if role_dead and ("revive" in r["n"].lower() or "sacred ash" in r["n"].lower()):
            return -300  # ROLE REVIVE: above Master tier
''')
R('''        if heal_need and any(k in n for k in HEAL):''','''        if role_low and any(k in n for k in HEAL): return -45 + [k in n for k in HEAL].index(True) / 10  # ROLE HEAL
        if heal_need and any(k in n for k in HEAL):''')
R('''    best = min(rew, key=rank)
''','''    best = min(rew, key=rank)
    bn = best["n"].lower()
    if role_dead and ("revive" in bn or "sacred ash" in bn): log(f"ROLE REVIVE w{w0}: {best['n']} for fainted {role_dead}")
    elif role_low and any(k in bn for k in HEAL): log(f"ROLE HEAL w{w0}: {best['n']} for low {role_low}")
''')
R('''                z = next((p for p in party if p["n"] == "Zacian"), None)''','''                z = role(party, PRIMARY)''')
R('''next((j for j, p in enumerate(party) if p["n"] == "Feebas"), None)''','''next((j for j, p in enumerate(party) if p is role(party, SECONDARY)), None)''',2)
R('''                        if z and z["hp"] <= 0: dead = party.index(z)''','''                        _sec = role(party, SECONDARY)
                        if _sec and _sec["hp"] <= 0: dead = party.index(_sec)
                        if z and z["hp"] <= 0: dead = party.index(z)  # primary first
                        _lp = (last_pick[0] or "").lower()
                        if _sec and _sec["hp"] > 0 and _sec.get("mx") and any(k in _lp for k in ("potion", "full restore", "full heal")) and not ("revive" in _lp):
                            _zr = z["hp"] / z["mx"] if z.get("mx") else 1; _sr = _sec["hp"] / _sec["mx"]
                            if _sr < 0.6 and not (_zr < 0.6 and _zr <= _sr): tgt = party.index(_sec); log(f"ROLE HEAL target secondary {_sec['n']} {_sr:.0%}")''')
R('''log("CANDY priority:''','''log(f"ROLES primary={PRIMARY[0]} secondary={SECONDARY[0]}/Milotic"); log("CANDY priority:''')
open(p,"w",encoding="utf-8").write(s); print("ok")
