p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
R('''    cands.sort(key=lambda c: -c[0])
    return cands[0][1]''','''    cands.sort(key=lambda c: -c[0])
    top = cands[0]; tm = top[1]
    def _low(m): return m["left"] < PP_CONSERVE_ABS or (m.get("max") and m["left"] / m["max"] < PP_CONSERVE_FRAC)
    def _e(m): return max(m.get("effs") or [1])
    if _low(tm):
        alts = [c for c in cands[1:] if not _low(c[1]) and c[0] >= 0.5 * top[0] and _e(c[1]) >= _e(tm) / 2]
        only_se = _e(tm) >= 2 and all(_e(c[1]) < 1 for c in cands[1:])
        if alts and not only_se:
            log(f"PP CONSERVE skip {tm['n']} ({tm['left']}/{tm.get('max')}) -> {alts[0][1]['n']}")
            return alts[0][1]
    return tm''')
R('''def pick_move(''','''PP_CONSERVE_ABS = 5
PP_CONSERVE_FRAC = 0.34
def pick_move(''')
R('''log(f"SHOP proactive:''','''log(f"PP CONSERVE: low<{PP_CONSERVE_ABS} or <{PP_CONSERVE_FRAC:.0%}"); log(f"SHOP proactive:''')
open(p,"w",encoding="utf-8").write(s); print("ok")
