"""Regenerate ITEM_PRIORITY.md from item_priority.json (the source of truth). Usage: python gen_item_priority_md.py [json] [md]"""
import json, sys, pathlib, re
H = pathlib.Path(__file__).parent
J = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else H / "item_priority.json"
M = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else H / "ITEM_PRIORITY.md"
d = json.loads(J.read_text(encoding="utf-8"))
old = M.read_text(encoding="utf-8") if M.exists() else ""
keep = ""
for sec in ("## Shop", "## Always / never rules"):
    m = re.search(re.escape(sec) + r".*?(?=\n## |\Z)", old, re.S)
    if m: keep += m.group(0).rstrip() + "\n\n"
o = ["# PokéRogue Classic farm: item priority list", "",
     f"> **Edits go in `{J.name}`** (same folder), not here. This page is generated from it by `gen_item_priority_md.py`. The farm reads the JSON at start and reloads it automatically when the file changes.", "",
     "## How ranking works",
     "1. **Specials** beat everything: " + ", ".join(f"{k} ({v})" for k, v in sorted(d["specials"].items(), key=lambda x: x[1])) + ".",
     "   " + "; ".join(f"*{k}*: {v}" for k, v in d.get("special_notes", {}).items()),
     f"2. **Junk** (rank ≥ {d['junk_threshold']}) always loses to any real item, whatever its tier; if the best card is junk the farm rerolls.",
     "3. Otherwise the **higher tier wins**: MASTER > ROGUE > ULTRA > GREAT > COMMON (tier read from the card). `min_tier` lifts an item to at least that tier.",
     "4. Inside a tier, the **lower rank wins**. Rules are checked top-down; the first rule whose pattern matches and whose condition is true sets the rank. No match = default " + str(d["default_rank"]) + ".",
     "5. Shop-buyable items are ordinary Common/Great cards, so they can never beat a rarer real item.", "",
     "Conditions use flags: " + ", ".join(f"`{f}`" for f in d["flags"]) + ". `step` adds step×(position of the matched pattern), e.g. best heal/ball first.", "",
     "## Rules (checked in this order)", "| # | id | Matches | Mode | Condition | Rank | Min tier | Shop? | Notes |", "|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(d["rules"], 1):
    rk = f"{r['rank']}" + (f" (+{r['step']}/pattern)" if r.get("step") else "") + (" **junk**" if r["rank"] >= d["junk_threshold"] else "")
    o.append(f"| {i} | {r['id']} | {', '.join(r['match'])} | {r.get('mode','substring')} | {r.get('when') or 'always'} | {rk} | {r.get('min_tier') or ''} | {'yes' if r.get('shop_buyable') else ''} | {r.get('notes','')} |")
o += ["", "Flame Orb / Toxic Orb are removed before ranking (banned, never bought).", "", keep.rstrip(), ""]
M.write_text("\n".join(o), encoding="utf-8"); print("wrote", M)
