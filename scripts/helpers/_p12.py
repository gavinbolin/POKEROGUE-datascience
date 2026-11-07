p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
I=" "*28
R("tag = None\n", "tag = None\n"+I+"_bud = REROLL_CHEAP_FRAC * _m0; _sp = rr_spent.get(w, 0)\n"+I+"if _sp + cost > _bud:\n"+I+"    log(f\"REROLL budget stop spent={_sp} next={cost} budget={int(_bud)}\"); _ok = False\n")
R("reroll_n[w] = reroll_n.get(w, 0) + 1; log(f\"{tag}", "XX")  if False else None
R("if tag:\n"+I+"    reroll_n[w] = reroll_n.get(w, 0) + 1", "if tag:\n"+I+"    reroll_n[w] = reroll_n.get(w, 0) + 1; rr_spent[w] = _sp + cost")
R("elif _ok and no_hi and not want and cost <= _cap:", "elif _ok and no_hi and not want:")
R("cheap_n = {};", "cheap_n = {}; rr_spent = {};")
R('log("REROLL nothing>ultra: within SHOP caps, max 5/screen");', 'log("REROLL budget: total rerolls <= 10% of money at screen open, max 5/screen, shop floor kept");')
open(p,"w",encoding="utf-8").write(s); print("ok")
