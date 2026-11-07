# Project layout and safe cleanup

- Root: stable entry points, shared JSON, README, CHANGELOG, SHINY_LOG and handoff record. These paths are deliberately unchanged.
- scripts/: current farm snapshot, launcher, CDP/run helpers. helpers/ remains in place.
- profiles/: live farm reads this directory; never relocate without updating the live configuration.
- control-app/, encounter_editor/, priority_editor/, data/: preserved in place to avoid breaking launchers and relative imports.
- docs/: project organization notes.
- archive/legacy-farm/: historical farm versions 9 through 16, preserved with git mv.
- archive/one-off/: completed wave-specific Skwovet tools and wave-184 note. Historical scripts are reference material, not supported launch points.
- box-extras/: retained as-is; contents may differ from current source.

Cleanup deleted only tracked historical text outputs under scripts/logs/. They remain recoverable from initial commit d6f1d1d7913c787a1580cbbe6689ed4fa5362a8a.
Ignored backups, screenshots, research dependencies and other untracked files were NOT deleted: they were not committed first and may contain unique data. They remain physically in their original folders.

Runtime paths kept unchanged:
- %TEMP%/prfarm/ (including pr_farm17.py, _re2.py and hidden launcher)
- C:/Users/gavin/agent-tools/ (control app, configuration, logs/status, stop flag/reason and screenshots)
- C:/Users/gavin/..PROJECT/pokerogue/profiles/
- C:/Users/gavin/..PROJECT/pokerogue/CHANGELOG.md
- C:/Users/gavin/..PROJECT/PROJECT CHIE/OTHER/POKEROGUE/Shiny Log.md

The two pr_farm17.py snapshots and two eternatus.json profiles differ, so neither was deduplicated. Root eelektross.json matches profiles/eelektross.json, but both stable paths are retained conservatively.
No runtime process, browser, port, scheduled routine, or live game state was changed. No push was requested for this cleanup.
