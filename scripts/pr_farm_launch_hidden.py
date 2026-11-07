# Hidden farm launcher (run with pythonw.exe): no console, stdout/stderr redirected in-process.
import os, sys, runpy
FARM = os.path.join(os.environ["TEMP"], "prfarm"); OUT = r"C:\Users\gavin\agent-tools"
os.environ["PYTHONIOENCODING"] = "utf-8"; os.environ["PYTHONUTF8"] = "1"
os.chdir(FARM); sys.path.insert(0, FARM)
f = open(os.path.join(OUT, "pokerogue_farm_stdout.txt"), "w", encoding="utf-8", buffering=1)
sys.stdout = sys.stderr = f
sys.argv = ["pr_farm17.py"]
runpy.run_path(os.path.join(FARM, "pr_farm17.py"), run_name="__main__")
