from pathlib import Path
p = Path(r"C:\Users\gavin\AppData\Local\Temp\prfarm\pr_farm13.py")
t = p.read_text(encoding="utf-8")
old = '''def pick_move(moves, def_types, doubles_like):
            """Return index of best move. Skip 0-eff and EQ in doubles."""
            scored = []
            for i, name in enumerate(moves or []):
                clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                at = MOVE_TYPE.get(clean)
                eff = effectiveness(at, def_types) if at else 1.0
                if clean == "Earthquake" and doubles_like:
                    log(f"skip EQ in doubles idx={i}")
                    continue
                if eff <= 0:
                    log(f"skip {clean} eff=0 vs {def_types}")
                    continue
                scored.append((eff, i, clean, at))
            if not scored:
                # fallback: first non-EQ if doubles else first
                for i, name in enumerate(moves or []):
                    clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                    if doubles_like and clean == "Earthquake":
                        continue
                    return i, clean, 1.0, MOVE_TYPE.get(clean)
                return 0, (moves or ["?"])[0], 1.0, None
            scored.sort(key=lambda x: (-x[0], x[1]))
            # Prefer SE (>1), else highest, else neutral
            best = scored[0]
            return best[1], best[2], best[0], best[3]'''
new = '''def pick_move(moves, def_types, doubles_like, stab_types=None):
            """Return index of best move. Skip 0-eff and EQ in doubles.
            When foe types unknown, prefer STAB (Fairy) and avoid EQ default."""
            stab_types = stab_types or ["Fairy"]
            scored = []
            for i, name in enumerate(moves or []):
                clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                at = MOVE_TYPE.get(clean)
                if clean == "Earthquake" and doubles_like:
                    log(f"skip EQ in doubles idx={i}")
                    continue
                if def_types:
                    eff = effectiveness(at, def_types) if at else 1.0
                    if eff <= 0:
                        log(f"skip {clean} eff=0 vs {def_types}")
                        continue
                    # STAB bonus for tie-break
                    stab = 1.1 if at in stab_types else 1.0
                    scored.append((eff * stab, eff, i, clean, at))
                else:
                    # Unknown foe: never default to EQ; prefer STAB Fairy, then non-Ground
                    if clean == "Earthquake":
                        score = 0.2
                    elif at in stab_types:
                        score = 1.5
                    elif at in ("Rock", "Fire", "Fighting", "Steel"):
                        score = 1.1
                    else:
                        score = 1.0
                    scored.append((score, 1.0, i, clean, at))
            if not scored:
                for i, name in enumerate(moves or []):
                    clean = re.sub(r"\s*\(N\)\s*$", "", name or "").strip()
                    if clean == "Earthquake":
                        continue
                    return i, clean, 1.0, MOVE_TYPE.get(clean)
                return 0, (moves or ["?"])[0], 1.0, None
            scored.sort(key=lambda x: (-x[0], x[2]))
            best = scored[0]
            return best[2], best[3], best[1], best[4]'''
if old not in t:
    raise SystemExit('pick_move block missing')
t = t.replace(old, new, 1)
t = t.replace(
    'idx, name, eff, at = pick_move(moves, def_types, doubles_like)',
    'idx, name, eff, at = pick_move(moves, def_types, doubles_like, stab_types=list(zmon.get("types") or ["Fairy"]))',
)
# Also improve type OCR: look for TYPE/ icons near enemy — broaden parse
p.write_text(t, encoding='utf-8')
print('pick_move patched')
