# PokéRogue Classic farm: item priority list

> **Edits go in `item_priority.json`** (same folder), not here. This page is generated from it by `gen_item_priority_md.py`. The farm reads the JSON at start and reloads it automatically when the file changes.

## How ranking works
1. **Specials** beat everything: master_ball (-400), role_revive (-300), sword (-290), prism_scale (-290), dna_pair (-250), emergency_heal (-240).
   *master_ball*: Gavin t138u/t140u: Master Ball beats everything; reserved for the wave-200 Eternatus catch every run.; *role_revive*: Revive/Max Revive/Sacred Ash when Zacian or secondary fainted; *sword*: Rusted/Ancient Sword while Zacian in party; *prism_scale*: while secondary is Feebas; *dna_pair*: DNA Splicers when unfused Kricketot/Kricketune + Zigzagoon/Linoone; *emergency_heal*: Full Restore/Max Potion/heal when Zacian <25% HP and next wave risky
2. **Junk** (rank ≥ 93) always loses to any real item, whatever its tier; if the best card is junk the farm rerolls.
3. Otherwise the **higher tier wins**: MASTER > ROGUE > ULTRA > GREAT > COMMON (tier read from the card). `min_tier` lifts an item to at least that tier.
4. Inside a tier, the **lower rank wins**. Rules are checked top-down; the first rule whose pattern matches and whose condition is true sets the rank. No match = default 50.
5. Shop-buyable items are ordinary Common/Great cards, so they can never beat a rarer real item.

Conditions use flags: `lure_active`, `out_of_balls`, `holding_balls`, `heal_need`, `role_low`, `pp_crit`, `pp_low`, `secondary_in_party`, `ally_dead`, `zhp_low`, `zacian_fainted`, `voucher_crit`, `emergency`. `step` adds step×(position of the matched pattern), e.g. best heal/ball first.

## Rules (checked in this order)
| # | id | Matches | Mode | Condition | Rank | Min tier | Shop? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | tera_shard | tera shard | substring | always | 97 **junk** |  |  | never take; junk |
| 2 | eviolite | eviolite | substring | always | 96 **junk** |  |  | useless on Zacian; junk |
| 3 | soothe_bell | soothe bell | substring | always | -99.5 | ULTRA |  | top of its tier; goes to secondary until 3 stacks, then Zacian |
| 4 | rarer_candy | rarer candy | substring | always | -56 | ULTRA |  | candy; just above Rare Candy within tier |
| 5 | candy | candy jar, rare candy | substring | always | -55 | ULTRA |  | candy priority |
| 6 | voucher | voucher | substring | not voucher_crit | -50 | ULTRA |  | egg vouchers; skipped only in emergency |
| 7 | zacian_revive | revive, sacred ash | substring | zacian_fainted | -50 |  | yes | (role revive special -300 normally fires first) |
| 8 | role_heal | full restore, max potion, hyper potion, sitrus berry, super potion, potion | substring | role_low | -45 (+0.1/pattern) |  | yes | Zacian/secondary <75% HP; index order = list order |
| 9 | heal_need | full restore, max potion, hyper potion, sitrus berry, super potion, potion | substring | heal_need | -40 (+1/pattern) |  | yes | Zacian <80%, or <99.9% before a risky wave; within tier only |
| 10 | vitamins | hp up, protein, iron, calcium, zinc, carbos, base stat | word | always | -30 |  |  | vitamins (TMs excluded) |
| 11 | leppa_pp_short | leppa | substring | pp_crit or pp_low | -20 |  |  |  |
| 12 | leppa | leppa | substring | always | 30 |  |  |  |
| 13 | pp_crit | max elixir, elixir, max ether, ether | substring | pp_crit | -10 (+0.1/pattern) |  | yes |  |
| 14 | pp_low | max elixir, elixir, max ether, ether | substring | pp_low | 45 (+0.1/pattern) |  | yes | fixed dead branch: low PP (<40%) makes them a mid pick |
| 15 | pp_fine | max elixir, elixir, max ether, ether | substring | always | 94 **junk** |  | yes | junk when PP fine |
| 16 | menu_items | tm, memory mushroom, mint, dna splicers | menu | always | 99 **junk** |  |  | open teach/party menus; junk (DNA pair handled by special -250) |
| 17 | ball_out | master ball, rogue ball, ultra ball, great ball, poke ball | ball | out_of_balls | -200 (+0.1/pattern) |  |  | out of balls: top of own tier, best ball first |
| 18 | ball_good | master ball, rogue ball | ball | holding_balls | 92 |  |  | bottom of own tier (still beats lower tiers) |
| 19 | ball_junk | ultra ball, great ball, poke ball | ball | holding_balls | 98 **junk** |  |  | junk while any ball held |
| 20 | lure_active | lure | substring | lure_active | 100.5 **junk** |  |  | worst of all while a lure is active |
| 21 | lure_secondary | lure | substring | secondary_in_party | -15 |  |  | keep a lure up for doubles (within tier) |
| 22 | lure | lure | substring | always | 88 |  |  |  |
| 23 | x_special | x sp. atk, x sp. def, x accuracy | prefix | always | 96 **junk** |  |  | battle items; junk |
| 24 | x_items | x , dire hit | prefix_or_substring | always | 93 **junk** |  |  | X Atk/Def/Spd, Dire Hit; junk (reroll) |
| 25 | revive_unneeded | revive | substring | not ally_dead | 90 |  | yes |  |
| 26 | potion_unneeded | potion | substring | not zhp_low | 80 |  | yes |  |
| 27 | pri_max_revive | max revive | substring | always | 2 |  | yes |  |
| 28 | pri_leftovers | leftovers | substring | always | 3 |  |  |  |
| 29 | pri_shell_bell | shell bell | substring | always | 4 |  |  |  |
| 30 | pri_kings_rock | king's rock | substring | always | 8 |  |  |  |
| 31 | pri_scope_lens | scope lens | substring | always | 9 |  |  |  |
| 32 | pri_quick_claw | quick claw | substring | always | 10 |  |  |  |
| 33 | pri_focus_band | focus band | substring | always | 11 |  |  |  |
| 34 | pri_lucky_egg | lucky egg | substring | always | 13 |  |  |  |
| 35 | pri_exp_all | exp. all | substring | always | 14 |  |  |  |
| 36 | pri_exp_share | exp. share | substring | always | 14 |  |  |  |
| 37 | pri_golden | golden | substring | always | 15 |  |  |  |
| 38 | pri_silk_scarf | silk scarf | substring | always | 16 |  |  |  |
| 39 | pri_fairy_feather | fairy feather | substring | always | 18 |  |  |  |
| 40 | pri_metal_coat | metal coat | substring | always | 19 |  |  |  |
| 41 | pri_berry | berry | substring | always | 20 |  |  |  |
| 42 | pri_full_restore | full restore | substring | always | 21 |  | yes |  |
| 43 | pri_max_potion | max potion | substring | always | 22 |  | yes |  |
| 44 | pri_revive | revive | substring | always | 23 |  | yes |  |
| 45 | pri_hyper_potion | hyper potion | substring | always | 24 |  | yes |  |
| 46 | pri_super_potion | super potion | substring | always | 29 |  | yes |  |
| 47 | pri_nugget | nugget | substring | always | 30 |  |  |  |
| 48 | pri_potion | potion | substring | always | 33 |  | yes |  |

Flame Orb / Toxic Orb are removed before ranking (banned, never bought).

## Shop (between-wave buys; not shown on waves ending in 0; unlocks one row per 30 waves)
Game shop: Potion, Ether, Revive | Super Potion, Full Heal | Elixir, Max Ether | Hyper Potion, Max Revive, Memory Mushroom | Max Potion, Max Elixir | Full Restore | Sacred Ash. The farm only buys heals/revives/Full Heal:

| Situation | What it buys | Spend cap |
|---|---|---|
| Zacian fainted | Most expensive of Max Revive / Revive it can afford | **No cap** (all money) |
| Secondary fainted | Max Revive / Revive | 25% of screen money, keep 25% reserve |
| Mon has a status and <75% HP | Full Restore | 25% |
| Mon has a status | Full Heal | 25% |
| Zacian or secondary <75% HP and missing ≥15% | Cheapest potion that covers the need (full missing HP if <30%, else half the missing + 15%) | 25% cap, 25% reserve |
| Next wave hard (waves 8/25/55/95/165/195 + learned, fixed battles, trainers, every x0) | Pre-heal: same logic but trigger is <99% HP | **75%** of screen money |
Fainted/lowest-HP mon handled first; Flame/Toxic Orb never bought; ≤8 buys per screen.

## Always / never rules
- **Flame Orb, Toxic Orb (and 'poison orb')**: removed from every screen and shop.
- **Dark Deal, GTS, Wonder Trade, any trade, Weird Dream**: always pick the last option (leave).
- **Shady Vitamin Dealer**: pricey deal (option 2) if affordable, otherwise leave.
- **Training Session**: always leave/opt out.
- **Rusted Sword/Shield** -290 while Zacian is in party. **Prism Scale** -290 while the secondary is Feebas.
- **DNA Splicers** -250 with unfused Kricketot/Kricketune (base, first) + Zigzagoon/Linoone (partner, second); otherwise 99.
- **Role revive** -300 when Zacian or the secondary is fainted.
- **Berries** go to Zacian and never beat a higher-tier useful item.
- **Soothe Bell** -99.5; goes to the secondary until it has 3, then Zacian.
- **TMs, Mints, Memory Mushroom** rank 99 and are excluded from the tier boost (they open menus); a TM that does get picked is blacklisted and left.
- Kricketot evolution stays paused; lure never re-bought while one is active.
