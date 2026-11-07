"""Launch the encounter rules editor (no console). If it is already running, just open the browser."""
import pathlib
import subprocess
import sys
import time
import urllib.request
import webbrowser

HERE = pathlib.Path(__file__).resolve().parent
URL = "http://127.0.0.1:8766/"
try:
    urllib.request.urlopen(URL + "api/ping", timeout=1)
    webbrowser.open(URL)
    sys.exit(0)
except Exception:
    pass
exe = sys.executable
log = open(HERE / "server.log", "a", encoding="utf-8")
subprocess.Popen(
    [exe, str(HERE / "server.py"), "--no-browser"],
    cwd=str(HERE),
    stdout=log,
    stderr=log,
    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "DETACHED_PROCESS", 0),
)
for _ in range(50):
    try:
        urllib.request.urlopen(URL + "api/ping", timeout=0.5)
        break
    except Exception:
        time.sleep(0.2)
webbrowser.open(URL)
