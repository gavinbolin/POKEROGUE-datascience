# Wiring encounter rules into the farm

Copy this folder to `encounter_editor` next to `item_priority.json`. The live rules file is:

`C:\Users\gavin\..PROJECT\pokerogue\encounter_rules.json`

On Windows the editor and `EncounterRules()` open that path. `--json` or the env var `ENCOUNTER_RULES_JSON` overrides it. On other systems the default is the sibling `encounter_rules.json`, which is the same place once this folder sits in `encounter_editor`.

The editor writes that file only. It does not write the simulator's pinned copy. Double-click `Encounter Editor.pyw` (no console window). The page is `http://127.0.0.1:8766/`. Saving copies the previous file into `encounter_rules_backups`, replaces the JSON atomically, and regenerates `ENCOUNTER_RULES.md` beside the JSON. The loader below re-reads the file when its mtime changes.

`encounter_rules.py` uses the Python standard library only. If the file is missing or invalid, `choose` uses the old hardcoded picks (pricey-or-leave, training leave, party-change leave, otherwise the top option).

## Call from MysteryEncounterUiHandler

Replace the block that sets `pick` (shady dealer, training session, block list, top option) with:

```python
import sys
from pathlib import Path
# encounter_editor sits next to the farm script's pokerogue folder
sys.path.insert(0, str(Path(__file__).resolve().parent / "encounter_editor"))
from encounter_rules import EncounterRules

RULES = EncounterRules()  # defaults to ../encounter_rules.json, reloads on mtime

# inside the MysteryEncounterUiHandler branch, after mekey / meets / labels exist:
decision = RULES.choose(
    mekey,                  # localization key, e.g. "shadyVitaminDealer"
    meets,                  # list of bools, one per option, from meetsRequirements()
    state={
        "money_fraction": money / money_cap if money_cap else None,
        "party_has_free_slot": len(party) < 6,
        "primary_hp_fraction": lead_hp / lead_max if lead_max else None,
    },
    option_labels=labels,   # used only by the hardcoded fallback
)
pick = decision.index
log(f"mystery encounter {mekey}: {decision.reason} -> {pick} follow={decision.follow_ups}")
await set_cursor(pick)
await Z()
```

`decision.follow_ups` is a dict of slot id to the selected key, only for slots that apply to the option that was picked. For a Pokémon slot the value is `lowest_index_alive`, `lead`, `secondary`, or `lowest_hp`. Resolve it when the party screen opens:

```python
from encounter_rules import party_slot
index = party_slot(decision.follow_ups.get("pokemon", "lowest_index_alive"), [
    {"index": i, "fainted": mon["fainted"], "hp_fraction": mon["hp"] / mon["max"]}
    for i, mon in enumerate(party)
])
```

`choice` and `fallback` in the JSON are option keys (`option_2`) or 0-based indexes. `leave: true` ignores `choice` and takes the last option whose requirements are met.

Do not point this loader at `simulator/rules/encounter_rules.v1.json`. That file is a one-time snapshot for dataset runs. A later edit reaches a dataset only when someone copies the live file over the pin on purpose and stamps the new hash.
