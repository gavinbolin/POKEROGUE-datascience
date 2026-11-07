import shutil, re, urllib.request
from pathlib import Path
from datetime import datetime
when = datetime.now().strftime("%Y-%m-%d %H:%M")
method = "Caught"
variant = 1
ball = "Rogue Ball"
d = Path(r"C:\Users\gavin\..PROJECT\PROJECT CHIE\OTHER\POKEROGUE")
L = d / "Shiny Log.md"
sp = d / "sprites" / "pr_947s.png"
print("sprite", sp.exists(), sp.stat().st_size if sp.exists() else 0)
raw = L.read_bytes()
bom = raw.startswith(b"\xef\xbb\xbf")
t = raw.decode("utf-8-sig")
bak = str(L) + ".bak_brambleghast_w78"
if not Path(bak).exists():
    shutil.copy2(L, bak)
lines = t.split("\n")
row = f"| {when} | ![[pr_947s.png\\|40]] | Brambleghast | 53 | {variant} | {method} | 78 | {ball} |"
if any("Brambleghast" in l and "| 78 |" in l and "2026-11-06" in l for l in lines):
    print("SKIP already exists")
else:
    i = next(k for k, l in enumerate(lines) if re.match(r"^\|\s*-", l))
    lines.insert(i + 1, row)
    t = "\n".join(lines)
    t = re.sub(r"(?m)^updated:.*$", "updated: 2026-11-06", t, count=1)
    L.write_bytes((b"\xef\xbb\xbf" if bom else b"") + t.encode("utf-8"))
    print("inserted", lines[i + 1])
shutil.copy2(L, Path(r"C:\Users\gavin\AppData\Local\Temp\prfarm\SHINY_LOG.md"))
print("when", when)
