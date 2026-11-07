# PokéRogue candy farm: project home

This folder is the organized archive and home copy. **The farm does not run from here.** The live files are still in:
- Scripts: `%TEMP%\prfarm\` (live `pr_farm17.py`, `pr_farm_launch_hidden.py`, `newrun.py`, `gx.py`, ...)
- Control app: `C:\Users\gavin\agent-tools\PokeFarmControl\PokeFarmControl.pyw`
- Config: `C:\Users\gavin\agent-tools\pokerogue_farm_config.json`
- Log: `C:\Users\gavin\agent-tools\pokerogue_farm_log.txt`
- Status: `C:\Users\gavin\agent-tools\pokerogue_farm_status.json`
- Stop flag: `C:\Users\gavin\agent-tools\pokerogue_farm_stop.flag` (reason in `pokerogue_farm_stop_reason.txt`)
- Hard waves: `C:\Users\gavin\agent-tools\pokerogue_significant_waves.json`

## What's here
| Path | Contents |
|---|---|
| ~~`SHINY_LOG.md`~~ | **Moved 2026-10-29.** The shiny log now lives at `C:\Users\gavin\..PROJECT\PROJECT CHIE\OTHER\POKEROGUE\PokeRogue Shiny Log.md` (CHIE vault). Egg/shiny odds note is beside it. |
| `CHANGELOG.md` | Full history of farm changes and watch runs (newest copy, from Grok Bot's box) |
| `scripts\` | Current `pr_farm17.py`, older `pr_farmN.py` versions, the hidden launcher, newrun.py, gx.py, CDP helpers, state.js |
| `scripts\backups\` | Every `pr_farm17.bak_*` patch backup and other .bak files |
| `scripts\helpers\` | One-off probe, fix, and unstick scripts and JS snippets |
| `scripts\logs\` | Small old stdout/run logs (the live log isn't copied) |
| `control-app\` | Copy of PokeFarmControl (Start/Stop app) plus its backups |
| `data\` | Config, significant-waves, a status.json snapshot, and `shiny_screenshots\` |
| `box-extras\` | Files that existed only on Grok Bot's box: base.py, patch scripts, control_app backups |

Snapshot taken 2026-10-29 ~10:50 PM MDT. To refresh it, copy from the live paths again. Don't edit here and expect the farm to pick the change up.
