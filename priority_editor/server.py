"""PokeRogue farm item priority editor - local server (stdlib only, 127.0.0.1).
Usage: python server.py [--json PATH] [--port 8765] [--no-browser]
Only rank, min_tier and specials values are changed by saves; everything else in the JSON
(rule order, patterns, conditions, notes) is preserved exactly. Rule order matters: prio.py is first-match-wins."""
import json, sys, os, re, math, time, shutil, argparse, threading, subprocess, webbrowser, importlib.util, pathlib, tempfile
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

HERE = pathlib.Path(__file__).resolve().parent
PROJ = HERE.parent
LIVE_JSON = PROJ / "item_priority.json"
ap = argparse.ArgumentParser()
ap.add_argument("--json", default=str(LIVE_JSON))
ap.add_argument("--port", type=int, default=8765)
ap.add_argument("--no-browser", action="store_true")
A = ap.parse_args()
JSON = pathlib.Path(A.json).resolve()
IS_LIVE = JSON == LIVE_JSON.resolve()
BACKUPS = (PROJ / "item_priority_backups") if IS_LIVE else (JSON.parent / (JSON.stem + "_backups"))
MD = (PROJ / "ITEM_PRIORITY.md") if IS_LIVE else JSON.with_suffix(".md")
GEN = PROJ / "gen_item_priority_md.py"
PY = sys.executable.replace("pythonw.exe", "python.exe")
LOCK = threading.Lock()

def _load_prio():
    for p in (pathlib.Path(os.environ.get("TEMP", "")) / "prfarm" / "prio.py", HERE / "prio_copy.py"):
        if p.exists():
            spec = importlib.util.spec_from_file_location("prio_ed", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m, str(p)
    return None, None
PRIO, PRIO_SRC = _load_prio()

SPRITES = {  # rule/special id -> sprite file (game item icon key from modifier-type.ts / items atlas)
 "tera_shard": "normal_tera_shard", "eviolite": "eviolite", "soothe_bell": "soothe_bell", "rarer_candy": "rarer_candy",
 "candy": "candy_jar", "voucher": "coupon", "zacian_revive": "revive", "role_heal": "full_restore", "heal_need": "hyper_potion",
 "vitamins": "hp_up", "leppa_pp_short": "leppa_berry", "leppa": "leppa_berry", "pp_crit": "max_elixir", "pp_low": "elixir",
 "pp_fine": "ether", "menu_items": "tm_normal", "ball_out": "mb", "ball_good": "rb", "ball_junk": "pb", "lure_active": "lure",
 "lure_secondary": "super_lure", "lure": "lure", "x_special": "x_sp_atk", "x_items": "x_attack", "revive_unneeded": "revive",
 "potion_unneeded": "potion", "pri_max_revive": "max_revive", "pri_leftovers": "leftovers", "pri_shell_bell": "shell_bell",
 "pri_kings_rock": "kings_rock", "pri_scope_lens": "scope_lens", "pri_quick_claw": "quick_claw", "pri_focus_band": "focus_band",
 "pri_lucky_egg": "lucky_egg", "pri_exp_all": "exp_share", "pri_exp_share": "exp_share", "pri_golden": "golden_punch",
 "pri_silk_scarf": "silk_scarf", "pri_fairy_feather": "fairy_feather", "pri_metal_coat": "metal_coat", "pri_berry": "sitrus_berry",
 "pri_full_restore": "full_restore", "pri_max_potion": "max_potion", "pri_revive": "revive", "pri_hyper_potion": "hyper_potion",
 "pri_super_potion": "super_potion", "pri_nugget": "nugget", "pri_potion": "potion",
 "role_revive": "max_revive", "sword": "rusted_sword", "prism_scale": "prism_scale", "dna_pair": "dna_splicers", "emergency_heal": "full_restore",
}
# keyword fallback for rules added later
KW = [("ball", "pb"), ("berry", "sitrus_berry"), ("potion", "potion"), ("revive", "revive"), ("candy", "rare_candy"), ("lure", "lure"), ("tm", "tm_normal")]

def sprite_for(rid, match=()):
    s = SPRITES.get(rid)
    if not s:
        for m in match:
            k = re.sub(r"[^a-z0-9]+", "_", m.lower()).strip("_")
            if (HERE / "sprites" / f"{k}.png").exists(): s = k; break
        else:
            s = next((v for kw, v in KW if any(kw in m for m in match)), None)
    if s and (HERE / "sprites" / f"{s}.png").exists(): return s, True
    return "unknown", False

def read():
    return json.loads(JSON.read_text(encoding="utf-8")), JSON.stat().st_mtime

def dump(d):
    return json.dumps(d, indent=1, ensure_ascii=False)  # same layout as the hand-written file (no trailing newline)

def num(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x): raise ValueError(f"not a finite number: {x!r}")
    x = round(float(x), 4)
    return int(x) if x == int(x) else x

SAMPLES = [  # (screen, flags) smoke screens to make sure prio.rank_item works on the new data
 ([{"n": "Master Ball", "t": 4}, {"n": "Sitrus Berry", "t": 0}, {"n": "Full Heal", "t": 0}], {"holding_balls": True}),
 ([{"n": "DNA Splicers", "t": 3}, {"n": "Super Lure", "t": 0}], {"lure_active": True}),
 ([{"n": "Rare Candy", "t": 0}, {"n": "Leftovers", "t": 2}, {"n": "Potion", "t": 0}], {"heal_need": True}),
 ([{"n": "X Attack", "t": 1}, {"n": "Ultra Ball", "t": 2}, {"n": "Lure", "t": 0}], {"holding_balls": True, "secondary_in_party": True}),
]

def validate(d):
    assert d.get("version") is not None and isinstance(d.get("rules"), list) and d["rules"], "rules missing"
    ids = [r.get("id") for r in d["rules"]]
    assert len(ids) == len(set(ids)) and all(ids), "rule ids must be unique and non-empty"
    tiers = d["tier_order"]
    for r in d["rules"]:
        assert r["match"] and all(isinstance(m, str) for m in r["match"]), f"{r['id']}: bad match"
        num(r["rank"])
        if r.get("min_tier") is not None: assert r["min_tier"] in tiers, f"{r['id']}: unknown min_tier {r['min_tier']}"
    for k, v in d["specials"].items(): num(v)
    num(d.get("junk_threshold", 93))
    if PRIO:
        PRIO._valid(d)
        for screen, flags in SAMPLES:
            for it in screen: PRIO.rank_item(it, flags, d)
    return True

def apply_edit(base, edit):
    """edit = {ranks:{id:rank}, min_tier:{id:TIER|null}, specials:{k:v}} - only these fields change."""
    d = json.loads(json.dumps(base))
    byid = {r["id"]: r for r in d["rules"]}
    for rid, v in (edit.get("ranks") or {}).items():
        if rid not in byid: raise ValueError(f"unknown rule {rid}")
        nv = num(v)
        if nv != byid[rid]["rank"]: byid[rid]["rank"] = nv
    for rid, v in (edit.get("min_tier") or {}).items():
        if rid not in byid: raise ValueError(f"unknown rule {rid}")
        r = byid[rid]
        if v in (None, "", "none"):
            r.pop("min_tier", None)
        elif r.get("min_tier") != v:
            if "min_tier" in r: r["min_tier"] = v
            else:  # insert right after rank to keep the file's field layout
                items = list(r.items()); i = [k for k, _ in items].index("rank") + 1
                items.insert(i, ("min_tier", v)); r.clear(); r.update(items)
    for k, v in (edit.get("specials") or {}).items():
        if k not in d["specials"]: raise ValueError(f"unknown special {k}")
        nv = num(v)
        if nv != d["specials"][k]: d["specials"][k] = nv
    return d

def write_atomic(d, reason):
    text = dump(d)
    validate(json.loads(text))
    BACKUPS.mkdir(parents=True, exist_ok=True)
    bk = None
    if JSON.exists():
        bk = BACKUPS / f"item_priority_{time.strftime('%Y%m%d_%H%M%S')}_{reason}.json"
        shutil.copy2(JSON, bk)
    fd, tmp = tempfile.mkstemp(prefix=".item_priority_", suffix=".tmp", dir=str(JSON.parent))
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f: f.write(text); f.flush(); os.fsync(f.fileno())
    for i in range(10):
        try: os.replace(tmp, JSON); break
        except PermissionError: time.sleep(0.1)
    else:
        os.unlink(tmp); raise RuntimeError("could not replace JSON (file locked)")
    md = "skipped"
    if GEN.exists():
        r = subprocess.run([PY, str(GEN), str(JSON), str(MD)], capture_output=True, text=True, timeout=60,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        md = "ok" if r.returncode == 0 else ("failed: " + (r.stderr or r.stdout)[-300:])
    return {"backup": bk.name if bk else None, "md": md}

def payload():
    d, mt = read()
    sp = {}
    for r in d["rules"]: sp[r["id"]] = sprite_for(r["id"], r["match"])
    for k in d["specials"]: sp["special:" + k] = sprite_for(k)
    return {"data": d, "mtime": mt, "path": str(JSON), "live": IS_LIVE, "prio": PRIO_SRC, "md_path": str(MD),
            "sprites": {k: v[0] for k, v in sp.items()}, "sprite_real": sum(1 for v in sp.values() if v[1]), "sprite_total": len(sp)}

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, code, body, ctype="application/json"):
        if not isinstance(body, (bytes, bytearray)): body = json.dumps(body).encode()
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        p = self.path.split("?")[0]
        try:
            if p in ("/", "/index.html"): return self._send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
            if p.startswith("/sprites/"):
                f = (HERE / "sprites" / pathlib.Path(p[9:]).name)
                if f.suffix == ".png" and f.exists(): return self._send(200, f.read_bytes(), "image/png")
                return self._send(404, {"error": "no sprite"})
            if p == "/api/data": return self._send(200, payload())
            if p == "/api/backups":
                BACKUPS.mkdir(parents=True, exist_ok=True)
                return self._send(200, {"backups": sorted((f.name for f in BACKUPS.glob("*.json")), reverse=True)[:100]})
            if p == "/api/ping": return self._send(200, {"ok": True, "json": str(JSON)})
            self._send(404, {"error": "not found"})
        except Exception as e: self._send(500, {"error": repr(e)})
    def do_POST(self):
        p = self.path.split("?")[0]
        if self.headers.get("Origin") not in (None, f"http://127.0.0.1:{A.port}", f"http://localhost:{A.port}"):
            return self._send(403, {"error": "bad origin"})
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            with LOCK:
                base, mt = read()
                if p == "/api/save":
                    if body.get("base_mtime") is not None and abs(body["base_mtime"] - mt) > 1e-6:
                        return self._send(409, {"error": "item_priority.json changed on disk since you loaded it. Reset to file and redo your edits."})
                    new = apply_edit(base, body)
                    validate(new)
                    if new == base: return self._send(200, {"ok": True, "unchanged": True, **payload()})
                    res = write_atomic(new, "presave")
                    return self._send(200, {"ok": True, **res, **payload()})
                if p == "/api/revert":
                    name = pathlib.Path(body.get("name", "")).name
                    f = BACKUPS / name
                    if not f.exists(): return self._send(404, {"error": "backup not found"})
                    d = json.loads(f.read_text(encoding="utf-8")); validate(d)
                    res = write_atomic(d, "prerevert")
                    return self._send(200, {"ok": True, "reverted_to": name, **res, **payload()})
                if p == "/api/quit":
                    threading.Timer(0.3, lambda: os._exit(0)).start(); return self._send(200, {"ok": True})
                if p == "/api/validate":
                    validate(apply_edit(base, body)); return self._send(200, {"ok": True})
            self._send(404, {"error": "not found"})
        except (AssertionError, ValueError, KeyError, TypeError) as e: self._send(400, {"error": f"validation failed: {e!r}"})
        except Exception as e: self._send(500, {"error": repr(e)})

if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", A.port), H)
    url = f"http://127.0.0.1:{A.port}/"
    print("Priority editor on", url, "editing", JSON, flush=True)
    if not A.no_browser: threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    srv.serve_forever()
