"""Unit tests for the farm encounter-rules loader and the editor save path."""
from __future__ import annotations

import json
import shutil
import tempfile
import threading
import time
import unittest
import urllib.request
from pathlib import Path

import encounter_rules as rules

ROOT = Path(__file__).resolve().parents[2]
LIVE = ROOT / "tools" / "encounter_rules.json"
PIN = ROOT / "simulator" / "rules" / "encounter_rules.v1.json"


def load_live() -> dict:
    return json.loads(LIVE.read_text(encoding="utf-8"))


class ChooseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = rules.EncounterRules(LIVE)

    def test_catalog_covers_thirty_one(self):
        doc = self.engine.doc
        self.assertIsNotNone(doc)
        self.assertEqual(len(doc["encounters"]), 31)
        self.assertEqual(doc["rules_version"], "encounter-rules-v1")
        self.assertEqual(LIVE.read_text(encoding="utf-8"), PIN.read_text(encoding="utf-8"))
        strategy = json.loads((ROOT / "simulator" / "strategy.json").read_text(encoding="utf-8"))
        self.assertEqual(strategy["encounter_rules_sha256"], rules.content_hash(doc))
        self.assertEqual(strategy["encounter_rules_version"], doc["rules_version"])

    def test_shady_pricey_when_it_meets(self):
        decision = self.engine.choose("mysteryEncounters/shadyVitaminDealer", [True, True, True])
        self.assertEqual(decision.index, 1)
        self.assertIn("Pricey", decision.reason)
        self.assertEqual(decision.follow_ups["pokemon"], "lowest_index_alive")
        self.assertEqual(decision.source, "rules")

    def test_shady_leave_when_pricey_unavailable(self):
        decision = self.engine.choose("shadyVitaminDealer", [True, False, True])
        self.assertEqual(decision.index, 2)
        self.assertIn("fallback", decision.reason)

    def test_training_weird_gts_dark_deal_leave(self):
        for key, count in (
            ("trainingSession", 4),
            ("weirdDream", 3),
            ("globalTradeSystem", 4),
            ("darkDeal", 2),
        ):
            meets = [True] * count
            decision = self.engine.choose(key, meets)
            self.assertEqual(decision.index, count - 1, key)
            self.assertIn("leave", decision.reason)

    def test_chest_opens(self):
        decision = self.engine.choose("mysteriousChest", [True, True])
        self.assertEqual(decision.index, 0)
        self.assertIn("Open", decision.reason)

    def test_generic_top_or_fallback(self):
        top = self.engine.choose("fightOrFlight", [True, True, True])
        self.assertEqual(top.index, 0)
        fallen = self.engine.choose("fightOrFlight", [False, True, True])
        self.assertEqual(fallen.index, 2)
        self.assertIn("fallback", fallen.reason)

    def test_condition_failure_uses_fallback(self):
        encounter = json.loads(json.dumps(self.engine.encounter("fightOrFlight")))
        encounter["conditions"] = [{"type": "money_above_fraction", "fraction": 0.5}]
        decision = rules.choose_from_encounter(encounter, [True, True, True], {"money_fraction": 0.2})
        self.assertEqual(decision.index, 2)
        self.assertIn("conditions failed", decision.reason)

    def test_missing_condition_state_fails_closed(self):
        encounter = json.loads(json.dumps(self.engine.encounter("fightOrFlight")))
        encounter["conditions"] = [{"type": "party_has_free_slot"}]
        decision = rules.choose_from_encounter(encounter, [True, True, True], {})
        self.assertEqual(decision.index, 2)
        encounter["conditions"] = [{"type": "primary_hp_above_fraction", "fraction": 0.75}]
        decision = rules.choose_from_encounter(encounter, [True, True, True], {})
        self.assertEqual(decision.index, 2)

    def test_conditions_pass(self):
        encounter = json.loads(json.dumps(self.engine.encounter("fightOrFlight")))
        encounter["conditions"] = [
            {"type": "money_above_fraction", "fraction": 0.25},
            {"type": "party_has_free_slot"},
            {"type": "primary_hp_above_fraction", "fraction": 0.5},
        ]
        state = {"money_fraction": 0.4, "party_has_free_slot": True, "primary_hp_fraction": 0.8}
        decision = rules.choose_from_encounter(encounter, [True, True, True], state)
        self.assertEqual(decision.index, 0)

    def test_leave_ignores_choice(self):
        encounter = json.loads(json.dumps(self.engine.encounter("trainingSession")))
        encounter["choice"] = "option_1"
        encounter["leave"] = True
        decision = rules.choose_from_encounter(encounter, [True, True, True, True])
        self.assertEqual(decision.index, 3)

    def test_choice_accepts_index(self):
        encounter = json.loads(json.dumps(self.engine.encounter("mysteriousChest")))
        encounter["choice"] = 0
        encounter["fallback"] = 1
        decision = rules.choose_from_encounter(encounter, [True, True])
        self.assertEqual(decision.index, 0)

    def test_party_slot(self):
        party = [
            {"index": 0, "fainted": True, "hp_fraction": 0},
            {"index": 1, "fainted": False, "hp_fraction": 0.9},
            {"index": 2, "fainted": False, "hp_fraction": 0.2},
        ]
        self.assertEqual(rules.party_slot("lowest_index_alive", party), 1)
        self.assertEqual(rules.party_slot("lead", party), 1)
        self.assertEqual(rules.party_slot("secondary", party), 1)
        self.assertEqual(rules.party_slot("lowest_hp", party), 2)

    def test_missing_and_broken_file_use_hardcoded(self):
        missing = rules.EncounterRules(Path(tempfile.gettempdir()) / "no-such-encounter-rules.json")
        pricey = missing.choose("shadyVitaminDealer", [True, True, True])
        self.assertEqual(pricey.index, 1)
        self.assertEqual(pricey.source, "hardcoded")
        leave = missing.choose("shadyVitaminDealer", [True, False, True])
        self.assertEqual(leave.index, 2)
        self.assertEqual(missing.choose("trainingSession", [True, True, True, True]).index, 3)
        self.assertEqual(missing.choose("weirdDream", [True, True, True]).index, 2)
        self.assertEqual(missing.choose("globalTradeSystem", [True] * 4).index, 3)
        self.assertEqual(missing.choose("darkDeal", [True, True]).index, 1)
        self.assertEqual(missing.choose("mysteriousChest", [True, True]).index, 0)
        text = missing.choose("funAndGames", [True, True], option_labels=["Trade your team", "Leave"])
        self.assertEqual(text.index, 1)
        self.assertEqual(text.source, "hardcoded")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "encounter_rules.json"
            path.write_text("{", encoding="utf-8")
            broken = rules.EncounterRules(path)
            decision = broken.choose("fightOrFlight", [True, True, True])
            self.assertEqual(decision.index, 0)
            self.assertEqual(decision.source, "hardcoded")

    def test_mtime_reload(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "encounter_rules.json"
            shutil.copy(LIVE, path)
            engine = rules.EncounterRules(path)
            self.assertEqual(engine.choose("mysteriousChest", [True, True]).index, 0)
            doc = json.loads(path.read_text(encoding="utf-8"))
            chest = next(item for item in doc["encounters"] if item["key"] == "mysteriousChest")
            chest["choice"] = "option_2"
            time.sleep(0.05)
            path.write_text(json.dumps(doc), encoding="utf-8")
            decision = engine.choose("mysteriousChest", [True, True])
            self.assertEqual(decision.index, 1)
            self.assertEqual(decision.source, "rules")


class SaveRoundTripTests(unittest.TestCase):
    def test_apply_edit_preserves_options_and_refuses_pin(self):
        base = load_live()
        original_options = json.loads(json.dumps(next(item for item in base["encounters"] if item["key"] == "shadyVitaminDealer")["options"]))
        edited = rules.apply_edit(
            base,
            {
                "encounters": [
                    {
                        "key": "shadyVitaminDealer",
                        "choice": "option_1",
                        "fallback": "option_3",
                        "leave": False,
                        "note": "Cheap deal, else leave.",
                        "conditions": [{"type": "money_above_fraction", "fraction": 0.1}],
                        "follow_ups": {"pokemon": "lead"},
                    }
                ],
                "special_encounters": [{"key": "wild_boss", "catch": False, "ball_cap": "none"}],
            },
        )
        shady = next(item for item in edited["encounters"] if item["key"] == "shadyVitaminDealer")
        self.assertEqual(shady["options"], original_options)
        self.assertEqual(shady["choice"], "option_1")
        self.assertEqual(shady["follow_ups"][0]["selected"], "lead")
        base_shady = next(item for item in base["encounters"] if item["key"] == "shadyVitaminDealer")
        self.assertEqual(shady["follow_ups"][0]["choices"], base_shady["follow_ups"][0]["choices"])
        boss = next(item for item in edited["special_encounters"] if item["key"] == "wild_boss")
        self.assertFalse(boss["catch"])
        untouched = next(item for item in edited["encounters"] if item["key"] == "mysteriousChest")
        original_chest = next(item for item in base["encounters"] if item["key"] == "mysteriousChest")
        self.assertEqual(untouched, original_chest)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "encounter_rules.json"
            backup = rules.save_document(path, edited, "test")
            self.assertIsNone(backup)
            round_trip = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(round_trip["encounters"][7]["options"], original_options)
            self.assertTrue((Path(tmp) / "ENCOUNTER_RULES.md").exists())
            self.assertIn("The Pricey Deal", (Path(tmp) / "ENCOUNTER_RULES.md").read_text(encoding="utf-8"))
            path.write_text(json.dumps(base), encoding="utf-8")
            backup = rules.save_document(path, edited, "presave")
            self.assertIsNotNone(backup)
            self.assertTrue(backup.exists())
            self.assertIn("The Pricey Deal", json.loads(backup.read_text(encoding="utf-8"))["encounters"][7]["options"][1]["label"])
        with self.assertRaises(ValueError):
            rules.save_document(PIN, edited, "nope")

    def test_simulator_module_agrees(self):
        import os
        import subprocess

        script = r"""
import { choose, contentHash, loadPinned, partySlot, optionSelectIndex } from "./simulator/encounter-rules.mjs";
const loaded = loadPinned();
const specs = [
  ["mysteryEncounters/shadyVitaminDealer", [true, true, true]],
  ["shadyVitaminDealer", [true, false, true]],
  ["trainingSession", [true, true, true, true]],
  ["weirdDream", [true, true, true]],
  ["globalTradeSystem", [true, true, true, true]],
  ["darkDeal", [true, true]],
  ["mysteriousChest", [true, true]],
  ["fightOrFlight", [false, true, true]],
  [7, [true, true, true]],
];
const cases = specs.map(([key, meets]) => {
  const picked = choose(loaded.doc, key, meets, null);
  return { key: String(key), index: picked.index, source: picked.source };
});
const fight = loaded.doc.encounters.find(item => item.key === "fightOrFlight");
const gated = { ...fight, conditions: [{ type: "money_above_fraction", fraction: 0.5 }] };
const failed = choose(loaded.doc, "unused", null);
const conditioned = choose({ encounters: loaded.doc.encounters.map(item => item.key === "fightOrFlight" ? gated : item), special_encounters: [] }, "fightOrFlight", [true, true, true], { money_fraction: 0.2 });
console.log(JSON.stringify({
  hash: contentHash(loaded.doc),
  cases,
  conditioned: conditioned.index,
  missing: failed.index,
  party: partySlot("lowest_hp", [
    { index: 0, fainted: false, hp_fraction: 0.9 },
    { index: 1, fainted: false, hp_fraction: 0.2 },
  ]),
  decline: optionSelectIndex(["First move", "Cancel"], { bug_move: "decline" }),
  nature: optionSelectIndex(["Hardy", "Adamant", "Modest"], { nature: "ADAMANT" }),
}));
"""
        env = os.environ.copy()
        env["PATH"] = os.path.expanduser("~/.local/bin") + os.pathsep + env.get("PATH", "")
        completed = subprocess.run(
            ["node", "--input-type=module", "-e", script],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            env=env,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["hash"], rules.content_hash(load_live()))
        engine = rules.EncounterRules(LIVE)
        expected = {
            "mysteryEncounters/shadyVitaminDealer": 1,
            "shadyVitaminDealer": 2,
            "trainingSession": 3,
            "weirdDream": 2,
            "globalTradeSystem": 3,
            "darkDeal": 1,
            "mysteriousChest": 0,
            "fightOrFlight": 2,
            "7": engine.choose("shadyVitaminDealer", [True, True, True]).index,
        }
        for case in payload["cases"]:
            self.assertEqual(case["index"], expected[case["key"]], case["key"])
            self.assertEqual(case["source"], "rules")
        self.assertEqual(payload["conditioned"], 2)
        self.assertEqual(payload["missing"], 0)
        self.assertEqual(payload["party"], 1)
        self.assertEqual(payload["decline"], 1)
        self.assertEqual(payload["nature"], 1)

    def test_markdown_lists_choice_not_a_ranking(self):
        text = rules.render_markdown(load_live())
        self.assertIn("The Pricey Deal", text)
        self.assertIn("no preference ranking", text.lower())
        self.assertNotIn("preference list", text.lower())
        self.assertIn("encounter-rules-v1", text)


class ServerRoundTripTests(unittest.TestCase):
    def test_http_save_round_trip(self):
        import server as editor_server

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "encounter_rules.json"
            shutil.copy(LIVE, path)
            pin_mtime = PIN.stat().st_mtime
            httpd = editor_server.make_server(path, "127.0.0.1", 0)
            port = httpd.server_address[1]
            thread = threading.Thread(target=httpd.serve_forever, daemon=True)
            thread.start()
            try:
                payload = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/api/data").read().decode())
                self.assertEqual(payload["data"]["rules_version"], "encounter-rules-v1")
                html = urllib.request.urlopen(f"http://127.0.0.1:{port}/").read().decode()
                self.assertIn("Fallback if unavailable", html)
                self.assertNotIn("drag", html.lower())
                body = {
                    "base_mtime": payload["mtime"],
                    "encounters": [
                        {
                            "key": "trainingSession",
                            "choice": "option_1",
                            "fallback": "option_4",
                            "leave": False,
                            "note": "Light training.",
                            "conditions": [],
                            "follow_ups": {"pokemon": "secondary"},
                        }
                    ],
                    "special_encounters": [],
                }
                request = urllib.request.Request(
                    f"http://127.0.0.1:{port}/api/save",
                    data=json.dumps(body).encode(),
                    headers={"Content-Type": "application/json"},
                )
                saved = json.loads(urllib.request.urlopen(request).read().decode())
                self.assertTrue(saved["ok"])
                disk = json.loads(path.read_text(encoding="utf-8"))
                training = next(item for item in disk["encounters"] if item["key"] == "trainingSession")
                original = next(item for item in load_live()["encounters"] if item["key"] == "trainingSession")
                self.assertEqual(training["options"], original["options"])
                self.assertEqual(training["choice"], "option_1")
                self.assertFalse(training["leave"])
                self.assertEqual(training["follow_ups"][0]["selected"], "secondary")
                self.assertEqual(training["follow_ups"][1]["choices"], original["follow_ups"][1]["choices"])
                self.assertEqual(PIN.stat().st_mtime, pin_mtime)
                self.assertTrue((Path(tmp) / "ENCOUNTER_RULES.md").is_file())
            finally:
                httpd.shutdown()


if __name__ == "__main__":
    unittest.main()
