# Eternatus catch plan (Classic wave 200) — Gavin t138u, 10/31/2026

Sources: pagefaultgames/pokerogue `main` (fetched 10/31/2026): src/phases/command-phase.ts (checkCanUseBall, handleBallCommand),
src/field/pokemon.ts (damage(), getMinimumSegmentIndex), src/battle-scene.ts (initFinalBossPhaseTwo, getEncounterBossSegments),
src/phases/quiet-form-change-phase.ts, src/data/pokeball.ts, src/phases/attempt-capture-phase.ts.

## How the fight works
- Wave 200 in Classic is the final boss (`isWaveFinal` = wave 200). Eternatus is forced to be a boss.
- Phase 1: Eternatus with shields (4 bars expected: base 2, +1 if level >= 100, +1 because its BST is 690 (>= 670)).
  In phase 1 the last bar cannot be broken (minimum segment index 1) and damage is capped, so it can't be KO'd in phase 1.
- When the phase-1 bars are gone, it becomes **Eternamax**: full heal (HP, status, PP), all tags cleared,
  **5 shield bars**, new moveset (Dynamax Cannon, Cross Poison, Flamethrower, Recover...), a non-stealable Mini Black Hole (steals your held items each turn),
  and the battle becomes a **double** (your 2nd mon is sent out). Final boss has no passive.
- Balls are allowed on the final boss only if you have caught all starters but at most one (`missingMultipleStarters` check). Gavin says he has them all.
- **Master Ball**: can be thrown at the final boss **at any time, even with shields up, in either phase**, as long as **no challenge is active** (Classic, no challenges = OK). Master Ball multiplier is -1 → guaranteed catch.
- **Any other ball** (Rogue/Ultra/...): blocked while the boss has 1+ shield bars ("must be weakened"). Because phase 1 can't drop below 1 bar, a non-Master catch is only possible in **Eternamax phase after all 5 bars are broken**, then normal catch math (low HP + status helps; Eternatus catch rate is very low, so expect many Rogue Balls).
- Ball throw is refused if more than one enemy is on the field (only Eternatus is, so fine).

## Procedure
### With a Master Ball (preferred)
1. Farm stops itself at the start of wave 200 (stopped_reason `eternatus_catch`, stop flag set). Pre-heal at 199 is automatic (x10 wave = hard wave).
2. First turn: Ball → **Master Ball** → throw at Eternatus. Do **not** attack first (no need, and attacks only make it angrier/stat-boosted).
3. Confirm the catch, nickname prompt → No, then let the run end normally (catching the final boss ends the battle; run completes).

### Without a Master Ball (Rogue Ball fallback)
1. Phase 1: break bars **one at a time**. Before each hit, estimate damage (game damage calc / per-hit % from previous turn). Each broken bar gives Eternatus a stat boost.
2. Phase 1 can't KO it, so strong moves are safe in phase 1.
3. Eternamax (5 bars, double battle): break bars one at a time with **resisted or weak moves** (Eternatus is Poison/Dragon: Fairy and Dragon are super effective — AVOID them near the last bar; use resisted hits, e.g. a Grass/Fighting/Bug/Poison move, or a weaker party mon). Lost-Nuzleaf lesson: never use a super-effective move once the next hit could take the last bar *and* the HP.
4. Once **0 bars**, stop attacking. If possible inflict sleep/paralysis. Throw Rogue Balls every turn; the other mon uses Calm Mind/protect/a status move, not damage.
5. Mini Black Hole steals a held item each turn, and Eternamax has Recover (HP comes back; broken bars do not). Keep throwing.
6. If the party is about to wipe, prioritise throwing over attacking.

## Not verified live
- Exact bar count in phase 1 depends on Eternatus' level at wave 200 (expected >= 100 → 4 bars).
- This is from the current GitHub `main`; pokerogue.net can lag behind main.
