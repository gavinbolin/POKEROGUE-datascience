import json, os, subprocess, time, datetime, tkinter as tk
from tkinter import messagebox
from pathlib import Path
OUT = Path(r"C:\Users\gavin\agent-tools")
FARM = Path(os.environ["TEMP"]) / "prfarm"
SCRIPT = "pr_farm17.py"
PY = r"C:\Users\gavin\AppData\Local\Programs\Python\Python310\python.exe"
STOP = OUT / "pokerogue_farm_stop.flag"; STATUS = OUT / "pokerogue_farm_status.json"
LOG = OUT / "pokerogue_farm_log.txt"; REASON = OUT / "pokerogue_farm_stop_reason.txt"
NOWIN = 0x08000000
CFGF = OUT / "pokerogue_farm_config.json"
CFG_DEF = {"secondary_field": "auto", "candy_target": "secondary"}
def cfg_load():
    d = dict(CFG_DEF)
    try: d.update({k: v for k, v in json.loads(CFGF.read_text(encoding="utf-8")).items() if k in CFG_DEF})
    except Exception: pass
    return d

def farm_pids():
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command",
            "Get-CimInstance Win32_Process -Filter \"name like 'python%'\" | ? {$_.CommandLine -like '*pr_farm*'} | % {$_.ProcessId}"],
            capture_output=True, text=True, creationflags=NOWIN, timeout=15)
        return [int(x) for x in r.stdout.split() if x.strip().isdigit()]
    except Exception:
        return []

def read_status():
    try: return json.loads(STATUS.read_text(encoding="utf-8"))
    except Exception: return {}

def read_reason():
    try: return REASON.read_text(encoding="utf-8").strip()
    except Exception: return ""

def tail(n=8):
    try:
        with open(LOG, "rb") as f:
            f.seek(0, 2); f.seek(max(0, f.tell() - 6000))
            return "\n".join(f.read().decode("utf-8", "replace").splitlines()[-n:])
    except Exception as e: return f"(no log: {e})"

class App:
    def __init__(s, root):
        s.root = root; root.title("PokéRogue Farm"); root.geometry("760x540")
        s.big = tk.Label(root, text="...", font=("Segoe UI", 28, "bold"), fg="white", bg="gray", height=1)
        s.big.pack(fill="x", padx=8, pady=8)
        s.info = tk.Label(root, text="", font=("Segoe UI", 12), justify="left", anchor="w"); s.info.pack(fill="x", padx=10)
        s.alert = tk.Label(root, text="", font=("Segoe UI", 14, "bold"), fg="#b000b0"); s.alert.pack(fill="x", padx=10)
        c = cfg_load(); s.v_sf = tk.StringVar(value="bench"); s.v_ct = tk.StringVar(value=c["candy_target"])
        for lbl, var, opts in (("Secondary in singles:", s.v_sf, ("bench",)), ("Candy target:", s.v_ct, ("primary", "both", "secondary"))):
            r = tk.Frame(root); r.pack(pady=2)
            tk.Label(r, text=lbl, width=18, anchor="e", font=("Segoe UI", 11, "bold")).pack(side="left")
            for o in opts:
                tk.Radiobutton(r, text=("Bench (locked)" if o == "bench" else o.capitalize()), value=o, variable=var, indicatoron=0, width=(14 if o == "bench" else 10), font=("Segoe UI", 11),
                               selectcolor="#90caf9", command=s.save_cfg).pack(side="left", padx=2)
        b = tk.Frame(root); b.pack(pady=6)
        tk.Button(b, text="START", width=14, font=("Segoe UI", 13, "bold"), bg="#2e7d32", fg="white", command=s.start).pack(side="left", padx=10)
        tk.Button(b, text="STOP", width=14, font=("Segoe UI", 13, "bold"), bg="#c62828", fg="white", command=s.stop).pack(side="left", padx=10)
        s.log = tk.Text(root, height=10, font=("Consolas", 9), wrap="none"); s.log.pack(fill="both", expand=True, padx=8, pady=8)
        s.pids = []; s.refresh()

    def save_cfg(s):
        try:
            try: d = json.loads(CFGF.read_text(encoding="utf-8-sig"))
            except Exception: d = {}
            d.update({"secondary_field": "bench", "candy_target": s.v_ct.get()})  # merge: keep primary etc.
            CFGF.write_text(json.dumps(d), encoding="utf-8")
        except Exception: pass

    def refresh(s):
        s.pids = farm_pids(); st = read_status(); z = st.get("zacian") or {}
        if s.pids: s.big.config(text=f"RUNNING  (pid {', '.join(map(str, s.pids))})", bg="#2e7d32")
        else: s.big.config(text="STOPPED", bg="#c62828")
        party = st.get("party") or []
        try: _cfg = json.loads(CFGF.read_text(encoding="utf-8"))
        except Exception: _cfg = {}
        _pid = _cfg.get("primary") or z.get("sp")
        pm = next((p for p in party if p.get("sp") == _pid), None) or z or (party[0] if party else {})
        _sid = _cfg.get("secondary")
        sm = next((p for p in party if _sid and p.get("sp") == _sid), None) or next((p for p in party if p.get("sp") in (349, 350) and p is not pm), None) or next((p for p in party if p is not pm), {})
        def _mon(m): return f"{m.get('n','?')} {m.get('hp','?')}/{m.get('mx','?')}{' FAINTED' if m and (m.get('hp') or 0) <= 0 else ''}" if m else "-"
        s.info.config(text=f"Wave: {st.get('wave','?')}    Primary: {_mon(pm)}    Secondary: {_mon(sm)}\n"
                           f"Last update: {st.get('ts','?')}    Stop flag: {'yes' if STOP.exists() else 'no'}")
        sr = st.get("stopped_reason") or ""
        if sr == "shiny_enemy": s.alert.config(text=f"SHINY ENEMY: {st.get('shiny_species','?')} wave {st.get('wave','?')}", fg="#b000b0")
        elif not s.pids and read_reason(): s.alert.config(text="Stop reason: " + read_reason()[:90], fg="#c62828")
        elif sr: s.alert.config(text="Stop reason: " + sr, fg="#c62828")
        else: s.alert.config(text="")
        s.log.delete("1.0", "end"); s.log.insert("end", tail())
        s.root.after(3000, s.refresh)

    def stop(s):
        STOP.touch()
        REASON.write_text(f"user_stop {datetime.datetime.now().isoformat(timespec='seconds')}", encoding="utf-8")
        for _ in range(16):
            if not farm_pids(): break
            time.sleep(0.5)
        for p in farm_pids():
            subprocess.run(["taskkill", "/PID", str(p), "/T", "/F"], creationflags=NOWIN, capture_output=True)

    def start(s):
        if farm_pids(): return
        st = read_status()
        STOP.unlink(missing_ok=True); REASON.unlink(missing_ok=True)
        env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
        out = open(OUT / "pokerogue_farm_stdout.txt", "ab")
        subprocess.Popen([PY, "-u", SCRIPT], cwd=str(FARM), env=env, stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                         creationflags=0x00000008 | 0x00000200 | NOWIN, close_fds=True)

root = tk.Tk(); App(root); root.mainloop()
