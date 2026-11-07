"""Data-driven reward ranking for pr_farm17 (Gavin 10/30 18:25 MT). Source of truth: item_priority.json."""
import json, re, pathlib, unicodedata
PRIO_PATHS = [pathlib.Path(r"C:\Users\gavin\..PROJECT\pokerogue\item_priority.json"), pathlib.Path(__file__).parent / "item_priority.json"]
_C = {"data": None, "path": None, "mtime": None, "src": None}
def norm(n):
    n = str(n).replace("\u2019", "'").replace("\u2018", "'").replace("\u00d7", "x")
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", n).strip().lower()
def _valid(d):
    assert isinstance(d.get("rules"), list) and d["rules"] and isinstance(d.get("tier_order"), dict) and isinstance(d.get("specials"), dict)
    for r in d["rules"]: assert r["match"] and isinstance(r["rank"], (int, float))
    return d
def load(log=print, force=False):
    for p in PRIO_PATHS:
        try:
            mt = p.stat().st_mtime
            if not force and _C["path"] == p and _C["mtime"] == mt: return _C["data"]
            d = _valid(json.loads(p.read_text(encoding="utf-8")))
            first = _C["data"] is None
            _C.update(data=d, path=p, mtime=mt, src=str(p))
            log(f"ITEM PRIORITY {'loaded' if first else 'RELOADED'}: {p} ({len(d['rules'])} rules, v{d.get('version')}, tier-first, junk>={d.get('junk_threshold')})")
            return d
        except FileNotFoundError: continue
        except Exception as e: log(f"!!! ITEM PRIORITY FILE INVALID {p}: {e!r} -- trying next"); continue
    if _C["data"] is None or _C["src"] != "BUILTIN":
        log("!!! ITEM PRIORITY FILE MISSING/INVALID -> BUILT-IN FALLBACK (tier-first, everything default 50, junk rules lost) !!!")
        _C.update(data={"tier_order": {"COMMON":0,"GREAT":1,"ULTRA":2,"ROGUE":3,"MASTER":4,"LUXURY":5}, "junk_threshold": 93, "default_rank": 50,
                        "specials": {"master_ball":-400,"role_revive":-300,"sword":-290,"prism_scale":-290,"mega_bracelet":-380,"eelektrossite":-370,"dna_pair":-250,"emergency_heal":-240},
                        "rules": [{"id":"lure_active","match":["lure"],"mode":"substring","when":"lure_active","rank":100.5},
                                  {"id":"menu","match":["tm","memory mushroom","mint","dna splicers"],"mode":"menu","rank":99}]},
                  src="BUILTIN", path=None, mtime=None)
    return _C["data"]
def _hit(n, pat, mode):
    if mode == "word": return re.search(r"\b" + re.escape(pat) + r"\b", n) is not None
    if mode == "prefix": return n.startswith(pat)
    if mode == "prefix_or_substring": return n.startswith(pat) if pat.endswith(" ") else pat in n
    if mode == "menu": return pat in n  # tm handled in within()
    if mode == "ball": return n.endswith(" ball") and pat in n
    return pat in n
def _when(expr, flags):
    if not expr: return True
    toks = re.findall(r"\(|\)|\w+", expr)
    py = " ".join(t if t in ("and", "or", "not", "(", ")") else repr(bool(flags.get(t, False))) for t in toks)
    return bool(eval(py, {"__builtins__": {}}))
def within(n, flags, d):
    for r in d["rules"]:
        mode = r.get("mode", "substring")
        for j, pat in enumerate(r["match"]):
            if mode == "menu" and pat == "tm":
                if not re.match(r"tm\d", n): continue
            elif not _hit(n, pat, mode): continue
            if not _when(r.get("when"), flags): break
            return r["rank"] + j * r.get("step", 0), r["id"], r.get("min_tier")
    return d.get("default_rank", 50), "default", None
TN = {0: "COMMON", 1: "GREAT", 2: "ULTRA", 3: "ROGUE", 4: "MASTER", 5: "LUXURY"}
def rank_item(r, flags, d):
    """Returns (sort_key, legacy_rank, rule_id). sort_key: lower wins. legacy_rank keeps the old scale for reroll thresholds."""
    n = norm(r["n"]); t = r.get("t") or 0; sp = d["specials"]; jt = d.get("junk_threshold", 93)
    tr = d["tier_order"].get(TN.get(t, ""), t)
    s = None
    if "master ball" in n and sp.get("master_ball") is not None: s = ("master_ball", sp["master_ball"])  # Gavin t138u: Master Ball #1
    elif "mega bracelet" in n and sp.get("mega_bracelet") is not None: s = ("mega_bracelet", sp["mega_bracelet"])  # MEGA t195u
    elif "eelektrossite" in n and flags.get("eelektross_in_party") and sp.get("eelektrossite") is not None: s = ("eelektrossite", sp["eelektrossite"])  # MEGA t199u
    elif "dna splicers" in n and flags.get("dna_pair"): s = ("dna_pair", sp["dna_pair"])
    elif ("rusted sword" in n or "ancient sword" in n) and flags.get("zacian_in_party"): s = ("sword", sp["sword"])
    elif "prism scale" in n and flags.get("secondary_is_feebas"): s = ("prism_scale", sp["prism_scale"])
    elif flags.get("role_dead") and ("revive" in n or "sacred ash" in n): s = ("role_revive", sp["role_revive"])
    elif flags.get("emergency") and any(k in n for k in ("full restore", "max potion", "hyper potion", "sitrus berry", "super potion", "potion")): s = ("emergency_heal", sp["emergency_heal"])
    if s: return (0, s[1], 0), s[1], s[0]
    v, rid, mt = within(n, flags, d)
    if mt: tr = max(tr, d["tier_order"].get(mt, tr))
    if v >= jt: return (2, v, -tr), v, rid
    br = ((-200 if tr >= 4 else -100) + min(v, 99) / 1000) if tr >= 3 else v
    return (1, -tr, v), br, rid
