p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''    ally_dead = any(''','''    _dm = [m for m in (st.get("zmoves") or []) if (m.get("pow") or 0) > 0]
    pp_crit = bool(_dm) and (sum(m["left"] for m in _dm) <= 3 or all(m["left"] <= 0 for m in _dm if max(m.get("effs") or [1]) >= 2) and any(max(m.get("effs") or [1]) >= 2 for m in _dm))
    ally_dead = any(''')
R('''        if "leppa" in n: return -20''','''        if "leppa" in n: return -20 if (pp_crit or pp_low) else 30  # Leppa: top only when PP is short
        if any(k in n for k in PP_ITEMS): return -10 if pp_crit else 94  # PP items: near bottom unless critical''')
R('''    if _seen: pass''','''    if not _seen and any(k in bn for k in PP_ITEMS) and pp_crit: log(f"PP item taken (critical) w{w0}: {best['n']}")
    elif not _seen and any(any(k in x["n"].lower() for k in PP_ITEMS) for x in rew): log(f"PP item skipped (pp ok) w{w0} -> {best['n']}")
    if _seen: pass''')
R('''log("FREEZE-DRY:''','''log("PP items: rank 94 unless pp_crit (dmg PP<=3 or all SE moves 0)"); log("FREEZE-DRY:''')
open(p,"w",encoding="utf-8").write(s); print("ok")
