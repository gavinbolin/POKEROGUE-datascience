"""Launch the item priority editor (no console). If it's already running, just open the browser."""
import sys, os, subprocess, webbrowser, urllib.request, pathlib, time
HERE = pathlib.Path(__file__).resolve().parent
URL = "http://127.0.0.1:8765/"
try:
    urllib.request.urlopen(URL + "api/ping", timeout=1); webbrowser.open(URL); sys.exit(0)
except Exception: pass
exe = sys.executable  # pythonw.exe when launched by double-click
log = open(HERE / "server.log", "a", encoding="utf-8")
subprocess.Popen([exe, str(HERE / "server.py"), "--no-browser"], cwd=str(HERE), stdout=log, stderr=log,
                 creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "DETACHED_PROCESS", 0))
for _ in range(50):
    try: urllib.request.urlopen(URL + "api/ping", timeout=0.5); break
    except Exception: time.sleep(0.2)
webbrowser.open(URL)
