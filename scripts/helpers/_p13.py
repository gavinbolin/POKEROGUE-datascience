p="pr_farm17.py"; s=open(p,encoding="utf-8").read()
def R(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
I=" "*28
R("if tag:\n"+I+"    reroll_n[w] = reroll_n.get(w, 0) + 1; rr_spent[w] = _sp + cost",
  "if tag:\n"+I+"    _n = reroll_n.get(w, 0); _p = REROLL_DECAY ** _n\n"+I+"    if random.random() >= _p:\n"+I+"        log(f\"REROLL decay skip n={_n} p={_p:.2f}\"); tag = None\n"+I+"if tag:\n"+I+"    reroll_n[w] = reroll_n.get(w, 0) + 1; rr_spent[w] = _sp + cost")
R("REROLL_CHEAP_MAX = 3\n", "REROLL_CHEAP_MAX = 3\nREROLL_DECAY = 0.6\n")
if "import random" not in s: s = "import random\n" + s
open(p,"w",encoding="utf-8").write(s); print("ok")
