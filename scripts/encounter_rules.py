"""Farm-side encounter rules loader. Python stdlib only.

The live file sits next to item_priority.json (the parent of this folder).
A running farm hot-reloads it when the mtime changes. If the file is missing
or broken, choose() falls back to the hardcoded farm17 picks.

choice and fallback are option keys (option_N) or 0-based indexes.
This module never writes the simulator pin.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
WINDOWS_RULES = Path(r"C:\Users\gavin\..PROJECT\pokerogue\encounter_rules.json")


def default_rules_path() -> Path:
    """Env ENCOUNTER_RULES_JSON (or ENCOUNTER_RULES_PATH) wins.

    On Windows the default is the farm file beside a dropped-in encounter_editor folder.
    On other systems it is the sibling encounter_rules.json, which is that same layout.
    """
    env = os.environ.get("ENCOUNTER_RULES_JSON") or os.environ.get("ENCOUNTER_RULES_PATH")
    if env:
        return Path(env)
    if os.name == "nt":
        return WINDOWS_RULES
    return HERE.parent / "encounter_rules.json"


DEFAULT_PATH = default_rules_path()

CONDITION_TYPES = ("money_above_fraction", "party_has_free_slot", "primary_hp_above_fraction")
BALL_CAPS = ("none", "poke", "great", "ultra", "rogue", "master")
XFORM_WORDS = (
    "trade",
    "in exchange for your",
    "give up a pok",
    "take one of your",
    "transform",
    "replace your",
    "change your pok",
    "changes your pok",
    "your team will",
    "swap your",
)
BLOCK_KEYS = ("weirddream", "globaltradesystem", "darkdeal", "wondertrade", "trade")


class Decision:
    def __init__(self, index: int, reason: str, follow_ups: dict | None = None, source: str = "rules", option_key: str = ""):
        self.index = index
        self.reason = reason
        self.follow_ups = follow_ups or {}
        self.source = source
        self.option_key = option_key

    def __iter__(self):
        yield self.index
        yield self.reason

    def __repr__(self) -> str:
        return f"Decision(index={self.index}, reason={self.reason!r}, source={self.source})"


def canonical_text(doc: dict) -> str:
    return json.dumps(doc, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def content_hash(doc: dict) -> str:
    return hashlib.sha256(canonical_text(doc).encode("utf-8")).hexdigest()


def short_hash(doc: dict) -> str:
    return content_hash(doc)[:12]


def is_sim_pin(path: Path | str) -> bool:
    text = str(path).replace("\\", "/").lower()
    return "encounter_rules.v1.json" in text or "/simulator/rules" in text


def assert_not_sim_pin(path: Path | str) -> None:
    if is_sim_pin(path):
        raise ValueError(f"refusing to write the simulator pin: {path}")


def _compact(key: str) -> str:
    text = str(key or "")
    if "/" in text:
        text = text.rsplit("/", 1)[-1]
    return re.sub(r"[^a-z0-9]", "", text.lower())


def option_index(encounter: dict, ref) -> int | None:
    options = encounter.get("options") or []
    if isinstance(ref, bool):
        return None
    if isinstance(ref, int):
        return ref if 0 <= ref < len(options) else None
    if isinstance(ref, str):
        for option in options:
            if option.get("key") == ref:
                return int(option["index"])
        match = re.fullmatch(r"option_(\d+)", ref.strip())
        if match:
            index = int(match.group(1)) - 1
            if 0 <= index < len(options):
                return index
        if ref.strip().isdigit():
            index = int(ref.strip())
            if 0 <= index < len(options):
                return index
    return None


def option_key(encounter: dict, index: int) -> str:
    for option in encounter.get("options") or []:
        if int(option["index"]) == index:
            return option["key"]
    return f"option_{index + 1}"


def _meets(meets, index: int) -> bool:
    if meets is None:
        return True
    if index < 0 or index >= len(meets):
        return False
    return bool(meets[index])


def last_legal(meets, count: int) -> int:
    if count <= 0:
        return 0
    if meets is None:
        return count - 1
    for index in range(count - 1, -1, -1):
        if _meets(meets, index):
            return index
    return count - 1


def conditions_pass(conditions, state) -> tuple[bool, str]:
    if not conditions:
        return True, ""
    state = state or {}
    for condition in conditions:
        kind = condition.get("type")
        if kind == "money_above_fraction":
            if "money_fraction" not in state or state.get("money_fraction") is None:
                return False, "money_fraction missing"
            fraction = float(condition["fraction"])
            if not (float(state["money_fraction"]) > fraction):
                return False, f"money {state['money_fraction']} is not above {fraction}"
        elif kind == "party_has_free_slot":
            if "party_has_free_slot" not in state or state.get("party_has_free_slot") is None:
                return False, "party_has_free_slot missing"
            if not state["party_has_free_slot"]:
                return False, "party has no free slot"
        elif kind == "primary_hp_above_fraction":
            if "primary_hp_fraction" not in state or state.get("primary_hp_fraction") is None:
                return False, "primary_hp_fraction missing"
            fraction = float(condition["fraction"])
            if not (float(state["primary_hp_fraction"]) > fraction):
                return False, f"primary HP {state['primary_hp_fraction']} is not above {fraction}"
        else:
            return False, f"unknown condition {kind}"
    return True, ""


def follow_ups_for(encounter: dict, picked_key: str) -> dict:
    out = {}
    for slot in encounter.get("follow_ups") or []:
        if picked_key in (slot.get("applies_to") or []):
            out[slot["id"]] = slot.get("selected")
    return out


def hardcoded_choice(key: str, meets, labels=None) -> Decision:
    compact = _compact(key)
    text = " ".join(labels or []).lower()
    count = len(meets) if meets is not None else max(1, len(labels or []))
    if "shadyvitamindealer" in compact:
        if _meets(meets, 1) and count > 1:
            return Decision(1, "hardcoded shady dealer -> pricey", source="hardcoded", option_key="option_2")
        index = last_legal(meets, count)
        return Decision(index, "hardcoded shady dealer -> leave (pricey unavailable)", source="hardcoded", option_key=f"option_{index + 1}")
    if "trainingsession" in compact:
        index = last_legal(meets, count)
        return Decision(index, "hardcoded training session -> leave", source="hardcoded", option_key=f"option_{index + 1}")
    blocked = any(token in compact for token in BLOCK_KEYS) or any(token in text for token in BLOCK_KEYS) or any(
        word in text for word in XFORM_WORDS
    )
    if blocked:
        index = last_legal(meets, count)
        return Decision(index, "hardcoded party-changing encounter -> leave", source="hardcoded", option_key=f"option_{index + 1}")
    return Decision(0, "hardcoded top option", source="hardcoded", option_key="option_1")


def choose_from_encounter(encounter: dict, meets, state=None, labels=None) -> Decision:
    options = encounter.get("options") or []
    count = len(options) or (len(meets) if meets is not None else 1)
    if encounter.get("leave"):
        index = last_legal(meets, count)
        key = option_key(encounter, index) if options else f"option_{index + 1}"
        return Decision(
            index,
            "leave: take the last available option",
            follow_ups_for(encounter, key),
            option_key=key,
        )
    ok, why = conditions_pass(encounter.get("conditions") or [], state)
    choice = option_index(encounter, encounter.get("choice"))
    fallback = option_index(encounter, encounter.get("fallback"))
    if fallback is None:
        fallback = last_legal(meets, count)
    if not ok:
        index = fallback if _meets(meets, fallback) else last_legal(meets, count)
        key = option_key(encounter, index) if options else f"option_{index + 1}"
        return Decision(index, f"conditions failed ({why}); fallback", follow_ups_for(encounter, key), option_key=key)
    if choice is not None and _meets(meets, choice):
        key = option_key(encounter, choice)
        label = options[choice]["label"] if options and choice < len(options) else key
        return Decision(choice, f"choice {label}", follow_ups_for(encounter, key), option_key=key)
    index = fallback if _meets(meets, fallback) else last_legal(meets, count)
    key = option_key(encounter, index) if options else f"option_{index + 1}"
    return Decision(index, "choice unavailable; fallback", follow_ups_for(encounter, key), option_key=key)


def party_slot(selected: str, party: list[dict]) -> int:
    """party entries: {index, fainted, hp_fraction}. Returns a party index."""
    if not party:
        return 0
    alive = [mon for mon in party if not mon.get("fainted")]
    pool = alive or party

    def by_index(mon):
        return mon.get("index", 0)

    if selected == "lead":
        lead = next((mon for mon in pool if mon.get("index", 0) == 0), None)
        return (lead or pool[0]).get("index", 0)
    if selected == "secondary":
        second = next((mon for mon in pool if mon.get("index", 0) == 1), None)
        return (second or pool[0]).get("index", 0)
    if selected == "lowest_hp":
        return min(pool, key=lambda mon: (float(mon.get("hp_fraction", 1)), by_index(mon))).get("index", 0)
    return min(pool, key=by_index).get("index", 0)


class EncounterRules:
    def __init__(self, path: Path | str | None = None):
        self.path = Path(path) if path else DEFAULT_PATH
        self._mtime: float | None = None
        self.doc: dict | None = None
        self.error: str | None = None
        self.reload_if_needed(force=True)

    def reload_if_needed(self, force: bool = False) -> bool:
        path = self.path
        if not path.exists():
            self.doc = None
            self.error = "missing"
            self._mtime = None
            return True
        mtime = path.stat().st_mtime
        if not force and self._mtime is not None and mtime == self._mtime and self.doc is not None:
            return False
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
            validate(doc)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            self.doc = None
            self.error = str(exc)
            self._mtime = mtime
            return True
        self.doc = doc
        self.error = None
        self._mtime = mtime
        return True

    @property
    def ready(self) -> bool:
        self.reload_if_needed()
        return self.doc is not None

    def encounter(self, key: str) -> dict | None:
        self.reload_if_needed()
        if not self.doc:
            return None
        compact = _compact(key)
        for encounter in self.doc["encounters"]:
            if encounter["key"] == key or _compact(encounter["key"]) == compact or _compact(encounter["enum_name"]) == compact:
                return encounter
        return None

    def choose(self, key: str, meets=None, state=None, option_labels=None) -> Decision:
        self.reload_if_needed()
        encounter = self.encounter(key) if self.doc else None
        if encounter is None:
            return hardcoded_choice(key, meets, option_labels)
        return choose_from_encounter(encounter, meets, state, option_labels)

    def special(self, key: str) -> dict | None:
        self.reload_if_needed()
        if not self.doc:
            return None
        for item in self.doc.get("special_encounters") or []:
            if item["key"] == key:
                return item
        return None


def validate(doc: dict) -> None:
    if not isinstance(doc, dict):
        raise ValueError("rules document must be an object")
    if not isinstance(doc.get("rules_version"), str) or not doc["rules_version"]:
        raise ValueError("rules_version is required")
    encounters = doc.get("encounters")
    if not isinstance(encounters, list) or not encounters:
        raise ValueError("encounters must be a non-empty list")
    seen = set()
    for encounter in encounters:
        key = encounter.get("key")
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError(f"bad encounter key {key!r}")
        seen.add(key)
        options = encounter.get("options")
        if not isinstance(options, list) or not options:
            raise ValueError(f"{key}: options required")
        keys = []
        for index, option in enumerate(options):
            if option.get("index") != index:
                raise ValueError(f"{key}: option index {option.get('index')} != {index}")
            opt_key = option.get("key")
            if not isinstance(opt_key, str) or not opt_key:
                raise ValueError(f"{key}: option key missing")
            if not isinstance(option.get("label"), str) or not option["label"]:
                raise ValueError(f"{key}: option label missing")
            keys.append(opt_key)
        if len(keys) != len(set(keys)):
            raise ValueError(f"{key}: duplicate option keys")
        if not isinstance(encounter.get("leave"), bool):
            raise ValueError(f"{key}: leave must be a boolean")
        for field in ("choice", "fallback"):
            if option_index(encounter, encounter.get(field)) is None:
                raise ValueError(f"{key}: {field} {encounter.get(field)!r} is not an option")
        _validate_conditions(key, encounter.get("conditions") or [])
        _validate_follow_ups(key, encounter.get("follow_ups") or [], keys)
        if not isinstance(encounter.get("note", ""), str):
            raise ValueError(f"{key}: note must be a string")
    for special in doc.get("special_encounters") or []:
        if not isinstance(special.get("catch"), bool):
            raise ValueError(f"{special.get('key')}: catch must be a boolean")
        if special.get("ball_cap") not in BALL_CAPS:
            raise ValueError(f"{special.get('key')}: bad ball_cap")


def _validate_conditions(key: str, conditions) -> None:
    if not isinstance(conditions, list):
        raise ValueError(f"{key}: conditions must be a list")
    seen = set()
    for condition in conditions:
        kind = condition.get("type")
        if kind not in CONDITION_TYPES:
            raise ValueError(f"{key}: bad condition {kind!r}")
        if kind in seen:
            raise ValueError(f"{key}: duplicate condition {kind}")
        seen.add(kind)
        if kind != "party_has_free_slot":
            fraction = condition.get("fraction")
            if isinstance(fraction, bool) or not isinstance(fraction, (int, float)):
                raise ValueError(f"{key}: {kind} needs a fraction")
            if not 0 <= float(fraction) <= 1:
                raise ValueError(f"{key}: {kind} fraction out of range")


def _validate_follow_ups(key: str, follow_ups, option_keys: list[str]) -> None:
    if not isinstance(follow_ups, list):
        raise ValueError(f"{key}: follow_ups must be a list")
    ids = set()
    for slot in follow_ups:
        slot_id = slot.get("id")
        if not isinstance(slot_id, str) or not slot_id or slot_id in ids:
            raise ValueError(f"{key}: bad follow-up id {slot_id!r}")
        ids.add(slot_id)
        mode = slot.get("mode")
        if mode not in ("single", "multi"):
            raise ValueError(f"{key}: follow-up {slot_id} mode")
        choices = slot.get("choices") or []
        choice_keys = [c.get("key") for c in choices]
        if not choice_keys or any(not isinstance(item, str) or not item for item in choice_keys):
            raise ValueError(f"{key}: follow-up {slot_id} choices")
        if len(choice_keys) != len(set(choice_keys)):
            raise ValueError(f"{key}: follow-up {slot_id} duplicate choices")
        applies = slot.get("applies_to") or []
        if not applies or any(item not in option_keys for item in applies):
            raise ValueError(f"{key}: follow-up {slot_id} applies_to")
        selected = slot.get("selected")
        if mode == "single":
            if selected not in choice_keys:
                raise ValueError(f"{key}: follow-up {slot_id} selected")
        else:
            if not isinstance(selected, list) or any(item not in choice_keys for item in selected):
                raise ValueError(f"{key}: follow-up {slot_id} selected")


def apply_edit(base: dict, edit: dict) -> dict:
    """Patch choice, fallback, leave, conditions, note, follow-up selections, and special knobs.

    Option labels, requirements, tiers, and follow-up choice lists stay as they were on disk.
    """
    doc = json.loads(json.dumps(base))
    by_key = {encounter["key"]: encounter for encounter in doc["encounters"]}
    for patch in edit.get("encounters") or []:
        key = patch.get("key")
        if key not in by_key:
            raise ValueError(f"unknown encounter {key}")
        encounter = by_key[key]
        if "choice" in patch:
            encounter["choice"] = patch["choice"]
        if "fallback" in patch:
            encounter["fallback"] = patch["fallback"]
        if "leave" in patch:
            if not isinstance(patch["leave"], bool):
                raise ValueError(f"{key}: leave must be a boolean")
            encounter["leave"] = patch["leave"]
        if "note" in patch:
            if not isinstance(patch["note"], str):
                raise ValueError(f"{key}: note must be a string")
            encounter["note"] = patch["note"]
        if "conditions" in patch:
            encounter["conditions"] = patch["conditions"]
        selected = patch.get("follow_ups") or {}
        slots = {slot["id"]: slot for slot in encounter.get("follow_ups") or []}
        for slot_id, value in selected.items():
            if slot_id not in slots:
                raise ValueError(f"{key}: unknown follow-up {slot_id}")
            slots[slot_id]["selected"] = value
    specials = {item["key"]: item for item in doc.get("special_encounters") or []}
    for patch in edit.get("special_encounters") or []:
        key = patch.get("key")
        if key not in specials:
            raise ValueError(f"unknown special encounter {key}")
        item = specials[key]
        if "catch" in patch:
            if not isinstance(patch["catch"], bool):
                raise ValueError(f"{key}: catch must be a boolean")
            item["catch"] = patch["catch"]
        if "ball_cap" in patch:
            item["ball_cap"] = patch["ball_cap"]
        if "note" in patch:
            if not isinstance(patch["note"], str):
                raise ValueError(f"{key}: note must be a string")
            item["note"] = patch["note"]
    validate(doc)
    return doc


def render_markdown(doc: dict) -> str:
    version = doc.get("rules_version", "")
    digest = content_hash(doc)
    lines = [
        "# Encounter rules",
        "",
        f"Version `{version}`. Content hash `{digest}`.",
        "",
        "Each encounter stores a chosen option and a fallback, as option keys (`option_1` is the first button). "
        "There is no preference ranking. `leave` takes the last option and ignores the chosen option. "
        "A fallback is used when the chosen option's requirements are not met, or when a simple condition fails.",
        "",
        "The farm editor writes the live `encounter_rules.json` next to `item_priority.json` and reloads it when the file changes. "
        "The simulator keeps its own pinned copy and does not read this file.",
        "",
        "## Mystery encounters",
        "",
        "| Encounter | Tier | Waves | Choice | Fallback | Leave | Follow-up | Note |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    labels = {}
    for encounter in doc["encounters"]:
        labels[encounter["key"]] = {option["key"]: option["label"] for option in encounter["options"]}
        choice = labels[encounter["key"]].get(encounter["choice"], encounter["choice"])
        fallback = labels[encounter["key"]].get(encounter["fallback"], encounter["fallback"])
        follow = []
        for slot in encounter.get("follow_ups") or []:
            picked = slot["selected"]
            if isinstance(picked, list):
                shown = ", ".join(_choice_label(slot, item) for item in picked) or "(none)"
            else:
                shown = _choice_label(slot, picked)
            follow.append(f"{slot['label']}: {shown}")
        waves = encounter.get("wave_range") or []
        wave = f"{waves[0]}–{waves[1]}" if len(waves) == 2 else ""
        lines.append(
            "| {name} | {tier} | {wave} | {choice} | {fallback} | {leave} | {follow} | {note} |".format(
                name=_cell(encounter["display_name"]),
                tier=encounter.get("tier", ""),
                wave=wave,
                choice=_cell(choice),
                fallback=_cell(fallback),
                leave="yes" if encounter.get("leave") else "no",
                follow=_cell("; ".join(follow)),
                note=_cell(encounter.get("note") or ""),
            )
        )
    lines += [
        "",
        "## Options",
        "",
    ]
    for encounter in doc["encounters"]:
        lines.append(f"### {encounter['display_name']}")
        lines.append("")
        lines.append(f"`{encounter['key']}` · {encounter.get('tier', '')} · waves {encounter.get('wave_range')}")
        lines.append("")
        for option in encounter["options"]:
            req = ", ".join(option.get("requirements") or []) or "none"
            party = " Selects a Pokémon." if option.get("selects_party") else ""
            lines.append(f"- `{option['key']}` **{option['label']}**.{party} Requirements: {req}.")
        if encounter.get("conditions"):
            lines.append("")
            lines.append("Conditions: " + ", ".join(_condition_text(item) for item in encounter["conditions"]) + ".")
        lines.append("")
    lines += [
        "## Other encounters",
        "",
        "These are not mystery encounters. The catch switch and ball cap refine the global catching setting.",
        "",
        "| Encounter | Catch | Ball cap | Note |",
        "| --- | --- | --- | --- |",
    ]
    for special in doc.get("special_encounters") or []:
        lines.append(
            f"| {_cell(special['display_name'])} | {'yes' if special.get('catch') else 'no'} | {special.get('ball_cap', '')} | {_cell(special.get('note') or '')} |"
        )
    lines.append("")
    return "\n".join(lines)


def _choice_label(slot: dict, key: str) -> str:
    for choice in slot.get("choices") or []:
        if choice.get("key") == key:
            return choice.get("label") or key
    return str(key)


def _condition_text(condition: dict) -> str:
    kind = condition.get("type")
    if kind == "party_has_free_slot":
        return "party has a free slot"
    if kind == "money_above_fraction":
        return f"money above {condition.get('fraction')}"
    if kind == "primary_hp_above_fraction":
        return f"primary HP above {condition.get('fraction')}"
    return str(kind)


def _cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def write_markdown(doc: dict, path: Path) -> None:
    path.write_text(render_markdown(doc), encoding="utf-8")


def markdown_path_for(json_path: Path) -> Path:
    if json_path.name == "encounter_rules.json":
        return json_path.parent / "ENCOUNTER_RULES.md"
    return json_path.with_name(json_path.stem + ".md")


def save_document(path: Path | str, doc: dict, reason: str) -> Path | None:
    """Backup the previous file, then replace it atomically and regenerate the markdown."""
    path = Path(path)
    assert_not_sim_pin(path)
    validate(doc)
    text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    backup = None
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        backup_dir = path.parent / "encounter_rules_backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = time.strftime("%Y%m%d_%H%M%S")
        backup = backup_dir / f"encounter_rules_{stamp}_{reason}.json"
        suffix = 1
        while backup.exists():
            backup = backup_dir / f"encounter_rules_{stamp}_{reason}_{suffix}.json"
            suffix += 1
        shutil.copy2(path, backup)
    fd, tmp_name = tempfile.mkstemp(prefix=".encounter_rules_", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, path)
    except Exception:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise
    write_markdown(doc, markdown_path_for(path))
    return backup
