"""Offline replay of REWARD pick / REROLL lines through prio.py (data ranker). Usage: python replay_test.py LOG JSON"""
import os, re, sys, ast, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent)); sys.path.insert(0, os.path.join(os.environ.get("TEMP", ""), "prfarm")); import prio
LOGF = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\gavin\agent-tools\pokerogue_farm_log.txt"
if len(sys.argv) > 2: prio.PRIO_PATHS = [pathlib.Path(sys.argv[2])]
D = prio.load(); TI = {v: k for k, v in prio.TN.items()}
TUP = re.compile(r"\((-?[\d.]+), '((?:[^'\\]|\\.)*)', '([A-Z]+)'(?:, '[^']*')?\)")
lines = open(LOGF, encoding="utf-8", errors="replace").read().splitlines()
res = []; lure_left = 0
for k, L in enumerate(lines):
    m = re.search(r"LURE active \((\d+) left\)", L)
    if m: lure_left = int(m.group(1)); continue
    if "LURE none active" in L: lure_left = 0; continue
    kind = "PICK" if " REWARD pick " in L else ("REROLL" if re.search(r" REROLL (cheap|junk|nothing)\S* ", L) else None)
    if not kind or "ranking=[" in L and False: pass
    if not kind: continue
    opts = [(float(a), b, c) for a, b, c in TUP.findall(L)]
    if len(opts) < 2: continue
    g = lambda pat, d=None: (re.search(pat, L).group(1) if re.search(pat, L) else d)
    zhp = float(g(r"zhp=(\d+)%", 100)) / 100; risky = g(r"risky_next=(\w+)") == "True"
    nm = lambda s: prio.norm(s)
    has = lambda f: any(f(o) for o in opts)
    ballout = has(lambda o: nm(o[1]).endswith(" ball") and 20 <= o[0] < 21)
    flags = dict(lure_active=lure_left > 0 and has(lambda o: "lure" in nm(o[1]) and o[0] >= 96), pp_low=g(r"pp_low=(\w+)") == "True",
                 heal_need=g(r"heal_need=(\w+)") == "True", zhp_low=zhp < 0.5, role_low=zhp < 0.75 or has(lambda o: -45 <= o[0] < -44),
                 out_of_balls=ballout, holding_balls=not ballout, secondary_in_party=True,
                 pp_crit=has(lambda o: any(x in nm(o[1]) for x in ("ether", "elixir")) and -10 <= o[0] < -9),
                 ally_dead=has(lambda o: "revive" in nm(o[1]) and o[0] in (2, 23)), role_dead=has(lambda o: o[0] == -300),
                 dna_pair=has(lambda o: o[0] == -250), zacian_in_party=True, secondary_is_feebas=has(lambda o: o[0] == -290 and "prism" in nm(o[1])))
    flags["emergency"] = flags["voucher_crit"] = zhp < 0.25 and risky and has(lambda o: "full restore" in nm(o[1]) or "max potion" in nm(o[1]))
    if kind == "PICK": old = g(r"REWARD pick (.+?) tier=")
    else: old = min(opts)[1]
    rew = [{"n": n, "t": TI[t]} for _, n, t in opts]
    rk = [(prio.rank_item(r, flags, D), r) for r in rew]
    best = min(rk, key=lambda x: x[0][0]); new = best[1]["n"]
    res.append(dict(ts=L[:8], kind=kind, old=old, new=new, junk=best[0][0][0] == 2, rule=best[0][2], opts=[(n, t) for _, n, t in opts], lure=flags["lure_active"], fl=flags))
ch = [r for r in res if r["old"] != r["new"]]
print(f"screens replayed: {len(res)} (PICK {sum(r['kind']=='PICK' for r in res)}, REROLL {sum(r['kind']=='REROLL' for r in res)}); pick changed: {len(ch)}")
pairs = collections.Counter((r["old"], r["new"]) for r in ch)
print("top changes old -> new:"); [print(f"  {c:4d}  {a} -> {b}") for (a, b), c in pairs.most_common(40)]
def show(ts):
    for r in res:
        if r["ts"] == ts: print(f"  {ts} {r['kind']} old={r['old']} new={r['new']} rule={r['rule']} lure_active={r['lure']} opts={r['opts']}")
print("required cases:"); show("18:11:13"); show("17:23:51")
# rule checks
bad = []
for r in res:
    tiers = {n: TI[t] for n, t in r["opts"]}
    if r["lure"] and "lure" in r["new"].lower() and not r["junk"]: bad.append(("lure while active", r))
    if r["lure"] and "lure" in r["new"].lower() and any("lure" not in n.lower() for n, _ in r["opts"]): bad.append(("lure while active beat something", r))
print("rule violations:", len(bad)); [print("  ", b[0], b[1]) for b in bad[:10]]
def _eff(n, t, fl): return prio.rank_item({"n": n, "t": TI[t]}, fl, D)[0]
lowtier = 0
for r in res:
    if r["junk"] or r["rule"] in ("role_revive", "sword", "prism_scale", "dna_pair", "emergency_heal"): continue
    kn = _eff(r["new"], dict(r["opts"])[r["new"]], r["fl"])
    if any(_eff(n, t, r["fl"])[:2] < kn[:2] for n, t in r["opts"]): lowtier += 1
print("picks where a real (non-junk) item of a higher effective tier lost (should be 0):", lowtier)
print("junk best (reroll still triggers):", sum(r["junk"] for r in res))
