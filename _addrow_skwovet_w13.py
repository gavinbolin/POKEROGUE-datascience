import shutil, re, urllib.request
from pathlib import Path
d = Path(r"C:\Users\gavin\..PROJECT\PROJECT CHIE\OTHER\POKEROGUE")
L = d / "Shiny Log.md"
sp = d / "sprites" / "pr_819s.png"
sp.parent.mkdir(parents=True, exist_ok=True)
url = "https://raw.githubusercontent.com/pagefaultgames/pokerogue-assets/beta/images/pokemon/icons/8/819s.png"
if not sp.exists():
    urllib.request.urlretrieve(url, sp)
    print("sprite dl", sp.stat().st_size)
else:
    print("sprite ok", sp.stat().st_size)
shutil.copy2(sp, Path(r"C:\Users\gavin\AppData\Local\Temp\prfarm") / "pr_819s.png")
raw = L.read_bytes()
bom = raw.startswith(b"\xef\xbb\xbf")
t = raw.decode("utf-8-sig")
bak = str(L) + ".bak_skwovet_0616"
if not Path(bak).exists():
    shutil.copy2(L, bak)
lines = t.split("\n")
row = "| 2026-11-06 06:16 | ![[pr_819s.png\\|40]] | Skwovet | 9 | 1 | Caught | 13 | Poké Ball |"
if any("Skwovet" in l and "| 13 |" in l and "2026-11-06" in l for l in lines):
    print("SKIP already exists")
else:
    i = next(k for k, l in enumerate(lines) if re.match(r"^\|\s*-", l))
    lines.insert(i + 1, row)
    t = "\n".join(lines)
    t = re.sub(r"(?m)^updated:.*$", "updated: 2026-11-06", t, count=1)
    L.write_bytes((b"\xef\xbb\xbf" if bom else b"") + t.encode("utf-8"))
    print("inserted at", i + 1, lines[i + 1])
temp = Path(r"C:\Users\gavin\AppData\Local\Temp\prfarm\SHINY_LOG.md")
shutil.copy2(L, temp)
print("synced temp SHINY_LOG.md")
