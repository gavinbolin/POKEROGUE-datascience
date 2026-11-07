p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
s=s.replace('''    if role_dead and ("revive" in bn''','''    _k = (w0, best["n"]); _seen = _k == getattr(pick_reward, "_rl", None); pick_reward._rl = _k
    if _seen: pass
    elif role_dead and ("revive" in bn''',1)
open(p,"w",encoding="utf-8").write(s)
