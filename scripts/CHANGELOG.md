## 2026-11-07 10:18-10:33 MST - run end w90 -> new run
- Farm (PID 108308) exited 10:18:27 MST ALL-FAINT Classic w90 vs Gym Leader Clay Golurk; whole party fainted. RUN LOG row w90 slot=0 luck=3 verified at top of CHIE Run Log.md. DONE farm17. No stop flag; no farm process (only PokeFarmControl 728).
- to_title.py -> Title -> `_re2.py newgame` (Classic). Pre-reduce: eggs=3, Ray candy 6 vr=2, Abra candy 14 vr=2, shinyHatched=140. `_re2.py reduce 384,63`: both vr=2 maxed; leftover candy spent as eggs (PC reduce path): Rayquaza 1 (x6, candy 6->0); Abra 1 (x12, candy 14->2). Eggs 3->5. Vouchers 815/165/49 unspent.
- Hatches this run: eggs 4->3 before title (1 non-shiny hatch); shinyHatched stayed 140. No new shiny egg hatches. No Shiny Log rows.
- New Classic slot 0 party [384,63,263,327,401] via nr_pick + `_re2.py start` + `_re2.py slot 0` (slot 0 Empty; slot 1 has data). Verified Classic mode 0, wave 1, slot 0, Rayquaza lead.
- Config unchanged primary=384 secondary=63 candy_target=primary. Cleared stop artifacts/status reasons; rotated stdout -> _prev; hidden Win32_Process Create pythonw PID 108060 parent WmiPrvSE 3808, single instance. WAVE UP 1->2->3 by 10:32:43.
## 2026-11-05 18:16-18:23 MST - overnight watch: caught wild shiny Deerling w47
- Farm stopped 18:16:38 on shiny_enemy Deerling (sid 585, Lv29, variant 1, singles); process gone, stop flag set. PID was 50260 earlier this run.
- Gavin-first wait elapsed; state unchanged (CommandPhase turn 1, foe 67/76, balls Poke 5 / Great 0 / Ultra 0 / Rogue 0 / Master 0). Took over.
- No attack (no shield). 1st Poké Ball (5 → 4) caught; Master untouched. Party full: _shiny_party_no.py No → storage; party unchanged. Declined Absol Psycho Cut.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_585s.png already present); backup .bak_deerling_w47_1822.
- _restart_after_shiny.py relaunched hidden (pythonw PID 118796, parent WmiPrvSE). One instance. No handoff.

## 2026-11-05 17:45-17:52 MST - watch run: run ended w114 (Team Plasma Sage Zinzolin / Vanilluxe), new run slot 2
- Party wiped at w114 vs Team Plasma Sage Zinzolin (Vanilluxe last); ALL-FAINT 17:45:11-16, Run Log row written (w114, slot 2, luck 3), DONE.
- to_title.py -> title -> _re2.py newgame (Classic). `_re2.py reduce 150,359`: no option (both maxed). Eggs: Mewtwo 2 (x6, 14 -> 2), Absol 1 (x12, 22 -> 10). Eggs 0 -> 3. Vouchers 675/134/45 unspent.
- New Classic slot 2 with Mewtwo/Zigzagoon/Kricketot/Mudkip/Absol/Spinda (all six present; Absol secondary). Farm launched hidden (pythonw PID 50260, parent WmiPrvSE); wave 6 by 17:50.

## 2026-11-05 16:43-16:50 MST - run ended w184 (Elite Four Bertha; whole party fainted vs Rhyperior), eggs, new slot-2 Classic run
- Farm exited 16:41:58 "DONE farm17" at w184 (SIG Elite Four Bertha; Mewtwo fell mid-fight, bench wiped ending on Rhyperior). No stop flag; status stale at 16:41:03. No farm process; no other controller.
- to_title.py -> title -> _re2.py newgame (Classic). Reduce 150,359: no options (maxed vr=2). Eggs: Mewtwo x3 (x6, candy 20 -> 2); Absol x3 (x12, candy 40 -> 4). Eggs 0 -> 6. Vouchers 669/129/44 left UNSPENT.
- nr_pick.py 150,359,263,327,401,258; tryStart via handler.tryStart() -> Confirm p:5 -> _re2.py slot 2 (empty). Verified Classic, wave 1, slot 2, party [150,359,263,327,401,258]; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Flags absent/cleared, stdout rotated, launched hidden via pythonw CREATE_NO_WINDOW pr_farm_launch_hidden.py (pythonw PID 47932, parent 55776). One instance; wave 8 Rival Ivy by 16:49.

## 2026-11-05 16:26-16:32 MST - wild shiny Mudsdale w156 caught (variant 1, singles)
- Overnight watch ~16:30: farm stopped shiny_enemy at 16:26:54 (Mudsdale Lv119 v1 sid 750, singles); process gone, stop flag set.
- Gavin-first wait elapsed; state unchanged (CommandPhase turn 1, foe 372/372, balls poke20/great15/ultra0/rogue17/master2). Took over.
- No attack (no shield). _sw.py ball Mudsdale: 1st Rogue Ball (17 -> 16) caught; Master untouched. Party full: _optno.py No -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_750s.png already present); backup .bak_mudsdale_1633.
- _restart_after_shiny.py relaunched hidden (pythonw PID 102884, parent WmiPrvSE). One instance; wave 157 by 16:31. No handoff.

## 2026-11-05 15:45 MST — wild shiny Rabsca catch (wave 76)

- Farm stopped on shiny Rabsca (sid 954, Lv49, variant 1, singles). Agent took over after Gavin window.
- Caught with 1st Rogue Ball (Rogue 5→4); Ultra was 0. Party full → storage (No).
- Shiny Log row added; stop flag cleared; same-run farm restarted hidden.

# PokéRogue farm changelog

## 2026-11-05 16:18-16:26 MST - wild shiny Excadrill w151 caught (variant 1, double with Rhyperior)
- Overnight watch ~16:20: farm process gone after shiny_enemy stop at 16:18:31 (PID 6328 gone); stop flag set; status wave 151 Excadrill Lv126 variant 1 sid 530 doubles with Rhyperior.
- Gavin-first wait elapsed; state unchanged (CommandPhase turn 1, foes full HP, balls poke20/great10/ultra0/rogue13/master2). Took over.
- Turn 1: Mewtwo Thunderous Kick single-target at Rhyperior (KO), Linoone Tidy Up. Excadrill untouched (439/439).
- _sw.py ball Excadrill: 1st Rogue Ball (13 -> 12) caught; Master untouched. Party full: _optno.py No -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_530s.png); backup .bak_excadrill_1624.
- _restart_after_shiny.py relaunched hidden (pythonw PID 97856, parent WmiPrvSE 113808). One instance; wave 152 by 16:25. No handoff.

## 2026-11-05 10:36 MST — caught shiny Drapion w71 (doubles); logged w68 misses
- Farm stopped 10:21 on shiny Drapion Lv51 v1 (double with Heliolisk). Hand catch after prior w68 Golett loss.
- KO'd Heliolisk with Mewtwo Thunderous Kick (mode-1 explicit target). Absol Leer (status). No confirm-mash on command menus.
- Mewtwo fainted to Drapion X-Scissor crit; switched Swampert. 5 Poké Balls after earlier fails → catch (11→4 Poké; Master untouched). Party full → No (storage). Dex drapion caughtCount 3.
- Declined Absol Future Sight. Mewtwo still Thunderous Kick / Psychic / Psybeam / Meteor Mash; Absol Leer / Spirit Break / Sacred Sword / Cross Poison.
- CHIE Shiny Log: Caught Drapion w71; Missed Cofagrigus + Golett w68 (intentional KO partner / accidental KO before ball).
- Cleared stop flag; hidden relaunch via _restart_after_shiny.py.
- 2026-10-29 01:08 MDT (overnight watch): farm now runs pr_farm15.py. Wave 71 stuck ~4 min in a Lum Berry party-apply loop (SelectModifierPhase, option 3); a live session patched/restarted at 01:07:32 and the blacklist fallback cleared it, now at wave 72 (doubles). Earlier at 01:02 the game loop froze (watchdog rAF restarts) until a stop/restart. No change made by this run.
## 2026-11-04 22:43 MT - MOVES (Gavin via school relay)
- profiles/mewtwo.json: protected+always-keep Meteor Mash, Thunderous Kick, Psystrike. target_moveset = those three (4th slot flexible via score; prefers Aura Sphere/Psychic in wanted/good). drop_first still Disable, Life Dew, Psyshock. Psychic/Aura Sphere no longer hard-protected.
- profiles/absol.json: learn_moves true (was false). target Night Slash / Spirit Break / Sacred Sword / Cross Poison. protected Spirit Break, Sacred Sword, Cross Poison. slot_replace {"Night Slash": 0} = replace only move slot 1 until Night Slash is learned; decline other learns meanwhile.
- pr_farm17.py: minimal learn_decide support for profile field slot_replace (takes effect on next farm launch). Untested in live play.
- Backups: *.bak_moves_20261104_224311 (live %TEMP%\prfarm and ..PROJECT\pokerogue).


## 2026-11-04 19:55-19:59 MST — overnight watch: shiny Palafin w180 (boss, 3 segments) caught
- Stopped 19:52:57 on shiny Palafin Lv188 v1 boss (604 HP). Eternatus Flamethrower x3 broke shield 1; Palafin healed 151 each turn under 50%, so switched to Mega Eelektross, Gunk Shot clamped at 202 (seg0, poisoned).
- Another controller (likely Gavin) threw the Rogue Ball (18->17) and caught it (storage); Gavin playing by hand to w182, farm left stopped. Logged Caught in CHIE Shiny Log; sprite icons/9/964s-zero.png.

## 2026-11-04 18:40 MST — overnight watch: caught shiny Golisopod w54 (doubles)
- Farm stopped 18:28 on shiny_enemy Golisopod Lv37 variant 2 (double with Parasect). After ~2 min Gavin-first wait, state unchanged.
- Eternatus Venoshock KO'd Parasect; switched Eelektrik→Kricketot (no status move). 1 Rogue Ball caught Golisopod (Rogue 5→4); party full → No (storage).
- Logged in CHIE Shiny Log (newest-first). Cleared stop flag/reasons; hidden relaunch pythonw PID 117552 (parent WmiPrvSE). Wave 56 by 18:42; Eternatus learned Flamethrower on rival wave 55.
## 2026-10-29 01:35 MDT — run ended: Zacian fainted at wave 110
- At 01:29:52, pr_farm15 stopped with ZACIAN FAINT. I checked gameInfo and the faint is real: Zacian hp 0/323 at wave 110 (trainer, singles, foe Rotom). Zacian was at 128/323 HP when the trainer fight started and took four turns.
- Stop flag set again. No patches made: the run is over and the skill forbids continuing without Zacian or starting a new Classic run unless Gavin asks.
- Frames saved to frames/: fight_menu_pp.png, reward_screen.png, party_switch_prompt.png, w110_zacian_fainted.png.
- Open items for the next run: Ether priority, battle-shot saving (last file is wave61), doubles faint switch, and a new one: heal before boss or trainer waves (Zacian started wave 110 at 40% HP).

## pr_farm16.py — 2026-10-29 08:05–08:50 MDT
Built from pr_farm15.py (backup pr_farm15.bak.py; intermediate pr_farm16.bak1/bak2.py on BOREN-0 %TEMP%\prfarm).
- Reward: Leppa Berry always top pick (rank -20); if the party target UI fails once for Leppa, retry on Zacian before blacklisting (lep_try).
- Reward: heal_need = Zacian <60% HP and (next wave %10==0, %10 in 5/8, or trainer) -> prefer Full Restore > Max/Hyper Potion > Sitrus > Super Potion > Potion. Verified w54 (picked Potion, heal_need=True).
- Battle shots restored to agent-tools\pokerogue_battle_shots\ (one per wave, wN_<move>_HHMMSS.jpg). prframes kept for stall/debug frames.
- Doubles forced switch-in: sends first alive non-field non-Zacian slot immediately, logs "switch-in".
- Faint check now needs 4 consecutive reads (avoid transient party misread).
- Ground moves skipped vs Levitate foes.
- Mystery encounters: choose last option that meets requirements (w26 stall: last option unmet); if ME asks for a party member, offer a non-Zacian ally (w36 loop); if no ally, take option 1.
- Run: old Classic wave-110 save (slot 2) replays into a deterministic Zacian faint, so started NEW Classic run in empty slot 4 (index 3) with Zacian; Endless slots 0/1 and old Classic slot untouched.
- 2026-10-29 08:58 MDT (watch): pr_farm16 alive (PID 71336), cleared w90 trainer at full HP, now w91 doubles with PP refilled. No patch. Open item: Ether/Max Ether picks don't seem to restore the low move (w87 Max Ether 'cannot be applied', w88/89 Ether left Spirit Break dropping to 0); check the move-select step after the party target.

## pr_farm17.py — 2026-10-29 09:10 MT (backup: pr_farm16.py untouched)
- Mystery encounters: always TOP option (cursor 0); removed the "last usable / leave" logic and the me_noparty back-out. ME party pick = Zacian (else slot 1). Confirm prompts in ME phases = first option; OptionSelect in any *Mystery* phase = Z (default/top).
- ME watchdog: same (handler, phase, cursor, optionsMode) for >20s -> screenshot `me_watchdog_*`, Up x4, Z.
- PP items (Ether/Elixir/Max Ether/Leppa): party option menu now reads option text labels (OPT_LABELS_JS), matches them to Zacian's move names, picks the lowest PP-left ratio; "Apply/Use" picked when present. Replaces the hard-coded enum 17..20 that never matched (log looped "slot 0 option 4"). The Zacian moveset is read from Zacian's party slot, not the field user.
- Faint: Zacian missing from the party read is no longer a faint (waits 30s and logs the party); a faint needs hp<=0 four reads in a row. Switching out while alive is logged. Zacian HP is logged on every change (`ZHP w.. hp/max onField ph`), and the faint line includes the last HP, foes and phase.
- Verified: py_compile OK (box + BOREN-0). Live: the w114 replay logged HP 309->167->28->faint (Drapion Sniper, then Ambipom). A real faint, stop correct.

## Fresh run on pr_farm17 — 2026-10-29 09:13–09:18 MDT
- Abandoned w114 replay (page reload at a SwitchPhase prompt, no Escape) -> Title -> New Game -> Classic (option 0; options were Classic/Daily/Challenge/Endless/...; Endless never touched) -> Zacian (filteredStarterIds idx 458 = 50 down, 8 right) -> Add to Party -> Right goes to Start -> Yes -> save slot 3 (the w114 Classic save; cursor 1 + scroll 2) -> overwrite Yes. Run = Classic wave 1, solo Zacian, slot 3. Frames: frames/newrun_*.png.
- New tools: cdp.py (state/key/screenshot/js helper, refuses Escape) and newrun.py <slot> --yes (scripted version of the steps above with asserts; not yet re-tested end to end). Kept separate from pr_farm17 so the farm loop is unchanged.
- Stop flag deleted, pr_farm17 launched 09:17 MDT (PID 131996).
- Verified w7: Max Elixir -> party opts labels ['Apply',...] -> Apply on Zacian; Mighty Cleave 1/5 -> 5/5 next turn.

## 2026-10-29 09:25 MDT — pr_farm17 patches (routine check)
- Stall at w16: Fight menu looped "no usable move - back" with only Earthquake having PP (soft rules excluded it). pick_move now falls back to any damaging move with PP instead of returning None. Log line for that case now includes foes/doubles.
- Ether/PP-item move menu labels came back as "[shadow]Earthquake 6/10[/shadow]", so name match failed and Ether went to slot 0 (Earthquake, not empty). Labels now stripped of tags and PP suffix so it targets the lowest-PP move.
- Restarted same run (Classic); progressing, at w28 when checked. Backups: pr_farm17.bak1.py, pr_farm17.bak2.py.

## pr_farm17 no-PP guard — 2026-10-29 09:24 MDT (backup pr_farm17.bak_nopp.py, box + BOREN-0)
- Merged onto the on-disk 09:25 pick_move fallback patch (any damaging move with PP) made by another session.
- After selecting a move: poll ~2 s (8x0.25 s with frame stepping). If a "no PP"/"PP left" message shows or the Fight menu is still open, mark the move 0 PP for (wave, user) in dead_moves, press Z x3 to clear the message, re-open Fight if back at Command, re-read PP from game state, pick_move excluding dead moves, else try the remaining slots in order; up to 5 retries; X only if no slot is left. Logs "NOPP stuck..." / "NOPP fallback -> ...". START line now tagged [nopp-guard].
- Same run restarted (Classic slot 3), not a new one. Two pr_farm17 processes briefly overlapped around 09:24; now one.

## pr_farm17 TM loop fix — 2026-10-29 09:27 MDT (backup pr_farm17.bak_tm.py)
- w32 stall: reward TM -> party 'Teach' -> Zacian declines LearnMove -> repeated forever. Now when the party option labels include "Teach", the item is blacklisted for that wave and we X back to rewards. Restarted 09:27 (PID 135368).
- Verified so far: ME w28 took TOP option and continued; PP items targeted the lowest move (w29 Ether -> Mighty Cleave 0/5 -> 5/5; w37 Mighty Cleave 2/5). No NOPP trigger seen yet.

## 2026-10-29 09:34 MDT (watch routine)
- Run ended: Zacian fainted on wave 64 (trainer wave, Seismitoad, Swift Swim) at 09:34:18. farm17 logged DONE.
- Wrote stop flag so no auto-restart; waiting for Gavin's go-ahead.
- Issue to fix next: on w63 reward, picked Ganlon Berry over Super Potion with Zacian at 79/183 (43%) right before a trainer wave (heal_need=False). Heal threshold before trainer/boss waves should be higher (e.g. <60%).

## 2026-10-29 09:37–09:56 MDT — heal fix + new Classic run (pr_farm17)
- Backups: pr_farm17.bak_heal.py (pre-heal, identical on box/BOREN-0 md5 e5ad8e4b…), pr_farm17.bak_heal2.py (pre-reload/cursor fix).
- Heal ranking: heal_need = Zacian HP <50% (any wave) OR <80% OR (<100% and next wave is x0 boss / x5 / x8 / trainer). When heal_need, Full Restore > Max > Hyper > Sitrus > Super > Potion rank -40..-35, above Leppa/PP items (wild-shiny catch still handled before rewards). Healing applies via existing party flow to Zacian's slot. Lures and all Balls dropped to rank 88. REWARD log now shows zhp% and risky_next. Offline test with the w63 case (79/183, Ganlon/Super Potion/Ultra Ball) -> Super Potion.
- New run: page reload -> newrun.py 3 --yes -> Classic w1, party [Zacian L5], slot 3 overwritten. Stop flag deleted, farm launched 09:39.
- 09:40 page reloaded itself to LoginPhase/Title at w6 (not a faint) and farm stopped on "Zacian missing 30s". Continue only restored w1 (later waves were not saved server-side). Fixes: Title with no faint seen -> press Continue (only if the label is "Continue", max 5).
- Reward cursor bug: setCursor didn't take, Z hit card 0 (TM), and the intended item got blacklisted as a "TM". Now verify cursor==i before Z (re-set otherwise); on Teach menu blacklist every TM in that wave's list, not the intended pick.
- w6 stall: log() print crashed on '♀' (cp1252 stdout) -> ERR loop in Fight UI. print falls back to ASCII; launch with PYTHONIOENCODING=utf-8.
- Relaunched 09:50 (PID 25584). Reached w42 by 09:55, Zacian 123/123.
- Open: at 95% HP before a risky wave with pp_low, heal (Sitrus) outranked Leppa (w~29) — consider Leppa first when HP>=80%. Sitrus/Lum at full HP "cannot be applied" -> blacklisted, fine.

## 2026-10-29 09:59 MT - farm17 [reroll] (backup: pr_farm17.bak_reroll.py, both box + BOREN-0)
- Reward screen: if best option ranks >= 80 (junk: unneeded potion 80, balls/lures 88, unneeded revive 90, TM/mushroom/mint 99) or every option is blacklisted, reroll when cost <= 20% of money. Money = scene.money, cost = handler.rerollCost (fallback phase.getRerollCost(lockModifierTiers)). Reroll via setRowCursor(0)/setCursor(0)+Z. Cap 5/wave. Logs `REROLL #n wX: cost/money` or `no reroll wX: cost/money`.
- Fix: TM teach-menu blacklist now adds last_pick (st.rew is empty in party UI) -> ended wave-46 TM046 Swift infinite loop.
- Heal-vs-Leppa ranking unchanged. Restarted same run at w49; ran w49->68 with no reroll needed (every screen had a useful item).

## 2026-10-29 10:06–10:15 MDT — farm17 [reroll+vit+balls+tier] (backups pr_farm17.bak_vit.py, pr_farm17.bak_tier.py, state.bak_tier.js; box + BOREN-0)
- Vitamins (HP Up/Protein/Iron/Calcium/Zinc/Carbos/"base stat") rank -30: below urgent heal (-40..-35), above Leppa (-20)/PP/Rare Candy. Word-boundary match, TMs excluded (first build matched "TM086 - Iron Tail" as Iron at 10:07 - fixed).
- Balls: Rogue/Master Ball rank 40; Poké/Great/Ultra rank 95 (junk -> reroll path if cost <=20% money, else last resort). Lure stays 88.
- Reward tier: state.js now reads modifierTypeOption.type.tier (0 COMMON,1 GREAT,2 ULTRA,3 ROGUE,4 MASTER). MASTER (-200) > ROGUE (-100) > everything, except Zacian <25% before a risky wave with a non-Rogue Full Restore/Max Potion offered. TMs/mints/mushrooms/splicers never get the tier bonus.
- Every REWARD log now shows tier=... and full ranking=[(rank,name,tier)...].
- Restarted same Classic run 10:06 (PID 33248) at w79, then 10:10 (PID 52396) at w98. w98->113 by 10:14 with tiers reading live (Super Lure GREAT, Egg Voucher GREAT, berries COMMON). No ROGUE/MASTER offer or reroll seen yet.

## 2026-10-29 10:2x MT — farm17 ranking: vouchers up, Tera Shards junk
- Tera Shards rank 97 (below common balls 95, above TM 99); >=80 triggers reroll if <=20% money.
- Any "voucher" item ranks -50: below ROGUE/MASTER (-100/-200), above heal (-40), vitamins (-30), Leppa (-20), PP (-10). Critical-heal exception kept (Zacian <25% before risky wave with Full Restore/Max Potion offered).
- Backup: pr_farm17.py.bak_vouch_tera. py_compile OK. NOT restarted: Zacian fainted w115 at 10:15:30 MT (Clefable Unaware) before patch; farm17 logged DONE.

## 2026-10-29 11:00–11:04 MDT — farm17 [ME release prompt] (backup pr_farm17.bak_mesum.py on BOREN-0)
- Stall w19: Pokémon Salesman ME bought Nickit with a full party -> "Release a Pokémon to make room?" prompt (Summary/Pokédex/Yes/No). Bug: `h == "OptionSelectUiHandler" and ph in (...) or "Mystery" in ph` precedence sent Z to every handler in a Mystery phase, so default "Summary" opened over and over.
- Fixes: parenthesized that condition (SummaryUiHandler now falls to stray-menu X back); ME watchdog presses X in Summary/Pokédex instead of Up+Z; OptionSelect whose first label is "Summary" with a "No" option -> pick No (keep the luck party). Option-select logs now list labels.
- Restarted same run 11:02:59 (PID 129868) at w19; prompt answered No, party unchanged, reached w22 by 11:03:38, Zacian full HP.

## 2026-10-29 12:45 MT — shiny-enemy stopper (pr_farm17.py; backup pr_farm17.bak_shinystop.py)
- On every poll in Command/Fight/TargetSelect/Ball UI, if any enemy on field has `shiny` true (both slots in doubles, trainer or wild):
  log `SHINY ENEMY: <species> wave <n> slot <k>`, save PNG to pokerogue_battle_shots\shiny_enemy_w<n>_*.png,
  write status.json (stopped_reason=shiny_enemy, shiny_species, shiny_slot, wave), create stop flag, exit with no key press.
- Runs before the old wild-shiny auto-ball branch, so that branch is now unreachable (manual handling by Gavin).
- Verified live w91/w106: party shiny partners true, Zacian false, enemies Gogoat/Tentacruel false.

## 2026-10-29 12:58 MT — Desktop control app
- C:\Users\gavin\agent-tools\PokeFarmControl\PokeFarmControl.pyw (tkinter, pythonw), shortcut Desktop\"PokéRogue Farm.lnk".
- RUNNING/STOPPED via python procs with pr_farm in cmdline (3 s refresh); wave/HP/ts/stopped_reason (shiny_enemy highlighted); log tail.
- STOP: stop flag + pokerogue_farm_stop_reason.txt "user_stop <ts>", waits 8 s, then taskkill /F. START: refuses double-launch, confirms on shiny/faint, clears flag+reason, launches python -u pr_farm17.py detached (UTF-8, cwd %TEMP%\prfarm).
- Farm found stopped: real Zacian faint w125 (mystery encounter top option). Not restarted; flag + reason zacian_faint written.

## 2026-10-29 1:05 PM MT — revive patch (backup pr_farm17.bak_revive.py)
- Zacian faint no longer quits if any partner is alive; keeps fighting with active mon.
- Reward rank: Revive/Max Revive/Sacred Ash = -50 (top) while Zacian is at 0 HP; revive target forced to Zacian.
- Still stops when the whole party is down. Note: ME "top option" KO'd Zacian at w125 — risk noted, unchanged.

## 2026-10-29 13:12 MT — wild-only shiny stop
- state.js: o.btype=battleType; o.trainer = !!cb.trainer || battleType===1.
- pr_farm17.py: shiny-enemy STOP now skipped when st.trainer; logs "trainer shiny ignored: <species> wave n" once per wave. Backups: pr_farm17.bak_wildshiny.py, state.bak_wildshiny.js.
- Verified live: w145 rival Finn (bt=1, trainer) shiny Rayquaza ignored; w154 wild Golem bt=0 trainer=false. Run continued 145->154.

## 2026-10-29 13:27–13:40 MT — new run #N
- Old run already over at w165 (Zacian faint 13:24:43, G-Max Copperajah). Zacian candy 16->4, bought 2 eggs (6 candy each).
- Gacha Shiny UP! (gachaCursor 2): 10 common (x10 pull) + 6 rare (x1 5-pull each) -> 40 eggs. Eggs 0->42. Frames gacha2_*.
- newrun.py fixes (PC; backup newrun_bak2.py): New Game index looked up by label (title has no Continue after a finished run); Start cursor reached by pressing right until startCursorObj visible.
- New Classic slot 3, party Zacian+5 shiny partners, luck 14. farm17 PID 63700 launched 13:39; w15 by 13:42.

## 2026-10-29 13:51 MT — mecancel
- OptionSelect in Mystery phases (or any >=3-option list with Cancel): strip color tags, pick Cancel instead of default (stops bug-move teach loop at w44).
- Loop guard: same phase+options seen >3 times -> pick last option.
- Backup: pr_farm17.bak_mecancel.py

## 2026-10-29 ~2:05 PM MT — ME party-transform guard (backup pr_farm17.bak_mexform.py)
- w68 Weird Dream (encounterType 23, mysteryEncounters/weirdDream) top option transformed whole party. Reloaded, picked "Quickly Leave" (party kept, levels reduced).
- MysteryEncounterUiHandler: blocklist (weirdDream key/"weird dream" text) -> last option; any ME whose visible text mentions transform/replace your/change your pok/your team will/swap your -> last option. Logs key/type.

## 2026-10-29 14:22–14:37 MDT — Zacian switch-in + new run
- Patch (backup pr_farm17.bak_switchin.py; Gavin OK card t27s3): CommandPhase, Zacian alive & off field, HP>=50% (or >0 if active <25%), active mon is weakest field slot (doubles), not trapped (isTrapped), once per (wave,turn,fieldIndex), max 2 tries/wave -> command cursor 2 (Pokemon), party UI CommandPhase -> Zacian slot, SEND_OUT. SwitchPhase/SwitchSummonPhase now prefers Zacian if alive off field. CheckSwitchPhase confirm -> Yes when Zacian >=50% off field.
- Old run ended w114 at 14:18:27 (whole party down, Torkoal) before patch could run live; switch-in not yet exercised live.
- Gacha Shiny UP!: 5 common vouchers (x1 pulls) -> 5 eggs. Zacian candy 15->3, 2 eggs. Eggs 0->7.
- New Classic slot 3, party Zacian/Yamper/Zigzagoon/Kricketot/Rattata/Nosepass, luck 14. farm17 PID 127040 launched ~14:34; w22 by 14:37.

## 2026-10-29 14:50–14:54 MDT — manual shiny catch w31
- Farm stopped 14:39 on wild shiny Tirtouga (w31, single, wild). Caught with 1 Rogue Ball (Rogue Balls 5->4), declined party release (No), party unchanged.
- Note: tab hidden -> AttemptCapturePhase looks frozen; manual frame stepping (STEP_JS) needed. Added %TEMP%\prfarm\step.py (steps frames until a UI handler) for manual takeovers.
- Cleared stop flag + stopped_reason; farm17 restarted PID 141292 at 14:54, w32 by 14:54.

## 2026-10-29 ~3:05 PM MDT — manual catch: wild shiny Dwebble (wave 40)
- Boss with 2 shield segments. Used Spirit Break (75 power, neutral vs Bug/Rock): 75 -> 38 HP, shield broken (bossSegmentIndex 0).
- 1 Rogue Ball thrown, caught. Release prompt -> No (sent to storage). Party unchanged.
- Rogue Balls 4 -> 3. Driven through game handlers via new helper %TEMP%\prfarm\jsq.py (runs a JS expression after HOOK/STEP).
- Flags cleared, pr_farm17.py restarted (PID 169328), advanced to wave 41.

## 2026-10-29 15:19 MDT — bak_memissing: ME battle limits party
- Backup: pr_farm17.bak_memissing.py (PC).
- When Zacian is absent from the party read AND `scene.currentBattle.mysteryEncounter` is set AND some party member has HP>0 (e.g. Expert Pokémon Breeder), skip the 30s "ZACIAN MISSING" stop; press Z on Command/Fight/Message/ModifierSelect/ME/Party handlers to fight with the active member. Logs "ME battle limits party". Real faint / run-end logic unchanged (only applies when Zacian is not in the party at all).

## 2026-10-29 15:23–15:32 MDT — manual catches w70 Aurorus, w71 Piloswine
- w70 wild shiny Aurorus (boss, 2 segments): one Bitter Blade broke the shield (212 -> 106), 1 Rogue Ball caught it. Release prompt (Summary/Pokédex/Yes/No) -> No; party unchanged. Keyboard X did not close the SummaryUiHandler opened from that prompt; handler.processInput(6 = CANCEL) did, then setCursor(3)+processInput(4) picked No.
- Farm restarted, then stopped at once on wild shiny Piloswine w71. Another actor (parallel key.py/restart) handled that one concurrently: Rogue Balls 2 -> 1, dex shows shiny Piloswine caught, farm17 relaunched PID 169268 at 15:31:52, w73 by 15:32.
- Note: only 1 Rogue Ball left; the next wild-shiny catch may run out. key.py now also supports 'x'.

## 2026-10-29 ~3:27-3:32 PM MDT — manual shiny catches (w70, w71)
- w70 wild shiny Aurorus Lv55 (Rock/Ice), 2 boss segments, 212 HP. One Zacian hit (Bitter Blade, neutral; the move was already selected when Fight was opened) did 106 dmg (212->106), which broke the shield. Caught with 1 Rogue Ball. Release prompt: No. Party unchanged.
- w71 wild shiny Piloswine Lv47, no shield. Caught with 1 Rogue Ball, no attack. Release prompt: No.
- Gotchas: jsq.py also runs STEP_JS, so it advanced the release prompt into Summary. Use the new read-only jsr.py (HOOK only) during manual catches. SummaryUiHandler got stuck with transitioning=true; fixed by setting transitioning=false and calling processInput(6). Picked No with setCursor(idx of 'No') + processInput(5).
- Rogue Balls left: 1 (Poké 10, Master 0). Farm restarted with PID 169268.

## 2026-10-29 15:38 MT - bak_abilityteach
- ME ConfirmUiHandler: if the message mentions teach/ability/surge/learn, answer No (cursor 1). Before this it picked Yes and got stuck in a "stray party UI in PostMysteryEncounterPhase" loop (Electric Surge ability offer, wave 88).

## 2026-10-29 15:52 MT — GTS -> leave
- Added "globaltradesystem" to BLOCK_ME in pr_farm17.py (backup pr_farm17.bak_gts.py). Before this, the farm picked the top option (trade a Pokemon), cancelled the species list and looped forever at w123. Now the GTS picks Leave; item trades are done by hand.

## 2026-10-29 3:53–3:55 PM MDT — manual catch: wild shiny Gengar (wave 124)
- Single wild, not a boss (Lv89, 224 HP). Rogue Ball 1 broke free (Gengar hit Zacian 343->313); Rogue Ball 2 caught it. Release prompt -> No; party unchanged.
- Rogue Balls 16 -> 14. Flag/stop_reason cleared, stopped_reason nulled, pr_farm17.py restarted (PID 116656); w126 by 3:55.

## 2026-10-29 15:56 MT — auto item transfer to Zacian (x1 waves)
- Backup pr_farm17.bak_transfer.py. Added XFER_JS + xfer_done: on ModifierSelectUiHandler, once per wave, if the Transfer button is visible (x1 waves), moves every transferable held item from Linoone/Zigzagoon/Boltund/Yamper to Zacian (speciesId 888) via scene.tryTransferHeldItemModifier (the function the Transfer UI uses); skips items Zacian is already maxed on; logs "TRANSFER wN: {...}". No party-menu keys. py_compile OK. NOT yet verified live.

## 2026-10-29 16:10 MT — fix Zacian item transfer (pr_farm17.py)
- Root cause: XFER_JS gated on `transferButtonContainer.visible`, but the game only shows that button ~0.5s after reward-card animations finish (and only when the party holds transferable items); the script checked immediately on entering ModifierSelectUiHandler, saw it hidden, and silently skipped (no log). Not tied to wave%10.
- Fix: gate on `scene.currentBattle.waveIndex % 10 === 1` instead; Zacian found by speciesId 888; sources Linoone/Zigzagoon/Boltund/Yamper; uses scene.tryTransferHeldItemModifier; skips items Zacian is maxed on; one attempt per wave (no loops); always logs `TRANSFER w<x1>`.
- Backup: pr_farm17.bak_transfer2.py. Dry-run detection verified at w146 (14 items found, Soothe Bell skipped as max).

## 2026-10-29 16:13–16:26 MDT — new run setup (slot 3)
- Shiny UP! gacha: 10 regular (one x10 pull), 3 Plus (5 each), 2 Premium (10 each) -> 45 eggs (0 -> 45). Vouchers now 0/0/0/0.
- Zacian candy 17 -> 5, bought 2 Zacian eggs. Total eggs 47.
- newrun.py 3 --party 888,835,263,401,19,299: New Game Classic, luck 14, slot 3.
- pr_farm17.py PID 67272 launched 16:22. TRANSFER w11 verified: Yamper Liechi Berry moved to Zacian (Zacian now Lum x1, Liechi x2).

## 2026-10-29 16:31–16:34 MDT — watch run: wild shiny Machop w31 (double, with Diglett)
- Watch routine started handling the catch, then found stop_reason.txt = "manual catch" (written 16:31:46 by another session) with moves being picked between its calls. Stopped sending input to avoid two controllers.
- Inputs the watch run sent before backing off: one Z (Fight; Earthquake got committed for Zacian), one X (back to Command, cancelled the EQ), one Command processInput(ACTION). Last seen state: Zacian Bitter Blade targeting Diglett, TargetSelect open. Nothing caught/KO'd by this run.
- Note: key.py keypresses appear to register twice (one Z went Command -> Fight -> move submit); prefer handler.processInput for manual catches.

## 2026-10-29 16:40 MT – manual w31 Diglett/Machop (t39u/t40u)
- Shiny Machop (wild double). Diglett KO'd by Zacian Bitter Blade (single target); Yamper Tail Whip. Note: key-driven Fight menu queued Earthquake by mistake (cancelled with X); use CommandPhase.handleCommand(0,idx) instead.
- Machop caught w/ 1 Rogue Ball (10->9), release prompt -> No. Declined Hyper Fang/Rest learn prompts.
- Took PP Max on Mighty Cleave (5->8). Wave 32 start: uiInputs.buttonMenu() -> Save and Quit -> title. Farm NOT restarted; stop flag + user_stop.


## 2026-10-29 17:17–17:22 MDT — watch run: run ended at wave 110 (slot 2), restart blocked
- Whole party fainted at w110 Power Plant (trainer battle, Zebstrika/Rotom left). Zacian fainted 17:01:53; farm logged DONE. Game sitting on "Raticate fainted!" message, sessionSlotId 2.
- Note: this w110 run was in slot 2 (loaded ~16:57 by another session); slot 3 still holds the w32 run saved at 16:40.
- Every game-input Shell call (cdp.py z) failed Auto-review with a classifier error (4 tries); reads worked. No input sent, nothing spent, farm not restarted.

- 2026-10-29 17:29 MDT (watch): w49 Expert Pokémon Breeder ME limited party to Linoone; Linoone fainted, so me_live (required an alive member) went false and the script stopped on "ZACIAN MISSING 30s+". Patched pr_farm17.py so me_live only checks currentBattle.mysteryEncounter (keeps pressing Z through the ME loss). Backup pr_farm17.bak_mefaint.py. Restarted; reached w50 with Zacian switched back in.

## 2026-10-29 17:41–17:45 MDT — watch run: wild shiny Araquanid w74 (slot 3), catch blocked
- Farm stopped itself 17:35:08 on shiny_enemy Araquanid (single wild, not a boss, Lv49, 140/140 HP). Game idle in CommandPhase, Zacian 216 HP. Balls: Poke 5, Great 5, Ultra 0, Rogue 14, Master 2.
- Every game-input Shell call (CommandPhase.handleCommand(1,3) Rogue Ball throw) failed Auto-review with a classifier error (3 tries). Reads worked. No input sent; flag left set; handed off to parent.

## 2026-10-29 18:30 MT — pr_farm17 Feebas + berry rules (backup: pr_farm17.bak_feebas.py)
- Soothe Bell -> Feebas first (party name "Feebas"); if apply fails/max, one retry on Zacian per wave (fb_fall).
- Rare Candy -> Feebas only when present; otherwise unchanged.
- Lure/Super Lure/Max Lure rank -15 when Feebas in party (below Master/Rogue tier, vouchers, vitamins, Leppa; else 88).
- Shiny prompt (Summary/.../No): party <6 and "Yes" offered -> Yes (join); else No (storage).
- Berries: any higher-tier non-berry outranks a berry. Berries targeted to Zacian only if a party member has Pickup (PICKUP_JS); else default target. Can't-take skip/blacklist unchanged.
- Startup log: "FEEBAS rules active: feebas_in_party=<bool> berry_rule pickup_present=<bool>".

## 2026-10-29 18:50 MT — candy/roles/eviolite/freeze-dry/PP items (backups: pr_farm17.bak_candyjar/.bak_roles/.bak_eviolite/.bak_freezedry/.bak_ppitems.py, state.bak_roles.js, state.bak_freezedry.js)
- Candy Jar / Rare Candy rank -55 (below Master -200/Rogue -100, above vouchers -50). Rare Candy still targets SECONDARY.
- ROLES: PRIMARY=("Zacian",{888}), SECONDARY=("Feebas",{349,350}) resolved by species (state.js party now has `sp`). Replaces Zacian/Feebas lookups in pick_reward, main loop z, Soothe Bell/Rare Candy/lure targeting.
- ROLE REVIVE: a role mon fainted -> Revive/Max Revive/Sacred Ash rank -300 (above Master); target primary first, else secondary.
- ROLE HEAL: role mon <60% -> heal items rank -45..; target secondary if it's lower and primary isn't <60%.
- EVIOLITE: rank -54 while SECONDARY is Feebas (349); applied to SECONDARY; log "EVIOLITE -> <name>".
- FREEZE-DRY: state.js effs use game e.getMoveEffectiveness(user,mv,false,true) for damaging moves, with fallback x4 for move 573 vs Water(11); log "FREEZE-DRY vs ... eff=".
- PP items (Ether/Elixir/Max): rank 94 unless pp_crit (damaging PP total <=3, or all SE moves at 0) -> -10. Leppa -20 only if PP low/critical, else 30. Logs "PP item skipped (pp ok)" / "PP item taken (critical)".
- 18:52 MT: PRISM SCALE (rank -290, -> SECONDARY while Feebas; evolution proceeds via default Z) and SWORD (Rusted/Ancient Sword rank -290 -> PRIMARY). Backups pr_farm17.bak_prism.py, .bak_sword.py.

## 2026-10-29 19:36 MT — proactive shop (backups pr_farm17.bak_shop.py, state.bak_shop.js)
- Config: SHOP_MAX_SPEND_FRAC=0.5, SHOP_RESERVE_FRAC=0.25, SHOP_MIN_RESERVE=0, SHOP_HURT=0.85.
- On each ModifierSelect screen, before the free reward: shop_plan() checks PRIMARY then SECONDARY: fainted -> Max Revive/Revive; status (state.js party `stt`) -> Full Restore if hurt else Full Heal; HP<85% -> cheapest right-sized potion.
- Buys via the game UI: setRowCursor(r)/setCursor(c) on shop row (r = L-k+1 for shopOptionsRows[k]), verify item name under cursor, Z; PartyUi target forced to the role mon (shop_tgt).
- Money confirmed after: log "SHOP BUY (proactive) <item> -> <mon> cost= money=a->b cap="; not charged -> fail count, 2 fails/wave or cursor mismatch -> shop off for that wave; max 8 buys/wave.
- Free-reward and PP-item logic unchanged. Non-role mons are not shopped for.

## 2026-10-29 19:42 MT — PP conserve in pick_move (backup pr_farm17.bak_ppconserve.py)
- PP_CONSERVE_ABS=5, PP_CONSERVE_FRAC=0.34. If the top-scored damaging move is low (left<5 or <34% max), pick the best non-low alternative with score >=0.5x top and effectiveness >= top/2. Keep the low move if it's the only SE move while all others are resisted, or if every alternative is low. Log "PP CONSERVE skip <move> (l/m) -> <chosen>". Applies to every user (Zacian, Milotic, others). 0-PP skip and game effectiveness unchanged. No KO-finish exception (no existing KO logic).

## 2026-10-29 19:46 MT — rerolls (backups pr_farm17.bak_cheapreroll.py, .bak_rerollbudget.py)
- REROLL_CHEAP_FRAC=0.10, REROLL_CHEAP_MAX=3. Order on reward screen: shop buys -> reroll decision -> free reward.
- (a) cheap: cost <10% money and no high-value pick (rank <=-35: tier Rogue/Master, vouchers, candy, revive-needed, prism/sword, eviolite, needed heal; or pp_crit PP item).
- (b) nothing>ultra: no Rogue/Master offered and nothing on the want list (also vitamins, rank <=-30).
- Cumulative budget: reroll_spent + next cost <= 10% of money at screen open, for both rules; shop reserve floor kept; max 5 rerolls/screen. Logs "REROLL cheap ...", "REROLL nothing>ultra ...", "REROLL budget stop spent= next= budget=". Old 20% rule replaced.
- 19:46 MT: REROLL_DECAY=0.6: a qualifying reroll is taken with p=0.6^n (n = rerolls already taken this screen); log "REROLL decay skip n= p=". Backup .bak_rerolldecay.py.

## 2026-10-29 19:48 MT — hard waves + significant-wave journal (backup pr_farm17.bak_hardwaves.py)
- HARD_WAVES_BASE={8,25,55,95,165,195} merged with learned_hard from C:\Users\gavin\agent-tools\pokerogue_significant_waves.json.
- Reward screen: next wave hard if in HARD_WAVES, gameMode.isFixedBattle, gameMode.isWaveTrainer, or %10==0 -> log "HARD WAVE NEXT n (reasons) -> pre-heal"; shop heals role mons below 99% (status/faint too), spend cap 0.75 (reserve floor unchanged).
- Journal: on CommandPhase of a trainer or boss wave, log "SIG WAVE n name" and keep a record; on WAVE UP append it to pokerogue_significant_waves.jsonl (run_id, wave, biome, trainer/type, bosses, is_rival, fixed, outcome, Zacian/secondary HP before/after, min role ratio). The .json summary holds wave_tally, records, learned_hard (trainer waves where a role mon fell below 50%).

## 2026-10-29 20:02 MDT — SECFIELD + CANDY_TARGET + live config (backup pr_farm17.bak_secfield.py)
- New config: CANDY_TARGET ('secondary' default | 'primary' | 'both' alternating per picked Soothe Bell/Rare Candy; failed/max falls back to other role mon).
- New config: SECONDARY_FIELD ('auto' default | 'bench' | 'field'). Singles only: CommandUi -> Pokémon -> Feebas on first CommandPhase of the wave, then existing ZACIAN SWITCH-IN brings Zacian back. Skips: hard waves (base+learned), boss, Zacian<50%, Feebas<50% (field) / <40% (auto), shiny enemy, trapped; auto also skips trainer + fixed waves (x10 allowed). Max 1 success/wave, 2 tries/wave, party-UI stuck >=4 -> give up wave. Auto: 2 Feebas faints while fielded -> bench rest of run.
- Live config file C:\Users\gavin\agent-tools\pokerogue_farm_config.json, re-read every wave ("CONFIG change ..." log).
- Control app: Bench/Field/Auto and Primary/Both/Secondary toggles above START/STOP, writes the config JSON (backup PokeFarmControl.bak_toggles.pyw). No popups.
- Verified w47: "SECFIELD w47: Feebas in" -> "Zacian back".

## 2026-10-29 20:10 MDT — Soothe Bell priority + label rename (backups pr_farm17.bak_soothe.py, PokeFarmControl.bak_label.pyw)
- Soothe Bell reward rank -99.5: just below Rogue/Master tier, above Candy Jar/Rare Candy (-55), vouchers, vitamins. Not a money-shop item, so no shop change.
- Soothe Bell always goes to the secondary first, falls back to Zacian if it fails or is maxed, whatever CANDY_TARGET says. CANDY_TARGET now governs Rare Candy only.
- Label "Feebas in singles" renamed to "Secondary in singles" (control app + log strings). Species matching unchanged.

## 2026-10-29 20:12 MDT — Potion spend cut (backup pr_farm17.bak_potion.py)
- Cause: proactive heal buys (SHOP_HURT 0.85). Wave 19-66 log: 21 buys, 4,831 total, mostly Potion/Super Potion for chip damage. Worst screens: w64 3 buys 1,350; w46 2 buys 1,059; w66 2 buys 928.
- No reward was ever displaced: a buy doesn't use up the free pick, and picking the reward closes the screen. Reroll budget is 10% of money at screen open, so buys did not starve it.
- SHOP_HURT 0.85 -> 0.75 outside hard waves. New SHOP_MIN_MISS_FRAC 0.15 skips tiny missing HP (non-hard). Per-screen heal spend cap 50% -> 25%. 25% reserve kept. Reroll 50% screen cap decoupled (unchanged).
- Unchanged: hard-wave pre-heal (75% spend, heal below 99%), revives for fainted role mons, Full Heal for status, cheapest heal that covers the missing HP.
- Verified: w74 Soothe Bell picked at rank -99.5 and given to Milotic (slot 1).

## 2026-10-29 20:32 MDT — X items/lure junk, secondary only-candy, berries->Zacian, shop fix, hidden launch (backup pr_farm17.bak_xlure.py)
- Battle items: X Sp. Atk/Sp. Def/Accuracy rank 96. X Attack/Defense/Speed and Dire Hit rank 93. If the best option ranks 93 or worse -> "REROLL junk" (shared 10% budget, max 5 per screen, 0.6^n decay, reserve). Berry rule no longer lifts a berry above battle items.
- Lure: -15 while the secondary is in the party (unchanged). If a DoubleBattleChanceBooster is already active (LURE_JS) -> rank 96 junk. Log "LURE active (N left) -> skip" / "LURE none active -> rank -15".
- Secondary gets ONLY Rare Candy/Candy Jar. Every other party-target item, including Soothe Bell, goes to Zacian, or is skipped if Zacian can't take it. Eviolite is now rank 96 junk.
- Exception constants: SEC_ALLOW_PRISM=True (TEMP), SEC_ALLOW_REVIVE=True (TEMP), SEC_ALLOW_HEAL=True. Heal threshold for the secondary is 75%.
- Berries -> PRIMARY. If Zacian can't take a berry it is skipped, no fallback to the secondary. Leppa unchanged.
- Rare Candy: no root bug in the current build. Zacian cases were 18:00-18:29 only, on the old build before the Feebas rule. Since 18:30 all went to Feebas/Milotic. Hardening: a shop target can no longer override a Rare Candy target. The fallback log now names the item.
- Shop: role mons are healed lowest-HP% first, fainted first. A mon whose buy came back "not charged" is skipped for the rest of the wave, so it is not retried into fail #2.
- HIDDEN LAUNCH (use for every restart; no cmd/conhost, so no console window):
  Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine='"C:\Users\gavin\AppData\Local\Programs\Python\Python310\pythonw.exe" "C:\Users\gavin\AppData\Local\Temp\prfarm\pr_farm_launch_hidden.py"'; CurrentDirectory='C:\Users\gavin\AppData\Local\Temp\prfarm'}
  pr_farm_launch_hidden.py sets PYTHONIOENCODING/PYTHONUTF8, chdir, and redirects stdout/stderr to agent-tools\pokerogue_farm_stdout.txt in-process, then runs pr_farm17.py. The name contains "pr_farm", so the control app detects it.
  Restart sequence: stop flag "patch_restart" -> wait for exit -> rotate stdout -> clear flags -> launch the command above.

## 2026-10-29 20:34 MDT — control app config sync
- Bug: the app kept toggle values in memory from when it opened. Clicking any toggle rewrote BOTH settings, so a stale "auto" overwrote the Bench set at 20:23 (log: 20:25:56 bench -> auto).
- Fix: refresh() re-reads pokerogue_farm_config.json every 3 seconds and syncs the radio buttons (backup PokeFarmControl.bak_cfgsync.pyw). secondary_field is set back to bench (20:34:16). App relaunched hidden as pythonw PID 44856.

## 2026-10-29 20:40–20:44 MDT — watch run: manual catch wild shiny Horsea w45
- Farm stopped 20:35:25 on shiny_enemy Horsea (single wild, Lv27, not a boss). Rogue Balls 0, so threw 1 Poke Ball (25->24) via CommandPhase.handleCommand(1,0): caught. Party was 2, so it joined automatically (no prompt); party now Zacian/Feebas/Horsea.
- Gotcha: PowerShell strips double quotes from python args; use single quotes only in jsr.py JS. Capture message needs handler.processInput(5) after step.py.
- Cleared flag/reasons, rotated stdout, launched hidden (PID 98024). It cleared w46 (Training Session ME took Feebas; Feebas fainted), then at 20:42:58 the page reloaded and the control app (pythonw 44856) did STOP + START at 20:43:00/20:43:14 -> farm now PID 42844 "python.exe -u pr_farm17.py" (control app launch, not the CHANGELOG hidden launcher). Not mine; left alone. Farm healthy at w49, Feebas back at 61/64 after reload.

## 2026-10-29 20:53 MDT — Secondary locked to bench + party order fix (backups pr_farm17.bak_lead.py, PokeFarmControl.bak_lock.pyw)
- Root cause of the Milotic/Zacian swaps: the config was toggled to field/auto (20:25, 20:48), and SECFIELD switched Milotic in. PokeRogue's in-battle switch also swaps party positions, so the order got shuffled across the 4-5 member party. That gave "Zacian slot 2" and wave-start switch-ins.
- SECFIELD_FORCE_BENCH=True overrides the config file. Startup logs "SECFIELD forced bench=True".
- PARTY_ORDER_FIX=True: once per reward screen (SelectModifierPhase only), REORDER_JS restores the order Zacian, Milotic/Feebas, then others via a JS array reorder, with no key input. Logs "PARTY ORDER wN: before -> after".
- Control app: the Secondary row only offers "Bench (locked)", and the app always writes secondary_field=bench.

## 2026-10-29 21:45–21:58 MDT — DONE (watch run): run ended w145, end-of-run procedure + new run slot 2
- Whole party fainted at w145 (Rival, Rayquaza/Metagross team). Farm exited 21:43:10 "ZACIAN FAINT ... DONE farm17".
- Patch (backup pr_farm17.bak_shopretry.py): shop buys kept failing "not charged" on the first Z press (81 fails today; Zacian never got a Max Revive at w140/w144). A mon is now skipped only after 2 failed buys on that wave, shop gives up after 4 fails (was 2), and the wait after pressing Z on a shop item is 1.2 s (was 0.6 s).
- Shiny UP! gacha: 30 regular + 4 Plus vouchers -> 50 eggs (0 -> 50). Vouchers now 0/0/0/0.
- Zacian: no candy upgrades left to buy (passive and cost reductions already owned). Bought 2 Zacian eggs, candy 13 -> 1. Eggs 52.
- Feebas: passive already owned; next upgrade "Reduce Cost to 2" costs 40, only 36 candy, so nothing bought. No Feebas eggs.
- New Classic run in slot 2 (was the ended run's slot, now Empty; slots 0/1 occupied, untouched), party Zacian 888 + Feebas 349. Done by hand with the new gx.py (JS-only helper: st, p:<button>, s:<frames>, js:<expr>), because cdp.py hangs on captureScreenshot while the tab is hidden, so newrun.py would hang too. Start in starter select = processInput(4) (SUBMIT -> tryStart).
- Farm launched hidden via the CHANGELOG launcher (pythonw PID 25160, parent WmiPrvSE, no console). w4 by 21:58.

## 2026-10-29 22:17–22:19 MDT — watch run: caught wild shiny Pineco w43
- Farm stopped 22:13:43 on shiny_enemy Pineco (single wild, Lv27, not a boss). Threw 1 Rogue Ball via handleCommand(1,3) (Rogue 5->4): caught first try. Party was 2, so it joined automatically; party now Zacian/Feebas/Pineco.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 42488, parent WmiPrvSE). Advancing: w45 (double) by 22:19.

## 2026-10-29 22:25–22:27 MDT — watch run: Memory Mushroom loop fix (backup pr_farm17.bak_mushroom.py)
- Stall since 22:19:55 at w46 reward: both TMs blacklisted, only Memory Mushroom left; its relearn-move list (Noble Roar, Laser Focus...) looped "party opts ... -> 0" every ~13 s for 6 min.
- Fix: the TM teach-menu skip now also fires when last_pick is Memory Mushroom (blacklist + X out). With all rewards blacklisted the existing "no reward options - X + confirm skip" path takes over.
- Stopped via flag patch_restart, rotated stdout, cleared flags, launched hidden via the CHANGELOG launcher (pythonw PID 119060, parent WmiPrvSE). w46 skipped cleanly 22:26:49, w47 fighting by 22:27.

## 2026-10-29 22:33–22:41 MDT — DONE (watch run): run ended w50, end-of-run procedure + new run slot 2, then Gavin STOPPED
- Whole party fainted at w50 (Zacian to Crustle; Feebas, then Forretress Self-Destruct vs Accelgor). Farm exited 22:31:18 "DONE farm17".
- Shiny UP! gacha (gachaCursor 2): 2 regular vouchers, single pulls -> eggs 3 -> 5. Vouchers now 0/0/0/0.
- Zacian: passive + max cost reduction already owned; 3 candy, too few for an egg. Nothing bought.
- Feebas: next cost reduction 40, only 39 candy. Nothing bought.
- New Classic run in slot 2 (Empty; slots 0/1 occupied Endless saves, untouched), party 888+349, by hand with gx.py (buttons: 0 up,1 down,4 submit,5 action,6 cancel; Feebas idx 171, Zacian idx 459 in filteredStarterIds).
- Launched hidden via CHANGELOG launcher (pythonw PID 81832). Cleared w1, then 22:40:18 Gavin pressed STOP in the control app (stop_reason.txt "user_stop"). Left stopped at w2.

## 2026-10-29 22:58–23:02 MDT — watch run: caught wild shiny Wiglett w31 (double, slot 2)
- Farm stopped 22:54:59 on shiny_enemy Wiglett (wild double with Mareanie, Lv18, not a boss). Rogue 0, Master 0.
- Zacian Mighty Cleave via handleCommand(0,1) + TargetSelect cursor 2 (Mareanie) -> KO; Feebas Calm Mind (no target, so no retarget onto Wiglett). Next turn handleCommand(1,0) Poke Ball (25->24): caught first throw. Party was 2, so it joined; party now Zacian/Feebas/Wiglett. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 65072, no console). Feebas evolved to Milotic; w33 fighting by 23:02.

## 2026-10-29 23:09–23:14 MDT — watch run: caught wild shiny Barraskewda w52 (double, slot 0)
- Farm stopped 23:06:12 on shiny_enemy Barraskewda (wild double with Dondozo, Lv31, not a boss). Rogue 0.
- Zacian Spirit Break + Milotic Freeze-Dry, both via handleCommand(0,2) + TargetSelect setCursor(3) (Dondozo) -> Dondozo KO. Next turn handleCommand(1,0) Poke Ball (29->28): caught first throw. Party was 3, so it joined; party now Zacian/Milotic/Wugtrio/Barraskewda. Logged in the CHIE shiny log.
- Gotcha: after the KO, pressing action (5) past the last message at CommandPhase opens Fight then target select; cancel (6) backs out to the command menu.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 87080). w54 fighting by 23:13.

## 2026-10-29 23:23-23:27 MDT - watch run: caught wild shiny Bombirdier w76 (mystery-encounter boss)
- Farm stopped 23:19:45 on shiny_enemy Bombirdier (Berries Abound ME boss, 2 segments). Zacian Bitter Blade broke the shield (175->88), Poke Ball first throw caught it; joined party (5th). Logged in CHIE shiny log.
- Cleared flag/reasons, rotated stdout, relaunched hidden via pythonw (PID 17084). w79 by 23:26.

## 2026-10-29 23:32-23:36 MDT - watch run: caught wild shiny Arcanine w83 (single, slot 2)
- Farm stopped 23:27:42 on shiny_enemy Arcanine (wild single, Lv59, not a boss). Rogue 5, Master 0.
- No attack. handleCommand(1,3) Rogue Ball (5->4): caught first throw. Party was 5, so it joined automatically; party now full (Zacian/Milotic/Wugtrio/Barraskewda/Bombirdier/Arcanine). Future shinies go to storage (No). Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via pythonw + pr_farm_launch_hidden.py (PID 152580, no console). Farm handled Arcanine's move-learn prompt; w86 fighting by 23:35.

## 2026-10-29 23:37-23:41 MDT - watch run: caught wild shiny Heatmor w89 (single, slot 0)
- Farm stopped 23:35:21 on shiny_enemy Heatmor (wild single, Lv63, not a boss). Rogue 4, Master 0.
- No attack. handleCommand(1,3) Rogue Ball (4->3): caught first throw. Party full, so the "release to make room" prompt (Summary/Pokedex/Yes/No) got No (cursor 3): Heatmor went to storage, party unchanged. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via pythonw + pr_farm_launch_hidden.py (PID 88492, no console). w95 (hard wave) by 23:40.

## 2026-10-30 00:18 MDT - Kricketot evo pause
- pr_farm17.py: every ~3s set pauseEvolutions=true on any party Kricketot (species 401), log "KRICKETOT evo paused (party idx N)"; fallback: Kricketot EvolutionPhase -> X cancel then Z Yes (pause). Backup pr_farm17.bak_krick.py.

## 2026-10-30 00:49–00:59 MDT — Gavin restart: abandon w118, eggs, new 5-mon run slot 2
- Stopped farm (flag gavin_restart, exited in 3s). Old Classic run slot 2 at w118 abandoned per Gavin (page reload via CDP, no Escape).
- Shiny UP! gacha: 15 regular (1 x10 + 5 x1), 2 Plus, 1 Premium -> 35 eggs (0 -> 35). Vouchers 0/0/0/0. In gx.py, the first processInput after setGachaCursor sometimes doesn't register; step frames (s:400) after each pull.
- Zacian: all upgrades owned; 2 eggs (6 each), candy 17 -> 5. Feebas: all upgrades owned (passive, cost reduction 2); 1 egg (12), candy 15 -> 3. Eggs 38.
- New Classic run slot 2 (overwrote the w118 save, authorized), party 888,349,263,327,401 (10/10 cost) by hand with gx.py; title->Menu->Egg Gacha; starter Use Candies menu.
- Launched hidden via CHANGELOG launcher (pythonw PID 49260). KRICKETOT evo pause active 00:58:03; w7 by 00:59.

## 2026-10-30 01:48 MDT — soothe2 (pr_farm17.py; backup pr_farm17.bak_soothe2.py)
- Soothe Bell: SEC_ALLOW_SOOTHE=True. Goes to secondary (Feebas/Milotic) until its SOOTHE_BELL stack hits getMaxStackCount() (=3), then Zacian. Exempt from secondary only-candy gate and shop target override. Logs `SOOTHE -> secondary X (n/max)` / `SOOTHE -> Zacian (secondary full n/max)`. Rank unchanged (-99.5).
- ME shadyVitaminDealer (by mysteryEncounter.localizationKey): pick option 2 (pricey) if meetsRequirements, else last option (leave); never cheap. Log `ME shady dealer -> pricey`.
- ME trainingSession (by localizationKey): always last option (leave). Log `ME training session -> leave`.
- Startup lines: `SOOTHE target=secondary-first ...`, `ME overrides: ...`. Kricketot evo pause untouched.

## 2026-10-30 02:39-02:57 MDT - watch run: run ended w200 (final boss E-Max Eternatus), end-of-run procedure + new run slot 2
- Farm exited 02:31:40 "ZACIAN MISSING 30s+ ... DONE farm17" after the w200 Eternatus fight (partners Spinda/Kricketot/Orbeetle switched in, then the game returned to the title; title shows New Game with no Continue). Whether it was a win or a wipe isn't confirmed from the log.
- Shiny UP! gacha (gachaCursor 2): 14 regular (1 x10 + 4 x1), 7 Plus, 2 Premium -> eggs 1 -> 70. Vouchers 0/0/0/0. Pattern: after each pull, one action press closes the result and the next press pulls.
- Zacian: no candy upgrades left (Use Candies only offers Buy an Egg x6). Bought 5 eggs, candy 33 -> 3. Eggs 75.
- Feebas: no upgrades left (only Buy an Egg x12), candy 27. Nothing bought.
- New Classic run in slot 2 (Empty; slots 0/1 Endless saves untouched), party 888+349, by hand with gx.py. Verified modeId 0 (Classic), wave 1, sessionSlotId 2.
- Cleared flag, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 71764, parent WmiPrvSE). w5 (Lass) fighting by 02:56.

## 2026-10-30 03:24–03:27 MDT — watch run: caught wild shiny Loudred w41 + shop buy fix (backup pr_farm17.bak_shopjs.py)
- Farm stopped 03:24:30 on shiny_enemy Loudred (single wild, Lv28, not a boss). Rogue Balls 0, so threw 1 Poke Ball via handleCommand(1,0) (Poke 5->4): caught first throw. Party was 2, so it joined; party now Zacian/Milotic/Loudred (PARTY ORDER fix restored Zacian to slot 1).
- Context: Zacian fainted w36 this run; every shop buy since then failed "not charged" (Revive/Full Heal/Potion, no party screen ever opened), so Zacian sat fainted until the w40 gym PartyHealPhase revived it. 276 "not charged" fails in the log overall.
- Patch: shop purchase now calls handler.processInput(5) (ACTION) directly instead of the Z key (falls back to Z if that returns false), then steps frames 6x0.2s. Not yet verified on a live shop buy.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 94592). w42 fighting by 03:27.

## 2026-10-30 04:06-04:12 MDT - watch run: caught wild shiny Muk w82
- Farm stopped 04:04:13 on shiny_enemy Muk (single wild, Lv54, not a boss). Rogue Balls 0, so threw Poke Balls via handleCommand(1,0) (Poke 24->20); caught on the 4th throw. No attack.
- Zacian (122/216) fainted to Muk during the 3rd throw; sent in Exploud (switch prompt) and kept throwing. Party was 3, so Muk joined: party now Exploud/Milotic/Zacian(fainted)/Muk. Farm's PARTY ORDER and ZREVIVE logic should restore and revive Zacian at the next shop. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 146988, parent WmiPrvSE). w84 fighting by 04:11.

## 2026-10-30 04:23-04:28 MDT - watch run: caught wild shiny Muk w89 (double)
- Farm stopped 04:16:03 on shiny_enemy Muk (wild double with Alolan Golem; Muk Lv65, not a boss). Catch can't be thrown with two foes up, so KO'd Golem with single-target moves: Zacian Spirit Break + Milotic Freeze-Dry (TargetSelect cursor 2 = Golem). Muk untouched (222/222).
- Rogue Balls 0, so threw 1 Poke Ball via handleCommand(1,0) (Poke 25->24): caught first throw. Party was 4, so it joined: Zacian/Milotic/Muk/Exploud(fainted)/Muk. Logged in the CHIE shiny log.
- Note: FightUiHandler setCursor(0) for Milotic didn't take (stayed 2 = Freeze-Dry); read back the cursor before confirming.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (pythonw PID 22728, not cmd/conhost). w90 fighting by 04:27.

## 2026-10-30 04:53-04:58 MDT - watch run: caught wild shiny Yungoos w12 (double)
- Farm stopped 04:48:57 on shiny_enemy Yungoos (wild double with Sentret; Yungoos Lv8, not a boss). KO'd Sentret with Zacian Spirit Break (TargetSelect cursor 3 = Sentret; field idx 2/3 = enemies); Milotic used Calm Mind so Yungoos stayed 28/28.
- Note: for Milotic, FightUiHandler.cursor stays at Zacian's value; read getCursor() (cursor2) to confirm the second mon's move.
- Rogue Balls 0, so threw 1 Poke Ball via handleCommand(1,0) (Poke 5->4): caught first throw. Party was 2, so it joined: Zacian/Milotic/Yungoos. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher with Win32_Process Create (pythonw PID 87008, parent WmiPrvSE). w16 by 04:57.

## 2026-10-30 05:42-05:46 MDT - watch run: caught wild shiny Xatu w81
- Farm stopped 05:36:30 on shiny_enemy Xatu (single wild, Lv55, not a boss). Rogue Balls 5, so threw Rogue Balls via CommandPhase.handleCommand(1,3) (Rogue 5->3): broke free once, caught on the 2nd throw. No attack.
- Party was full (6: Zacian/Milotic/Gumshoos/Lombre/Dusclops/Octillery), so chose No (option index 3) on the release prompt; Xatu went to storage. Note: pressing ACTION at cursor 0 opens Summary; move the cursor to No first. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher with Win32_Process Create (pythonw PID 104144, parent WmiPrvSE). w84 by 05:46.
## 2026-10-30 08:13-08:16 MDT - watch run: caught wild shiny Skeledirge w92, then saw manual control
- Farm stopped 08:09:10 on shiny_enemy Skeledirge (single wild, Lv67, not a boss). No attack. CommandPhase.handleCommand(1,0) Poke Ball (Rogue 0, Poke 35->34): caught first throw; party was 2, so it joined (3rd). A LearnMovePhase "replace with Close Combat?" prompt followed.
- Gotcha: PowerShell 5 strips embedded double quotes from native-exe args, so gx.py js: snippets with "..." silently return null. Use backtick template literals instead.
- About 20 s later the game was in SelectStarterPhase (party empty, page not reloaded, focused/visible, cursor moving between reads), so someone was driving it by hand. No further game input sent; farm NOT restarted. Stop flag left in place; status stopped_reason set to shiny_caught_then_manual_control. Whether the w92 run was saved with Skeledirge is unconfirmed. Logged in the CHIE shiny log.

## 2026-10-30 10:35 MDT
- Took over Gavin's manual five-mon Classic run (slot 2: Zacian, Feebas, Spinda, Zigzagoon, Kricketot). Farm pr_farm17.py PID 28964 already started 10:31 via control app; no second launch.


## 2026-10-30 11:01-11:07 MDT - watch run: caught wild shiny Sableye w79 (double)
- Farm stopped 10:56:41 on shiny_enemy Sableye (wild double with Mawile, Lv57, not a boss); game sat idle at CommandPhase until this run. Zacian Bitter Blade (handleCommand(0,3) + TargetSelect setCursor(3)) KO'd Mawile; Milotic Calm Mind. handleCommand(1,3) Rogue Ball (Rogue 14->13): caught first throw. Party full (6), so chose No on the release prompt (option index 3) and it went to storage. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher with Win32_Process Create.


## 2026-10-30 11:12-11:16 MDT - watch run: caught wild shiny Diggersby w87
- Farm stopped 11:08:18 on shiny_enemy Diggersby (single wild, Lv61, not a boss). No attack. handleCommand(1,3) Rogue Ball (Rogue 13->12): caught first throw. Party full (6), so chose No (option index 3) on the release prompt; it went to storage. Party unchanged. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher with Win32_Process Create (pythonw PID 143964, parent WmiPrvSE). w91 by 11:15.

## 2026-10-30 11:25-11:28 MDT - watch run: caught wild shiny Salamence w105
- Farm stopped 11:19:22 on shiny_enemy Salamence (single wild, Lv73, not a boss); game idle at CommandPhase. No attack. handleCommand(1,3) Rogue Ball: broke free once, caught on the 2nd throw (Rogue 12->10; Zacian took a hit, 141->75). Party full (6), so chose No (option index 3) on the release prompt; it went to storage. Party unchanged. Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout. Farm came back as one instance (python.exe PID 159872, parent the control app pythonw PokeFarmControl.pyw, no console); w109 by 11:27.

## 2026-10-30 11:32-11:38 MDT - watch run: run ended w114 (wipe), manual control seen, stood down
- Farm exited 11:30:14 "ZACIAN FAINT ... DONE farm17" at w114 (Crobat/Bronzong/Alakazam; whole party fainted). Game at title.
- Started run-end step 1: Title > Menu > Egg Gacha, setGachaCursor(2) Shiny UP!, one x1 press. Vouchers stayed 8/0/0/0 (that press didn't spend one).
- Meanwhile, 11:34:10-11:34:34, someone bought 3 Zacian eggs (candy 18 -> 0) and 2 Feebas eggs (25 -> 1) by hand (tab focused/visible, no script running, no reload), then left it at title, which now shows Continue. Treated as Gavin playing by hand: no further input, no new run. Status stopped_reason set to run_end_then_manual_control. Remaining: 8 regular vouchers, Zacian/Feebas upgrades all owned (passive 3, reduction 2), new five-mon run not started.

## 2026-10-30 12:05-12:10 MDT - watch run: caught wild shiny Florges w86 (double)
- Farm stopped 11:59:50 on shiny_enemy Florges (wild double with Ampharos, Lv64, not a boss); game idle at CommandPhase. Zacian Mighty Cleave (handleCommand(0,1) + TargetSelect setCursor(3)) left Ampharos at 2 HP, then Bitter Blade KO'd it; Milotic Calm Mind both turns. handleCommand(1,3) Rogue Ball (Rogue 15->14): caught first throw. Party had 5, so it joined automatically (6th, no prompt). Logged in the CHIE shiny log.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher with Win32_Process Create (pythonw PID 162720, parent WmiPrvSE). w89 by 12:10.

## 2026-10-30 12:44-12:49 MDT - watch run: caught wild shiny Varoom w40 (double boss wave)
- Farm stopped 12:43:48 on shiny_enemy Varoom (wild double with Koffing; Varoom Lv24 no shield). Zacian Mighty Cleave + Milotic Steam Eruption (setCursor(3)) KO'd Koffing. Gotcha: extra ACTION presses after the KO queued a Zacian attack on Varoom; Cancel (p:6) at Milotic's command undid it.
- Rogue Balls 0, Poke Ball (10 -> 9) caught first throw; party had 5, joined as 6th. Logged in CHIE shiny log.
- Control app relaunched pr_farm17.py itself at 12:48:06 (PID 137772); no second instance. w41 by 12:48.

## 2026-10-30 12:53-12:56 MDT - watch run: caught wild shiny Probopass w50 (boss, party full)
- Farm stopped 12:50:06 on shiny_enemy Probopass (wild single boss, Lv36, 2 segments). Two Zacian Mighty Cleaves broke the shield (97 -> 49 HP). Rogue Balls 0, Poke Ball (9 -> 8) caught first throw. Party full, chose No on the release prompt. Logged in the CHIE shiny log.
- Relaunched hidden (pythonw PID 135860, one instance). w52 by 12:56.

## 2026-10-30 13:47-13:51 MDT - watch run: caught wild shiny Scream Tail w196
- Wild single Lv168, no attack, Rogue Ball first throw (35->34), party full so No -> storage. Logged in CHIE shiny log. Relaunched hidden (pythonw PID 118352, one instance); w200 Eternatus by 13:49.

## 2026-10-30 13:54-14:09 MDT - watch run: run ended w200 (Eternatus), end-of-run procedure + new run slot 2
- Farm exited 13:51:39 at w200 vs E-Max Eternatus; game went to title, slot 2 empty. Win or wipe not confirmed from the log.
- Shiny UP! gacha: 17 regular (1 x10 + 7 x1), 6 Plus, 2 Premium -> eggs 0 -> 67. Vouchers 0/0/0/0.
- Zacian: no upgrades left; bought 4 eggs, candy 28 -> 4. Feebas: no upgrades left, candy 63. Eggs 71.
- New Classic run slot 2, party 888,349,327,263,401 by hand with gx.py. Verified modeId 0, wave 1, slot 2.
- Launched hidden (pythonw PID 87372, parent WmiPrvSE, one instance). w6 by 14:08.

## 2026-10-30 14:48-14:53 MDT - watch run: caught wild shiny Alakazam w88
- Farm stopped 14:45:20 on shiny_enemy Alakazam (wild single, Lv61, not a boss). No attack. Rogue Balls 0, so CommandPhase.handleCommand(1,0) Poke Ball (35->34): caught first throw. Party had 5, so it joined as 6th (Zacian/Milotic/Spinda/Linoone/Kricketot/Alakazam).
- The CHIE shiny log is now named "Shiny Log.md" (no "PokeRogue " prefix) in OTHER\POKEROGUE; row added there.
- Cleared flag/reasons, rotated stdout, launched hidden via the launcher with Win32_Process Create (pythonw PID 67100, one instance). w91 by 14:51.

## 2026-10-30 14:56-14:59 MDT - watch run: caught wild shiny Magcargo w104
- Farm stopped 14:55:28 on shiny_enemy Magcargo (wild single, Lv73, not a boss). No attack. Poke Ball (Rogue 0; Poke 39->38) caught first throw. Party full, chose No; went to storage. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden (pythonw PID 31076, one instance). w107 by 14:58.

## 2026-10-30 15:15-15:19 MDT - watch run: caught wild shiny Mawile w139 (double)
- Farm stopped 15:09:59 on shiny_enemy Mawile (wild double with Comfey, Lv115, not a boss). Zacian Bitter Blade (TargetSelect cursor 2 = Comfey) KO'd Comfey; Milotic Calm Mind. Rogue Ball (10->9) caught first throw. Party full, chose No; went to storage. Logged in CHIE Shiny Log.md.
- Relaunched hidden (pythonw PID 21252, one instance). w142 by 15:19.

## 2026-10-30 15:23-15:26 MDT - watch run: caught wild shiny Glalie w153
- Farm stopped 15:23:00 on shiny_enemy Glalie (wild single, Lv117, not a boss). No attack. Rogue Ball via handleCommand(1,3) (14->13): caught first throw. Party full, chose No (setCursor(3)); went to storage. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden (pythonw PID 107776, one instance). w154 by 15:25.

- 2026-10-30 15:34 MT: pr_farm17 - Rogue Balls rank last within Rogue tier (-99.6; other Rogue items ~-100, Soothe Bell -99.5). Backup pr_farm17.bak_rogueball.py.

## 2026-10-30 15:38-15:43 MDT - watch run: FAILED wild shiny Chandelure w187 (double)
- Farm stopped 15:36:39 on shiny_enemy Chandelure (wild double with a non-shiny Chandelure; shiny Lv157, not a boss).
- Mistake: aimed BOTH Zacian (Mighty Cleave) and Milotic (Steam Eruption) at the partner (cursor 3). Zacian KO'd it first, and Milotic's single-target move retargeted onto the remaining foe, the shiny, and KO'd it. No ball thrown; shiny lost.
- RULE for doubles shiny: only ONE mon attacks the partner; the other uses a non-damaging move (Milotic Calm Mind). If one hit may not KO, repeat over turns rather than double-attacking.
- Logged in CHIE Shiny Log.md as not caught. Cleared flags, rotated stdout, relaunched hidden (pythonw PID 67580) from the w187 shop screen.

## 2026-10-30 16:14-16:20 MDT - watch run: caught wild shiny Drilbur w48 (double)
- Farm stopped 16:13:43 on shiny_enemy Drilbur (wild double with Dugtrio, Lv33, not a boss). Zacian Bitter Blade (handleCommand(0,3) + TargetSelect cursor 2 = Dugtrio) KO'd Dugtrio; Milotic Calm Mind only. Rogue Ball handleCommand(1,3) (5->4): caught first throw. Party full, chose No (setCursor(3)); went to storage. Logged in CHIE Shiny Log.md.
- Gotcha: one ACTION press too many after the turn opened the Fight menu; Cancel (p:6) backed out safely before throwing.
- Cleared flags, rotated stdout, relaunched hidden via launcher (pythonw 87216 -> python 44220, one instance). w50 by 16:19.

## 2026-10-30 17:45 MT - DNA Splicer fusion (Kricketot base via Apply, Zigzagoon/Linoone partner via Splice); DNA -250 only with unfused pair else 99; state.js fs field; XFER drains fused partner. Live Kricketot passive = Honey Gather.

## 2026-10-30 17:42-17:46 MDT - watch run: caught wild shiny Pumpkaboo w41
- Farm stopped 17:40:37 on shiny_enemy Pumpkaboo (wild single, Lv28, not a boss). No attack. Rogue Balls 0, so Poke Balls via handleCommand(1,0): first broke free, second caught (15->13). Party had 5, so it joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden via the launcher (pythonw PID 17876, one instance). w44 by 17:45.

## 2026-10-30 17:55-17:58 MDT - watch run: caught wild shiny Sableye w59
- Farm stopped 17:50:02 on shiny_enemy Sableye (wild single, Lv40, not a boss). No attack. Rogue Balls 0, so Poke Balls via handleCommand(1,0): two broke free, third caught (13->10). Party full, chose No (setCursor(3)); went to storage. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden via the launcher (pythonw PID 73064, one instance). w61 by 17:58.

- 2026-10-30 18:15 MT: pr_farm17 - Master Ball (Master tier) and Rogue Ball (Rogue tier) get their tier boost back (bottom of their own tier), so they always beat lower-tier and shop items. Fixes w104+ picking Sitrus Berry over a Master Ball. Poke/Great/Ultra Balls stay junk while any ball is held. Backup pr_farm17.bak_masterball.py.

## 2026-10-30 18:17-18:26 MDT - watch run: run ended w110 (wipe, slot 2), gacha done, manual control seen, stood down
- Farm exited 18:14:43 "ZACIAN FAINT ... DONE farm17" at w110 (Starmie/Golduck/Quagsire/Dracovish trainer); whole party fainted (Pumpkaboo last). slot 2.
- Gotcha: pressing ACTION on the game-over text carried through Title -> New Game -> Classic into starter select; backed out with Cancel + confirm Yes to title (no Escape).
- Shiny UP! gacha (setGachaCursor(2)): 13 regular (1 x10 + 3 x1), 3 Plus (5 each) -> eggs 0 -> 28. Vouchers 0/0/0/0.
- Zacian and Feebas upgrades all owned (passive 3, reduction 2). Opened Zacian's Use Candies (candy was 21), and meanwhile someone (tab focused/visible, no script) bought eggs by hand: Zacian 21 -> 3, Feebas 58 -> 10, eggs 28 -> 35. Treated as Gavin playing: no more input, no new run. status stopped_reason = run_end_then_manual_control.
- New helper navsp.py <species> (PC %TEMP%\prfarm): moves the starter-select cursor onto a species via processInput arrows.

## 2026-10-30 18:50 MT: data-driven reward ranking (rarity first)
- New `item_priority.json` (pokerogue project folder; copy in %TEMP%\prfarm as fallback) is the single source of truth; `ITEM_PRIORITY.md` is regenerated from it (`gen_item_priority_md.py`). Farm loads it at start, auto-reloads on change, loud log + built-in fallback if missing/invalid.
- New `prio.py` ranker: specials (role revive -300, sword/prism -290, DNA pair -250, emergency heal -240) > real items by tier MASTER>ROGUE>ULTRA>GREAT>COMMON > junk (>=93, any tier, triggers reroll). Within-tier rank orders inside a tier.
- Candy Jar/Rare Candy/Rarer Candy/Soothe Bell/vouchers have min_tier ULTRA (top of Ultra, below Rogue/Master, as before).
- Fixed: Rarer Candy (-56), Exp. All, King's Rock curly apostrophe, Poké é/× normalisation, TM match only "TM###", dead pp_low branch (PP items 45 when PP <40%), berry special rule removed (tier-first covers it).
- Balls: Master/Rogue bottom of own tier while holding balls; Poké/Great/Ultra junk; out of balls = top of tier, best first. Lure while active 100.5.
- Replay test `replay_test.py` over farm log: 3103 screens, 644 picks change, 0 rule violations; 18:11:13 picks Master Ball; 17:23:51 no lure. Backup pr_farm17.bak_datarank.py.

## 2026-10-30 19:30-19:35 MDT - watch run: caught wild shiny Simipour w123
- Farm stopped 19:29:09 on shiny_enemy Simipour (wild single, Lv95, not a boss). No attack. Rogue Balls 0, so Poke Ball via handleCommand(1,0): caught first throw (35->34). Party had 5, so it joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden via the launcher (Win32_Process Create pythonw PID 31228).

## 2026-10-30 19:45-19:49 MDT - watch run: caught wild shiny Barraskewda w138
- Farm stopped 19:42:26 on shiny_enemy Barraskewda (wild single, Lv101, not a boss). No attack. Rogue Balls 0, so Poke Balls via handleCommand(1,0): two broke free, third caught (34->31). Party full, chose No (setCursor(3)); went to storage. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden via the launcher (Win32_Process Create pythonw PID 50260, one instance). w140 by 19:49.

## 2026-10-30 20:01-20:25 MDT - watch run: run ended w145 (wipe, slot 2), end-of-run procedure + new five-mon run slot 2
- Farm exited 19:59:40 "ZACIAN FAINT ... DONE farm17" at w145 (trainer: Feraligatr/Aggron/Archaludon/Rayquaza/Toucannon/Polteageist); whole party fainted (Simipour last). Game was paused at MessagePhase (hidden tab); s:80 + one ACTION reached the title (no Continue).
- Shiny UP! gacha (setGachaCursor(2)): 7 regular (x1 each) + 2 Plus (5 each, setCursor(2)) -> eggs 0 -> 17. Vouchers 0/0/0/0.
- Zacian and Feebas upgrades all owned (passive 3, reduction 2); nothing to buy. Zacian Use Candies: 2 eggs (6 each), candy 17 -> 5. Eggs 19. Feebas candy 50, untouched.
- New Classic run slot 2 (Empty; slots 0/1 Endless untouched), party 888,349,327,263,401 (10/10) via navsp.py + gx.py. Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (Win32_Process Create pythonw PID 9944).

## 2026-10-30 20:38-20:46 MDT - watch run: caught wild shiny Tympole w33 (double)
- Farm stopped 20:33:59 on shiny_enemy Tympole (wild double with Poliwag, Lv20, not a boss). Zacian Bitter Blade (resisted, Poliwag 54->20) then Mighty Cleave (handleCommand(0,1) + TargetSelect cursor 2) KO'd Poliwag; Milotic Calm Mind both turns. Declined Milotic's Life Dew. Poke Ball handleCommand(1,0) (Rogue 0; Poke 5->4): caught first throw. Party had 5, joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flags, rotated stdout, relaunched hidden via the launcher (Win32_Process Create pythonw PID 30728, one instance). w37 by 20:43.

## 2026-10-30 20:48-20:58 MDT - watch run: caught three wild shinies (Phantump w42, Spiritomb w49, Impidimp w51)
- Phantump w42 (Uncommon Breed mystery encounter, wild single, Lv30, not a boss): no attack, Poke Ball first throw (14->13). Party full (6), chose No, storage.
- Spiritomb w49 (wild double with Litwick, Lv33): Zacian Mighty Cleave (CommandPhase.handleCommand(0,1), target cursor 2) KO'd Litwick; Milotic Calm Mind (handleCommand(0,3)). Poke Ball first throw (13->12). Storage.
- Impidimp w51 (wild single, Lv32): no attack, Poke Ball first throw (12->11). Storage.
- Note: handleCommand lives on the CommandPhase (ph), not the UI handler. All three logged in CHIE Shiny Log.md.
- Each time: cleared flags, rotated stdout, relaunched hidden via the launcher (last pythonw PID 77652, one instance). w53 by 20:56.

## 2026-10-30 21:43-21:47 MDT - watch run: run ended w145 (wipe, slot 2), manual control seen, stood down
- Farm exited 21:41:09 "ZACIAN FAINT ... DONE farm17" at w145 (rival trainer with Goodra/Rayquaza; whole party fainted, Seismitoad last). s:80 + one ACTION reached the title.
- Vouchers at that point 7 regular / 2 Plus, eggs 0, Zacian candy 18, Feebas 75. Opened Menu > Egg Gacha, setGachaCursor(2) Shiny UP!, no pull pressed yet.
- Between my calls (~21:44:50-21:45:30) the 2 Plus vouchers were spent (eggs 0 -> 10) and the UI went to starter select and then back to the title, none of it from me (tab focused and visible). Treated as Gavin playing by hand: no further input, no new run. Status stopped_reason = run_end_then_manual_control. Remaining: 7 regular vouchers, candy steps, new five-mon run in slot 2.

## 2026-10-30 21:50 MDT - watch run: still manual control, stood down
- Farm not running (ended 21:41 w145). Since 21:47 someone else bought Zacian eggs (Zacian candy 18 -> 0, eggs 10 -> 13) and the game now sits on starter select (0/10, SelectStarterPhase). 7 regular vouchers still unspent, Feebas candy 75. Gavin is playing by hand: no input sent, no new run started.

## 2026-10-30 21:52 MDT - watch run: still manual control, stood down
- Farm not running. Game unchanged since 21:50: SelectStarterPhase, StarterSelect cursor 65, frame ~3043486, 7 regular vouchers, eggs 13, Zacian candy 0, Feebas 75. Last manual activity ~21:47-21:50, under 10 min idle, so no input sent. Next runs: if still identical (cursor 65, vouchers 7, eggs 13) after ~22:00, finish run-end steps (7 vouchers on Shiny UP!, Feebas upgrades check, new five-mon run slot 2) and relaunch.

## 2026-10-30 21:59 MDT - watch run: manual control still active, stood down
- Farm not running. Game changed since 21:52 (not idle): StarterSelect cursor 65 -> 36 with 8/10 cost picked, eggs 13 -> 19, Feebas candy 75 -> 3, vouchers still 7/0/0/0, Zacian candy 0. Gavin is clearly setting up a run by hand, so no input sent.

## 2026-10-30 22:08 MDT - watch run: Gavin playing a new run by hand, stood down
- Farm not running (ended 21:41 w145). Page had been reloaded (camera hook gone); re-installed the read-only hook only. Game is a new Classic run in slot 2 at w16 (LearnMovePhase), party Rayquaza/Milotic/Abra, tab visible and focused. Vouchers 7/0/0/0, eggs 10, Zacian candy 0, Feebas 3. Clearly manual play, so no input sent and no farm launched.

## 2026-10-30 22:13 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145). Manual Classic run advanced w16 to w30 since 22:08 (party Rayquaza/Milotic/Kadabra). Read-only check, no input sent.

## 2026-10-30 22:17 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag. Camera hook gone again (page reloaded since 22:13), so no wave read; manual play was active at 22:13 (w30). Read-only check, no input sent, no farm launched.

## 2026-10-30 22:23 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag. Manual Classic run now at w61 Snowy Forest (party Milotic/Rayquaza/Alakazam), up from w30 at 22:13; tab visible and focused. Read-only check, no input sent, no farm launched.

## 2026-10-30 22:26 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag, no farm process. Manual Classic run was active at w61 at 22:23 (3 min ago). Read-only check, no input sent, no farm launched.

## 2026-10-30 22:32 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag, no farm process. Manual Classic run was active at w61 at 22:23. Read-only check, no input sent, no farm launched.

## 2026-10-30 22:39 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag, no farm process. Manual Classic run last seen active at w61 at 22:23. BOREN-0 went offline mid-check, so no game read and no project-folder copy this run. No input sent, no farm launched.

## 2026-10-30 22:45 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag, no farm process. Manual Classic run last seen active at w61 at 22:23. BOREN-0 went offline right after the status check, so no game read and no project-folder copy. No input sent, no farm launched.

## 2026-10-30 22:48 MDT - watch run: Gavin still playing by hand, stood down
- Farm not running (ended 21:41 w145), stopped_reason run_end_then_manual_control, no stop flag, no farm process. Gavin's own manual Classic run (Rayquaza/Milotic/Alakazam, last seen w61 at 22:23) is not the farm lineup, so not taking it over. Read-only check, no input sent, no farm launched.

## 2026-10-30 22:53 MDT - watch run: manual play, stood down
- Someone launched pr_farm17 at 22:49:40; it stopped itself at 22:50:10 (ZACIAN MISSING, party read Rayquaza Lv26 + Feebas Lv18, a manual run without Zacian). No farm process now, no stop flag, stopped_reason run_end_then_manual_control. Another session was polling the farm process at 22:52. No input sent, no farm launched.

## 2026-10-30 22:59 MDT - watch run: manual play / Rayquaza run, stood down
- No farm process, no stop flag, stopped_reason run_end_then_manual_control. Last launch 22:49:40 stopped itself (Zacian missing; party Rayquaza Lv26 + Feebas Lv18). No input sent, no farm launched.

## 2026-10-30 23:05 MDT — Lead-agnostic farm + per-primary profiles (Gavin t136u)
- PRIMARY is no longer hard-coded Zacian. `resolve_primary()` picks config key `primary` (name or species id, optional) else the first non-Feebas/Milotic mon in party order; re-resolved at run start / new run (wave drops). JS hooks use `window.__pr_prim` instead of species 888 (party reorder, Linoone/Zigzagoon held-item transfer).
- Generic: faint/missing/switch-out logs, ally-alive check, switch-in target, fight history, PP-item move targeting, DNA exclusion, emergency heal / revive / berries / Soothe Bell overflow (already role-based) now follow the primary.
- Profiles: `profiles/*.json` (`C:\Users\gavin\..PROJECT\pokerogue\profiles\` first, then `%TEMP%\prfarm\profiles\`), hot-reloaded on mtime. zacian.json = old behaviour (Rusted/Ancient Sword signature, decline all moves). rayquaza.json = protected Core Enforcer/V-create, wanted Hyper Voice/Air Slash, replaceable Hyper Beam/Twister/Ancient Power/…, normal-type moves replaceable, good_moves list, primary_move Core Enforcer, spread_moves list.
- Move learning (primary only): LearnMovePhase confirm -> `learn_decide()`; accept calls the phase's own learnMove(slot) (forget order: replaceable list, normal-type, status, weakest); decline -> No (+ "stop teaching" -> Yes). Non-primary mons unchanged (decline).
- TMs: state.js exposes reward moveId/name/type/power and primary compatibleTms; profile-approved TMs rank -50 within their tier and are taught to the primary via "Teach"; others still blacklisted as before.
- Battle: primary_move used first whenever it hits (eff>=1), not PP-low, and no move is >=2x more effective; spread moves excluded while a wild shiny is out.
- Backups: pr_farm17.bak_agnostic.py, state.bak_agnostic.js, prio.bak_agnostic.py.

## 2026-10-30 23:10 MDT - watch run: another session patching (lead-agnostic, 23:05), stood down
- No farm process, no stop flag, stopped_reason run_end_then_manual_control. No input sent, no farm launched.

## 2026-10-30 23:30 MT — REVIVEFIX / SHOPSEL (pr_farm17.py, backup pr_farm17.bak_revive.py)
- Shop item selection: ROOT CAUSE = game resets the shop cursor to settings.shopCursorTarget (cursor 0 = Potion) when the intro animations finish; we set it before that. Now waits for handler.awaitingActionInput, then looks the item up by NAME in live shopOptionsRows, verifies, retries up to 8x (0.4s) before skipping.
- Shop Revive/Max Revive is only bought if the target mon is fainted in a LIVE party read; its slot index is taken from that live read.
- Party-target step (reward/shop item apply): re-reads live party HP by index. Revives go to the fainted primary first, else first fainted mon. Any non-revive item aimed at a fainted mon is redirected to an alive mon (secondary first) — never a berry/heal/status item on a fainted mon.
- pick_reward: when the primary is fainted, heal_need/emergency are off, Revive/Max Revive/Sacred Ash/Reviver Seed rank -300 above everything, and berries/potions/status/PP items rank 99 (junk) unless the alive secondary needs a potion (and SEC_ALLOW_HEAL).
- w35 note: the shop Revive actually worked (Rayquaza 0 -> 50/100, charged 4482->3342 on 2nd try; 1st try "not charged" because the target slot was stale: Milotic had switched into slot 0). The "cannot be applied" was the FREE reward Revive (rank 90, nobody fainted any more) - harmless, blacklisted. Live slot index now used for revives.
- 2026-10-30 23:24 MDT: Safe-restarted pr_farm17 (pid 146152 -> 44236) to load revive/shop-cursor/fainted-heal patch; PRIMARY Rayquaza + rayquaza profile confirmed, advancing (w33).

## 2026-10-30 23:51 MDT - watch run: run ended w107 (wipe, slot 2), run-end procedure IN PROGRESS by this watch
- Farm exited 23:48:12 "PRIMARY Rayquaza FAINT ... DONE farm17" at w107 (Ace Trainer / mysterious challengers); party Milotic + Rayquaza both 0 HP.

## 2026-10-31 00:06 MDT - watch run: run-end steps in progress by another session, stood down
- Run ended 23:48 at w107 (whole party fainted: Rayquaza, then Milotic vs Ace Trainer Thievul). No farm process, no stop flag. Another session is running gacha_all.py (pid 63148, started 00:04:46, output updating). No input sent, no farm launched.

## 2026-10-31 00:14 MDT - watch run: new run just launched by another session, stood down
- Another session finished run-end steps and launched pr_farm17 (pythonw pid 13680 via pr_farm_launch_hidden.py, started 00:13:09, parent WmiPrvSE, hidden). PRIMARY Rayquaza + Feebas, advancing (w3 at 00:13). No stop flag. No input sent.

## 2026-10-31 00:15 MDT - watch run (same session as 23:51): run-end done, new Rayquaza run slot 2; shiny Fidough w6 caught by someone else
- Shiny UP! gacha (setGachaCursor(2)) via new helper gacha_all.py (PC %TEMP%\prfarm; guarded loop: x10 while regular>=10, x1, then Plus, Premium; stops when all vouchers are 0): 20 regular (2 x10), 2 Plus, 1 Premium -> eggs 0 -> 40. Vouchers 0/0/0/0. No hatches.
- Rayquaza: passive owned, cost reduction 1 of 2; next reduction (x15 to cost 7) not affordable (13 candy). Bought 2 Rayquaza eggs (6 each), candy 13 -> 1. Eggs 42. Feebas upgrades all owned (passive 3, reduction 2), candy 20 untouched.
- New Classic run slot 2 (Empty; slots 0/1 Endless untouched), party Rayquaza 384 + Feebas 349 (10/10) via navsp.py + guarded gx.py. Verified modeId 0, wave 1, sessionSlotId 2.
- Gotcha: BOREN-0 shell calls that report "temporarily unreachable" can still execute. One relative ACTION ran twice and opened Settings. Use state-guarded JS (check handler name and cursor before processInput) for every input.
- Cleared flag/reasons, rotated stdout, launched hidden via the CHANGELOG launcher (Win32_Process Create pythonw PID 13680). w6 by 00:13:57.
- 00:13:57 farm stopped on shiny_enemy Fidough (wild double with Wooloo, Lv4). Before this session sent any input, someone else (control app / by hand) KO'd Wooloo and caught Fidough with a Poke Ball (5 -> 4); Fidough joined the party as 3rd. The control app then restarted the farm (python.exe -u pr_farm17.py PID 89040, parent PokeFarmControl 170576). One instance, w8 at 00:16. Left alone. Logged Fidough in CHIE Shiny Log.md.

## 2026-10-31 00:18-00:22 MDT - watch run: shiny Spearow w11 caught by someone else, stood down
- Farm stopped 00:16:02 on shiny_enemy Spearow (wild double with Zigzagoon, Lv7, not a boss). While this run was reading state, another controller (by hand / control app) was already mid-turn: Rayquaza Ancient Power on Zigzagoon, Feebas Moonblast aimed at Spearow (it survived 9/23), then a Poke Ball (4 -> 3) caught it; party had 3, joined as 4th (Rayquaza/Feebas/Fidough/Spearow). This run's single handleCommand attempt was refused by its own phase guard (phase was SelectTargetPhase), so no input was sent.
- Control app restarted the farm (python.exe PID 92292, parent PokeFarmControl 170576) at 00:19:16. One instance, no stop flag, w14 by 00:19:46. Logged Spearow in CHIE Shiny Log.md.
- Note: the hand catch had Feebas attack the shiny itself (Moonblast). Rule is the secondary uses Calm Mind or switches out in a doubles shiny catch.

## 2026-10-31 00:26 MDT - watch run: Reviver Seed loop fixed
- Farm stuck from 00:20:05 at w15 reward screen: REVIVEFIX live-target check matched "revive" inside "Reviver Seed" (held item), found no fainted mon, cancelled forever ("REVIVE target live: Reviver Seed -> slot None").
- Patch pr_farm17.py ~line 1001 (backup pr_farm17.bak_reviverseed.py): _isrev excludes "reviver seed".
- Killed control-app instance 92292 (not relaunched), rotated stdout, launched one hidden instance via pr_farm_launch_hidden.py (pythonw PID 74728, parent WmiPrvSE). w22 by 00:26:35.

## 2026-10-31 01:00-01:10 MDT - watch run: run ended w115 (wipe, slot 2), run-end done, new Rayquaza run slot 2
- Farm exited 00:55:52 "PRIMARY Rayquaza FAINT ... DONE farm17" at w115 (Team Galactic Boss Cyrus). Rayquaza fell to Weavile, then Milotic, Dachsbun and shiny Fearow; live read confirmed all 4 at 0 HP. Game-over advanced to title (no Escape).
- Shiny UP! gacha via gacha_all.py (title Menu > Egg Gacha): 6 regular vouchers -> 6 eggs (0 -> 6). Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 10: passive owned, reduction 1 of 2, next reduction x15 not affordable. Bought 1 Rayquaza egg (x6), candy 10 -> 4, eggs 7. Feebas: all upgrades owned (passive 3, reduction 2), candy 36 untouched.
- New Game > Classic > Rayquaza 384 + Feebas 349 (guarded processInput; Start reached by pressing Right from the grid) > Yes > slot 2 (Empty; slots 0/1 Endless untouched). Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reason, rotated stdout, launched hidden via pr_farm_launch_hidden.py (Win32_Process Create, pythonw PID 156892). One instance, w3 by 01:10:15.

## 2026-10-31 01:18-01:20 MDT - watch run: caught wild shiny Galarian Zigzagoon w34
- Farm stopped 01:16:57 on shiny_enemy Zigzagoon (Galarian, species 4263; single wild, Lv20, not a boss). No other controller active. No attack; threw 1 Rogue Ball via guarded CommandPhase.handleCommand(1,3) (Rogue 5 -> 4): caught first throw. Party was 2, so it joined as 3rd (Rayquaza/Milotic/Zigzagoon). Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via pr_farm_launch_hidden.py (Win32_Process Create, pythonw PID 54948). One instance, w37 by 01:19.

## 2026-10-31 01:36-01:44 MDT - watch run: run ended w80 (wipe, slot 2), run-end done, new Rayquaza run slot 2
- Farm exited 01:31:49 "PRIMARY Rayquaza FAINT ... DONE farm17" at w80 (trainer: Stoutland/Cinccino/Bouffalant). Rayquaza, then Milotic, then shiny Obstagoon fell; live read confirmed all 3 at 0 HP. s:80 + one ACTION reached the title (no Escape).
- Shiny UP! gacha via gacha_all.py: 2 regular vouchers -> 2 eggs (1 -> 3). Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 7: next reduction x15 not affordable. Bought 1 Rayquaza egg (x6), candy 7 -> 1, eggs 4. Feebas all upgrades owned, candy 44 untouched.
- New Classic run slot 2 (Empty; slots 0/1 Endless untouched), Rayquaza 384 + Feebas 349 (Start reached from the party column with Down). Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reason, rotated stdout. First launch accidentally ran as plain python under the remote shell; killed it and relaunched via Win32_Process Create pythonw (PID 119576). One instance, w8 by 01:43.

## 2026-10-31 01:54-02:05 MDT - watch run: run ended w37 (wipe, slot 2), run-end done, new Rayquaza run slot 2
- Farm exited 01:48:39 at w37: mysteriousChest top option (Gimmighoul trap) KO'd Rayquaza, Milotic then fell to boss Gimmighoul. Reached title (extra ACTION opened mode select; Cancel, no Endless).
- Shiny UP! gacha: 2 regular + 1 Plus -> eggs 1 -> 8. No hatches. Rayquaza candy 5 (nothing affordable). Feebas all owned, candy 45.
- New Classic slot 2 (empty), Rayquaza 384 + Feebas 349, verified modeId 0 w1 slot 2. Launched hidden pythonw PID 38456 (parent WmiPrvSE), w5 by 02:05.
- Mysterious Chest risk flagged to Gavin; not patched.

## 2026-10-31 02:19-02:21 MDT - watch run: shop "notready" wait extended
- Run healthy (slot 2, Rayquaza + Feebas, w38-42), but every shop attempt since 02:12 failed "SHOP cursor mismatch notready ... after 8 tries", so no heals were bought (incl. hard-wave pre-heal at w38). The handler's awaitingActionInput stayed false longer than 8x0.4s.
- Patch pr_farm17.py (backup pr_farm17.bak_shopwait.py): SHOP_SEL_JS retry loop 8 -> 20 tries (about 8s).
- Killed PID 38456, rotated stdout, relaunched hidden via pr_farm_launch_hidden.py (Win32_Process Create pythonw PID 61868). One instance, w42 at 02:20. Next watch: confirm SHOP BUY lines return.

## 2026-10-31 02:32-02:45 MDT - watch run: run ended w60 (wipe, slot 2), run-end done, new Rayquaza run slot 2
- Farm exited 02:31:44 at w60 (Gym Leader Giovanni: Dugtrio/Rhydon/Persian/Nidoqueen). Rayquaza, Feebas, then Darmanitan fell; live read confirmed all 3 at 0 HP.
- Tab was hidden (visibilityState hidden), so STEP couldn't advance the GameOverPhase; new helper front.py (PC %TEMP%\prfarm: /json/activate + Page.bringToFront) fixed it and the game reached the title.
- Shiny UP! gacha via title Menu (cursor 4 Egg Gacha) + gacha_all.py: 4 regular vouchers -> eggs 1 -> 5. Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 7 (passive owned, reduction 1 of 2; needs 15 for the next). Saving candy per RAYQUAZA TEAM PLAN, no eggs bought. Feebas all owned, candy 51.
- New Classic slot 2 (empty; slots 0/1 Endless untouched). Rayquaza 384 + Feebas 349 fills the cost limit 10/10 (Rayquaza 8, Feebas 2), so no room for Spinda/Zigzagoon/Kricketot yet. Start path: Right off grid col 8 into party column, Down to Start (Down from Start goes to Random, Up from Random goes to filter bar). Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create pythonw (PID 76520). One instance, w3 by 02:44.

## 2026-10-31 02:49-02:53 MDT - watch run: shop "notready" root cause fixed (hidden tab)
- Run healthy (slot 2, Rayquaza + Feebas, w10-17), but every shop attempt still failed "notready after 20 tries" (w7, w9 incl. hard-wave pre-heal). Probe: document.visibilityState = hidden (Chrome window normal at -1076,861 but occluded), so the game loop only advances via STEP_JS; the shop wait loop slept without stepping, so the intro anims never finished and awaitingActionInput stayed false.
- Patch pr_farm17.py (backup pr_farm17.bak_shopstep.py): in the SHOP_SEL_JS retry loop, on 'notready' run STEP_JS 5x before sleeping.
- Killed PID 76520, rotated stdout, relaunched hidden (Win32_Process Create pythonw PID 25796, parent WmiPrvSE). One instance. 02:52:46 SHOP BUY (proactive) Potion -> Feebas worked at w17.

## 2026-10-31 03:10-03:14 MDT - watch run: caught wild shiny Pineco w44
- Farm stopped 03:08:09 on shiny_enemy Pineco (single wild, Lv29, not a boss). No other controller active. Rogue Balls 0, so threw a Poke Ball via guarded CommandPhase.handleCommand(1,0) (15 -> 14): caught first throw. Tab was hidden and the "Gotcha!" message waited for input; dismissed with guarded processInput(5). Party was 2, joined as 3rd (Rayquaza/Feebas/Pineco). Logged in CHIE Shiny Log.md.
- New PC helpers in %TEMP%\prfarm: rd_field_ro.py (read-only field/phase read), rd_msg.py (message/awaiting-input read), catch_pb.py, catch_ack.py.
- Cleared flag/reasons, rotated stdout, launched hidden via pr_farm_launch_hidden.py (Win32_Process Create pythonw PID 27724). One instance, w45 by 03:13.

## 2026-10-31 04:03-04:15 MDT - watch run: run ended w114 (wipe, slot 2), run-end done, new Rayquaza run slot 2
- Farm exited 03:59:00 "PRIMARY Rayquaza FAINT ... DONE farm17" at w114 (wild Revavroom/Mabosstiff). Live read confirmed all 6 at 0 HP (Torterra, Rayquaza, Milotic, Spritzee, Forretress, Granbull). front.py + STEP + one ACTION reached the title (second ACTION opened mode select; Cancel, no Endless).
- Shiny UP! gacha via title Menu (cursor 4) + gacha_all.py: 6 regular + 1 Plus vouchers -> eggs 0 -> 11. Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 14 (passive owned, reduction 1 of 2; 1 short of the 15 for the next). Saved, no eggs bought. Feebas all owned, candy 65.
- New Classic slot 2 (empty; slots 0/1 Endless untouched). New helper nr_pick.py (PC %TEMP%\prfarm) picks starters with guarded processInput + STEP. Rayquaza 384 + Feebas 349 fill 10/10; Spinda/Zigzagoon/Kricketot didn't fit. Right x6 from grid col 3 reached Start. Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create pythonw (PID 38144). One instance, w3 by 04:14.

## 2026-10-31 04:42-04:51 MDT - watch run: run ended w50 (wipe, slot 2), Rayquaza 2nd cost reduction bought, full five-mon team started
- Farm exited 04:36:15 "PRIMARY Rayquaza FAINT ... DONE farm17" at w50 (Gym Leader Katy; Rayquaza fell to Lokix, then Feebas and Darumaka). Live read confirmed all 3 at 0 HP. front.py + s:80 + one ACTION reached the title (no Escape).
- Shiny UP! gacha via title Menu (cursor 4) + gacha_all.py: 2 regular vouchers -> eggs 0 -> 2. Vouchers 0/0/0/0. No hatches.
- Rayquaza had 15 candy: bought the x15 Reduce Cost to 7 (valueReduction 1 -> 2). Candy 15 -> 0, no eggs. Feebas all owned, candy 67 untouched. New helper nav_open.py (PC %TEMP%\prfarm) navigates starter select to a species and opens its option menu (Use Candies is index 8).
- New Classic slot 2 (empty; slots 0/1 Endless untouched): full team 384,349,327,263,401 fits 10/10 via nr_pick.py. Right x6 to Start, Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (full pythonw path; bare pythonw.exe silently failed) PID 110452. One instance, w2 by 04:50.

## 2026-10-31 05:05-05:07 MDT - watch run: caught wild shiny Hoppip w29
- Farm stopped 05:04:20 on shiny_enemy Hoppip (single wild, Lv18, not a boss). No other controller active. No attack; threw 1 Rogue Ball via guarded CommandPhase.handleCommand(1,3) (new helper catch_rb_hoppip.py; Rogue 5 -> 4): caught first throw. Dismissed "Gotcha!" with catch_ack.py. Party had 5, joined as 6th (Rayquaza/Feebas/Spinda/Zigzagoon/Kricketot/Hoppip). Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create pythonw (PID 142912). One instance, w30 by 05:06:31.

## 2026-10-31 05:23-05:25 MDT - watch run: lost wild shiny boss Nuzleaf w49
- Farm stopped 05:20:08 on shiny_enemy Nuzleaf (single wild boss, 2 segments, Lv36, 105/105 HP) from the Berries Abound mystery encounter. No other controller active.
- New guarded helper catch_shiny.py (PC %TEMP%\prfarm; args: species cmd arg; cmd 0 = fight move index, 1 = ball type; refuses Master Ball, refuses attacking a non-boss). Used Rayquaza Air Slash (weakest, but super effective on Grass/Dark) to break the shield: it KO'd Nuzleaf from full HP instead of stopping at the segment line. No ball thrown. Logged as failed in CHIE Shiny Log.md.
- Lesson: segment damage is NOT clamped here; a hit from full can KO a 2-segment boss. Next time estimate damage first and prefer a resisted/not-very-effective move, or a weaker party mon.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create pythonw (PID 89580). One instance, w50 by 05:24.

## 2026-10-31 06:38-07:01 MDT - watch run: run ended w140 (wipe, slot 2), run-end done, new five-mon Rayquaza run slot 2
- Farm exited 06:34:22 "PRIMARY Rayquaza FAINT ... DONE farm17" at w140 (wild Crawdaunt; Rayquaza and Milotic fell first, then Linoone, Kricketot, shiny Jumpluff). Live read confirmed all 6 at 0 HP (Jumpluff, Rayquaza, Milotic, Spinda, Linoone, Kricketot).
- Gotcha: my title loop's state check returned null (bad expression), so repeated ACTIONs carried Title -> New Game -> Classic -> starter select and toggled a starter's option menu open/closed; nothing bought. Backed out with Cancel + Yes to title (no Escape). Always verify the check expression returns a value before looping.
- Shiny UP! gacha via title Menu (cursor 3 Menu, cursor 4 Egg Gacha) + gacha_all.py: 9 regular + 2 Plus vouchers -> eggs 0 -> 19. Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 6 (passive + both reductions owned); not enough for an egg, saved. Feebas all owned, candy 86 untouched.
- New Classic slot 2 (empty; slots 0/1 Endless untouched): nr_pick.py 384,349,327,263,401 all added; Right until startCursorObj.visible, Start, Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2, party [384,349,327,263,401].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 17012, parent WmiPrvSE. One instance, w4 by 07:01.

## 2026-10-31 07:17-07:21 MDT - watch run: caught wild shiny Combee w26 (double)
- Farm stopped 07:14:25 on shiny_enemy Combee (wild double with Turtwig, both Lv16, no boss). No other controller active.
- New guarded helper dbl_combee.py (PC %TEMP%\prfarm; modes ray/tgt/mil/ball/ack/rd). Rayquaza Air Slash (single target) via CommandPhase.handleCommand(0,3), TargetSelect cursor set to BattlerIndex 2 (Turtwig) + processInput(5); Milotic Calm Mind. Turtwig KO'd, Combee untouched (38/38). Next turn Rogue Ball handleCommand(1,3) (5 -> 4): caught first throw, dismissed Gotcha with catch_ack.py. Party had 5, joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 125332. One instance, w29 by 07:20:47.

## 2026-10-31 08:24-08:36 MDT - watch run: run ended w110 (wipe, slot 2), run-end done, new five-mon Rayquaza run slot 2
- Farm exited 08:21:32 "PRIMARY Rayquaza FAINT ... DONE farm17" at w110 (wild Mismagius, Levitate). Live read confirmed all 6 at 0 HP (Kricketot, Rayquaza, Milotic, Combee, Linoone, Spinda). front.py + one ACTION reached the title; a second ACTION opened mode select again, Cancel (cursor 5), no Endless.
- Shiny UP! gacha via title Menu (cursor 3, then 4 Egg Gacha) + gacha_all.py: 4 regular + 1 Premium vouchers -> eggs 0 -> 14. Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 10 (all upgrades owned): bought 1 egg (x6), candy 10 -> 4, eggs 14 -> 15. Feebas all owned, candy 97 untouched.
- New Classic slot 2 (empty; slots 0/1 untouched): nr_pick.py 384,349,327,263,401 all added; Right until startCursorObj.visible, Start, Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2, party [384,349,327,263,401].
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 31784. One instance, w3 by 08:36.

## 2026-10-31 09:01-09:10 MDT - watch run: caught wild shiny Loudred w43 (double)
- Farm stopped 09:00:01 on shiny_enemy Loudred (wild double with Nosepass Lv26 Sturdy; Loudred Lv29, not a boss). No other controller active.
- New generic guarded helper dbl_shiny.py (PC %TEMP%\prfarm, box /workspace/prfarm/tmp; modes rd / mv FIELD MOVE / tgt BATTLER (refuses a shiny target) / ball SPECIES / ack). Rayquaza Air Slash (single target, resisted by Rock) on Nosepass (BattlerIndex 2), Feebas Calm Mind each turn. Turn 1 missed, turn 2 Sturdy left 23/55, turn 3 KO. Loudred untouched 88/88. Rogue Ball (5 -> 4) caught first throw; party had 5, joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 117144, parent WmiPrvSE. One instance, w45 by 09:09.

## 2026-10-31 09:36-09:39 MDT - watch run: caught wild shiny Krookodile w69
- Farm stopped 09:27:36 on shiny_enemy Krookodile (single wild, Lv48, not a boss, 149/149). No other controller active.
- No attack. dbl_shiny.py ball Krookodile: Rogue Ball (4 -> 3) caught first throw. catch_ack.py dismissed Gotcha; party full (6), so new helper krook_no.py picked "No" on the release prompt (options Summary/Pokedex/Yes/No) and it went to storage. Party unchanged. Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 131964, parent WmiPrvSE. One instance, w70 by 09:38.

## 2026-10-31 10:15-10:28 MDT - watch run: run ended w115 (wipe, slot 2), run-end done, new five-mon Rayquaza run slot 2
- Farm exited 10:13:48 "PRIMARY Rayquaza FAINT ... DONE farm17" at w115 (wild boss G-Max Eevee, Protean, left at 26/345). Live read confirmed all 6 at 0 HP (Exploud, Rayquaza, Milotic, Linoone, Spinda, Kricketot). New helper to_title.py (guarded ACTION loop, asserts a non-null check) reached the title in one ACTION.
- New helpers open_gacha.py (title Menu cursor 3 -> Egg Gacha cursor 4) and ui.py (generic guarded setCursor/processInput/eval sequence; refuses input 7). gacha_all.py: 7 regular + 1 Plus vouchers -> eggs 0 -> 12. Vouchers 0/0/0/0. No hatches.
- Rayquaza candy 14 (all upgrades owned): bought 2 eggs (x6 each), candy 14 -> 2, eggs 12 -> 14. Feebas all owned, candy 115 untouched.
- New Classic slot 2 (empty; slots 0/1 untouched): nr_pick.py 384,349,327,263,401 all added; Right until startCursorObj.visible, Start, Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2, party [384,349,327,263,401].
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 139672, parent WmiPrvSE. One instance, w5 by 10:27.

## 2026-10-31 10:37-10:39 MDT - watch run: caught wild shiny Minior w51
- Farm stopped 10:36:24 on shiny_enemy Minior (single wild, Lv31, not a boss, Shields Down, 81/81). No other controller active.
- No attack. dbl_shiny.py ball Minior: Rogue Ball (5 -> 4) caught first throw. catch_ack.py dismissed Gotcha; party had 5, joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 132828. One instance, w52 by 10:38.

## 2026-10-31 11:15 MT — Master Ball run + Eternatus stop (Gavin t138u)
- prio.py + item_priority.json: new special `master_ball` = -400 (beats sword/DNA/revive). Revert: remove special.
- pr_farm17.py: REROLL_CHEAP_FRAC 0.10 -> 0.20, new REROLL_MAX 8 (was hardcoded 5). TEMPORARY for this run.
- pr_farm17.py: BallUiHandler fallback never selects Master Ball (cursor <= 3).
- pr_farm17.py: ETERNATUS_STOP_WAVE=200: at wave >= 200 no input, status stopped_reason=eternatus_catch, stop flag + stop_reason file.
- Backups: *.bak_mb_20261031_1114 in %TEMP%\prfarm. Plan: ETERNATUS_PLAN.md.

## 2026-10-31 11:21-11:24 MDT - watch run: shiny Bewear w49 already caught by another controller
- Farm stopped 11:20:15 on shiny_enemy Bewear (wild double, w49). By 11:21 Bewear was already in the party (6th) and Rogue Balls were 0; farm relaunched 11:21:35 from PokeFarmControl (PID 95748). Watch sent no game input. Logged Bewear in CHIE Shiny Log.md (ball "Rogue Ball (likely)"). Farm healthy at w55.

## 2026-10-31 11:31 MDT - watch run: shiny Whimsicott w61 and Venusaur w70 handled by another controller
- Farm stopped on shiny_enemy Whimsicott (11:24) and Venusaur (11:28); both times relaunched from PokeFarmControl by the other controller (latest PID 135204 at 11:29:53). Watch sent no game input. Whimsicott is in the party (Bewear gone); Venusaur outcome unknown, not logged. Logged Whimsicott in CHIE Shiny Log.md. Farm healthy at w72, no stop flag.

## 2026-10-31 11:54-11:58 MDT - watch run: shiny Magnezone w141 lost (two controllers)
- Farm stopped 11:53:39 on shiny_enemy Magnezone (wild double with Electivire; Magnezone Lv114, not a boss, Sturdy). Watch: Zacian Spirit Break KO'd Electivire (single target), Milotic Calm Mind; Magnezone untouched.
- While the watch was only stepping messages, another controller threw Rogue Balls (10 -> 7, no catch), Milotic fainted, then the page was reloaded; afterwards Magnezone was fainted (0 HP), Rogue Balls 9, and the farm was relaunched from PokeFarmControl at 11:56:22 (PID 124060). Watch stopped input once it saw the foreign throws. Logged as failed in CHIE Shiny Log.md.
- Lesson: another controller now catches shinies within a minute of the stop; wait ~2 min and check for foreign activity before taking over.

## 2026-10-31 12:05 MDT - watch run: Master Ball in hand; shinies Bibarel w151 and Lickilicky w159 handled by another controller
- Farm picked 1A- Master Ball at 11:59:57 (w154). Farm stopped on shiny_enemy Bibarel (11:58:59) and Lickilicky (12:01:28); both times relaunched from PokeFarmControl by the other controller (latest PID 103476 at 12:05:15, w162). Watch sent no game input. Outcomes unknown (neither in the full party; may be in storage), not logged. Farm healthy at w162, Zacian 523/523, no stop flag.

## 2026-10-31 12:20 MDT - watch run: user_stop at w190
- Farm stopped 12:15:10 with stop_reason user_stop (wave 190, Zacian 649/649, Master Ball held since w154). No farm process running. Per rules, watch did not restart and sent no game input.

## 2026-10-31 12:26 MDT - watch run: Eternatus run over; Gavin started a new Eternatus-led run
- After the 12:15 user_stop at w190, the Zacian run was finished by hand. At 12:25:13 Gavin launched pr_farm17.py from PokeFarmControl (PID 63200) on a new run with Eternatus (890) as the solo lead, which means Eternatus was caught. Farm healthy at w2. Watch sent no game input.
- PENDING: revert the temporary Master Ball changes (REROLL_CHEAP_FRAC 0.20 -> 0.10, REROLL_MAX 8 -> 5, the master_ball special, backups *.bak_mb_20261031_1114). Deferred because Gavin is actively driving and the revert needs a farm restart; do it on a later watch once things are idle.

## 2026-10-31 12:31 MDT - executor ACTIVE: Eternatus candy-grind setup (revert MB changes, eternatus profile, restart)
- In progress: reverting master_ball special / reroll 20%/8 / eternatus_catch stop; adding profiles/eternatus.json; reading candy data; then a safe restart. Watch: do not restart or intervene while this entry is the latest.

## 2026-10-31 12:42 MDT - executor: Eternatus grind setup done; farm NOT running (Gavin driving by hand)
- Rerolls back to 10% / max 5 (Gavin t140u). Master Ball special -400 KEPT and now also added to the project item_priority.json (it was missing there, so it was not live before), wave-200 eternatus_catch stop KEPT. ITEM_PRIORITY.md regenerated. Backups *.bak_et_20261031_1231, pr_farm17.py.bak_learnscore_20261031_1235.
- New profiles/eternatus.json with learn_mode=score (Gavin t141u): score = power x acc x STAB 1.5 (Poison/Dragon) x stat ratio (Atk 85 / SpA 145) x 0.6 recharge x 0.8 self-drop + 8 per newly covered SE type; replace weakest non-protected if >10% better; never drop last damaging STAB; protected Dynamax Cannon + Eternabeam. LEARN logs show both scores. SOLO EARLY DEATH log line added.
- Restart: stopped 12:35:57 via flag; hidden relaunch 12:36:09 aborted (page at Title after a reload). At 12:41 the run is at w19 in a hand-driven item-transfer screen with a new Tarountula, no farm process. Left for Gavin; restart from PokeFarmControl when done (code is already patched on disk).

## 2026-10-31 12:45 MDT - watch run: farm still not running, Gavin hand-driving
- No farm process, no stop flag; last log 12:36:09 ABORT not Classic. Per the 12:42 entry Gavin is hand-driving the w19 run (item transfer, new Tarountula). Watch sent no game input. Patched code is on disk; restart from PokeFarmControl or on a later watch once the game sits idle 10+ min.

## 2026-10-31 12:48 MDT - watch run: game advancing without the farm (another controller)
- No pr_farm process and no stop flag, but the game went from w19 (12:41) to w55 (12:47, trainer Ivy sending out Sceptile); party Eternatus 190/190, Spidops 55/88. Someone else is actively driving (Gavin or another session). Watch sent no game input. Patched code on disk; restart only once the game sits idle 10+ min.

## 2026-10-31 12:55 MDT - watch run: still driven by another controller
- No pr_farm process, no stop flag; game moved w67 -> w72 in ~1 min (party Eternatus, Spidops, Gengar). Watch sent no game input.

## 2026-10-31 13:00 MDT - watch run: still driven by another controller
- No pr_farm process, no stop flag; game moved w76 -> w77 in ~25 s (party Eternatus 210/273, Gengar, Spidops). Watch sent no game input (added read-only helper %TEMP%\prfarm\_wave_ro.py).

## 2026-10-31 13:03 MDT - watch run: still driven by another controller
- No pr_farm process, no stop flag; game moved w90 -> w91 in ~15 s (party Spidops, Gengar, Eternatus; page reloaded ~1.5 min earlier). Watch sent no game input.

## 2026-10-31 13:12 MDT - watch run: game being driven by hand (Pokedex open)
- No pr_farm process, no stop flag; page reloaded (no hook), screen changing between checks, now on the Pokedex entry for Eternatus (E-Max form). Someone is actively using the game. Watch sent no game input.

## 2026-10-31 13:17 MDT - watch run: someone on starter select by hand
- No pr_farm process, no stop flag; page has no hook, screen changed between two checks 15 s apart, now on starter select (Drifloon highlighted, 0/10 party). Someone (likely Gavin) is setting up a run by hand. Watch sent no game input.

## 2026-10-31 13:23 MDT - watch run: game still driven by hand (Pokedex browsing)
- No pr_farm process, no stop flag, page has no hook (reloaded); screen changed between two shots 15 s apart (Pokedex, Garchomp entry menu). Someone is using the game. Watch sent no game input.

## 2026-10-31 13:28 MDT - watch run: someone on starter select by hand
- No pr_farm process, no stop flag, page has no hook; screen changed between two shots 15 s apart (starter select, Capsakid highlighted, 0/10 party). Someone is setting up a run by hand. Watch sent no game input.

## 2026-10-31 13:36 MDT - watch run: Gavin on starter select by hand
- No pr_farm process, no stop flag, page has no hook; screen changed between shots 15 s apart (starter select, 0/10 cost, cursor on Spheal). Watch sent no game input.

## 2026-10-31 13:40 MDT - watch run: Gavin still on starter select by hand
- No pr_farm process, no stop flag, page has no hook; screen changed between shots 15 s apart (starter select, Caught filter, cursor on Lugia, 0/10 cost). Watch sent no game input.

## 2026-10-31 13:43 MDT - watch run: starter select, cursor unchanged since 13:40
- No pr_farm process, no stop flag, page has no hook; starter select, Caught filter, cursor still on Lugia, 0/10 cost (same as the 13:40 watch). Shot md5s differ but that may just be sprite animation. Watch sent no game input. If the cursor/screen is still identical at ~13:50+ (10+ min idle), consider the game idle and decide on resuming (likely tell Gavin once rather than taking over a hand-started setup).

## 2026-10-31 13:49 MDT - watch run: new Lugia run being played by hand
- No pr_farm process, no stop flag, log still ends 12:36:09 ABORT. Game is now in battle at Plains wave 18 with Lugia Lv16 (61/64) leading and Zigzagoon in the party; screen changed between shots 15 s apart. Someone (likely Gavin) started a new run with Lugia and is driving it. Watch sent no game input. Note: Lugia has no profile yet (profiles/ has zacian, rayquaza, eternatus) if the farm is resumed on this run.

## 2026-10-31 13:52 MDT - executor ACTIVE: Lugia run setup + farm restart (Gavin voice)
- Executor is the controller now (watch: do not restart/act). Game: fresh Classic run, w18, Lugia/Milotic/Kricketot/Spinda/Zigzagoon.
- Config: add "primary":"Lugia" (candy_target already "primary"). New profiles/lugia.json (score mode, primary_move Aeroblast, protected Aeroblast+Lumina Crash, Air Cutter > Weather Ball by score). Farm logic unchanged. Safe restart of pr_farm17.

## 2026-10-31 13:53 MDT - watch run: executor active (Lugia setup), no action
- The 13:52 entry shows an executor is currently the controller (Lugia profile + pr_farm17 safe restart). Watch sent no game input and made no changes.

## 2026-10-31 13:55 MDT
- Correction to the 13:52 entry: the farm was NOT restarted (the launch was interrupted, nothing started). Gavin is playing the Lugia run by hand. No session is driving the farm now. Config primary=Lugia and profiles/lugia.json are in place. Do not take over; wait for Gavin to press Start or say go.

## 2026-10-31 13:57 MDT - watch run: Gavin playing Lugia run by hand, no action
- No pr_farm process, no stop flag, log still ends 12:36:09 ABORT. The 13:55 entry (another session, 2 min ago) says Gavin is driving the Lugia run by hand and to wait for his Start/go. Config primary=Lugia in place. Watch sent no game input and made no changes.

## 2026-10-31 14:19-14:22 MDT - watch run: caught wild shiny Camerupt w99 (Lugia run)
- Farm stopped 14:18:08 on shiny_enemy Camerupt (single wild, Lv67, not a boss, 175/175). Waited past 2 min (GAVIN GOES FIRST); state unchanged at 14:20:21, no farm process, no other controller.
- New helper dbl_shiny2.py (copy of dbl_shiny.py; ball mode prefers Rogue > Ultra > Great > Poke, never Master). Rogue Balls 0, so threw 1 Ultra Ball (5 -> 4): caught first throw. catch_ack.py dismissed Gotcha; party had 5, joined as 6th. Logged in CHIE Shiny Log.md.
- Cleared flag/reasons, rotated stdout, launched hidden via pr_farm_launch_hidden.py (Win32_Process Create pythonw PID 96044, parent WmiPrvSE). One instance, w101 by 14:21:41.

## 2026-10-31 14:26-14:32 MDT - watch run: caught wild shiny boss Crustle w110 (Lugia run)
- Farm stopped 14:24:09 on shiny_enemy Crustle (single wild boss, Lv87, 2 segments, Shell Armor, 227/227). Waited past 2 min (GAVIN GOES FIRST); state unchanged at 14:26:15, no farm process, no other controller.
- Lugia's weakest safe option (Lumina Crash, resisted, STAB) estimated 115-135, more than half, so switched Lugia out (new helper dbl_shiny3.py = dbl_shiny2.py + modes sw FIELD PARTYIDX / pty PARTYIDX / ok for faint-switch). Linoone High Horsepower 46 (227->181), Linoone fainted; Spinda Superpower 57 (->124), Spinda fainted; Camerupt Flame Wheel was clamped at the shield line (->114, bossSegmentIndex 0 = shield broken). Note: the game clamps a hit at the segment boundary.
- 1 Ultra Ball (4 -> 3, no Rogue Balls): caught first throw. Party full, krook_no.py pick chose No, so Crustle went to storage. Logged in CHIE Shiny Log.md.
- Relaunched hidden 14:31 (PID 170276); farm advanced to w112; Linoone and Spinda are fainted (helpers), Lugia benched and should switch back in via ZACIAN SWITCH-IN.

## 2026-10-31 14:37-14:51 MDT - watch run: Lugia run ended w120 (wipe, slot 2), run-end done, new Lugia run slot 2
- Farm exited 14:37:51 "PRIMARY Lugia FAINT ... DONE farm17" at w120 (Gym Leader Marlon: Feraligatr, Carracosta, Mantine, Jellicent, Wailord, Seismitoad). Lugia fell first, then Milotic, Linoone, Kricketot, Camerupt, Spinda. A live read right after the exit showed Spinda at 96 HP, so I treated the exit as premature and relaunched; on relaunch the all-faint was real (all 6 at 0).
- Patch pr_farm17.py (backup pr_farm17.bak_allfaint.py): the all-party-fainted stop now needs about 14 consecutive faint reads (~6 s) before breaking, logging "ALL-FAINT read ... rechecking (transient?)", so a transient party read can't end a run early.
- to_title.py reached the title; open_gacha.py + gacha_all.py: 15 regular + 3 Plus vouchers -> eggs 0 -> 30. Vouchers 0/0/0/0. No hatches.
- Lugia candy 9 (valueReduction 1, passive not owned). Menu: x10 Unlock Passive, x15 Reduce Cost to 6, x6 Buy an Egg. Per LUGIA order (reductions first) nothing bought, candy saved. Feebas all owned (passive 3, reductions 2), candy 21 untouched.
- New Classic slot 2 (empty; slots 0/1 untouched): nr_pick.py 249,349,263,401,327 all added. Start path this time: setCursor(35), Right, Down x3 (startCursorObj visible), ACTION, Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2, party [249,349,263,401,327].
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (full pythonw path) PID 62956, parent 113808 (same WMI host). One instance, w5 by 14:50.

## 2026-10-31 15:18 MT — Encounter editor installed + farm wired to encounter_rules.json
- Installed encounter editor (cloud-agent package, rules v1) to `..PROJECT\pokerogue\encounter_editor` (launcher: `Encounter Editor.pyw`, http://127.0.0.1:8766/, no console). Live rules: `..PROJECT\pokerogue\encounter_rules.json`; readable table `ENCOUNTER_RULES.md`. Editor saves back up to `encounter_rules_backups\`.
- pr_farm17.py (backup `pr_farm17.py.bak_encrules_20261031_151747`): MysteryEncounterUiHandler non-safety branch now picks via `encounter_rules.py` (copied to %TEMP%\prfarm, reloads on file mtime). Falls back to TOP option on missing file/entry, error, or an option whose requirements fail.
- Hardcoded rules still win over the file: TRADE BLOCK (Dark Deal/GTS/Weird Dream/any trade -> leave), team-transform text -> leave, Shady Vitamin Dealer -> pricey else leave, Training Session -> leave, Mysterious Chest -> open. Ability-teach prompts (OptionSelect) unchanged -> No. Follow-up slots (which Pokémon etc.) not wired yet.
- Safe restart 15:18 MT at wave 83 via stop flag; relaunched hidden, PID 54208 (launcher), advancing (w87 at 15:19).

## 2026-10-31 15:22 MT — Lugia: one Psychic move only (Gavin t148u)
- profiles/lugia.json: protected Aeroblast, Lumina Crash, Ancient Power, Air Slash; decline_moves (Future Sight, Extrasensory, Stored Power, Psychic, Psycho Cut, Zen Headbutt); max_one_damaging_of_types [13]; avoid_in_battle [Future Sight]. Old profile backed up as lugia.json.bak_lugiapsy_20261031_152139.
- pr_farm17.py (patched on top of live 15:17:47 copy, backup pr_farm17.py.bak_lugiapsy_20261031_152139): PROFILE_DEFAULT new keys; learn_score declines decline_moves and a 2nd damaging move of a capped type; extra unprotected capped-type move (e.g. Future Sight) is the replacement target for any acceptable uncapped new move; pick_move skips avoid_in_battle moves unless nothing else damaging has PP (logs "AVOID skip"). py_compile OK. Copied to ..PROJECT\pokerogue\scripts.
- Restart: stopped old farm 15:24:35 (w95), relaunched PID 148884 at 15:24:50 (loaded new profile), then a user_stop (stop flag + reason, 15:25:00, not from this agent) ended it at 15:25:04; page then showed wave 0 / empty party. NOT relaunched. Farm is STOPPED.

## 2026-10-31 15:56-15:57 MT - watch run: Lugia run ended w140, Gavin setting up next run by hand
- Farm exited 15:52:59 "PRIMARY Lugia FAINT ... DONE farm17" at w140 (trainer with Mr. Mime / Espeon); all 6 at 0 HP after 2 ALL-FAINT rechecks.
- By 15:56 the game was already on starter select (6/10 cost) and the cursor moved 63 -> 3 within 15 s, so someone (Gavin) is driving. Lugia candy 0, valueReduction 2, vouchers 7 regular + 1 Plus unspent, eggs 1. No farm process, no stop flag. Sent no game input. Next watches: don't take over; resume only after 10+ min idle and a clear state.

## 2026-10-31 15:58 MT - Lugia fixed loadout (Gavin t154u)
- lugia.json learn_mode=fixed, replace_map {Aeroblast: Weather Ball, Air Slash: Air Cutter}. Current set Lumina Crash/Aura Sphere/Ancient Power/Weather Ball. Only Aeroblast (Lv71) replaces Weather Ball; all else declined + logged. pr_farm17.py learn_decide fixed branch, py_compile OK. Not restarted.

## 2026-10-31 16:00 MT - Lugia flex slot (Gavin t155u)
- replace_map removed; flex_final=Aeroblast, flex_types=[2]; protected Lumina Crash/Aura Sphere/Ancient Power. Flying offers replace flex slot (Weather Ball) if score > x1.10; Aeroblast always; then decline all. pr_farm17.py fixed branch rewritten, py_compile OK. Not restarted.

## 2026-10-31 16:10-16:11 MT - watch run: safe restart to load Lugia flex-slot code
- Farm (PID 27356, started 15:55:52 from PokeFarmControl) predated the 15:59:38 pr_farm17.py / lugia.json edits. Untouched 10+ min, so safe restart at w46 via stop flag (reason agent_safe_restart, exited 16:10:17).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 95596, parent WMI host 113808). One instance; w47 -> 48 by 16:11:13.

## 2026-10-31 16:16-16:25 MT - watch run: Lugia run ended w50 (wipe, slot 2), run-end done, new Lugia run slot 2
- Farm exited 16:12:57 "PRIMARY Lugia FAINT ... DONE farm17" at w50 (Ancient Ruins, Gallade Lv35, Steadfast); Lugia (Lv39) fell first, then the rest one by one; 2 ALL-FAINT rechecks, game on "Sinistea fainted!". No other controller active.
- to_title.py -> title; open_gacha.py + gacha_all.py: 11 regular + 1 Plus vouchers -> eggs 0 -> 16 (one tier-3 egg). Vouchers 0. No hatches.
- Lugia candy 2 (valueReduction 2 = both reductions owned, passive not owned, too few candy): nothing bought. Feebas candy 10 (passive 3, reductions 2) untouched.
- New Classic slot 2 (empty; slots 0/1 untouched): nr_pick.py 249,349,263,401,327,854 all added. Start path with a 6-mon party: setCursor(35), Right, then Up x4 (Down/Up cycles party column -> Random -> filter -> Start). Yes, save slot cursor 2. Verified modeId 0, wave 1, sessionSlotId 2, party [249,349,263,401,327,854].
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 162940).

## 2026-10-31 16:56-17:04 MT - watch run: caught wild shiny Manectric w52 (double)
- Farm stopped 16:55:34 on shiny_enemy Manectric (wild double with Electabuzz Lv34; Manectric Lv36, not a boss, 99/99). Waited past 2 min (16:57:46), state unchanged, no other controller.
- dbl_shiny.py: Lugia Lumina Crash (single target) on Electabuzz (BattlerIndex 2), Feebas Calm Mind. Electabuzz KO'd, Manectric untouched.
- Balls held: only Poke Balls (Rogue/Ultra/Great 0). Poke Ball x3 (5 -> 2): two broke free, third caught. Feebas fainted to Manectric between throws; dbl_shiny3.py pty 4 + ok sent Spinda in. Party full, krook_no.py pick -> No, Manectric went to storage. Logged in CHIE Shiny Log.md.
- Note: ball stock is low (Poke 2, no Rogue/Ultra/Great); balls are ranked junk while any ball is held, so the next shiny may run out.
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 148968, parent WmiPrvSE). One instance, w54 by 17:03.

## 2026-10-31 17:12-17:14 MT - watch run: Lugia run ended w66 (wipe), Gavin already started next run by hand
- Farm exited 17:10:43 "PRIMARY Lugia FAINT ... DONE farm17" at w66 (Lugia fell; Spinda/Linoone/Kricketot/Sinistea switched in vs Crustle then Beheeyem; 2 ALL-FAINT rechecks).
- By 17:12 the game was already in a NEW Classic run at wave 1 (playTime 3s), lineup Lugia, Feebas, Kricketot, Spinda, Zigzagoon, Nosepass (Nosepass replaced Sinistea), so Gavin set it up himself. Run-end voucher/candy steps not verified by this agent. No farm process, no stop flag. Sent no game input. Next watches: don't take over; resume (launch farm on this run) only after 10+ min idle and a clear state.

## 2026-10-31 18:25-18:37 MT - watch run: Lugia run ended w91 (wipe, slot 2), run-end done, new Lugia run slot 2
- Farm exited 18:20:50 "PRIMARY Lugia FAINT ... DONE farm17" at w91 (Desert, wild double Brambleghast + Dodrio). Lugia fell first, then the rest; live scene read confirmed all 6 at 0 HP, game idle on the message, no other controller.
- to_title.py -> title; open_gacha.py + gacha_all.py: 7 regular + 2 Plus vouchers -> eggs 0 -> 17. No hatches. Gacha exit: B doesn't leave the machine menu; move cursor to Cancel (index 5) and ACTION.
- Lugia candy 9 (valueReduction 2 = both reductions owned, passive not owned, costs 10): saved for passive, nothing bought. Feebas candy 23 (passive 3, reductions 2) untouched.
- New helper gx2.py (button sequence + "e:<js>" evals, prints handler/options). Load Game list: slots 0/1 Endless data, 2-4 empty. New Game -> Classic (idx 0) -> nr_pick.py 249,349,263,401,327,299 (Gavin's latest hand lineup with Nosepass) -> setCursor(35), Right, Up until startCursorObj visible -> Yes -> slot 2. Verified modeId 0, sessionSlotId 2, wave 1.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 157660, parent WMI host 113808). One instance, w4 by 18:36.

## 2026-10-31 18:43-18:57 MT - watch run: w27 reward-screen stall fixed (Lugia run, slot 2)
- Lugia fainted in the w27 Mysterious Chest ME; shop revived it, then the reward pick chose Max Revive (GREAT tier beats COMMON) with nobody fainted. The party-target code found no target and pressed X ~80 times; that left ModifierSelectUiHandler.onActionInput = null, so every later Z did nothing (STALL x450).
- After a restart the farm resolved PRIMARY = Zigzagoon (Lugia had been switched out, so Zigzagoon was slot 0). Added "primary": 249 to agent-tools\pokerogue_farm_config.json (candy_target/secondary_field untouched).
- Patches to pr_farm17.py (backups bak_revnone_1845, bak_revrank_1848, bak_smcb_1855):
  - REVIVENONE (pick_reward): when no party member is fainted, revive/Sacred Ash rewards are dropped from the pick list (Reviver Seed excluded) if anything else is offered.
  - REVIVENONE (party target): revive with no fainted target -> blacklist that reward for the wave and re-pick instead of looping on X.
  - SMCB (stall handler): on a ModifierSelectUiHandler stall >= 25 with onActionInput null, rebuild the phase callback (reward/shop/reroll/transfer/lock) and call phase.resetModifierSelect(cb).
- Unstuck live by the same callback rebuild; the run moved on to w28 at 18:53. Restarted hidden (Win32_Process Create, parent WMI host), one instance. Script copied to ..PROJECT\pokerogue\scripts.

## 2026-10-31 19:10-19:18 MT - watch run: Lugia run ended w66 (wipe, slot 2), Lugia PASSIVE bought, new Lugia run slot 2
- Farm exited 19:08:00 "PRIMARY Lugia FAINT ... DONE farm17" at w66 (wild Claydol after Raichu/Medicham; Lugia fell first, rest switched in). Live read: all 6 at 0 HP, MessagePhase idle, no other controller.
- to_title.py -> title; open_gacha.py + gacha_all.py: 5 regular + 1 Plus vouchers -> eggs 0 -> 10. Vouchers 0. No hatches. Exit: setCursor(5)+ACTION, then CANCEL -> title.
- Lugia candy 11 (both reductions owned): bought x10 Unlock Passive (passiveAttr 0 -> 3), candy 11 -> 1. Egg (x6) unaffordable. Lugia upgrades now all owned; future candy -> Lugia eggs. Use Candies is option index 7 in Lugia's menu. Feebas candy 33 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,263,401,327,299 -> setCursor(35), Right, Up x5 until startCursorObj visible -> ACTION, Yes -> save slot (cursor 1 + scroll 1 = slot 2, empty; slots 0/1 untouched). Verified modeId 0, sessionSlotId 2, wave 1.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 134024, parent WMI host 113808). One instance, w5 by 19:17.

## 2026-10-31 19:25-19:28 MT - watch run: caught wild shiny Magikarp w27 (Lugia run)
- Farm stopped 19:23:02 on shiny_enemy Magikarp (single wild, Lv17, not a boss, 37/37). Waited past 2 min; state unchanged at 19:25:41, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Magikarp: Rogue Ball (5 -> 4) caught first throw. catch_ack.py, then party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md.
- Flags cleared, farm relaunched hidden (PID 44252, parent WmiPrvSE), advancing at w29.

## 2026-10-31 19:34-19:39 MT - watch run: caught wild shiny Krabby w37 (double, Lugia run)
- Farm stopped 19:30:02 on shiny_enemy Krabby (wild double with Mareanie Lv22; Krabby Lv25, not a boss, 55/55). Past 2 min at 19:33, state unchanged, no farm process, no other controller.
- dbl_shiny.py: Lugia Lumina Crash (single target) on Mareanie (BattlerIndex 2), Feebas Calm Mind. Mareanie KO'd, Krabby untouched. Acked messages with dbl_shiny.py ack.
- Rogue Ball (4 -> 3) caught first throw. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md.
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (PID 131924, parent WMI host 113808). One instance, w38 by 19:38.

## 2026-10-31 19:47-19:55 MT - watch run: caught wild shiny Arctovish w54 (double, Lugia run)
- Farm stopped 19:46:09 on shiny_enemy Arctovish (wild double with Barraskewda Lv38; Arctovish Lv36, not a boss, Ice Body, 114/114). Past 2 min at 19:48:32, state unchanged, no farm process, no other controller.
- dbl_shiny.py: Lugia attacked only Barraskewda (BattlerIndex 3), Linoone used Tidy Up. Turn 1 Lumina Crash and turn 3 Aura Sphere did no damage (likely Protect on alternate turns); turn 2 and turn 4 Aura Sphere landed, Barraskewda KO'd. Arctovish never hit.
- Lugia fainted to Arctovish later in that turn; dbl_shiny3.py pty 4 + ok sent Spinda in. Rogue Ball (8 -> 7) caught first throw. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md.
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (PID 138620, parent WMI host 113808). One instance; Lugia revived, w55 (Rival Ivy) by 19:54.

## 2026-10-31 20:18-20:21 MT - watch run: LOST wild shiny Dugtrio w73 (double, Lugia run)
- Farm stopped 20:15:08 on shiny_enemy Dugtrio (wild double with non-shiny Dugtrio Lv49 Arena Trap; shiny Lv50, not a boss, 110/110). Past 2 min at 20:18, state unchanged, no farm process, no other controller.
- Turn 1: Lugia Lumina Crash on partner (94 -> 7), Milotic Calm Mind; partner's Earthquake hit the shiny (110 -> 23). Turn 2: Lugia Ancient Power on partner, but the partner moved first and its Earthquake KO'd the shiny. No ball possible with two foes up.
- LESSON: in a double where the partner has a spread move (Earthquake etc.), the partner can KO the shiny. Consider KOing the partner with the strongest single-target move on turn 1 and checking whether the partner is faster (Lugia 142 Spe still moved after Dugtrio).
- Logged as not caught in CHIE Shiny Log.md. Cleared flag/reason/stopped_reason, rotated stdout, launched hidden (PID 129188, parent WMI host 113808). One instance, w74 by 20:20:48.

## 2026-10-31 20:30-20:36 MT - watch run: caught wild shiny Scovillain w77; STEP_JS tween-time fix
- Farm stopped 20:24:41 on shiny_enemy Scovillain (single wild, Lv56, not a boss, Insomnia, 153/153). Past 2 min at 20:30, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Scovillain: Rogue Ball (7 -> 6). The capture then froze in AttemptCapturePhase: the tab was hidden (visibilityState hidden even after front.py), and the old STEP_JS advanced the game loop but not the TweenManager, whose delta comes from real Date.now() (gap > maxLag 500 -> lagSkip), so tweens never progressed.
- New PC helpers step2.py / step3.py (step3 ... ack): step loop that sets scene.tweens.prevTime = Date.now()-16.7 before each L.step. Capture finished: "Gotcha! Scovillain was caught!". Party full, krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md.
- PATCH pr_farm17.py STEP_JS (backup pr_farm17.bak_tweenstep.py): same prevTime fix inside the 45-frame step loop, so a hidden tab no longer stalls tween-driven phases.
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden (pythonw PID 21948, parent WMI host 113808). One instance, w78 by 20:35:51.

- 2026-10-31 20:55 MT: PokeFarmControl status line now shows active Primary and Secondary (name HP/max) instead of hardcoded 'Zacian HP'. Control app only; farm not restarted.

## 2026-10-31 21:24-21:32 MT - watch run: Lugia run ended w164 (wipe, slot 2), 1 Lugia egg bought, new Lugia run slot 2
- Farm exited 21:22:03 "PRIMARY Lugia FAINT ... DONE farm17" at w164 (Cave; Clawitzer, Crobat, then Malamar Contrary; Nosepass last). Live scene read: all 6 at 0 HP, MessagePhase idle, no other controller. (gameInfo briefly showed Nosepass 63/296; stale.)
- to_title.py -> title; open_gacha.py + gacha_all.py: 11 regular + 4 Plus vouchers -> eggs 0 -> 31. Vouchers 0. No hatches. Exit: ui.py c5 b5 b6 -> title.
- Lugia candy 8 (all upgrades owned): Use Candies (index 8 this time) -> x6 Buy an Egg once, candy 8 -> 2, eggs 32. Feebas candy 67 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,263,401,327,299 -> ui.py c35 b3 then b0 x6 until startCursorObj visible -> b5, Yes -> save slot b1 b1 (cursor 1 + scroll 1 = slot 2, empty; slots 0/1 untouched). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 144240, parent WMI host 113808). One instance, w5 by 21:32.

## 2026-10-31 22:41 MDT — shiny logs newest-first
- Sorted Shiny Log.md (73), Shiny Egg Log.md (16), PokeRogue Shiny Egg Log.md (3) and box SHINY_LOG.md newest-first by Date (MDT); .bak_ backups kept.
- pr_farm17.py: new md_insert_top(); egg_append_md now inserts new rows directly under the table separator (TEMP, scripts, box copies). Farm not restarted.

## 2026-10-31 23:21-23:26 MT - watch run: Lugia run ended w39 (wipe, slot 2), new Lugia run slot 2
- Farm exited 23:20:45 "PRIMARY Lugia FAINT ... DONE farm17" at w39 (Absolute Avarice ME, "Battle It" vs Greedent; Lugia fell first, the rest switched in one by one; 2 ALL-FAINT rechecks). Farm had been launched 23:07 from PokeFarmControl; no other controller active.
- to_title.py -> title. Vouchers 13 regular left UNSPENT (Gavin t165u). Lugia candy 4 (all upgrades owned; egg costs 6): nothing bought. Feebas candy 13 (all owned) untouched. Eggs 1.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> setCursor(35), Right, Up x5 (startCursorObj visible; Up x7 overshoots, Down x2 back) -> ACTION, Yes -> save slots [0,1 data; 2-4 empty] -> Down x2 (cursor 1 + scroll 1 = slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 8640, parent WMI host 113808). One instance, w6 by 23:25:40.

## 2026-10-31 23:41-23:46 MT - watch run: Lugia run ended w50 (wipe, slot 2), 1 Lugia egg bought, new Lugia run slot 2
- Farm exited 23:40:33 "PRIMARY Lugia FAINT ... DONE farm17" at w50 (trainer battle; Toxtricity Punk Rock + Houndstone left; Lugia fell first, the rest switched in one by one). Live scene read: all 6 at 0 HP, MessagePhase. No other controller.
- to_title.py -> title. Vouchers 16 regular left UNSPENT (Gavin t165u). Lugia candy 8 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg once, candy 8 -> 2, eggs 0 -> 1. Feebas candy 20 (all owned) untouched.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> c35, Right, Up x5 (startCursorObj visible) -> ACTION, Yes -> save slots [0,1 data; 2-4 empty] -> Down x2 (cursor 1 + scroll 1 = slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 141692, parent WMI host 113808). One instance, w7 by 23:45:35.

## 2026-10-31 23:54-23:58 MT - watch run: Lugia run ended w23 (wipe, slot 2), new Lugia run slot 2
- Farm exited 23:51:47 "PRIMARY Lugia FAINT ... DONE farm17" at w23 (wild Gimmighoul, Rattled; Lugia fell first, the rest switched in one by one, 2 ALL-FAINT rechecks). Live scene read: all 6 at 0 HP, MessagePhase. No other controller.
- to_title.py -> title. Vouchers 17 regular + 1 Plus left UNSPENT. Lugia candy 2 (egg costs 6): nothing bought. Feebas candy 24 (all owned) untouched. Eggs 1.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> c35, Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Rotated stdout, launched hidden via Win32_Process Create (pythonw PID 64412, parent WMI host 113808). One instance, w5 by 23:58.

## 2026-11-01 00:05 MT - pr_farm17 EARLYWIPE patch (3 early Lugia wipes w39/w50/w23)
- w39 (23:20): absoluteAvarice -> RULES "Battle It" vs boss Greedent; Lugia (119 max HP) fainted on turn 4, bench swept. FIX: hardcoded absoluteAvarice -> first available non-battle option.
- w50 (23:40): Part-Timer ME at w42 ("Make Deliveries") sent Lugia (ME party select always picks primary) and drained its PP: Aura Sphere 13->2/20, Air Cutter 20->2/25. w43 Ether then skipped ("pp ok": pp_crit only fired at total dmg PP<=3). Lugia died at w50 to Houndstone. FIX: partTimer party select -> bench ally (not primary/secondary); pp_crit also true when 2+ damaging moves are <=3 PP or <15%.
- w23 (23:51): mysteriousChest opened (hardcoded) -> Gimmighoul trap KO'd Lugia before any turn; bench lost. Not changed (chest-open is Gavin's hardcoded rule) - flagged.
- Contributing: candy_target=secondary sends all Rare Candy to Feebas/Milotic, so Lugia is underleveled (68 HP at w23). No move-choice immunity bug for Lugia found; Spinda used 0-eff Tackle vs Ghost only because its other moves were also immune/status.
- Backup: %TEMP%\prfarm\pr_farm17.bak_earlywipe_*.py. py_compile OK.

## 2026-11-01 00:10-00:15 MT - watch run: Lugia run ended w16 (wipe, slot 2), new Lugia run slot 2
- Farm exited 00:03:52 "PRIMARY Lugia FAINT ... DONE farm17" at w16 (wild Qwilfish, Poison Point; Lugia fell first, the rest switched in one by one, 2 ALL-FAINT rechecks). Live scene read 00:10: all 6 at 0 HP, MessagePhase, idle. Ran on the earlywipe-patched pr_farm17 (00:00/00:02 edits). 4th early wipe in a row (w39, w50, w23, w16).
- to_title.py -> title. Vouchers 17 regular + 2 Plus left UNSPENT. Lugia candy 3 (egg costs 6): nothing bought. Feebas candy 25 (all owned) untouched. Eggs 1.
- New Game (straight to starter select, modeId 0 Classic) -> nr_pick.py 249,349,263,401,327,299 -> c35, Right, Up x5 (startCursorObj visible) -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (cursor 1 + scroll 1 = slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 49504, parent WmiPrvSE). One instance, w6 by 00:14:22.

## 2026-11-01 00:43-00:47 MT - watch run: wild shiny Claydol w81 (double, Lugia run) - Explosion, then page reload; left to Gavin
- Farm stopped 00:40:47 on shiny_enemy Claydol (wild double; shiny Claydol Lv58 variant 1, Levitate, 150/150, not a boss; partner Beheeyem Lv57 164/164). Past 2 min at 00:43, state unchanged, no farm process, no other controller.
- Turn 1: Lugia Air Slash on Beheeyem (164 -> 98), Feebas Calm Mind. Claydol then used EXPLOSION (moveset: Earth Power, Explosion, Heal Block, Imprison): Claydol fainted, Beheeyem 29, Lugia 190, Feebas 42.
- Cleared flag/reasons, rotated stdout, launched hidden (PID 6660). At ~00:44:42 the page was reloaded externally (not by the farm; possibly Gavin), farm pressed Continue, wave 81 restarted from save with shiny Claydol back at full HP, farm stopped again 00:44:52 shiny_enemy. Per GAVIN GOES FIRST (a reload = Gavin handling it), no further input sent. Shiny Log row not added yet (outcome pending).
- LESSON: a shiny with Explosion/Self-Destruct can KO itself on turn 1; no rule covers this yet.

## 2026-11-01 00:52 MT - watch run: Gavin handled shiny Claydol w81 himself (00:44-00:51), relaunched farm from PokeFarmControl at 00:51:34 (PID 92440); farm healthy at w83, one instance. Claydol outcome unknown (not in party), no Shiny Log row yet.

## 2026-11-01 00:58 MT - watch run: Lugia run w90 (gauntlet), no input sent
- Farm (PID 92440, started 00:51:33) re-selected Aeroblast every ~1.3 s vs Alakazam from 00:54:42 to ~00:58:10 with no turn advancing (PP stayed 2/5), then recovered on its own and kept fighting (w90 Espathra/Florges, Lugia 101/263). Possible cause to verify: a move-lock (Disable/Imprison/Encore) not detected, so the farm keeps picking a blocked move.
- pr_farm17.py was edited at 00:54:42 by another session (box copy 00:55), after this instance started; no restart done by the watch since another session was active.

## 2026-11-01 01:04 MT - watch run: safe restart to load the 00:54 pr_farm17 patch
- Farm (PID 92440, PokeFarmControl launch 00:51) was healthy at w98 but older than the 00:54:42 script edit (chest ban / candy_target). No edits or other activity for ~10 min, no shiny, not eternatus_catch.
- Killed 92440, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 108476, parent WmiPrvSE 113808). One instance; w100 -> 101 by 01:04:26, fighting normally. Claydol w81 already logged as Missed.

## 2026-11-01 01:19-01:24 MT - watch run: Lugia run ended w112 (wipe, slot 2), 2 Lugia eggs bought, new Lugia run slot 2
- Farm exited 01:17:32 "PRIMARY Lugia FAINT ... DONE farm17" at w112 (wild Dugtrio/Camerupt; Lugia fell first, bench switched in, Spinda last; 2 ALL-FAINT rechecks). Live scene: all 6 at 0 HP, MessagePhase. No other controller.
- to_title.py -> title. Vouchers 21 regular + 2 Plus + 1 Premium left UNSPENT. Lugia candy 13 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg twice, candy 13 -> 1, eggs 0 -> 2. Feebas candy 48 (all owned) untouched.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> c35, Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 94948, parent WmiPrvSE 113808). One instance, w3 by 01:24.

## 2026-11-01 01:05-01:11 MST (second 1 AM, after DST ended) - watch run: caught wild shiny Brionne w45 (Lugia run)
- Farm stopped 01:05:14 on shiny_enemy Brionne (single wild, Lv27, variant 1, not a boss, 72/72). Waited past 2 min; state unchanged at 01:07:34, no farm process, no other controller.
- Only Poke Balls held (Rogue/Ultra/Great 0, Master 2 kept for Eternatus). No attack (Lugia's weakest hit would likely KO). dbl_shiny2.py ball Brionne: throw 1 broke free (10 -> 9), throw 2 caught (9 -> 8). New read helper cap_rd.py N (read + N frame steps, read-only otherwise).
- catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (sprite pr_729s.png downloaded).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 155536, parent WmiPrvSE 113808). One instance, w46 by 01:10:46.

## 2026-11-01 01:40-01:46 MST - watch run: MEFIGHT patch (Expert Breeder ME stuck on a 0-PP move)
- w63 theExpertPokemonBreeder ME (option 1 -> Linoone solo vs Marill). The ME-without-primary branch just pressed Z, so from ~01:36 the fight menu kept re-confirming High Horsepower at 0/10 PP (turn 11 never advanced; Extreme Speed 5/5 unused).
- FIX 1: in that branch, on FightUiHandler, pick_move() on the active member and set_cursor before Z (logs "ME fight ...").
- FIX 2: the restart mid-ME resolved PRIMARY = Linoone (config primary 249 absent, fell back to first bench mon); one Soothe Bell went to Linoone at w63. resolve_primary now returns None while a configured primary is absent, so it waits for Lugia instead.
- Backup %TEMP%\prfarm\pr_farm17.bak_mefight_20261101_0145.py. py_compile OK. Relaunched hidden (PID 132912, parent WmiPrvSE): Lugia resolved from lugia.json, fighting w64.

## 2026-11-01 03:05-03:11 MST - watch run: Lugia run ended w115 (wipe, slot 2), 1 Lugia egg bought, new Lugia run slot 2
- Farm exited 03:04:46 "PRIMARY Lugia FAINT ... DONE farm17" at w115 (wild Nihilego, Beast Boost; bench switched in one by one, Nosepass last; 2 ALL-FAINT rechecks). Live scene: all 6 at 0 HP, MessagePhase. No other controller.
- to_title.py -> title. Vouchers 31 regular + 2 Plus + 1 Premium left UNSPENT. Lugia candy 11 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg once, candy 11 -> 5, eggs 0 -> 1. Feebas candy 79 (all owned) untouched.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> c35, Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Rotated stdout, launched hidden via Win32_Process Create (pythonw PID 73784, parent WmiPrvSE). One instance, w2 reward by 03:10:59.

## 2026-11-01 03:18-03:22 MST - watch run: caught wild shiny Bidoof w11 (Lugia run)
- Farm stopped 03:17:09 on shiny_enemy Bidoof (single wild, Lv8, variant 2, not a boss, 29/29). Waited past 2 min; state unchanged at 03:19:33, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Bidoof: Great Ball (5 -> 4; Rogue/Ultra 0) caught first throw (cap_rd.py 60 to step the animation). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (sprite pr_399s.png downloaded).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 167880, parent WmiPrvSE 113808). One instance, w12 by 03:21:51.

## 2026-11-01 05:15 MST — DNA Splicer option cursor fix
- Symptom: every DNA Splicer bailed ("DNA option cursor -> 0 (Apply) got 3" then "no Apply option on base"), 5 wasted splicers (w116, w66, w79, w106, w113).
- Cause: set_cursor() returns h.cursor (party slot) while PartyUiHandler is in options mode; the option cursor is h.optionsCursor.
- Fix: dna_opt now reads back optionsCursor when optionsMode. Backup pr_farm17.bak_dnaoptcur_20261101_0515.py. Patched while running (Lugia run w114 trainer battle); next watch does the safe restart to load it.

## 2026-11-01 05:20-05:27 MST - watch run: Lugia run ended w115 (wipe, slot 2), 3 Lugia eggs bought, new Lugia run slot 2
- Farm exited 05:19:59 "PRIMARY Lugia FAINT ... DONE farm17" at w115 (wild Vikavolt/Araquanid/Heracross; bench switched in one by one, Nosepass last; 2 ALL-FAINT rechecks). Live scene: all 6 at 0 HP, MessagePhase. No other controller.
- to_title.py -> title. Vouchers 37 regular + 3 Plus + 2 Premium left UNSPENT. Lugia candy 21 (all upgrades owned): Use Candies -> x6 Buy an Egg three times, candy 21 -> 3, eggs 0 -> 3. Feebas candy 101 (all owned) untouched.
- New Game -> Classic (modeId 0) -> nr_pick.py 249,349,263,401,327,299 -> Start cursor -> Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified sessionSlotId 2, wave 1, party [249,349,263,401,327,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 105432, parent WmiPrvSE 113808). One instance, w2 by 05:27:12. This launch loads the 05:13 DNA option-cursor patch.

## 2026-11-01 05:56-06:00 MST - watch run: caught wild shiny Vivillon w31 (Lugia run)
- Farm stopped 05:54:40 on shiny_enemy Vivillon (single wild, Lv19, variant 1, not a boss, 64/64). Waited past 2 min; state unchanged at 05:56:44, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Vivillon: Ultra Ball x3 (5 -> 2; Rogue/Great 0), caught on throw 3. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (sprite pr_666s.png = 666s-meadow icon, form not read).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create with full pythonw path (bare pythonw returned 9 again).

## 2026-11-01 06:10-06:13 MST - watch run: caught wild shiny Shuppet w42 (Lugia run)
- Farm stopped 06:07:18 on shiny_enemy Shuppet (single wild, Lv28, variant 1, not a boss, 67/67). Waited past 2 min; state unchanged at ~06:11, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Shuppet: Ultra Ball (2 -> 1; Rogue/Great 0) caught first throw (cap_rd.py 60). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (sprite pr_353s.png downloaded).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create with full pythonw path (PID 58868, parent WmiPrvSE 113808). One instance, w43 by 06:12:27.

## 2026-11-01 06:22-06:29 MST - watch run: caught wild shiny Mawile w54 (double, Lugia run)
- Farm stopped 06:21:16 on shiny_enemy Mawile (wild double with Haunter Lv38 Levitate; Mawile Lv35, variant 2, not a boss, 84/84). Past 2 min at 06:23:28, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Haunter (BattlerIndex 2, super effective vs Poison; Mawile resists Psychic anyway), Milotic Calm Mind. Haunter KO'd, Mawile untouched. Needed cap_rd.py frame stepping (tab hidden). Linoone's Flail learn prompt declined (gx.py p:6).
- Balls: Ultra 1 (broke free), then Poke Balls 25 -> 21, caught on Poke throw 4. Party full, krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (sprite pr_303s.png already present).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 157412, parent WmiPrvSE 113808). One instance, w55 by 06:28:50.
- Note: no Rogue/Great/Ultra Balls left (Poke 21).

## 2026-11-01 07:28-07:32 MST - watch run: MISSED wild shiny Minior w98 (double, Lugia run)
- Farm stopped 07:24:46 on shiny_enemy Minior (wild double with Claydol Lv74 Levitate; Minior Lv69 Meteor form, Shields Down, variant 1, not a boss, 181/181). Past 2 min at 07:28, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aeroblast on Claydol (bi 3, neutral; left it at 28/178), Milotic Calm Mind. Claydol then exploded (spread hit Minior 181 -> 146), and Minior used a self-KO move (Self-Destruct/Explosion) on its own turn -> "Wild Minior fainted!" before any ball could be thrown. No ball spent (Poke 26, Rogue 15).
- Lesson: Minior and Claydol both carry self-KO moves; a 1-turn partner KO isn't guaranteed. Nothing in the script to patch for this.
- Logged as Missed in CHIE Shiny Log.md. Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 94760, parent WmiPrvSE 113808). One instance, w99 by 07:31:38.
## 2026-11-01 08:18-08:20 MST - watch run: STRUGGLE fix (w120 Gym Leader Skyla, all PP empty)
- Lugia ran all 4 moves to 0 PP vs Skyla's last mon (Corviknight); the FightUi branch logged "no usable move ... - back" every second from 08:16:20 (endless loop).
- Patch (backup pr_farm17.bak_struggle_20261101_0820.py): when every move shows 0 PP, confirm move 0 so the game uses Struggle; otherwise keep the old back-out.
- Restarted hidden via Win32_Process Create (pythonw PID 66600). Struggle KO'd Corviknight at 08:18:50, gym won, WAVE UP 120 -> 121 at 08:19:02.

## 2026-11-01 09:19-09:25 MST - watch run: Lugia run ended w165 (wipe vs Mega Golisopod); manual control detected, no restart
- Farm exited 09:17:53 "PRIMARY Lugia FAINT ... DONE farm17" at w165 (Mega Golisopod, Tough Claws; bench switched in one by one, Nosepass last).
- At ~09:20 the game was already on starter select (slot 2, Classic), not title; to_title.py had sent 12 action presses before this was noticed (no starters ended up selected; option menu left open on cursor 67).
- Read-only: Lugia candy 4 (vr 2, passive owned), Feebas candy 11 (was 101 at 05:20), eggs 13, vouchers 45/5/4. Looks like Gavin already spent candy by hand. No farm process. Sent no further input; left it to Gavin.

## 2026-11-01 09:23 MST - watch run: Gavin started the new run himself
- New Lugia run (Lugia, Feebas, Mawile, Zigzagoon, Spinda, Kricketot) launched from PokeFarmControl at 09:21:35 (pr_farm17.py PID 78352, one instance). Farm at w7 by 09:22:37. No input sent.

## 2026-11-01 09:29-09:31 MST - watch run: caught wild shiny Bidoof w18 (Lugia run)
- Farm stopped 09:25:39 on shiny_enemy Bidoof (single wild, Lv12, variant 1, not a boss, 37/37). Past 2 min at 09:29, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Bidoof: Poke Ball (5 -> 4; Rogue/Great/Ultra 0) caught first throw (cap_rd.py 60). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 75504, parent WmiPrvSE 113808). One instance, w21 by 09:30:53.

## 2026-11-01 09:34-09:40 MST - watch run: caught wild shiny Hoppip w27 (double, Lugia run)
- Farm stopped 09:32:50 on shiny_enemy Hoppip (wild double with Venipede Lv18; Hoppip Lv16, variant 1, not a boss, 37/37). Past 2 min at 09:35:13, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Venipede (bi 2, neutral vs Bug/Poison, single target), Milotic Calm Mind. Venipede KO'd, Hoppip untouched. Spinda's Psybeam learn prompt declined (gx.py p:6).
- Rogue Ball (5 -> 4) caught first throw (cap_rd.py 60). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_187s.png present). Two shiny Feebas egg hatches at 09:32 were already logged by the script.
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 45180, parent WmiPrvSE 113808). One instance.

## 2026-11-01 09:39-09:45 MST - watch run: wild shiny Cottonee w28 (double) - Gavin took over mid-catch
- Farm stopped 09:39:32 on shiny_enemy Cottonee (wild double with Beautifly Lv17; Cottonee Lv19, variant 2, not a boss, 48/48). Past 2 min at 09:41:29, state unchanged, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Beautifly (bi 2), Milotic Calm Mind. Beautifly KO'd, Cottonee untouched.
- While stepping messages, a Rogue Ball was thrown that this watch didn't throw (4 -> 3) and the release prompt was answered by someone else -> stopped all input. Cottonee caught; party unchanged, so it went to storage. Logged as Caught (Rogue Ball) in CHIE Shiny Log.md.
- By 09:43:59 the game was at w29 (mystery encounter) with no farm process: Gavin is playing by hand. Farm NOT restarted; no further input.

## 2026-11-01 09:49-09:53 MST - watch run: caught wild shiny Weepinbell w43 (double, epic variant, Lugia run)
- Farm (relaunched by Gavin from PokeFarmControl at 09:44) stopped 09:47:23 on shiny_enemy Weepinbell (wild double with Heracross Lv27 Guts; Weepinbell Lv27, variant 3, not a boss, 77/77). Past 2 min at 09:49:45, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Heracross (bi 3, neutral vs Bug/Fighting, single target), Milotic Calm Mind. Heracross KO'd, Weepinbell untouched.
- Rogue Ball (3 -> 2) caught first throw. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_70s.png downloaded).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 70040, parent WmiPrvSE 113808). One instance, w46 by 09:53.

## 2026-11-01 10:30-10:42 MST - watch run: Lugia run ended w120 (wipe vs Crabominable), 2 Lugia eggs bought, new Lugia run slot 2; caught shiny Zigzagoon w3
- Farm exited 10:26:32 "PRIMARY Lugia FAINT ... DONE farm17" at w120 (wild Clawitzer then Crabominable, Iron Fist; bench switched in one by one, Kricketot last). Game untouched at 10:30 (MessagePhase, all 0 HP), no other controller.
- to_title.py -> title. Vouchers 51 regular + 6 Plus + 4 Premium left UNSPENT. Lugia candy 12 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg twice, candy 12 -> 0, eggs 0 -> 2. Feebas candy 70 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,303,263,327,401 (Gavin's 09:21 lineup with Mawile) -> Start -> Yes -> slots [0,1 data; 2-4 empty] -> slot 2. Verified Classic, sessionSlotId 2, wave 1, party [249,349,303,263,327,401].
- Launched hidden (PID 17936). Stopped 10:35:23 on shiny_enemy Zigzagoon w3 (wild double with Bidoof; Lv3, variant 1). Waited past 2 min, state unchanged at 10:37:58.
- dbl_shiny2.py: Lugia Aura Sphere on Bidoof (bi 3), Feebas Calm Mind. Bidoof KO'd, Zigzagoon untouched. Poke Ball (5 -> 4) caught first throw. Party full, krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_263s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 36100, parent WmiPrvSE 113808). One instance, w6 by 10:41:27.

## 2026-11-01 11:25-11:28 MST - watch run: Encore loop at w114 fixed (Lugia run)
- Farm stuck since ~11:24 in w114 (Galactic Commander Saturn, Rhyperior): Lugia had EncoreTag on Aeroblast (1 PP left), so PP CONSERVE kept choosing Aura Sphere/Lumina Crash, the game refused them, and the fight menu looped (PP never changed).
- Patch (backup pr_farm17.bak_encore_20261101_1127.py): in the FightUiHandler branch, read the field user's EncoreTag; if the encored move has PP, use it instead of pick_move's choice (log "ENCORE: locked into ...").
- Restarted hidden via Win32_Process Create (pythonw PID 147148, parent WmiPrvSE 113808). One instance. ENCORE fired at 11:27:33 (Aeroblast), battle moved on to Ambipom/Crobat.

## 2026-11-01 11:31-11:38 MST - watch run: PP-critical item fix; Lugia run ended w120 (wipe vs trainer, Ribombee), 1 Lugia egg bought, new Lugia run slot 2
- Bug seen w114-118: Lugia ran all four moves to 0 PP and Struggled. pp_crit was set, but tier-first sorting let ULTRA/GREAT items (Wide Lens, Hyper Potion) and a Leppa Berry beat Max Ether/Ether, and the log misleadingly said "PP item skipped (pp ok)".
- Patch (backup pr_farm17.bak_ppcrit_20261101_1135.py): in pick_reward, when pp_crit and the primary is alive, Ether/Elixir items get sort key (0, -60, 0) ("pp_crit_top"): above all normal items, still below specials (Master Ball, revive, sword, prism, DNA, emergency heal).
- Run ended 11:32:37 at w120 (trainer, Ribombee last; all six fainted). Game untouched until this watch. to_title.py -> title. Vouchers 56 regular + 7 Plus + 4 Premium left UNSPENT. Lugia candy 10 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg once, candy 10 -> 4, eggs 0 -> 1. Feebas candy 92 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,303,263,327,401 -> c35, Right, Up x5 (startCursorObj visible) -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,303,263,327,401].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 59248, parent WmiPrvSE 113808). One instance, w4 by 11:38 with the PP fix loaded.

## 2026-11-01 12:29-12:41 MST - watch run: Lugia run ended w114 (wipe vs wild Clefable), 2 Lugia eggs bought, new Lugia run slot 2; caught shiny Nidoran♀ w4
- Farm exited 12:22:22 "PRIMARY Lugia FAINT ... DONE farm17" at w114 (wild Clefable, Cute Charm; bench switched in one by one, Kricketot last). Game untouched at 12:29 (MessagePhase, all 0 HP), no other controller.
- to_title.py -> title. Vouchers 63 regular + 7 Plus + 4 Premium left UNSPENT. Lugia candy 12 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg twice, candy 12 -> 0, eggs 0 -> 2. Feebas candy 116 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,303,263,327,401 -> c35, Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,303,263,327,401].
- Launched hidden (PID 99072). Stopped 12:34:00 on shiny_enemy Nidoran♀ w4 (wild double with Scatterbug; Lv4, variant 1). Past 2 min at 12:36:24, state unchanged.
- dbl_shiny2.py: Lugia Lumina Crash on Scatterbug (bi 3), Feebas Calm Mind. Scatterbug KO'd, Nidoran untouched. Poke Ball (5 -> 4) caught first throw. Party full, krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_29s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 86172, parent WmiPrvSE 113808). One instance, w6 by 12:40.

## 2026-11-01 13:23 MST - watch run: Lugia run ended w102 (wipe vs Latias/Flutter Mane); Gavin already started a new run by hand
- Farm exited 13:19:49 "PRIMARY Lugia FAINT ... DONE farm17" at w102 (Latias then Flutter Mane; bench switched in one by one, Kricketot last).
- At 13:23 the game was already on a new run at w2 (MessagePhase) with party Lugia, Feebas, Spinda, Zigzagoon, Kricketot, Sinistea, and no farm process: Gavin did the run-end/new-run himself. No input sent, candy not touched, farm not launched.

## 2026-11-01 13:29 MST - watch run: farm healthy at w20; Gavin handled shiny Lechonk w13
- Farm (PID 151004, launched 13:26:37 from PokeFarmControl) advancing normally, w19-20 at 13:29, one instance, no stop flag.
- Shiny Lechonk Lv8 variant 1 stopped the farm at w13 13:26:00; Gavin resolved it and relaunched within 38 s. Poke Balls 5 -> 4 and Lechonk dex has the shiny bit, so logged as Caught (Poke Ball).
- Shiny Log: added Lechonk row at top; removed duplicate audit row "UNKNOWN x1 (candidates: #249x2)" (same 13:17 shiny Lugia egg hatch). Backup in ..PROJECT\pokerogue\backups.

## 2026-11-01 14:07-14:11 MST - watch run: caught wild shiny Aggron w81 (Lugia run)
- Farm stopped 14:05:23 on shiny_enemy Aggron (single wild, Lv60, variant 2, not a boss, 155/155, Sturdy). Past 2 min at 14:07:29, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Aggron: Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_306s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 126416, parent WmiPrvSE 113808). One instance, w82 by 14:10.

## 2026-11-01 14:49-14:56 MST - watch run: Lugia run ended w120 (wipe vs wild Arctovish/Glaceon), 3 Lugia eggs bought, new Lugia run slot 2
- Farm exited 14:44:57 "PRIMARY Lugia FAINT ... DONE farm17" at w120 (wild Arctovish then Glaceon; bench switched in one by one, Sinistea last). Game untouched at 14:49 (MessagePhase, all 0 HP), no other controller.
- to_title.py -> title. Vouchers 76 regular + 7 Plus + 4 Premium left UNSPENT. Lugia candy 19 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x3, candy 19 -> 1, eggs 0 -> 3. Feebas candy 56 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,854 (Gavin's 13:23 hand lineup with Sinistea) -> setCursor(35), Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,854].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 66348, parent WmiPrvSE 113808). One instance, w2 by 14:55.

## 2026-11-01 15:05-15:09 MST - watch run: caught wild shiny Meowth w15 (double, Lugia run)
- Farm stopped 15:03:20 on shiny_enemy Meowth (wild double with a non-shiny Meowth; Lv9, variant 1, not a boss, 27/27). Past 2 min at 15:05:30, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on the non-shiny Meowth (bi 3), Feebas Calm Mind. Partner KO'd, shiny untouched. Poke Ball (5 -> 4) caught first throw. Party had 5, Meowth joined as 6th. Logged in CHIE Shiny Log.md (top row; sprite pr_52s.png present).
- Cleared flag/reason/stopped_reason, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 119784, parent WmiPrvSE 113808). One instance, w16 by 15:09.

## 2026-11-01 15:17-15:21 MST - watch run: caught wild shiny Foongus w28 (Lugia run)
- Farm stopped 15:15:46 on shiny_enemy Foongus (single wild, Lv17, variant 2, not a boss, 55/55). Past 2 min at 15:17:50, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Foongus: Poke Ball (4 -> 3; Rogue/Great/Ultra 0) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_590s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 102736, parent WmiPrvSE 113808). One instance, w29 by 15:20.

## 2026-11-01 15:45-15:49 MST - watch run: caught wild shiny Aipom w59 (Lugia run)
- Farm stopped 15:42:32 on shiny_enemy Aipom (single wild, Lv38, variant 1, not a boss, 100/100, Pickup). Past 2 min at 15:45:13, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Aipom: Great Ball (5 -> 4) broke free; second Great Ball (4 -> 3) caught. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_190s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 125672, parent WmiPrvSE 113808). One instance, w60 by 15:49.

## 2026-11-01 16:31-16:37 MST - watch run: Lugia run ended w114 (wipe vs wild Muk/Clodsire/Salazzle), 1 Lugia egg bought, new Lugia run slot 2
- Farm exited 16:26:13 "PRIMARY Lugia FAINT ... DONE farm17" at w114 (wild Muk, Clodsire, Salazzle; bench switched in one by one, Persian last). Game untouched at 16:31 (MessagePhase), no other controller.
- to_title.py -> title. Vouchers 81 regular + 9 Plus + 4 Premium left UNSPENT. Lugia candy 11 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg once, candy 11 -> 5, eggs 0 -> 1. Feebas candy 66 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,854 -> setCursor(35), Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,854].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 42820, parent WmiPrvSE 113808). One instance, w3 by 16:36.

## 2026-11-01 17:26-17:30 MST - watch run: lost wild shiny Gigalith w106 (double, Lugia run) to its own self-KO move
- Farm stopped 17:21:20 on shiny_enemy Gigalith (wild double with non-shiny Hawlucha; Lv76, variant 1, not a boss, 215/215, Sturdy). Past 2 min at 17:26, state unchanged (full HP, command menu, balls unchanged), no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Hawlucha (bi 3, single target), Milotic Calm Mind. Hawlucha KO'd; then Gigalith fainted on its own turn while Lugia (322->234) and Milotic (311->173) took damage, so it most likely used Explosion/Self-Destruct. Gigalith was never targeted. No ball thrown.
- Note: balls can't be thrown while two foes are up, so KOing the partner first was the only route; a shiny with Explosion/Self-Destruct can still self-KO on that turn (bad luck, no patch).
- Logged as Missed in CHIE Shiny Log.md (top row; sprite pr_526s.png present).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 152828, parent WmiPrvSE 113808). One instance, w108 by 17:29.

## 2026-11-01 17:40-17:46 MST - watch run: Lugia run ended w110 (wipe vs wild Swoobat/Archeops), 2 Lugia eggs bought, new Lugia run slot 2
- Farm exited 17:31:13 "PRIMARY Lugia FAINT ... DONE farm17" at w110 (wild Swoobat then Archeops; bench switched in one by one, Kricketot last). Game untouched at 17:40 (MessagePhase), no other controller.
- to_title.py -> title. Vouchers 89 regular + 9 Plus + 4 Premium left UNSPENT. Lugia candy 13 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x2, candy 13 -> 1, eggs 0 -> 2. Feebas candy 87 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,854 -> setCursor(35), Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,854].
- Rotated stdout, launched hidden via Win32_Process Create (pythonw PID 91560, parent WmiPrvSE). One instance, w3 by 17:45.

## 2026-11-01 18:57-19:03 MST - watch run: Lugia run ended w169 (wipe vs wild double Brambleghast), 2 Lugia eggs bought, new Lugia run slot 2
- Farm exited 18:54:31 "PRIMARY Lugia FAINT ... DONE farm17" at w169 (wild double Brambleghast, Wind Rider; bench switched in one by one, Sinistea last). Game untouched at 18:57 (MessagePhase), no other controller.
- to_title.py -> title. Vouchers 102 regular + 12 Plus + 4 Premium left UNSPENT. Lugia candy 13 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x2, candy 13 -> 1, eggs 0 -> 2. Feebas candy 113 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,854 -> setCursor(35), Right, Up x5 -> Start, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,854].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 45372, parent WmiPrvSE 113808). One instance, w6 by 19:02.

## 2026-11-01 19:23-19:29 MST - watch run: caught wild shiny Honedge w61 (double, Lugia run)
- Farm stopped 19:19:48 on shiny_enemy Honedge (wild double with non-shiny Cofagrigus; Lv38, variant 1, not a boss, 91/91, No Guard). Past 2 min at 19:22:39, state unchanged (full HP, command menu), no farm process, no other controller.
- dbl_shiny2.py: Lugia Lumina Crash on Cofagrigus (bi 3, single target) x2, Feebas Calm Mind both turns. Cofagrigus KO'd (98 -> 41 -> 0), Honedge untouched. Rogue Ball (15 -> 14) caught first throw. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_679s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 49628, parent WmiPrvSE 113808). One instance, w64 by 19:28.

## 2026-11-01 19:35-19:39 MST - watch run: caught wild shiny Camerupt w71 (Lugia run)
- Farm stopped 19:31:16 on shiny_enemy Camerupt (single wild, Lv48, variant 1, not a boss, 129/129, Magma Armor). Past 2 min at 19:35, state unchanged (full HP, command menu, Rogue 14), no farm process, no other controller.
- No attack. dbl_shiny2.py ball Camerupt: Rogue Ball (14 -> 13) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_323s.png present).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 28968, parent WmiPrvSE). One instance, w73 by 19:38.

## 2026-11-01 20:58-21:03 MST - watch run: caught wild shiny Copperajah w143 (double, Lugia run)
- Farm stopped 20:52:51 on shiny_enemy Copperajah (wild double with non-shiny Excadrill; Lv116, variant 1, not a boss, 416/416, Sheer Force). Past 2 min at 20:58, state unchanged (full HP, command menu, Rogue 38), no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere on Excadrill (bi 3, single target) x2, Milotic Calm Mind both turns. Excadrill's spread move hit Copperajah 416 -> 45 on turn 1 (close call); Excadrill KO'd turn 2. Rogue Ball (38 -> 37) caught first throw. catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_879s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 2604, parent WmiPrvSE 113808). One instance, w145 by 21:02.

## 2026-11-01 21:07-21:14 MST - watch run: Lugia run ended w145 (wipe vs wild Garchomp/Magmortar), 2 Lugia eggs bought, new Lugia run slot 2
- Farm exited 21:06:31 "PRIMARY Lugia FAINT ... DONE farm17" at w145 (wild Garchomp then Magmortar; bench switched in one by one, Sinistea last). Game untouched at 21:07 (MessagePhase), no other controller.
- to_title.py -> title. Vouchers 114 regular + 12 Plus + 5 Premium left UNSPENT. Lugia candy 12 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x2, candy 12 -> 0, eggs 0 -> 2. Feebas candy 140 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,854 -> setCursor(35), Right, Up x5 -> Start, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,854].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 89160, parent WmiPrvSE). One instance, w3 by 21:13.

## 2026-11-01 22:34 MT - orbmilotic (backup bak_orbmilotic_20261101_2234)
- Flame/Toxic Orb no longer banned: picked by normal priority only if Milotic is alive and doesn't already hold that orb; party target forced to Milotic, never Lugia/others. state.js party now exposes ho (held orbs).
- SEC_NO_STATUS_CURE: Milotic's burn/poison never cured (no Full Heal/Full Restore/Lum/cure items, shop or reward); shop heals Milotic only when HP low, plain potions only. Lugia status cures unchanged.
- Pickup transfer (Linoone etc.): Lugia first, leftovers (max stack/refused) -> Milotic; orbs -> Milotic only. Log shows ->Lugia / ->Milotic.

## 2026-11-01 22:40 MT - evoitem (backup bak_evoitem_20261101_2240)
- Evolution items: state.js tags rewards with eligible party indices (selectFilter); eligible non-Lugia/non-Milotic member -> rank -280 and party target (Sinistea first). None eligible -> normal rank. Orb/status/pickup rules untouched.

## 2026-11-01 22:57 MT - RUNLOG
- New `Run Log.md` (CHIE POKEROGUE, beside Shiny Log): at primary faint (run end) RUNLOG_JS reads slot, wave, party (species/lv/shiny variant/fusion), luck, primary held items (berries/vitamins hidden), trainer name + live foes; row inserted at top. Log line `RUN LOG row w.. slot=.. luck=..`. Backfilled 13 run ends 11/01 from farm log (levels/luck/items unknown -> em dash). Backup pr_farm17.bak_runlog_20261101_2254.py. state.js unchanged.


## 2026-11-01 23:20-23:23 MST - watch run: caught wild shiny Breloom w85 (Lugia run)
- Farm stopped 23:17:05 on shiny_enemy Breloom (single wild, Lv59, variant 3, not a boss, 146/146, Poison Heal). Past 2 min at 23:19:33, state unchanged, no farm process, no other controller.
- No attack. dbl_shiny2.py ball Breloom: Rogue Ball (4 -> 3) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_286s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 45640). Advanced to w88 by 23:23.
- Gotcha: a CIM CommandLine -match 'pr_farm' check also matches the PowerShell host running it; filter on Name like 'python%'.

## 2026-11-01 23:25-23:29 MST - watch run: caught wild shiny Amoonguss w88 (double, Lugia run)
- Farm stopped 23:23:05 on shiny_enemy Amoonguss (wild double with non-shiny Miltank; Lv66, variant 2, not a boss, 231/231). Past 2 min at 23:25:07, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere on Miltank (bi 2, single target), Milotic Calm Mind. Miltank KO'd, shiny untouched.
- MISTAKE caught in time: a gx.py p:5 message-step loop kept pressing ACTION past "What will Lugia do?" and queued Lugia's move 0 + Milotic's Fight menu. Backed out with gx.py p:6 twice (Milotic Fight -> Milotic command -> Lugia command); no move resolved, Amoonguss still 231/231. Lesson: step messages one at a time and stop on mode 2 / CommandPhase.
- Rogue Ball (3 -> 2) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_591s.png downloaded).
- Cleared flag/reasons, rotated stdout, launched hidden (pythonw PID 165904).

## 2026-11-01 23:36-23:40 MST - watch run: logged Gavin's manual shiny catches (no input sent)
- Shiny stops w96 Nidoqueen (Lv70, v2, 23:32:12) and w107 Shiftry (Lv83, v1, 23:34:56) were handled by Gavin; farm relaunched from PokeFarmControl 23:33:00 and 23:35:17 (python.exe parent PokeFarmControl.pyw). Dex read: Nidoqueen caughtCount 1 + shiny v2 bit; Shiftry shiny v1 bit, AttemptCapturePhase seen at relaunch. Logged both as Caught (ball unknown) in CHIE Shiny Log.md; sprites pr_31s/pr_275s downloaded.
- ISSUE: Lugia holds FLAME_ORB and is burned (status 6); farm never picked an orb (both offers 23:30:41/23:35:28 skipped), source unknown. Farm buys Full Heals for Lugia each screen. No input sent; flagged to Gavin.

## 2026-11-01 23:52-00:00 MST - watch run: lost wild shiny Tapu Koko w130 (boss, Lugia run) to its own recoil; primary pinned in config
- Farm stopped 23:48:52 on shiny_enemy Tapu Koko (single wild boss, Lv109, variant 1, 3 segments, 279/279, Electric Surge). At 23:52 (past 2 min) state unchanged, no farm process, no other controller.
- Lugia Aura Sphere (resisted) x2: 279 -> 186 -> 93; game clamps boss damage at each shield threshold (confirmed). Rogue Ball 20 -> 19 broke free; Koko's move KO'd Lugia (189 HP) and its recoil took Koko to 46 (likely Wild Charge). Sent Probopass; Rogue Ball 19 -> 18 broke free; Koko hit Probopass (296 -> 19) and fainted from recoil. Logged Missed in CHIE Shiny Log.md (sprite pr_785s.png downloaded).
- Lesson: a shiny with a recoil move can self-KO at low HP; nothing safe to patch (Thunder Wave/sleep would help if a party mon had it).
- Relaunch at 23:56:53 resolved PRIMARY = Probopass (slot 0 after the faint switch, Lugia fainted). Lugia was revived at the shop. Fix: added "primary": "249" to agent-tools\pokerogue_farm_config.json (backup .bak_primary_20261102_0000; secondary_field/candy_target untouched) and restarted hidden (pythonw PID 142236, parent WmiPrvSE 113808). Log: "PRIMARY resolved: Lugia (species 249, slot 2) source=config", w137 by 23:59.
- NOTE: when Gavin switches to a different lead, the config primary must be changed (or set to "auto").

## 2026-11-02 00:03-00:10 MST - watch run: Lugia run ended w140 (wipe vs Gym Leader Gordie's Barbaracle), 3 Lugia eggs bought, new Lugia run slot 2
- Farm exited 00:01:33 "PRIMARY Lugia FAINT ... RUN LOG row w140 ... DONE farm17" (Trainer Gordie, Barbaracle/Sniper; bench switched in one by one, Krigoon last). Game untouched at 00:03, no other controller.
- to_title.py -> title. Vouchers 130 regular + 14 Plus + 7 Premium left UNSPENT. Lugia candy 19 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x3, candy 19 -> 1, eggs 0 -> 3. Feebas candy 31 (all owned) untouched.
- Lineup: run history showed Gavin's hand-started 22:5x run used starters 401(+263 fused),249,349,299 Nosepass,327 (Sinistea dropped; Pachirisu met w52). New run uses 249,349,327,263,401,299.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,299 -> c35, Right, Up x5 -> ACTION, Yes -> slots [0,1 data; 2-4 empty] -> Down x2 (slot 2). Verified modeId 0, sessionSlotId 2, wave 1.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 95684, parent WmiPrvSE 113808). One instance, w7 by 00:09.
- Open issue still: ended run's Lugia held FLAME_ORB (burned); source unknown, not from a farm pick.


## 2026-11-02 00:36-00:40 MST - watch run: logged Gavin's manual shiny Xatu w67 (no input sent)
- Farm stopped 00:31:29 on shiny_enemy Xatu (wild double, Lv44, variant 1). Gavin handled it: farm relaunched from PokeFarmControl 00:36:06 (python.exe PID 109904, parent PokeFarmControl.pyw), now w68 vs Chimecho/Dusclops.
- Dex 178 caughtAttr 158 has the shiny bit (default variant); party full, Xatu not in party. Logged as Caught (ball unknown) at top of CHIE Shiny Log.md (sprite pr_178s.png already present).

## 2026-11-02 00:44 MST - ORBFIX: primary-held Flame/Toxic Orb -> Milotic (Gavin approved)
- Backup pr_farm17.bak_orbfix_*.py; py_compile OK; synced TEMP/scripts/box (md5 9f996f4c).
- Transfer waves only: primary FLAME/TOXIC_ORB -> Milotic; if Milotic absent/fainted/holds orb -> kept + logged (ORBFIX wN: KEPT ...).
- Shop: no Full Heal/Full Restore for primary status while it holds an orb; HP heals unchanged.
- Restarted between battles (shop w76) as one hidden pythonw PID 52352; 'ORBFIX active' logged 00:44:04.

## 2026-11-02 00:55-01:02 MST - watch run: caught wild shiny Hypno w87 (double, Lugia run)
- Farm stopped 00:54:57 on shiny_enemy Hypno (wild double with non-shiny Sigilyph; Lv61, variant 1, not a boss, 188/188). Past 2 min at 00:57:15, state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aeroblast on Sigilyph (bi 2, single target), Milotic Calm Mind, three turns (Sigilyph 170 -> 25, healed to 67, then KO'd). On turn 2 Hypno dropped 188 -> 141 from something other than our attack (Sigilyph unchanged, likely a self-hit); stayed catchable. Stepped messages with dbl_shiny2.py ack.
- Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, went to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_97s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 38128, parent WmiPrvSE 113808). One instance, back in the w87 shop by 01:01.
## 2026-11-02 03:00-03:03 MST - watch run: caught wild shiny Hypno w178 (single, Lugia run)
- Farm stopped 02:52:18 on shiny_enemy Hypno (single wild, Lv145, variant 1, not a boss, 411/411). At 03:00 (past 2 min) state unchanged, CommandPhase, no farm process, no other controller.
- catch_shiny.py Hypno 1 3: Rogue Ball (34 -> 33) caught first throw (cap_rd.py 80, catch_ack.py). Party had 5, so Hypno auto-joined as slot 6. Logged in CHIE Shiny Log.md (top row; sprite pr_97s.png present).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 64304, parent WmiPrvSE 113808). One instance, w179 by 03:02.

## 2026-11-02 03:16-03:21 MST - watch run: caught wild shiny Gogoat w185 (double, Lugia run)
- Farm stopped 03:13:11 on shiny_enemy Gogoat (wild double with non-shiny Gigalith/Sand Stream; Lv156, variant 2, not a boss, 577/577). At 03:16 (past 2 min) state unchanged, CommandPhase, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere on Gigalith (bi 3, single target) KO'd it in one hit; Milotic Calm Mind. Gogoat untouched.
- Rogue Ball 33 -> 32 broke free (Gogoat hit Milotic 613 -> 326); Rogue Ball 32 -> 31 caught. catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_673s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 117868, parent WmiPrvSE 113808). One instance, w186 (Elite Four Flint) by 03:20.

## 2026-11-02 03:33 MST — PPIDX: reward screen read the wrong mon's PP
- Symptom: w188 reward offered Max Elixir + Ether while Lugia had Lumina Crash 2/16 and Aeroblast 0/8, but log said "PP item skipped (pp ok)" and took Rare Candy.
- Cause: when the field mon at the reward screen isn't the primary, the zmoves fallback read party[0] (Milotic) instead of the primary's slot (Lugia is slot 1).
- Fix (pr_farm17.py ~L1016): fallback now reads party[z.i] like the PP check at ~L1267. Backup pr_farm17.bak_ppidx_20261102_0333.py. Restarted hidden at 3:33 (w190, Champion Cynthia), single instance confirmed.

## 2026-11-02 03:40 MST - NMOVE: farm looped selecting unimplemented Bide (N)
- Symptom: w190 (Champion Cynthia), Lugia/Milotic/Spinda down, Krione chose "Bide (N)" every ~1.4 s for 2+ min with PP never dropping (game won't use it).
- Fix (pick_move start): drop moves whose name ends in "(N)" when any other usable damaging move has PP. Backup pr_farm17.bak_nmove_*.py; py_compile OK.
- Restarted hidden via Win32_Process Create (pythonw PID 96692, parent WmiPrvSE 113808), single instance. Krione used Bonemerang at 03:38:44, loop cleared.

## 2026-11-02 03:41-03:47 MST - watch run: Lugia run ended w190 (wipe vs Champion Cynthia), 9 Lugia eggs bought, new Lugia run slot 2
- Farm exited 03:39:32 "ALL-FAINT ... RUN LOG row w190 ... DONE farm17" (Cynthia's Giratina took Lugia; Mega Garchomp and Lucario swept the bench, Hypno last). Best Lugia run so far.
- to_title.py -> title. Vouchers 145 regular + 15 Plus + 8 Premium left UNSPENT. Lugia candy 58 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x9 (menu closes after each buy; nav_open.py 249 each time), candy 58 -> 4, eggs 0 -> 9. Feebas candy 62 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,299 -> p:4 (Start) -> Yes -> slots [0,1 data; 2-4 empty]. Slot list: cursor+scrollCursor is the slot index (Down x2 overshot to 3; Up once -> 2). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,299].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 11124, parent WmiPrvSE 113808). One instance, w4 by 03:47. Lugia's moveset now shows Steam Eruption in place of Aeroblast.

## 2026-11-02 03:54-03:58 MST - watch run: caught wild shiny Poochyena w11 (double, Lugia run)
- Farm stopped 03:52:38 on shiny_enemy Poochyena (wild double with non-shiny Meowth; Lv7, variant 1, not a boss, 22/22). At 03:54:32 (past 2 min) state unchanged, CommandPhase, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere on Meowth (bi 2, single target) KO'd it; Milotic Calm Mind. Poochyena untouched. Milotic's Refresh learn prompt declined (gx.py p:6).
- Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_261s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 75040, parent WmiPrvSE 113808). One instance, w12 by 03:58.

## 2026-11-02 04:08-04:11 MST - watch run: caught wild shiny Spearow w19 (Lugia run)
- Farm stopped 04:03:33 on shiny_enemy Spearow (wild single, Lv12, variant 2, not a boss, 32/32). At 04:08 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 4, no farm process, no other controller.
- catch_shiny.py Spearow 1 3: Rogue Ball (4 -> 3) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_21s.png already present).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 76196, parent WmiPrvSE). One instance, w21 by 04:11.

## 2026-11-02 04:48-04:51 MST - watch run: caught wild shiny Clamperl w59 (Lugia run)
- Farm stopped 04:44:57 on shiny_enemy Clamperl (wild single, Lv40, variant 1, not a boss, 79/79). At 04:48 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 8, no farm process, no other controller.
- catch_shiny.py Clamperl 1 3: Rogue Ball (8 -> 7) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_366s.png downloaded). New read-only helper _rdstate.py (PC %TEMP%\prfarm) prints phase/turn/party HP/balls/enemy.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 156876, parent WmiPrvSE 113808). One instance, w60 (Gym Leader Juan) by 04:50.

## 2026-11-02 05:31-05:35 MST - watch run: caught wild shiny Tinkaton w92 (Lugia run)
- Farm stopped 05:29:00 on shiny_enemy Tinkaton (wild single, Lv62, variant 2, not a boss, 179/179). At 05:31:59 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 7, no farm process, no other controller.
- catch_shiny.py Tinkaton 1 3: Rogue Ball (7 -> 6) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_959s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 25560, parent WmiPrvSE 113808). One instance, w93 by 05:34.

## 2026-11-02 06:47-06:51 MST - watch run: caught wild shiny Diggersby w152 (Lugia run)
- Farm stopped 06:45:24 on shiny_enemy Diggersby (wild single, Lv121, variant 1, not a boss, 373/373). At 06:47:38 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 21, no farm process, no other controller.
- catch_shiny.py Diggersby 1 3: Rogue Ball (21 -> 20) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_660s.png already present).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 23348, parent WmiPrvSE 113808). One instance, w154 by 06:50.

## 2026-11-02 07:03-07:15 MST - watch run: Lugia run ended w163 (wipe vs wild G-Max Centiskorch), 5 Lugia eggs bought, new Lugia run slot 2
- Farm exited 06:59:59 "ALL-FAINT ... PRIMARY Lugia FAINT ... RUN LOG row w163 ... DONE farm17" (wild Gigantamax Centiskorch / Flash Fire; bench switched in one by one, Probopass last). Game untouched at 07:02, no other controller.
- to_title.py -> title. Vouchers 161 regular + 16 Plus + 8 Premium left UNSPENT. Lugia candy 34 (all upgrades owned): Use Candies (index 8) -> x6 Buy an Egg x5 (nav_open.py 249 each time), candy 34 -> 4, eggs 0 -> 5. Feebas candy 82 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 249,349,327,263,401,299 -> p:4 (Start) -> Yes -> Down x2 (cursor 1 + scroll 1 = slot 2, empty). Verified modeId 0, sessionSlotId 2, wave 1, party [249,349,327,263,401,299].
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 66532).
- One instance (parent WmiPrvSE), w2 by 07:09.

## 2026-11-02 07:53-07:57 MST - watch run: caught wild shiny Porygon w52 (Lugia run)
- Farm stopped 07:50:33 on shiny_enemy Porygon (wild single, Lv35, variant 1, not a boss, 94/94). At 07:53 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 5, no farm process, no other controller.
- catch_shiny.py Porygon 1 3: Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_137s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 116644, parent WmiPrvSE 113808). One instance, w53 rewards by 07:56.

## 2026-11-02 08:35 MST — TARGETFIX (pr_farm17.py)
- Bug: in doubles the TargetSelect screen just pressed Z, so single-target moves always hit the left foe. Wave 81 (Shedinja Wonder Guard + Lurantis): every Lugia/Milotic/Linoone hit went into immune Shedinja for ~8 turns; Lugia, Milotic and Linoone fainted (run survived via Kricketot's Stone Axe).
- Fix: after picking a move, remember foes ranked by that move's effectiveness (immune foes dropped); on TargetSelectUiHandler set the cursor to the best live foe's battler index via JS before confirming. Logs "TARGET pick ...". Backup: pr_farm17.bak_target_20261102_0835.py. Restarted hidden at w82; verified at w83.

## 2026-11-02 09:14-09:25 MST - watch run: shiny Claydol w116 missed (self-KO), shiny Aegislash w117 caught (Lugia run)
- Farm stopped 09:08:34 on shiny_enemy Claydol (wild double with Golurk; Lv81, variant 1, not a boss). At 09:14 (past 2 min) state unchanged, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere into Golurk (Ghost, immune, no damage), Milotic Steam Eruption KO'd Golurk. Claydol then fainted on its own move (both our mons took damage; likely Explosion/Self-Destruct) before a ball could be thrown. Logged as Missed in CHIE Shiny Log.md.
- Relaunched hidden (PID 153188); farm stopped again 09:18:10 on shiny_enemy Aegislash (wild double with Chandelure; Lv85, variant 1, not a boss). At 09:20:32 state unchanged.
- Same plan: Lugia Aura Sphere into Chandelure (Ghost, immune), Milotic Steam Eruption KO'd Chandelure. Rogue Ball (19 -> 18) caught first throw at 138/199. Party had 5, so Aegislash joined the party (6th). Logged Caught (sprite pr_681s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 31288, parent WmiPrvSE 113808). One instance, w118 by 09:23.

## 2026-11-02 09:27-09:34 MST - watch run: caught wild shiny Cofagrigus w119 (double, Lugia run)
- Farm stopped 09:24:38 on shiny_enemy Cofagrigus (wild double with non-shiny Aegislash; Lv95, variant 1, not a boss, 226/226). At 09:27 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 18, no farm process, no other controller.
- dbl_shiny2.py: Lugia Aura Sphere into Aegislash (Ghost, immune) both turns; Milotic Steam Eruption (Aegislash 205 -> 81, Stance Change to Blade), then Moonblast KO'd it. Cofagrigus untouched.
- Rogue Ball (18 -> 17) caught first throw (cap_rd.py 80). catch_ack.py, party full so krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_563s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 146612, parent WmiPrvSE 113808). One instance, w120 by 09:33.

## 2026-11-02 09:40-09:46 MST - watch run: Lugia run ended w120 (wipe vs Drifblim), 4 Lugia eggs, ZACIAN SWITCH done, new Zacian run slot 2
- Farm exited 09:36:42 "ALL-FAINT ... PRIMARY Lugia FAINT ... RUN LOG row w120 ... DONE farm17" (Drifblim / Aftermath swept; Aegislash last). Game untouched until 09:40, no other controller.
- to_title.py -> title. Vouchers 170 regular + 19 Plus + 8 Premium left UNSPENT. Lugia candy 28 (all upgrades owned): Use Candies -> x6 Buy an Egg x4, candy 28 -> 4, eggs 0 -> 4. Feebas candy 99 (all owned) untouched. Zacian candy 5 (passive + 2 reductions already owned).
- ZACIAN SWITCH (Gavin t180u): New Game -> Classic -> nr_pick.py 888,349,327,263,401,299 -> Nosepass didn't fit (10/10). Start -> Yes -> Down x2 (cursor 1 + scroll 1 = slot 2, empty). Verified modeId 0, sessionSlotId 2, wave 1, party [888,349,327,263,401].
- agent-tools\pokerogue_farm_config.json primary 249 -> "888" (backup pokerogue_farm_config.bak_lugia_20261102.json); profile zacian.json resolves from the primary.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 169888, parent WmiPrvSE 113808). One instance, w7 by 09:45.

## 2026-11-02 10:14-10:19 MST - watch run: caught wild shiny Altaria w100 (boss, Zacian run)
- Farm stopped 10:11:47 on shiny_enemy Altaria (wild single boss, Lv80, variant 1, 2 segments, 234/234). At 10:14 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 0, Great 5, no farm process, no other controller.
- Shield break: Zacian Bitter Blade (Fire, resisted by Dragon) x2 via catch_shiny.py Altaria 0 3: 234 -> 131, then clamped to 117 (shield broken), Altaria ended at 101/234.
- Great Ball (5 -> 4) caught first throw (cap_rd.py 80, catch_ack.py). Party full, krook_no.py pick -> No, to storage (script crashed only on printing a ruble sign afterwards; harmless). Logged in CHIE Shiny Log.md (top row; sprite pr_334s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 146604, parent WmiPrvSE). One instance, w102 by 10:18.

## 2026-11-02 10:34-10:39 MST - watch run: caught wild shiny Crustle w116 (Zacian run)
- Farm stopped 10:29:14 on shiny_enemy Crustle (wild single, Lv91, variant 1, not a boss, 231/231). At 10:34 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 5, no farm process, no other controller.
- catch_shiny.py Crustle 1 3: Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80, catch_ack.py). Party full, krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_558s.png already present).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 130812, parent WmiPrvSE 113808). One instance, w119 by 10:38.

## 2026-11-02 11:11-11:18 MST - watch run: caught wild shiny Rhyperior w157 (double, Zacian run)
- Farm stopped 11:03:31 on shiny_enemy Rhyperior (wild double with non-shiny Camerupt; Lv132, variant 1, not a boss, 445/445). At 11:11 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 14, no farm process, no other controller.
- dbl_shiny2.py has no "sw" mode (NameError, no input sent). Plan instead: Zacian (fastest, Spe 495) Mighty Cleave (Rock, neutral) targeted at Camerupt (bi 2) -> KO first; Milotic Calm Mind (no damage), so nothing could retarget into the shiny.
- Turn 2: Rogue Ball (14 -> 13) caught first throw (cap_rd.py 80, catch_ack.py). Party full, krook_no.py pick -> No, to storage. Logged in CHIE Shiny Log.md (top row; sprite pr_464s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 8904, parent WmiPrvSE 113808). One instance, w159 by 11:17.

## 2026-11-02 11:30-11:38 MST - watch run: Zacian run ended w165 (wipe vs Groudon), 2 Zacian eggs, new Zacian run slot 2
- Farm exited 11:23:46 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w165 ... DONE farm17" (wave 165 boss Groudon / Drought; bench switched in one by one, Bewear last). Game untouched until 11:30, no other controller.
- to_title.py -> title. Vouchers 180 regular + 20 Plus + 8 Premium left UNSPENT. Zacian candy 14 (passive + 2 reductions owned): Use Candies -> x6 Buy an Egg x2, candy 14 -> 2, eggs 0 -> 2. Feebas candy 131 (all owned) untouched.
- New Game -> Classic -> nr_pick.py 888,349,327,263,401,299 -> Nosepass didn't fit (10/10). gx.py p:4 (Start) -> p:5 Yes -> Down x2 (slot 2, empty). Verified Classic, sessionSlotId 2, wave 1, party [888,349,327,263,401].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 7652, parent WmiPrvSE). One instance, w4 by 11:38.

## 2026-11-02 12:22-12:26 MST - watch run: caught wild shiny Sigilyph w89 (Zacian run)
- Farm stopped 12:16:44 on shiny_enemy Sigilyph (wild single, Lv65, variant 1, not a boss, 175/175). At 12:22 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 15, no farm process, no other controller.
- catch_shiny.py Sigilyph 1 3: Rogue Ball (15 -> 14) caught first throw (cap_rd.py 80, catch_ack.py). Party had 5, so Sigilyph joined as slot 6. Logged in CHIE Shiny Log.md (top row; sprite pr_561s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 79344, parent WmiPrvSE 113808). One instance, w92 by 12:25.

## 2026-11-02 12:38 MST — LUMFIX (pr_farm17.py)
- Pickup transfer sent Lum Berries to Milotic when the primary's stack was full (w111: Lum x2 -> Milotic), breaking the never-cure-Milotic rule. Lum Berries now go to the primary only (stay on the picker if full). Backup: pr_farm17.bak_lum_20261102_1238.py. Restarted hidden at w113; advancing.

## 2026-11-02 13:45 MST — ETERNATUS STOP (handoff sent)
- Farm stopped at w200 (eternatus_catch, 13:33). No Master Ball (Rogue 24, Ultra 5, Great 5, Poke 15). No input sent. Handoff sent to Gavin 13:45; later watches: stay quiet until resolved.

## 2026-11-02 14:10 MST — watch: game left wave 200 (asked Gavin)
- Status still eternatus_catch (13:33), stop flag present, no farm process. Game now on Starter Select (SelectStarterPhase, empty party), so someone (Gavin) played past wave 200 by hand. Outcome (Eternatus caught? win/loss?) unknown; no Run Log row written. No input sent. Asked Gavin once whether to do run-end eggs and start the next Zacian run; later watches stay quiet until he answers or clears the flag.

## 2026-11-02 14:15 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:17 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:22 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:29 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:33 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:37 MST — watch: still waiting on Gavin
- eternatus_catch stop flag still present, no farm process. Already asked Gavin at 14:10; no input sent, stayed quiet.

## 2026-11-02 14:42 MST - run end w200 (Eternatus, played by Gavin), eggs, new Zacian run slot 2
- Run Log row added: w200, Zacian/Milotic/Sigilyph/Spinda/Krione, "Eternatus, played by Gavin by hand, outcome unknown" (slot 2 was empty afterward; vouchers now 198/25/9).
- Zacian upgrades already owned. Eggs: Zacian 3 (6 each, 21 -> 3 candy), Feebas 14 (12 each, 172 -> 4 candy). 17 eggs total; no vouchers spent.
- Stray inputs while the tab was hidden had added Diglett + Unown to the party; removed (popPartyStarter). Key presses now stepped with STEP_JS (helper _nav.py in prfarm).
- New Classic run slot 2 (modeId 0): Zacian, Feebas, Spinda, Zigzagoon, Kricketot (10/10).
- Cleared stop flag/reason, rotated stdout, launched hidden via Win32_Process Create (pythonw PID 109864). One instance, w6 by 14:41.

## 2026-11-02 14:46-14:49 MST - watch run: caught wild shiny Sentret w14 (double, Zacian run)
- Farm stopped 14:44:11 on shiny_enemy Sentret (wild double with non-shiny Yungoos; Lv9, variant 1, not a boss, 27/27). At 14:46 (past 2 min) state unchanged: turn 1, CommandPhase, only Poke Balls 5, no farm process, no other controller.
- dbl_shiny2.py: Zacian Bitter Blade targeted at Yungoos (bi 3) KO'd it; Feebas Calm Mind. Sentret untouched.
- Poke Ball (5 -> 4) caught first throw (cap_rd.py 80, catch_ack.py). Party had 5, so Sentret joined as slot 6. Logged in CHIE Shiny Log.md (top row; sprite pr_161s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 131892, parent WmiPrvSE 113808). One instance, w16 by 14:49.

## 2026-11-02 15:12-15:17 MST - watch run: caught wild shiny Toucannon w57 (double, Zacian run)
- Farm stopped 15:08:17 on shiny_enemy Toucannon (Lv38, variant 1, not a boss) in a wild double with Simisage. At ~15:12 (past 2 min) state unchanged: CommandPhase turn 1, full HP, no farm process.
- dbl_shiny2.py: Zacian Bitter Blade on Simisage (KO); Milotic Calm Mind. Toucannon untouched.
- Ultra Ball #1 broke out, #2 caught (Ultra 5 -> 3). Party full: chose No at the release prompt (sent to storage; helper _capno.py). Logged in CHIE Shiny Log.md (top row; sprite pr_733s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 40388, parent WmiPrvSE). One instance, w59 by 15:16.

## 2026-11-02 15:37-15:44 MST - watch run: caught wild shiny Articuno w90 (boss, epic variant 3, Zacian run)
- Farm stopped 15:36:34 on shiny_enemy Articuno (wild single boss, Lv74, variant 3, 2 segments, 234/234, Competitive). At 15:39:31 (past 2 min) state unchanged: turn 1, CommandPhase, Rogue Balls 5, no farm process, no other controller.
- Zacian Spirit Break (Fairy, neutral, est. 92-109 vs 117 shield line) via catch_shiny.py Articuno 0 2: clamped at the shield line, 234 -> 117, shield broken. Articuno's Hurricanes took Zacian to 16/256 (Competitive boost).
- Rogue Balls 5 -> 0: four broke free, the fifth caught (catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_144s.png downloaded). New read-only helper _rdmoves.py (field mon stats/moves).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 33148, parent WmiPrvSE 113808). One instance, w92 by 15:43; Zacian healed to full.
- Note: TRANSFER log lines still label the primary as "Lugia" (likely a hardcoded name in the order string; not verified this run).

## 2026-11-02 16:32-16:41 MST - watch run: Zacian run ended w165 (wipe vs Trainer Ghetsis's Eelektross), eggs for Zacian + Feebas, new Zacian run slot 2
- Farm exited 16:29:05 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w165 slot=2 ... DONE farm17". Game untouched until this watch, no other controller. Run Log row confirmed.
- to_title.py -> title. Vouchers 206 regular + 26 Plus + 9 Premium left UNSPENT. Zacian/Feebas upgrades all owned.
- Eggs: Zacian 3 (x6, candy 18 -> 0), Feebas 9 (x12, candy 115 -> 7). Eggs 0 -> 12. Via nav_open.py <sp> + setCursor(8) Use Candies + Buy an Egg (guarded loop).
- New Classic run: nr_pick.py 888,349,327,263,401,299 (Nosepass didn't fit, 10/10). Start -> Yes -> slot 2 (empty). Verified modeId 0, slot 2, wave 1, party [888,349,327,263,401].
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 8092, parent WmiPrvSE 113808). One instance, fighting w1 at 16:40.

## 2026-11-02 17:10-17:13 MST - watch run: caught wild shiny Emolga w53 (single, Zacian run)
- Farm stopped 17:06:42 on shiny_enemy Emolga (wild single, Lv37, variant 1, not a boss, 96/96). At 17:10 (past 2 min) state unchanged: CommandPhase turn 1, full HP, only Poke Balls 10, no farm process, no other controller.
- No attack. catch_shiny.py Emolga 1 0: Poke Ball (10 -> 9) caught first throw (cap_rd.py 80, catch_ack.py). Party had 5, so Emolga joined as slot 6. Logged in CHIE Shiny Log.md (top row; sprite pr_587s.png downloaded).
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 124024, parent WmiPrvSE 113808). One instance, w55 by 17:12.

## 2026-11-02 17:28-17:37 MST - watch run: caught wild shinies Persian w74 and Tauros w78 (singles, Zacian run)
- Farm stopped 17:25:33 on shiny_enemy Persian (Lv47, variant 2, not a boss). At 17:28:52 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 5, no farm process. No attack. catch_shiny.py Persian 1 3: Rogue Ball (5 -> 4) caught first throw (cap_rd.py 80, catch_ack.py). Party had 5, so Persian joined as slot 6. Logged (sprite pr_53s.png downloaded).
- Relaunched (PID 29380); farm stopped again 17:31:31 on shiny_enemy Tauros (Lv51, variant 1). At 17:33:48 unchanged. catch_shiny.py Tauros 1 3: Rogue Ball (4 -> 3) caught first throw. Party full: _capno.py no -> storage. Logged (sprite pr_128s.png downloaded).
- Note: clearing config stop fields with PowerShell Set-Content -Encoding UTF8 added a BOM to pokerogue_farm_config.json; rewrote it without BOM. Use [IO.File]::WriteAllText with UTF8Encoding($false) instead.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 19308, parent WmiPrvSE 113808). One instance, w81 by 17:36.

## 2026-11-02 17:41-17:44 MST - watch run: caught wild shiny Breloom w86 (single, Zacian run)
- Farm stopped 17:38:56 on shiny_enemy Breloom (wild single, Lv58, variant 1, not a boss, 146/146, Poison Heal). At 17:41 (past 2 min) state unchanged: CommandPhase, full HP, Rogue 3, Master 1 (kept for Eternatus), no farm process, no other controller.
- No attack. catch_shiny.py Breloom 1 3: Rogue Ball (3 -> 2) caught first throw (cap_rd.py 80, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_286s.png already present).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 34512, parent WmiPrvSE 113808). One instance, w87 by 17:43.

## 2026-11-02 17:57-18:02 MST - watch run: caught wild shiny Forretress w103 (double, Zacian run)
- Farm stopped 17:52:12 on shiny_enemy Forretress (Lv70, variant 2, not a boss, Sturdy) in a wild double with Scolipede. At 17:57 (past 2 min) state unchanged: CommandPhase, full HP, Rogue 7, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Bitter Blade targeted at Scolipede (bi 3) KO'd it; Milotic Calm Mind. Forretress untouched.
- Rogue Ball (7 -> 6) caught first throw (cap_rd.py 80, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_205s.png downloaded).
- Cleared flag, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 52468, parent WmiPrvSE 113808). One instance, w107 by 18:02.

## 2026-11-02 18:09-18:13 MST - watch run: caught wild shiny Ariados w113 (single, Zacian run)
- Farm stopped 18:05:20 on shiny_enemy Ariados (wild single, Lv87, variant 3, not a boss, 229/229, Swarm). At 18:09:40 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 6, Master 1 (kept for Eternatus), no farm process, no other controller.
- No attack. catch_shiny.py Ariados 1 3: Rogue Ball (6 -> 5) caught first throw (cap_rd.py 80, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_168s.png downloaded). New read-only helper _rdfull.py (phase/turn/party HP/balls/enemy boss state).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 103420, parent WmiPrvSE 113808). One instance, fighting w114 by 18:12.

## 2026-11-02 18:24-18:30 MST - watch run: shiny Aegislash w125 (double) - Gavin finished the catch
- Farm stopped 18:16:48 on shiny_enemy Aegislash (Lv90, variant 1, not a boss) in a wild double with Claydol. At 18:24 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 20, Master 1, no farm process.
- dbl_shiny2.py: Zacian Spirit Break targeted at Claydol (bi 2) KO'd it; Milotic Calm Mind. Aegislash untouched.
- While this run's ball command was queued, a manual throw was already in progress (ball cmd returned "bad phase"; AttemptCapturePhase began without our input). Gavin caught Aegislash himself (Rogue 20 -> 18) and put it in the party in place of Emolga, then started pr_farm17 from PokeFarmControl at 18:27:20 (PID 123544). No further input from the watch.
- Logged in CHIE Shiny Log.md (top row, 18:27, Caught, Rogue Ball; sprite pr_681s.png present). Farm fighting w127 by 18:28.

## 2026-11-02 18:35 MST - watch run: shiny Brambleghast w139 (double) - game reloaded, left to Gavin (no input sent)
- Farm stopped 18:32:06 on shiny_enemy Brambleghast (wild double, Lv111, variant 1, slot 1). At 18:35 (past 2 min) the game was on LoginPhase / loading modal with an empty party (page reloaded by someone else), no farm process. State changed, so Gavin is handling it: no input sent. Next watch: check outcome, log the shiny (Caught/Missed) and resume only once idle and understood.

## 2026-11-02 18:44-18:50 MST - watch run: caught wild shiny Magcargo w154 (double, Zacian run)
- Farm stopped 18:39:40 on shiny_enemy Magcargo (Lv124, variant 1, not a boss, Flame Body) in a wild double with Gogoat. At 18:45 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 17, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Bitter Blade targeted at Gogoat (bi 2) KO'd it; Milotic Calm Mind. Magcargo untouched.
- Rogue Ball (17 -> 16) caught first throw (cap_rd.py, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_219s.png present).
- Brambleghast w139 (18:32, left to Gavin) still has no Shiny Log row: outcome unconfirmed (Rogue 18 -> 17 between 18:27 and 18:39, dex 947 shiny flag set, not in party). Not logged to avoid guessing.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 9520, parent WmiPrvSE 113808). One instance, w158 by 18:49.

## 2026-11-02 18:52-18:57 MST - watch run: caught wild shiny Grumpig w162 (double, Zacian run)
- Farm stopped 18:50:42 on shiny_enemy Grumpig (Lv128, variant 1, not a boss, Own Tempo) in a wild double with Magmortar (Fire). At 18:52:44 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 16, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, single-target, SE) targeted at Magmortar (bi 3) KO'd it; Milotic Calm Mind. Grumpig untouched.
- Rogue Ball (16 -> 15) caught first throw (cap_rd.py, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_326s.png downloaded).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 77884, parent WmiPrvSE 113808). One instance, w163 by 18:56.

## 2026-11-02 19:00-19:03 MST - watch run: caught wild shiny Magmortar w166 (double, Zacian run)
- Farm stopped 18:58:26 on shiny_enemy Magmortar (Lv135, variant 3, not a boss, Flame Body) in a wild double with Torkoal (Fire). At 19:00:44 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 15, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, single-target, SE) targeted at Torkoal (bi 3) KO'd it; Milotic Calm Mind. Magmortar untouched.
- Rogue Ball (15 -> 14) caught first throw (cap_rd.py, catch_ack.py). Party full: _capno.py no -> storage (crashed only printing a ruble sign; harmless). Logged in CHIE Shiny Log.md (top row; sprite pr_467s.png downloaded).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (pythonw PID 36132, parent WmiPrvSE). One instance, w170 by 19:03.

## 2026-11-02 19:28-19:33 MST - watch run: manual play in progress, no input sent
- Flag still set from the 19:09 shiny_enemy Malamar stop (w187, double), but no farm process is running and the game advanced w191 -> w194 within ~5 min: Gavin is playing by hand. No input sent.
- Malamar (dex 687) caughtAttr 150 includes the shiny bit, caughtCount 2, not in party; can't tell if this w187 shiny was the catch, so no Shiny Log row added yet.

## 2026-11-02 19:33 MST - watch run: manual play continues, no input sent
- Flag still set from the 19:09 Malamar shiny stop; no farm process. Game now w198 (SelectModifierPhase), up from w194 at ~19:30: Gavin still playing by hand. Party full HP; Rogue 17, Master 1. No input sent. Malamar w187 outcome still unlogged.

## 2026-11-02 19:37 MST - watch run: run ended during manual play, Gavin on starter select, no input sent
- Flag still set from the 19:09 Malamar shiny stop; no farm process. Game was w198 at 19:33 and is now SelectStarterPhase (party empty): the run ended under Gavin's hand (no Run Log row written, since the farm wasn't running). Outcome (wipe or Classic win) unknown.
- Candy now: Zacian 0, Feebas 90, Mudkip 8; 5 eggs in the egg list. Gavin may be doing run-end steps / new-run setup himself. No input sent.
- MUDKIP SWAP still pending: if a later watch finds starter select idle 10+ min with no new run, do the Feebas eggs (and any remaining Zacian candy) and build Zacian + Mudkip + helpers, then launch hidden.
## 2026-11-02 19:44 MST - watch run: Gavin started a Zacian + Mudkip run himself, farm healthy
- Gavin set up the new run by hand and launched pr_farm17.py from PokeFarmControl at 19:42 (PID 62980). Party: Zacian, Mudkip, Zigzagoon, Kricketot, Spinda. MUDKIP SWAP effectively DONE (by Gavin). Wave 8 by 19:44, one instance, no stop flag. No input sent.
- Ended run (w198+) wrote no Run Log row (farm wasn't running when it ended).

## 2026-11-02 19:47 MST - watch run: MUDKIP secondary patch in pr_farm17.py
- SECONDARY now includes the Mudkip line (258/259/260) alongside Feebas/Milotic, so Mudkip gets secondary heals, Soothe Bells, revives and stays in slot 2 at reward screens (REORDER_JS).
- Orbs stay Feebas/Milotic-only (orb_for_sec checks sp 349/350), so Mudkip never gets a Flame/Toxic Orb. The no-status-cure rule now applies only to Feebas/Milotic, so Mudkip's status can be cured.
- Backup pr_farm17.py.bak_mudkip_1946. Safe restart at w19 (killed PID 62980, relaunched hidden via Win32_Process Create).

## 2026-11-02 20:41 MST - watch run: Mudkip status cures at reward screens
- Bug: the reward-screen party target check still blocked Full Heal/status cures on ANY secondary, so a burned Swampert (Mudkip line) had Full Heal redirected to Zacian and blacklisted ("SEC STATUS skip ... Milotic").
- Fix: the SEC_NO_STATUS_CURE check in the SelectModifierPhase secondary-target gate (and its log line) now applies only to Feebas/Milotic (sp 349/350), matching shop_plan. Mudkip/Marshtomp/Swampert get status cures normally.
- Backup pr_farm17.bak_mudstatus_20261102_2045.py. Safe restart at w139 (killed PID 12900 from the control app, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py, PID 3876, parent WmiPrvSE 113808). One instance, w140 pre-heal by 20:42.

## 2026-11-02 20:49-20:57 MST - watch run: caught wild shinies Wailord w154 (single) and Tentacruel w155 (double), Zacian run
- Farm stopped 20:47:28 on shiny_enemy Wailord (wild single, Lv128, variant 1, not a boss). At 20:49:40 (past 2 min) state unchanged: CommandPhase turn 1, no farm process. No attack. catch_shiny.py Wailord 1 3: Rogue Ball (15 -> 14) caught first throw. Party had 5, so Wailord joined as slot 6. Logged (sprite pr_321s.png downloaded).
- Relaunched (PID 35768); stopped again 20:51:09 on shiny_enemy Tentacruel (Lv127, variant 1) in a wild double with a non-shiny Tentacruel. At 20:53:44 unchanged. dbl_shiny2.py: Zacian Mighty Cleave (Rock, neutral, single-target) at the partner (bi 3) KO'd it; Swampert (Mudkip line) Shore Up. Rogue Ball (14 -> 13) caught first throw. Party full: _capno.py no -> storage. Logged (sprite pr_73s.png downloaded).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 56560, parent WmiPrvSE). One instance, fighting w158 by 20:57.

## 2026-11-02 21:10-21:16 MST - watch run: caught wild shiny Weavile w178 (double, Zacian run)
- Farm stopped 21:03:40 on shiny_enemy Weavile (Lv144, variant 1, not a boss, Pressure) in a wild double with Abomasnow (Grass/Ice). At 21:11 (past 2 min) state unchanged: CommandPhase turn 1, full HP, Rogue 13, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Bitter Blade (Fire, single-target, 4x) targeted at Abomasnow (bi 3) KO'd it; Swampert Shore Up. Weavile untouched.
- Rogue Ball (13 -> 12) caught first throw (cap_rd.py, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_461s.png downloaded).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py.

## 2026-11-02 21:37-21:40 MST - watch run: shiny Cacnea w34 handled by Gavin, no input sent
- New Zacian + Marshtomp run (helpers Zigzagoon, Spinda, Kricketot, Phanpy) farming from the control app. Farm stopped 21:36:09 on shiny_enemy Cacnea (wild, Lv22, variant 1, w34, single slot). Within a minute the game moved on and pr_farm17.py was relaunched from PokeFarmControl (PID 24852, 21:36:52): Gavin handled it. No input sent.
- Cacnea (331) dex: shiny flag set, caughtCount 1, not in party; outcome (caught to storage or missed) not confirmed, so no Shiny Log row yet. Farm fighting w35 at 21:38, one instance.

## 2026-11-02 22:21-22:25 MST - watch run: caught wild shiny Simipour w166 (double, Zacian run)
- Farm stopped 22:18:21 on shiny_enemy Simipour (Lv137, variant 1, not a boss, Gluttony) in a wild double with Zebstrika (Electric, Motor Drive). At 22:21 (past 2 min) state unchanged: CommandPhase turn 1, Rogue 24, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, neutral, single-target) targeted at Zebstrika (bi 2) KO'd it; Swampert Shore Up. Simipour untouched.
- Rogue Ball (24 -> 23) caught first throw (cap_rd.py, catch_ack.py). Party full: _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_516s.png present).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 82584, parent WmiPrvSE). One instance, w170 by 22:24.

## 2026-11-02 22:30 MST - watch run: shiny Chimecho w174 (double) handled by another controller, no input sent
- Farm stopped 22:25:52 on shiny_enemy Chimecho (wild, Lv138, variant 2, not a boss) in a double with Gengar. At 22:30 the game was on CommandPhase turn 1, but within seconds it moved to SelectModifierPhase with both Chimecho and Gengar at 0 HP, Rogue 33 -> 32, Zacian Lv168 -> 170, with no farm process running: Gavin (or another session) is driving. No input sent. Outcome (caught or missed) to confirm next run before logging.

## 2026-11-02 22:32 MST - watch run: second shiny Chimecho w176 (double) handled by Gavin, no input sent
- Farm (relaunched after the w174 Chimecho) stopped 22:31:35 on shiny_enemy Chimecho (wild, Lv149, variant 2, not a boss) in a double with Golurk. By 22:32:11, well inside the 2-minute wait, the game was on SelectModifierPhase with both foes at 0 HP and Rogue 32 -> 31; by 22:32:39 it was on w177 with no farm process. Gavin is playing by hand. No input sent.
- Chimecho (358) dex: shiny flag set, caughtCount 3. Neither the w174 nor the w176 Chimecho outcome (caught or missed) is confirmed, so no Shiny Log rows were added.

## 2026-11-02 22:43-22:59 MST - watch run: caught shiny Brute Bonnet w199, Eternatus caught with the Master Ball (Classic win), eggs, new Zacian + Mudkip run slot 2
- Farm stopped 22:41:43 on shiny_enemy Brute Bonnet (Lv175, variant 2, not a boss) in a wild double with Roaring Moon. At 22:43:55 (past 2 min) unchanged: CommandPhase turn 1, full HP, no farm process. dbl_shiny2.py: Zacian Spirit Break at Roaring Moon (bi 2) KO'd it; Swampert Shore Up. Rogue Ball (41 -> 40) caught first throw; party full, _capno.py no -> storage. Logged in CHIE Shiny Log.md (top row; sprite pr_986s.png downloaded).
- Relaunched; farm stopped at w200 (eternatus_catch, 22:46:35, Master Ball 1). At 22:49 (past 2 min) untouched, no other controller. Acked "Foe Eternatus appeared!" to CommandPhase, threw the Master Ball (new helper mb_eternatus.py = dbl_shiny2.py ball mode limited to ball 4 at wave 200): Eternatus caught, party full -> storage. Run ended GameOverPhase (Classic win).
- Run Log row written by hand (farm wasn't running at the end): 22:50, slot 2, w200, luck 12, "Classic win: Eternatus caught with the Master Ball".
- to_title.py -> title -> New Game -> Classic (helper _re.py). Upgrades all owned. Eggs: Zacian 6 (x6, candy 36 -> 0), Feebas 3 (x12, candy 38 -> 2). Eggs 0 -> 9. Mudkip candy 71 untouched. Vouchers 271/52/15 unspent.
- New Classic run slot 2 (empty): Zacian, Mudkip, Spinda, Zigzagoon, Kricketot (Nosepass didn't fit). Note: StarterSelect needs ~15 frame steps after a RIGHT press before startCursorObj shows. Verified Classic, wave 1, slot 2, modeId 0.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 110772, parent WmiPrvSE 113808). One instance, w5 by 22:59.

## 2026-11-02 23:17-23:19 MST - watch run: shiny Skiddo w53 caught by Gavin, no input sent
- Farm stopped 23:13:09 on shiny_enemy Skiddo (wild single, Lv32, variant 1). By 23:17 (past the 2-minute wait) the game was on w54 with Skiddo in party slot 6 and pr_farm17.py relaunched from PokeFarmControl at 23:17:23 (PID 19004): Gavin caught it himself. No input sent.
- Logged in CHIE Shiny Log.md (top row, 23:13, Caught, ball unknown; sprite pr_672s.png downloaded). Farm fighting w54, one instance.

## 2026-11-02 23:45-23:48 MST - watch run: shiny backfill (5 Caught rows), Zacian + Mudkip run healthy w136
- Per Gavin's 23:41 rule (log every caught shiny, whoever catches it), settled five hand-handled stops from dex data (PokéRogue keeps no PC box; a catch with a full party only registers in the dex). Live dexData caughtAttr: Brambleghast 947 = 158 (shiny v1 only, no non-shiny bit, ct 2), Malamar 687 = 150 (shiny v1 only, ct 2), Cacnea 331 = 159 (shiny v1 + non-shiny, ct 1, no earlier shiny Cacnea logged), Chimecho 358 = 190 (shiny + variant-2 bit, no non-shiny bit, ct 3). No earlier log rows for any of them, and Rogue Balls dropped by one at the Brambleghast and both Chimecho stops.
- Added to CHIE Shiny Log.md, newest-first at their stop times, all Caught: Chimecho 22:31 (Lv149, v2, w176, Rogue Ball), Chimecho 22:25 (Lv138, v2, w174, Rogue Ball), Cacnea 21:36 (Lv22, v1, w34, ball unknown), Malamar 19:09 (Lv153, v1, w187, ball unknown), Brambleghast 18:32 (Lv111, v1, w139, Rogue Ball). Sprites pr_358s/pr_331s/pr_687s/pr_947s downloaded. Backup Shiny Log.md.bak_backfill_2345.
- Farm: pr_farm17.py launched from PokeFarmControl 23:41 (PID 18584), one instance, fighting w136 at 23:45 (Zacian, Swampert, Linoone, Spinda, Magmortar, Kricketot). No game input sent.

## 2026-11-02 23:54 - 2026-11-03 00:03 MST - watch run: Zacian + Mudkip run ended w140 (wild Kingler), eggs bought, shiny Magmortar logged; Gavin setting up next run
- Farm (pr_farm17, launched 23:41) wiped at w140 vs a wild Kingler (Hyper Cutter) at 23:46:55; the game reset to the title but the session in slot 2 was NOT cleared (no run-history entry), and the farm stopped on "PRIMARY Zacian MISSING 30s+" without writing a Run Log row. Gap: the ALL-FAINT -> title path skips the run-log/run-end handling.
- Shiny Log: added the missing shiny Magmortar (23:39, Lv98, v3, Caught, w122, ball unknown; it was in the party at w140). Backup Shiny Log.md.bak_magmortar_2355.
- Eggs (before noticing the slot was still occupied): Zacian 4 (x6, candy 24 -> 0), Feebas 1 (x12, candy 16 -> 4). Eggs 0 -> 5. Mudkip candy 98 untouched. Vouchers 279/53/16 unspent.
- Slot 2 still held the w140 save, so instead of a new run I reloaded it via Load Game (new helper _reload.py load <slot>; picks "Load Game" in the slot option menu) and relaunched the farm hidden (PID 80540). Same seeded wipe vs Kingler at 00:01:30; this time the farm saw the faint, wrote the Run Log row (00:01, slot 2, w140, luck 3, "Wild: Kingler") and the game over cleared normally. No new candy after the wipe.
- At 00:02 the game was on StarterSelect with Zacian + Mudkip already picked and no script running: Gavin is setting up the next run by hand. No further input sent.

## 2026-11-03 00:34-00:40 MST - watch run: caught wild shiny Persian (Alolan) w108 (double, Zacian run); Gavin took over right after
- Farm stopped 00:30:20 on shiny_enemy Persian (Alolan, sid 2053, Dark, Lv81, variant 1, not a boss, Fur Coat) in a wild double with Alolan Marowak (Fire/Ghost). At 00:34 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 15, Master 1, no farm process.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, single-target) at Marowak (bi 2) KO'd it; Swampert Shore Up. Persian untouched.
- While my helper was only stepping frames, someone else (Gavin, by hand; no farm process) threw a Rogue Ball (15 -> 14): Persian caught and joined as party slot 6. Gavin then picked the reward and kept playing (w109 Ninetales, then a new biome). I stopped sending input.
- Logged in CHIE Shiny Log.md (top row, 00:30, Caught, Rogue Ball; sprite pr_53s.png, no separate Alolan icon in the assets repo). Backup Shiny Log.md.bak_persian_0040.
- Farm not relaunched: Gavin is driving by hand. Stop flag left in place; resume once the game has sat idle ~10 min.

## 2026-11-03 00:42-00:45 MST - watch run: Heal Block loop fixed (w114 Bronzong, Saturn trainer)
- Farm (pr_farm17, launched from PokeFarmControl 00:37 after Gavin's Persian catch) looped from 00:39:20 at w114 re-picking Bitter Blade every ~1.4s; game message "Zacian is prevented from healing, so it can't use Bitter Blade!" (Heal Block). The NOPP guard only recognised "no PP" messages.
- PATCH pr_farm17.py (backup pr_farm17.bak_healblock_20261103_0045.py): the NOPP stuck check also fires on "can't use" / "cannot use" / "prevented from" messages, so a blocked move (Heal Block, Imprison, Disable, etc.) is marked dead for the wave and the next move is tried.
- Killed PID 157776, cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 102228, parent WmiPrvSE). Log 00:43:27 "NOPP stuck on ['Bitter Blade']" -> Spirit Break; fight moving on through the w114 trainer team. One instance.

## 2026-11-03 01:06-01:11 MST - watch run: caught wild shiny Rabsca w142 (double, Zacian run)
- Farm stopped 01:04:48 on shiny_enemy Rabsca (sid 954, Bug/Psychic, Lv110, variant 1, not a boss) in a wild double with Sandslash. Unchanged after the 2-minute wait (CommandPhase turn 1, full HP, Rogue 24, no farm process).
- dbl_shiny2.py: Zacian Spirit Break (single-target) at Sandslash (bi 2) KO'd it; Swampert Shore Up. Next turn Rogue Ball (24 -> 23): caught. Party full, picked "No" at the release prompt (new helper _optno.py; _opts.py reads OptionSelect labels). Dex 954 caughtCount 2, shiny bit set.
- Logged in CHIE Shiny Log.md (top row, 01:04, Caught, Rogue Ball); sprite pr_954s.png downloaded. Backup Shiny Log.md.bak_rabsca_0110.
- Cleared flag/reason, rotated stdout, relaunched hidden (Win32_Process Create, PID 31980). Farm at w143 by 01:10. One instance.

## 2026-11-03 01:55-02:02 MST - watch run: Zacian + Mudkip run ended w195 (wipe vs Rival Ivy's Baxcalibur), eggs bought, new run slot 2
- Farm exited 01:54:10 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w195 slot=2 luck=1 ... DONE farm17". Run Log row confirmed. No other controller.
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs: Zacian 2 (x6, candy 13 -> 1), Feebas 0 (candy 6, egg costs 12). Eggs 3 -> 5. Mudkip candy 27 untouched. Vouchers 295/59/17 unspent.
- nr_pick.py 888,258,327,263,401,299: all six fit this time (Zacian, Mudkip, Spinda, Zigzagoon, Kricketot, Nosepass). _re.py "start" assert failed with a full 6-party (startCursorObj not reached); used _re.py key 4 (SUBMIT) -> Confirm Yes -> slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 18180, parent WmiPrvSE 113808). One instance, w5 by 02:01.

## 2026-11-03 03:33-03:38 MST - watch run: caught wild shiny Swanna w146 (double, Zacian run)
- Farm stopped 03:32:36 on shiny_enemy Swanna (sid 581, Water/Flying, Lv115, variant 1, not a boss) in a wild double with Golduck. Unchanged after the 2-minute wait (CommandPhase turn 1, full HP, Rogue 25, no farm process).
- dbl_shiny2.py: Zacian Spirit Break (single-target) at Golduck (bi 2) KO'd it; Swampert Shore Up. Next turn Rogue Ball (25 -> 24): caught. Party full, _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 03:32, Caught, Rogue Ball); sprite pr_581s.png downloaded. Backup Shiny Log.md.bak_swanna_0340.
- Cleared flag/reasons, rotated stdout, relaunched hidden (Win32_Process Create, PID 144048, parent WmiPrvSE). Farm picking w146 rewards by 03:37. One instance.

## 2026-11-03 04:03-04:06 MST - watch run: caught wild shiny Komala w175 (single, Zacian run)
- Farm stopped 03:59:14 on shiny_enemy Komala (sid 775, wild single, Lv145, variant 1, not a boss, 352/352). At 04:02:57 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 44, Master 1 (kept for Eternatus), no farm process, no other controller.
- No attack. catch_shiny.py Komala 1 3: Rogue Ball (44 -> 43) caught first throw (cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 03:59, Caught, Rogue Ball); sprite pr_775s.png downloaded. Backup Shiny Log.md.bak_komala_0405.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 162932, parent WmiPrvSE 113808). One instance, fighting w176 by 04:05.

## 2026-11-03 04:08-04:12 MST - watch run: caught wild shiny Cherrim w179 (single, Zacian run)
- Farm stopped 04:06:31 on shiny_enemy Cherrim (sid 421, wild single, Lv156, variant 1, not a boss, 384/384). At 04:09:02 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 43, Master 1 (kept for Eternatus), no farm process, no other controller.
- No attack. catch_shiny.py Cherrim 1 3: Rogue Ball (43 -> 42) caught first throw (cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 04:06, Caught, Rogue Ball). Sprite: icons/4/421s.png doesn't exist; used 421s-overcast.png as pr_421s.png. Backup Shiny Log.md.bak_cherrim_0411.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 67388, parent WmiPrvSE 113808). One instance, fighting w180 by 04:11.

## 2026-11-03 04:16-04:23 MST - watch run: caught wild shiny Dusknoir w185 (double, epic variant, Zacian run)
- Farm stopped 04:15:54 on shiny_enemy Dusknoir (sid 477, Ghost, Lv154, variant 3, not a boss, Pressure) in a wild double with Chandelure (Ghost/Fire, Lv161). At 04:18:13 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 47, Master 1 (kept for Eternatus), no farm process, no other controller.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, single-target, 2x on Fire) at Chandelure (bi 3) KO'd it; Swampert Shore Up. Dusknoir untouched.
- Rogue Ball 1 (47 -> 46) broke out; Rogue Ball 2 (46 -> 45) caught (cap_rd.py "Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 04:15, Caught, Rogue Ball); sprite pr_477s.png downloaded. Backup Shiny Log.md.bak_dusknoir_0425.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 128056, parent WmiPrvSE 113808). One instance, picking w185 rewards by 04:22.

## 2026-11-03 04:37-04:48 MST - watch run: Eternatus caught with the Master Ball (Classic win w200), eggs, new Zacian + Mudkip run slot 2
- Farm stopped 04:34:21 at w200 (eternatus_catch, Master Ball 1). At 04:37 (past 2 min) untouched, no other controller. Stepped/acked to CommandPhase (declined the ScanIvs confirm with new helper _confno.py), Eternatus not shiny. mb_eternatus.py ball: Master Ball (1 -> 0) caught it; party full, _optno.py "No" -> storage. GameOver (Classic win) -> title.
- Run Log row written by hand: 04:40, slot 2, w200, luck unknown, "Classic win: Eternatus caught with the Master Ball" (backup Run Log.md.bak_w200_0445).
- _re.py newgame (Classic). Eggs: Zacian 4 (x6, candy 28 -> 4), Feebas 0 (candy 6, egg costs 12). Eggs 0 -> 4. Mudkip candy 68 untouched. Vouchers 307/61/19 unspent.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 (Confirm Yes) -> slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 68348, parent WmiPrvSE). One instance, w4 by 04:47.

## 2026-11-03 06:03-06:08 MST - watch run: caught wild shiny Pincurchin w139 (double, Zacian + Mudkip run)
- Farm stopped 06:01:46 on shiny_enemy Pincurchin (sid 871, Electric, Lv110, variant 1, not a boss, Lightning Rod) in a wild double with Basculin (Water, Lv109). At 06:04:16 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 20, Master 0, no farm process, no other controller.
- dbl_shiny2.py: Zacian Spirit Break (Fairy, single-target) at Basculin (bi 3) KO'd it; Swampert Shore Up. Pincurchin untouched.
- Rogue Ball (20 -> 19) caught first throw (cap_rd.py "Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 06:01, Caught, Rogue Ball); sprite pr_871s.png downloaded. Backup Shiny Log.md.bak_pincurchin_0608.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 120984, parent WmiPrvSE). One instance, fighting w140 (Gym Leader Juan) by 06:07.

## 2026-11-03 06:16-06:20 MST - watch run: caught wild shiny Golisopod w143 (single, Zacian + Mudkip run)
- Farm stopped 06:09:49 on shiny_enemy Golisopod (sid 768, wild single, Lv118, variant 1, not a boss, 307/307). At 06:16 (past 2 min) unchanged: CommandPhase turn 1, full HP, Rogue 19, Master 0, no farm process, no other controller.
- No attack. catch_shiny.py Golisopod 1 3: Rogue Ball (19 -> 18) caught first throw (cap_rd.py "Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 06:09, Caught, Rogue Ball); sprite pr_768s.png downloaded. Backup Shiny Log.md.bak_golisopod_0619.
- Shiny backfill (Brambleghast/Malamar/Cacnea/Chimecho x2) was already settled on Nov 2 (see the 23:41-rule entry); nothing more to add.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 139472, parent WmiPrvSE 113808). One instance, w144 mystery encounter by 06:18.

## 2026-11-03 06:40-06:45 MST - watch run: caught wild shiny Scovillain w173 (double, Zacian + Mudkip run)
- Farm stopped 06:37:02 on shiny_enemy Scovillain (sid 952, Grass/Fire, Lv145, variant 1, not a boss) in a wild double with Donphan (Ground, Sturdy, Lv142). At ~06:40 (past 2 min) unchanged: CommandPhase turn 1, Rogue 18, Master 0, no farm process, no other controller (only PokeFarmControl's poll).
- dbl_shiny2.py, 2 turns: Zacian Bitter Blade (single-target) at Donphan (bi 2), Sturdy held it the first turn, KO'd on the second; Swampert Shore Up both turns. Scovillain untouched (368/368).
- Rogue Ball (18 -> 17) caught first throw (cap_rd.py "Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 06:37, Caught, Rogue Ball); sprite pr_952s.png downloaded. Backup Shiny Log.md.bak_scovillain_0645.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 170408, parent WmiPrvSE 113808). One instance, fighting w174 by 06:44.
- Note: TRANSFER log lines still say "Lugia"/"no milotic" as the order labels in a Zacian + Mudkip run; cosmetic for now, worth a look if item routing seems off.

## 2026-11-03 07:23 MST - watch run: Eternatus stop w200, no Master Ball
- Farm stopped 07:05:21 at w200 (eternatus_catch). Master Ball 0, Rogue 22, Ultra 10, Great 5, Poke 10. Party full HP. No input sent; handed off to Gavin. Farm not restarted (waiting on him).

## 2026-11-03 09:24-09:28 MST - watch run: caught wild shiny Gogoat w109 (single, Zacian + Mudkip run)
- Eternatus w200 stop from 07:05 was resolved by someone else; new run (Zacian, Swampert, Spinda, Krigoon, Probopass) was at w109.
- Farm stopped 09:23:01 on shiny_enemy Gogoat (sid 673, wild single, Lv84, variant 1, not a boss, 314/314). At 09:25:20 (past 2 min) unchanged: CommandPhase turn 1, Rogue 15, Master 0, no farm process, no other controller.
- No attack. catch_shiny.py Gogoat 1 3: Rogue Ball (15 -> 14) caught first throw (cap_rd.py "Gotcha!", catch_ack.py). Party had 5, so Gogoat joined as slot 6.
- Logged in CHIE Shiny Log.md (top row, 09:23, Caught, Rogue Ball); sprite pr_673s.png present. Backup Shiny Log.md.bak_gogoat_0927.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 153568, parent WmiPrvSE 113808). One instance, fighting w110 by 09:27.

## 2026-11-03 09:55-10:01 MST - watch run: Zacian + Mudkip run ended w146 (wipe vs wild G-Max Garbodor), 6 Zacian eggs, new run slot 2
- Farm exited 09:54:51 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w146 slot=2 luck=1 ... DONE farm17". Run Log row confirmed. No other controller (only PokeFarmControl's poll).
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs: Zacian 6 (x6, candy 36 -> 0), Feebas 0 (candy 6, egg costs 12). Eggs 1 -> 7. Mudkip candy 156 untouched. Vouchers 332/71/22 unspent.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 (Confirm Yes) -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 85148, parent WmiPrvSE). One instance, w1 rewards by 10:01.

## 2026-11-03 10:50-10:56 MST - watch run: caught wild shiny Malamar w88 (double, Zacian + Mudkip run)
- Farm stopped 10:50:08 on shiny_enemy Malamar (sid 687, Dark/Psychic, Lv60, variant 1, not a boss, Contrary) in a wild double with a non-shiny Malamar (Lv65). At 10:52:29 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 / Great 0 / Ultra 0 / Rogue 0 / Master 1, no farm process, no other controller.
- dbl_shiny2.py: Zacian Spirit Break (single-target) at the partner (bi 2) KO'd it; Swampert Shore Up. Shiny untouched (185/185).
- Poke Ball (5 -> 4; no Rogue/Ultra/Great held) caught first throw ("Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 10:50, Caught, Poké Ball); sprite pr_687s.png present. Backup Shiny Log.md.bak_malamar_1056.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 28544, parent WmiPrvSE 113808). One instance, fighting w89 by 10:55.
- Note: ball stock is low (Poke 4, no Rogue/Ultra/Great) for future shiny catches.

## 2026-11-03 10:59-11:03 MST - watch run: Zacian + Mudkip run ended w90 (wipe vs wild double Empoleon/Floatzel), no eggs affordable, new run slot 2
- Farm exited 10:57:45 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w90 slot=2 luck=3 ... DONE farm17". Run Log row confirmed. No other controller.
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs: none bought (Zacian candy 3, egg costs 6; Feebas candy 6, egg costs 12). Eggs 6. Mudkip candy 173 untouched. Vouchers 338/71/22 unspent.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 (Confirm Yes) -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 36472, parent WmiPrvSE 113808). One instance, w4 by 11:03.

## 2026-11-03 11:53-11:59 MST - watch run: caught wild shiny Hypno w89 (double, Zacian + Mudkip run)
- Farm stopped 11:49:24 on shiny_enemy Hypno (sid 97, Psychic, Lv66, variant 1, not a boss, Insomnia) in a wild double with Sigilyph (Psychic/Flying, Lv64). At 11:53 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 25 / Great 10 / Ultra 0 / Rogue 5 / Master 0, no farm process, no other controller.
- dbl_shiny2.py: Zacian Mighty Cleave (Rock, single-target, 2x on Flying) at Sigilyph (bi 2) KO'd it; Swampert Shore Up. Hypno untouched (192/192).
- Rogue Ball (5 -> 4) caught first throw ("Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 11:49, Caught, Rogue Ball) via _addrow_hypno.py; sprite pr_97s.png present. Backup Shiny Log.md.bak_hypno_1158.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 107284, parent WmiPrvSE 113808). One instance, w91 by 11:57.

## 2026-11-03 12:33-12:42 MST - watch run: MISSED wild shiny Floatzel w150 (double, both bosses, Zacian + Mudkip run)
- Farm stopped 12:31:21 on shiny_enemy Floatzel (sid 419, Water, Lv131, variant 2, boss with 1 shield, Swift Swim) in a wild double with boss Palafin (Lv133). At 12:33:54 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 30 / Great 10 / Ultra 0 / Rogue 9 / Master 1, no farm process, no other controller.
- dbl_shiny2.py, 2 turns: Zacian Spirit Break at Palafin (446 -> 223 clamped at its shield, then KO); Swampert Growl (single-target here) then Shore Up.
- Shield break on Floatzel: Zacian Spirit Break (STAB Fairy, est. ~350-410 raw vs 410 HP) relying on the boss shield clamp to stop at 205. It did NOT clamp: Floatzel was KO'd from full HP. Missed.
- LESSON: never rely on the shield clamp. For shield breaks pick a move whose max roll (incl. crit) stays under half the shiny's current HP (e.g. resisted Bitter Blade vs Water), even if it takes two hits. New helper _shatk.py (dbl_shiny2 + modes shatk FIELD MOVE / stgt BI, only allowed on a shielded shiny).
- Logged Missed in CHIE Shiny Log.md (top row, 12:31, Ball —) via _addrow_floatzel.py; sprite pr_419s.png present. Backup Shiny Log.md.bak_floatzel_1240.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 161500, parent WmiPrvSE 113808). One instance, w152 by 12:40.

## 2026-11-03 12:46 MT - Mega Bracelet -380 / Swampertite -370 (Swampert-only target); Master Ball -400 unchanged. Backups *.bak_mega_20261103_1244. Restarted hidden PID 163968, w168.

## 2026-11-03 13:01 MST - watch run: Eternatus stop w200 (12:59:22, Master Ball 1) taken over by someone else
- At 13:01 (past 2 min) the game was on the TitlePhase, so another controller (likely Gavin) is handling wave 200. No input sent, farm not restarted. Next watch: settle the outcome (Eternatus caught? run ended?) and do run-end steps incl. MUDKIP EGGS if the run ended.

## 2026-11-03 13:10 MST - watch run: w200 run end handled by another controller; MUDKIP EGGS DONE
- The w200 run (Eternatus stop 12:59, Master Ball 1) was finished by someone else (likely Gavin); new run started ~13:06 from PokeFarmControl (pr_farm17.py PID 92580, parent PokeFarmControl pythonw), one instance, w16 by 13:09.
- MUDKIP EGGS DONE (by the other controller): Mudkip candy 173 at 11:03 -> 50 now; 15 Mudkip eggs hatched at w10 (13:07), one shiny Mudkip var 2 (already in Shiny Log). Mudkip candy is now left unspent again. Zacian candy 5, Feebas 6. Vouchers 360/73/25 unspent. Eternatus dex caughtCount 6.
- Run Log.md has no row for the w200 run (newest row 10:57 w90); outcome (Eternatus caught or not) not confirmed from data. No game input sent this watch.

## 2026-11-03 13:35-13:40 MST - watch run: caught wild shiny Aggron w94 (double, Zacian + Mudkip/Swampert run)
- Farm stopped 13:33:00 on shiny_enemy Aggron (sid 306, Steel/Rock, Lv63, variant 1, not a boss, Sturdy) in a wild double with Rhydon (Lv63). At 13:35 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 20 / Great 0 / Ultra 5 / Rogue 5 / Master 0, no farm process, no other controller.
- _shatk.py: Zacian Spirit Break (single-target) at Rhydon (bi 2) KO'd it; Swampert Shore Up. Aggron untouched by us (164/176 after its own turn chip).
- Rogue Ball (5 -> 4) caught first throw (catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 13:33, Caught, Rogue Ball) via _addrow_aggron.py; sprite pr_306s.png present. Backup Shiny Log.md.bak_aggron_1340.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create pythonw pr_farm_launch_hidden.py (PID 35280, parent WmiPrvSE 113808). One instance, w96 by 13:39. (Config rewritten without BOM after clearing.)

## 2026-11-03 13:53-13:57 MST - watch run: Zacian + Swampert run ended w142 (wipe vs Trainer Riley's Landorus), new run slot 2
- Farm exited 13:53:23 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w142 slot=2 luck=2 ... DONE farm17". Run Log row confirmed. No other controller (state unchanged 13:53-13:54).
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs: Zacian 3 (x6, candy 18 -> 0). Feebas none (rule: never). Mudkip candy 67 left unspent (MUDKIP EGGS already DONE 13:10). Eggs 0 -> 3. Vouchers 365/75/25 unspent.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Launched hidden via Win32_Process Create (PID 25956, parent WmiPrvSE 113808). One instance, w2 by 13:57.

## 2026-11-03 14:04-14:08 MST - watch run: caught wild shiny Spearow w14 (single, Zacian + Mudkip run)
- Farm stopped 14:00:04 on shiny_enemy Spearow (sid 21, Lv9, variant 1, not a boss). At 14:05 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 / others 0, no farm process, no other controller.
- No attack. catch_shiny.py Spearow 1 0: Poke Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 14:00, Caught, Poke Ball) via _addrow_spearow.py; sprite pr_21s.png checked. Backup Shiny Log.md.bak_spearow_1408.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create with full pythonw path (bare "pythonw" returned no PID). PID 27180, parent WmiPrvSE 113808. One instance, w18 by 14:07.
- Note: ball stock is low (Poke 4 only) for future shiny catches.

## 2026-11-03 14:19-14:24 MST - watch run: caught wild shiny Trubbish w39 (double with Shuppet)
- Farm stopped 14:13:19 on shiny_enemy Trubbish (sid 568, Lv24, variant 1, not a boss) in a double with Shuppet (Lv26). At 14:20 (6+ min) unchanged: CommandPhase turn 1, full HP, balls Poke 9 / Great 5, no farm process, no other controller.
- _shatk.py: Zacian Spirit Break (single-target) at Shuppet (bi 2) KO'd it; Marshtomp Shore Up. Trubbish untouched (62/62).
- Great Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 14:13, Caught, Great Ball) via _addrow_trubbish.py; sprite pr_568s.png present. Backup Shiny Log.md.bak_trubbish_1423.
- Cleared flag, rotated stdout, relaunched hidden via Win32_Process Create with full pythonw path (PID 99384). Reached w43 by 14:23, then stopped again 14:23:44 on shiny_enemy Meowth (Lv28, var 1, double).

## 2026-11-03 14:25-14:30 MST - watch run: caught wild shiny Meowth w43 (double with Rhyhorn)
- Stop 14:23:44 shiny_enemy Meowth (Lv28, var 1, not a boss), partner Rhyhorn Lv26. At 14:25:51 (2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 9 / Great 4, no farm process.
- Zacian Spirit Break (single-target) at Rhyhorn KO'd it; Marshtomp Shore Up. Spinda's level-up offered Sucker Punch: declined (No). Meowth untouched (74/74).
- Great Ball (4 -> 3) caught first throw. Party full: "No" -> storage. Logged in CHIE Shiny Log.md (top row, 14:23, Caught, Great Ball); sprite pr_52s.png. Backup Shiny Log.md.bak_meowth_1430.
- Cleared flag, rotated stdout, relaunched hidden (PID 35588, parent WmiPrvSE 113808). One instance, w45 by 14:29.
- Ball stock now Poke 9 / Great 3 / Ultra 0 / Rogue 0.

## 2026-11-03 15:05-15:10 MST - watch run: caught wild shiny Wobbuffet w141 (double with Grumpig)
- Farm stopped 14:59:36 on shiny_enemy Wobbuffet (sid 202, Lv108, variant 1, not a boss, Shadow Tag) in a wild double with Grumpig (Lv114, Thick Fat). At 15:05 (6 min) unchanged: CommandPhase turn 1, full HP, balls Poke 24 / Great 13 / Ultra 0 / Rogue 20, no farm process, no other controller.
- _shatk.py: Zacian Spirit Break (single-target) at Grumpig (bi 2) KO'd it; Mega Swampert Shore Up. Wobbuffet untouched (560/560).
- Rogue Ball (20 -> 19) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 14:59, Caught, Rogue Ball) via _addrow_wobbuffet.py; downloaded sprite pr_202s.png. Backup Shiny Log.md.bak_wobbuffet_1510.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create with full pythonw path (PID 43408, parent WmiPrvSE 113808). One instance, w145 by 15:09.

## 2026-11-03 15:14-15:18 MST - watch run: caught wild shiny Hypno w147 (single)
- Farm stopped 15:09:59 on shiny_enemy Hypno (sid 97, Lv109, variant 1, not a boss, Insomnia). At 15:14 (5 min) unchanged: CommandPhase turn 1, full HP 322/322, balls Poke 24 / Great 13 / Ultra 0 / Rogue 24, no farm process, no other controller.
- No attack. catch_shiny.py Hypno 1 3: Rogue Ball (24 -> 23) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 15:09, Caught, Rogue Ball) via _addrow_hypno2.py; sprite pr_97s.png checked. Backup Shiny Log.md.bak_hypno_1517.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create with full pythonw path (PID 86428, parent WmiPrvSE 113808). One instance, w151 by 15:17.

## 2026-11-03 15:28-15:32 MST - watch run: Zacian + Swampert run ended w180 (wipe vs wild double Carracosta/Kingler), new run slot 2
- Farm exited 15:25:59 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w180 slot=2 luck=3 ... DONE farm17". Run Log row confirmed. No other controller.
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs: Zacian 3 (x6, candy 20 -> 2). Feebas none (rule). Mudkip candy 101 unspent (MUDKIP EGGS already DONE). Eggs 0 -> 3. Vouchers 383/78/26 unspent.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Launched hidden via Win32_Process Create (PID 134804, parent WmiPrvSE 113808). One instance, w4 by 15:31.

## 2026-11-03 15:49-15:54 MST - watch run: caught wild shiny Xatu w63 (double with Claydol)
- Farm stopped 15:45:40 on shiny_enemy Xatu (sid 178, Lv42, variant 1, not a boss, Early Bird) in a wild double with Claydol (Lv43, Levitate). At 15:49:51 (4 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 / Rogue 15, no farm process, no other controller.
- _shatk.py: Zacian Spirit Break (single-target) at Claydol (bi 2) KO'd it; Swampert Shore Up. Xatu untouched (109/109).
- Rogue Ball (15 -> 14) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage. (catch_shiny.py doesn't fit doubles; used _shatk.py ball mode.)
- Logged in CHIE Shiny Log.md (top row, 15:45, Caught, Rogue Ball) via _addrow_xatu.py; sprite pr_178s.png present. Backup Shiny Log.md.bak_xatu_1555.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create with full pythonw path (PID 85764, parent WmiPrvSE 113808). One instance, w65 by 15:53.

## 2026-11-03 16:13-16:20 MST - watch run: Zacian + Swampert run ended w114 (wipe vs wild Tsareena/Mandibuzz), Zacian + Mudkip eggs, new run slot 2
- Farm exited 16:10:11 "ALL-FAINT ... PRIMARY Zacian FAINT ... RUN LOG row w114 slot=2 luck=3 ... DONE farm17". Run Log row confirmed. No other controller.
- to_title.py -> title -> _re.py newgame (Classic). Upgrades all owned. Eggs (RUN-END EGGS UPDATE): Zacian 5 (x6, candy 31 -> 1), Mudkip 7 (x15, candy 119 -> 14). Feebas none (candy 6). Eggs 0 -> 12. Vouchers 390/78/27 unspent.
- Note: after the 2nd Mudkip egg the game dropped to LoadingModal -> TitleUiHandler (eggs saved, 7 total); redid _re.py newgame and continued buying.
- nr_pick.py 888,258,327,263,401,299 (all six), _re.py key 4 -> key 5 -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2, modeId 0.
- Launched hidden via Win32_Process Create (PID 17744, parent WmiPrvSE 113808). One instance, w5 by 16:19.

## 2026-11-03 16:25-16:30 MST - watch run: double shiny w28 (Psyduck + Goldeen), caught Goldeen
- Farm stopped 16:24:32 on shiny_enemy at w28: a wild double where BOTH foes were shiny (Psyduck Lv19 var 1, Goldeen Lv16 var 1, neither a boss). At 16:26:32 (2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 only, no farm process, no other controller.
- Only one can be caught (no ball throws with two foes up). Dex: Psyduck caughtAttr 223 (shiny incl. epic variant, ct 5, already in Shiny Log), Goldeen 159 (ct 1). Chose Goldeen.
- New helper _shatk2.py (= _shatk.py + mode `tgtn BI NAME`, targets a named foe even if shiny). Zacian Spirit Break at Psyduck (bi 2) KO'd it; Marshtomp Shore Up. Declined Pin Missile (_confno.py).
- Poke Ball (5 -> 4) caught Goldeen first throw ("Gotcha!"). Party full: _optno.py "No" -> storage.
- Shiny Log: Goldeen Caught (Poke Ball) and Psyduck Missed rows at top (backup Shiny Log.md.bak_goldeen_1630; downloaded sprite pr_118s.png).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 31044, parent WmiPrvSE 113808). One instance, w30 by 16:29.
- Ball stock low: Poke 4 only.

## 2026-11-03 16:49-16:54 MST - watch run: caught wild shiny Sandslash w85 (double with Sandslash)
- Farm stopped 16:47:39 on shiny_enemy Sandslash (Lv59, variant 1, not a boss, Sand Veil) in a wild double with a non-shiny Sandslash (Lv62). At 16:49:47 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 19 only, no farm process, no other controller.
- _shatk2.py: Zacian Spirit Break at the non-shiny Sandslash (bi 3, tgt mode refuses shiny) KO'd it; Swampert Shore Up. Shiny untouched (167/167).
- Poke Ball 1 (19 -> 18) broke free; Poke Ball 2 (18 -> 17) caught ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 16:47, Caught, Poké Ball) via _addrow_sandslash.py; sprite pr_28s.png downloaded. Backup Shiny Log.md.bak_sandslash_1655.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 81408, parent WmiPrvSE 113808). One instance, w88 by 16:53.

## 2026-11-03 17:07-17:12 MST - watch run: caught wild shiny Carracosta w130 (single, boss, 3 segments)
- Farm stopped 17:05:28 on shiny_enemy Carracosta (sid 565, Water/Rock, Lv100, variant 1, boss 3 segments, 282 HP, Solid Rock). At 17:07:36 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 22 / Great 5 / Rogue 10 / Master 1, no farm process, no other controller.
- Shield breaks with Zacian Bitter Blade (Fire, 0.25x vs Water/Rock, est. max ~64 incl. crit vs 282) via catch_shiny.py Carracosta 0 3, HP re-checked between hits: 282 -> 244 -> 208 -> 188 (shield 1) -> 152 -> 113 -> 94 (shield 2, seg0). 6 hits; Zacian 336/399.
- Rogue Ball (10 -> 9) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 17:05, Caught, Rogue Ball) via _addrow_carracosta.py; downloaded sprite pr_565s.png. Backup Shiny Log.md.bak_carracosta_1712.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 50960, parent WmiPrvSE 113808). One instance, w135 by 17:11.

## 2026-11-03 17:20-17:23 MST - watch run: caught wild shiny Lanturn w148 (double with Barraskewda)
- Farm stopped 17:15:27 on shiny_enemy Lanturn (sid 171, Water/Electric, Lv122, variant 1, not a boss, Illuminate) in a wild double with Barraskewda (Lv120). At ~17:20 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 32 / Great 5 / Rogue 9 / Master 1, no farm process, no other controller.
- _shatk2.py: Zacian Spirit Break at Barraskewda (tgtn 3) KO'd it; Mega Swampert Shore Up. Lanturn untouched (473/473).
- Rogue Ball (9 -> 8) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 17:15, Caught, Rogue Ball) via _addrow_lanturn.py; downloaded sprite pr_171s.png. Backup Shiny Log.md.bak_lanturn_1725.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 164516, parent WmiPrvSE 113808). One instance, w149 by 17:23.

## 2026-11-03 17:29-17:33 MST - watch run: caught wild shiny Sandslash w168 (single, variant 2)
- Farm stopped 17:29:07 on shiny_enemy Sandslash (sid 28, Lv147, variant 2, not a boss). At 17:31:40 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 37 / Great 10 / Rogue 8 / Master 1, no farm process, no other controller.
- No attack. catch_shiny.py Sandslash 1 3: Rogue Ball (8 -> 7) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 17:29, Caught, Rogue Ball) via _addrow_sandslash2.py; sprite pr_28s.png present. Backup Shiny Log.md.bak_sandslash2_1733.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 114244, parent WmiPrvSE 113808). One instance, w169 by 17:33.

## 2026-11-03 17:49-17:57 MST - watch run: Eternatus caught with the Master Ball (Classic win w200), Zacian + Mudkip eggs, new run slot 2
- Farm stopped 17:44:18 at w200 (eternatus_catch, Master Ball 1). At 17:49 (past 2 min) untouched (NextEncounterPhase, full HP, same balls), no farm process, no other controller.
- mb_eternatus.py ack/rd stepped to CommandPhase; Eternatus not shiny. mb_eternatus.py ball: Master Ball (1 -> 0) caught it ("Gotcha!", cap_rd.py, catch_ack.py); party full, _optno.py "No" -> storage. GameOver (Classic win) -> title.
- Run Log row written by hand via _runlog_w200b.py: 17:53, slot 2, w200, luck ?, "Classic win: Eternatus caught with the Master Ball" (backup Run Log.md.bak_w200_1753).
- _re.py newgame (Classic). Eggs: Zacian 7 (x6, candy 45 -> 3), Mudkip 6 (x15, candy 104 -> 14). Feebas none (candy 6). Eggs 0 -> 13. Vouchers 408/80/30 unspent.
- nr_pick.py 888,258,327,263,401,299, _re.py key 4 -> key 5 -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2.
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 107560, parent WmiPrvSE 113808). One instance, w4 by 17:56.

## 2026-11-03 18:42-18:46 MST - watch run: shiny Magcargo w106 handled by someone else (caught), logged
- Farm stopped 18:38:33 on shiny_enemy Magcargo (sid 219, Lv74, variant 1) in a wild double at w106. At 18:43 the state had changed: game in TrainerVictoryPhase vs Garganacl (later wave), Magcargo Lv82 now in the party, no farm process. Another controller (Gavin) is driving, so no input sent.
- Logged in CHIE Shiny Log.md (top row, 18:38, Caught, Ball unknown) via _addrow_magcargo.py; sprite pr_219s.png present. Backup Shiny Log.md.bak_magcargo_1845.
- Farm left stopped (stop flag still set) until the manual session goes idle.

## 2026-11-03 19:25-19:28 MST - watch run: shiny Abomasnow w185 handled by someone else (outcome pending)
- Farm stopped 19:18:58 on shiny_enemy Abomasnow (sid 460, Lv162, variant 1) in a wild double at w185. By 19:25 the game had moved on (w188 boss Dragonite, then w189 double Eiscue/Furret), no farm process, so another controller (Gavin) is driving. No input sent.
- Outcome not settled yet: Abomasnow is not in the party (6 full); dex 460 caughtAttr 155 (shiny bit set) caughtCount 3, but no earlier baseline to compare. Game stats now: pokemonCaught 1855, shinyPokemonCaught 816. Balls now Poke 55 / Great 10 / Ultra 0 / Rogue 17 / Master 2. Re-check once the manual session is idle and log Caught/Missed.
- Note: CHIE Shiny Log.md has a script-written "UNKNOWN x123" egg row at 18:56 listing ~every dex entry as "new attr" (looks like a false diff, not real hatches). Left in place for now.
- Farm left stopped (stop flag still set) until the manual session goes idle.

## 2026-11-03 19:38 MST - watch run: manual session still active, no input
- Game now at SelectStarterPhase (no battle, party empty), farm not running, stop flag still set (shiny_enemy Abomasnow w185). gameStats pokemonCaught 1859 (was 1855 at 19:25), shinyPokemonCaught 817 (was 816). Dex 460 caughtAttr 155, caughtCount 3 (unchanged since 19:25; no pre-stop baseline, so Abomasnow outcome still unsettled).
- No new Run Log row since 19:06; "UNKNOWN x123" egg row no longer in Shiny Log.md (file edited 19:36 by another session). No input sent; farm left stopped while Gavin drives.

## 2026-11-03 19:43 MST - watch run: still at starter select under manual control, no input
- Game still SelectStarterPhase (party empty, wave 0, playTime 6012), no farm process, stop flag set (shiny_enemy Abomasnow w185). gameStats unchanged since 19:38 (caught 1859, shiny 817); dex 460 caughtAttr 155, caughtCount 3. Abomasnow outcome still unsettled.
- Run Log newest row is still 19:06 (w165); no row yet for the run that passed w189. Both CHIE logs were last edited 19:39 by another session.
- Idle at starter select ~5+ min; under the 10-min rule, no takeover yet. Next watch: if still idle and unchanged, do run-end eggs + new run per the saved steps.

## 2026-11-03 19:46 MST - watch run: still idle at starter select, no input
- Game still SelectStarterPhase (party empty, wave 0, playTime 6012 unchanged since 19:38), no farm process, stop flag set (shiny_enemy Abomasnow w185). gameStats caught 1859, shiny 817; dex 460 caughtAttr 155, caughtCount 3. Last outside-session file edits 19:39, so idle ~7 min, under the 10-min rule. No input sent. Next watch (~19:51): if still unchanged, do run-end eggs + new run.

## 2026-11-03 19:56 MT - Tynamo secondary (Gavin t199u)
- New hand-built run (slot 2, Classic): Zacian (shiny) primary, Tynamo 602 secondary, shiny helpers Kricketot/Sentret/Zigzagoon/Spinda.
- pr_farm17.py: SECONDARY = Tynamo line {602,603,604} (Mudkip 258-260 and Feebas/Milotic no longer secondary); REORDER_JS keeps Tynamo line in slot 2; orbs still never go to secondary.
- Doubles Earthquake: when a Tynamo-line partner (Levitate) is alive on the field and no wild shiny is out, Zacian may use Earthquake (score x1.25 instead of x0.8 soft-avoid).
- Mega: Swampertite special removed; Eelektrossite rank -370 only while Eelektross 604 alive in party, applied only to Eelektross. Mega Bracelet -380, Master Ball -400 unchanged (item_priority.json + prio.py).
- profiles/eelektross.json created (Levitate, secondary role, doubles EQ rule; helpers not listed). Config: secondary=Tynamo.
- Run-end candy is done by the overnight watch (not code): Zacian eggs all candy; Tynamo passive + cost reductions first, then eggs; Sentret passive + cost reductions only (no eggs); Mudkip/Feebas unspent; no vouchers.
- Backups: *.bak_tynamo_20261103_1955.

## 2026-11-03 21:13-21:18 MST - watch run: caught wild shiny Jellicent w133 (single)
- Farm stopped 21:12:24 on shiny_enemy Jellicent (sid 593, Lv99, variant 1, not a boss). At 21:14:55 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 10 / Great 5 / Ultra 5 / Rogue 10 / Master 0, no farm process, no other controller.
- No attack. catch_shiny.py Jellicent 1 3: Rogue Ball (10 -> 9) caught first throw ("Gotcha!", cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 21:12, Caught, Rogue Ball) via _addrow_jellicent.py; sprite pr_593s.png present. Backup Shiny Log.md.bak_jellicent_2120.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 87656, parent WmiPrvSE 113808). One instance, w134 by 21:17.

## 2026-11-03 21:27-21:32 MST - watch run: caught wild shiny Noivern w144 (double with Parasect, epic variant)
- Farm stopped 21:24:02 on shiny_enemy Noivern (sid 715, Lv110, variant 3, not a boss, Infiltrator) in a wild double with Parasect (Lv109). At ~21:28 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 10 / Great 5 / Ultra 5 / Rogue 9 / Master 0, no farm process, no other controller.
- _shatk2.py: Zacian Bitter Blade at Parasect (tgtn 3) KO'd it. Eelektrik has no status move, so dbl_shiny3.py sw 1 2 switched it out for Kricketot. Noivern untouched (329/329).
- Rogue Ball (9 -> 8) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 21:24, Caught, Rogue Ball) via _addrow_noivern.py; downloaded sprite pr_715s.png. Backup Shiny Log.md.bak_noivern_2135.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 64336, parent WmiPrvSE 113808). One instance, w145 by 21:31.

## 2026-11-03 21:48-21:55 MST - watch run: run ended w165 (Kyurem boss wipe), Tynamo passive + Zacian eggs, new run slot 2
- Farm ended 21:45:11 at w165 (all six fainted vs boss Kyurem). Run Log row written by the script (21:45, slot 2, w165, luck 2).
- to_title.py -> title -> _re.py newgame (Classic). Candy (TYNAMO SWITCH): Zacian 4 eggs (x6, candy 29 -> 5). Tynamo x40 Unlock Passive (passiveAttr 0 -> 3, candy 53 -> 13); x60 Reduce Cost and x20 egg unaffordable. Sentret candy 29: passive x40 / reduction x60 unaffordable, nothing bought. Mudkip 15 unspent. Eggs 0 -> 4. Vouchers 441/88/32 unspent. No hatches.
- nr_pick.py 888,602,401,161,263,327 (Zacian, Tynamo, Kricketot, Sentret, Zigzagoon, Spinda), _re.py key 4 -> key 5 -> _re.py slot 2 (empty). Verified Classic, wave 1, slot 2.
- New helper _rd_cand.py (reads candy/passive/valueReduction for 888/602/161/258).
- Cleared flag/reasons, rotated stdout, launched hidden via Win32_Process Create (PID 152740, parent WmiPrvSE 113808). One instance, w5 by 21:54.

## 2026-11-03 22:00-22:12 MST - watch run: caught wild shiny boss Happiny w10; config primary fix
- Farm stopped 21:56:12 on shiny_enemy Happiny (sid 440, Lv8, variant 2, boss 2 segments, 36 HP). At 22:00 (past 2 min) unchanged: CommandPhase, full HP, balls Poke 5 only, no farm process, no other controller.
- First Poke Ball refused ("too strong", shield up). Zacian (Spirit Break ~89 dmg) far too strong, so dbl_shiny3.py sw 0 3 switched in Sentret; two Scratches (36 -> 26 -> 18) broke the shield. Poke Ball (5 -> 4) caught first throw. Party full: _optno.py "No" -> storage. New helper _ackc.py (ack a BattleMessage even in CommandPhase).
- Logged in CHIE Shiny Log.md (top row, 21:56, Caught, Poke Ball); downloaded sprite pr_440s.png. Backup Shiny Log.md.bak_happiny_2205.
- BUG: agent-tools\pokerogue_farm_config.json had no "primary" key, so resolve_primary() fell back to party slot 1 (Sentret after the catch switch) and the farm treated Sentret as primary (Rare Candy went to Sentret at w11, Sentret fought w12-13 and fainted; Zacian stayed benched). Fix: added "primary": "Zacian" to config (first write had a PowerShell BOM and was ignored; rewritten BOM-free via python). Backup pokerogue_farm_config.json.bak_2210.
- Relaunched hidden via Win32_Process Create (final PID 142432, parent WmiPrvSE). PRIMARY resolved: Zacian source=config; one instance, Zacian fighting at w17 by 22:11.

## 2026-11-03 22:33-22:39 MST - watch run: caught wild shiny Electrode w56 (double with Pawmot, rare variant)
- Farm stopped 22:31:55 on shiny_enemy Electrode (sid 101, Lv37, variant 2, not a boss, Soundproof) in a wild double with Pawmot (Lv37). At 22:34:33 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 14 / Great 5 / Ultra 0 / Rogue 0 / Master 0, no farm process, no other controller.
- dbl_shiny3.py mv 0 2 + tgt 3: Zacian Spirit Break at Pawmot KO'd it. Eelektrik has no status move, so dbl_shiny3.py sw 1 3 switched it out for Kricketot. Electrode untouched (102/102).
- Great Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 22:31, Caught, Great Ball) via _addrow_electrode.py; downloaded sprite pr_101s.png. Backup Shiny Log.md.bak_electrode_2240.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 54568, parent WmiPrvSE 113808). One instance, w58 by 22:38.

## 2026-11-03 22:54-22:59 MST - watch run: caught wild shiny Golduck w84 (single, rare variant)
- Farm stopped 22:52:46 on shiny_enemy Golduck (sid 55, Lv55, variant 2, not a boss). At 22:55:20 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 14 / Great 4 / Ultra 0 / Rogue 10 / Master 0, no farm process, no other controller.
- No attack. catch_shiny.py Golduck 1 3: Rogue Ball (10 -> 9) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage. shinyPokemonCaught 824 -> 826.
- Logged in CHIE Shiny Log.md (top row, 22:52, Caught, Rogue Ball) via _addrow_golduck.py; downloaded sprite pr_55s.png. Backup Shiny Log.md.bak_golduck_2300.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 67868, parent WmiPrvSE). One instance, fighting w85 by 22:58.

## 2026-11-03 23:05-23:08 MST - watch run: Disable loop fix (w89)
- Farm looped from ~23:01:50 at w89 (double, Drednaw + Slowking): Slowking used Disable on Eelektrik's Leech Life; pick_move kept choosing Leech Life every ~1.5 s and the NOPP guard never caught it (no message text).
- Patch (backup pr_farm17.bak_disable_20261103_2310.py): before pick_move in the Fight menu, read the active mon's restricted moves (isMoveRestricted, plus DisabledTag/Torment/Taunt/Imprison tags) and add them to the dead set; logs "RESTRICTED <mon>: [...] -> skip".
- Restarted hidden via Win32_Process Create (PID 47336, parent WmiPrvSE 113808). One instance; RESTRICTED fired, w89 cleared by 23:07. Script copied to ..PROJECT\pokerogue\scripts.

## 2026-11-03 23:29-23:32 MST - watch run: shiny Jellicent w117 handled by another controller
- Farm stopped 23:27:44 on shiny_enemy Jellicent (sid 593, Lv91, variant 2, single). By 23:29:54 the game had moved on without the farm: wave 122 turn 2, shiny Jellicent (Lv98) now in the party in Spinda's old slot, Rogue Balls 13, shinyPokemonCaught 828. Another controller (likely Gavin) is driving, so no input sent and the farm was not relaunched.
- Logged in CHIE Shiny Log.md (top row, 23:27, Caught, Ball unknown). Backup Shiny Log.md.bak_jellicent2_2331.
- Stop flag left in place; relaunch only once the game sits idle ~10+ min.

## 2026-11-03 23:37 MST - watch run: still under manual control
- Farm still stopped (shiny_enemy Jellicent flag). Game live at w141 turn 2 (MoveEffectPhase), up from w122 at 23:30, so another controller is actively playing. Party Zacian, Eelektross, Kricketot line, Furret, Jellicent. No input sent, no relaunch.

## 2026-11-03 23:42 MST - watch run: still under manual control
- Farm still stopped (shiny_enemy Jellicent flag). Game live at w157 turn 1 (CommandPhase), up from w141 at 23:37, so another controller is still playing. Party Zacian, Eelektross, Kricketot line, Jellicent (Lv150). No input sent, no relaunch.

## 2026-11-03 23:48 MST - watch run: still under manual control
- Farm still stopped (shiny_enemy Jellicent flag). Game live at w170 turn 5 (MessagePhase vs Crustle), up from w157 at 23:42, so another controller is still playing. Party Zacian, Mega Eelektross, Kricketot line, Jellicent. No input sent, no relaunch.

## 2026-11-03 23:52 MST - watch run: still under manual control
- Farm still stopped (shiny_enemy Jellicent flag). Game live at w179 turn 1 (SelectTargetPhase, double vs Vespiquen + Amoonguss), up from w170 at 23:48, so another controller is still playing. Party Zacian, Mega Eelektross, Kricketot line, Jellicent. No input sent, no relaunch.

## 2026-11-04 00:09 MST - watch run: still under manual control (w200 Eternatus)
- Farm still stopped (shiny_enemy Jellicent flag from 23:27). Game live at w200 turn 14 (CommandPhase) vs E-Max Eternatus, so another controller (Gavin) is fighting the final boss by hand. Party Zacian 676 HP, Kricketune 504 HP, Jellicent/Gholdengo/Mega Eelektross fainted. Balls Poke 19 / Great 9 / Rogue 17 / Master 0. No input sent, no relaunch.

## 2026-11-04 00:14 MST - watch run: run over, Gavin at starter select
- Farm still stopped (shiny_enemy Jellicent flag from 23:27). Game was at w200 vs Eternatus at 00:09; now SelectStarterPhase with empty party (playTime 10305), so the manual run ended and another controller (Gavin) is at starter select / new-run setup. Balls show Poke 5 only (fresh state). shinyPokemonCaught 828 -> 830 since 23:30 (two more shinies caught by hand; species not yet identified, check storage/party and log them). Run Log.md has no row for this run yet (last write 21:45). No input sent, no relaunch; take over only after ~10 min idle with state understood.

## 2026-11-04 00:30 MT - ETERNTEAM (Gavin t200u/t201u)
- New-run "max luck" team, save slot 2: 1 Eternatus (890, primary), 2 Tynamo (602, secondary), 3 Kricketot (401 shiny v3), 4 Spinda (327 shiny v2), 5 Zigzagoon (263 shiny v2), 6 Nosepass (299 shiny v3). In config new_run_party.
- Config primary=890/eternatus.json, secondary=Tynamo/eelektross.json, run_end_eggs 890+602 (no BOM).
- Eternatus score-learns level-up moves; secondary: Wild Charge replaces Charge Shot/Charge Beam; Thunder Stone -> Eelektrik rank -360; Toxic Orb -> Tynamo line only, Flame Orb nobody; item transfer primary then secondary.
- Backups *.bak_eternteam_20261104_0030

## 2026-11-04 00:36-00:40 MST - watch run: caught wild shiny Marshtomp w38 (double with Psyduck, rare variant)
- Farm stopped 00:34:37 on shiny_enemy Marshtomp (sid 259, Lv24, variant 2, not a boss) in a wild double with Psyduck (Lv24). At 00:36:58 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 10 / Rogue 5, no farm process, no other controller.
- dbl_shiny3.py mv 0 1 + tgt 2: Eternatus Venoshock at Psyduck KO'd it. dbl_shiny3.py sw 1 2 switched Tynamo out for Kricketot (no status move). Marshtomp untouched (68/68).
- Rogue Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 00:34, Caught, Rogue Ball) via _addrow_marshtomp.py; sprite pr_259s.png. Backup Shiny Log.md.bak_marshtomp_0040.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 113836, parent WmiPrvSE 113808). One instance; party reordered Eternatus/Tynamo, w38 reward picked by 00:39.

## 2026-11-04 00:44-00:49 MST - watch run: caught wild shiny boss Quagsire w40 (single, rare variant)
- Farm stopped 00:40:30 on shiny_enemy Quagsire (sid 195, Lv25, variant 2, boss 2 segments, 89 HP, Water Absorb). At 00:44:27 (4 min, past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 10 / Rogue 4, no farm process, no other controller.
- First Rogue Ball refused (shield up, ball not used). Eternatus Incinerate (resisted) did 8 (89 -> 81), Shadow Ball broke the shield (81 -> 45).
- Rogue Ball (4 -> 3) caught first throw ("Gotcha!"). Party full: _optno.py "No" -> storage. shinyPokemonCaught 832 -> 834.
- Logged in CHIE Shiny Log.md (top row, 00:40, Caught, Rogue Ball) via _addrow_quagsire.py; sprite pr_195s.png. Backup Shiny Log.md.bak_quagsire_0050.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 106240, parent WmiPrvSE 113808). One instance; Eternatus fighting w41 by 00:48.

## 2026-11-04 00:57 MST — TYNACURE (watch)
- Shop kept planning Full Heal for Tynamo (Toxic Orb poison, Poison Heal) at w48; it couldn't be applied and was blacklisted after several loops. SEC_NO_STATUS_CURE only covered Milotic (349/350).
- Patched pr_farm17.py: shop_plan `_nc` and the reward SEC STATUS skip now include Tynamo line 602/603/604 (status never cured; HP heals via plain potions only). Backup pr_farm17.bak_tynacure_20261104_0057.py. py_compile OK.
- Safe restart at w50/51 (no shiny, no eternatus_catch): killed 106240, relaunched hidden via Win32_Process Create (PID 159548, parent WmiPrvSE 113808). One instance; fighting w51 by 00:55.

## 2026-11-04 01:18-01:23 MST - watch run: caught wild shiny Musharna w81 (double with Musharna, standard variant)
- Farm stopped 01:14:47 on shiny_enemy Musharna (sid 518, Lv59, variant 1, not a boss) in a wild double with a non-shiny Musharna (Lv57). At 01:18:18 (3.5 min, past 2 min) unchanged: CommandPhase, full HP, balls Poke 20 / Rogue 3 / Master 1, no farm process, no other controller.
- Eternatus Dragon Pulse x2 at the non-shiny Musharna (211 -> 74 -> KO); Eelektrik switched out for Kricketot, then Kricketot for Spinda (no damaging moves from slot 2). Shiny untouched (211/211).
- Rogue Ball (3 -> 2) caught first throw ("Gotcha!"). Party full: _optno.py "No" -> storage. Master Ball kept (1).
- Logged in CHIE Shiny Log.md (top row, 01:14, Caught, Rogue Ball) via _addrow_musharna.py; sprite pr_518s.png. Backup Shiny Log.md.bak_musharna_0125.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 8284, parent WmiPrvSE 113808). One instance; fighting w82 by 01:22.

## 2026-11-04 01:38-01:46 MST - watch run: caught wild shiny Claydol w98 (double with Alakazam, standard variant) + TSTONE patch
- Farm stopped 01:34:49 on shiny_enemy Claydol (sid 344, Lv68, variant 1, not a boss, Levitate) in a wild double with Alakazam (Lv73). At ~01:38 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 20 / Rogue 2 / Master 1, no farm process, no other controller.
- Eternatus Dynamax Cannon at Alakazam (bi 3, single target) KO'd it; Eelektrik switched out for Nosepass. Claydol untouched (161/161).
- Rogue Ball (2 -> 1) caught first throw. Party full: _optno.py "No" -> storage. Master Ball kept (1).
- Logged in CHIE Shiny Log.md (top row, 01:34, Caught, Rogue Ball) via _addrow_claydol.py; sprite pr_344s.png. Backup Shiny Log.md.bak_claydol_0145.
- Relaunched hidden (PID 116264); w98 Thunder Stone was routed to Eternatus by the SECONDARY ONLY-CANDY guard (Eelektrik is the secondary), failed to apply and was blacklisted (Nugget taken instead).
- TSTONE patch: the secondary guard `_ok3` now allows Thunder Stone on Eelektrik (603) and Eelektrossite on Eelektross (604). Backup pr_farm17.bak_tstone_20261104_0146.py. py_compile OK. Safe restart at w101 (PID 43948, hidden via Win32_Process Create). Copied script to ..PROJECT\pokerogue\scripts.

## 2026-11-04 02:08-02:14 MST - watch run: Eternatus run ended w120 (wipe vs wild Torkoal, Drought), eggs, new run slot 2
- Farm ended 02:05:17 at w120 (all six fainted vs wild Torkoal). Run Log row written by the script (slot 2, w120, luck 2).
- to_title.py -> title -> _re2.py newgame (Classic). New helpers _re2.py (start check uses 890, shows Eternatus/Tynamo candy) and _rd_cand2.py (890/602/888/161/258/349 + vouchers).
- Eggs: Eternatus 1 (x5, candy 6 -> 1), Tynamo 1 (x20, candy 38 -> 18). Eggs 0 -> 2. Zacian 42, Sentret 33, Mudkip 26, Feebas 6 left unspent. Vouchers 463/97/33 unspent.
- nr_pick.py 890,602,401,327,263,299 (Eternatus, Tynamo, Kricketot, Spinda, Zigzagoon, Nosepass), key 4 -> key 5 -> slot 2 (empty). Verified Classic, wave 1, slot 2.
- Rotated stdout, launched hidden via Win32_Process Create with full pythonw path (PID 169112, parent WmiPrvSE 113808). One instance, w3 by 02:13.

## 2026-11-04 02:49-02:53 MST - watch run: caught wild shiny Sinistea w49 (single, standard variant)
- Farm stopped 02:43:38 on shiny_enemy Sinistea (sid 854, Lv32, variant 1, not a boss) at w49. At 02:49 (6 min, past 2 min) unchanged: CommandPhase turn 1, Sinistea 61/69, balls Poke 5 / Great 5, no farm process, no other controller.
- No attack. catch_shiny.py Sinistea 1 1: Great Ball (5 -> 4; no Rogue/Ultra) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage. shinyPokemonCaught 838 -> 839.
- Logged in CHIE Shiny Log.md (top row, 02:43, Caught, Great Ball) via _addrow_sinistea.py; sprite pr_854s.png downloaded. Backup Shiny Log.md.bak_sinistea_0252. New read helper _rd_sh.py (party/enemy HP, balls, turn).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 109304, parent WmiPrvSE 113808). One instance; fighting w50 by 02:52.

## 2026-11-04 03:47-03:52 MST - watch run: Eternatus run ended w114 (wipe vs Trainer Oleana's Milotic), eggs, new run slot 2
- Farm ended 03:46:06 at w114 (all fainted vs Oleana's Milotic, Competitive). Run Log row written by the script (slot 2, w114, luck 2).
- to_title.py -> title -> _re2.py newgame (Classic). Eggs: Eternatus 1 (x5, candy 6 -> 1), Tynamo 1 (x20, candy 38 -> 18). Eggs 0 -> 2. Zacian 42, Sentret 33, Mudkip 26, Feebas 6 unspent. Vouchers 470/98/33 unspent.
- nr_pick.py 890,602,401,327,263,299, key 4 -> key 5 -> slot 2 (empty). Verified Classic, wave 1, slot 2.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 23356, parent WmiPrvSE 113808). One instance; w1 reward picked by 03:51.

## 2026-11-04 04:15-04:22 MST - watch run: caught wild shiny Nidorino w38 (double with Nymble, standard variant)
- Farm stopped 04:12:12 on shiny_enemy Nidorino (sid 33, Lv24, variant 1, not a boss) in a wild double with Nymble (Lv25). At 04:15 (past 2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 only, no farm process, no other controller.
- dbl_shiny3.py mv 0 0 + tgt 2: Eternatus Venoshock (single target) at Nymble KO'd it. dbl_shiny3.py sw 1 2 switched Tynamo out for Kricketot. Nidorino untouched (69/69).
- Poke Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 04:12, Caught, Poké Ball) via _addrow_nidorino.py; sprite pr_33s.png downloaded. Backup Shiny Log.md.bak_nidorino_0420.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 93424).
- Note: ball stock low (Poke 4 only).

## 2026-11-04 05:15 MST - PPDRY (pr_farm17.py)
- w115 (Team Star Penny): Eternatus had all four attacks at 0 PP and Struggled until it fainted; at w114 a Big Nugget had beaten Max Ether because PP was only "low", not "critical".
- Fix: pp_crit now also fires when total attack PP is under 30% of max, so Ether/Elixir/Max Ether rank top; ZACIAN SWITCH-IN never brings the primary back in when all its attacks are at 0 PP.
- Backup: pr_farm17.bak_ppdry_20261104_0515.py. Restarted hidden (PID 70664).

## 2026-11-04 05:39-05:42 MST - watch run: caught wild shiny Crobat w147 (single, standard variant)
- Farm stopped 05:34:10 on shiny_enemy Crobat (sid 169, Lv120, variant 1, not a boss) at w147 (the run survived the w115 PP scare). At 05:39 (5 min, past 2 min) unchanged: CommandPhase turn 1, Crobat 362/362, balls Poke 14 / Rogue 15 / Master 1, no farm process, no other controller.
- No attack. catch_shiny.py Crobat 1 3: Rogue Ball (15 -> 14) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 05:34, Caught, Rogue Ball) via _addrow_crobat.py; sprite pr_169s.png downloaded. Backup Shiny Log.md.bak_crobat_0541.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 72456, parent WmiPrvSE 113808). One instance; fighting w148 by 05:42.

## 2026-11-04 06:00-06:03 MST - watch run: caught wild shiny Maractus w169 (single, epic variant)
- Farm stopped 05:58:06 on shiny_enemy Maractus (sid 556, Lv141, variant 3, not a boss) at w169. At 06:00:30 (past 2 min) unchanged: CommandPhase turn 2, Maractus 394/394, balls Poke 14 / Rogue 14 / Master 1, no farm process, no other controller.
- No attack. catch_shiny.py Maractus 1 3: Rogue Ball (14 -> 13) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage. Dex caught 844 -> 845. Master Ball kept.
- Logged in CHIE Shiny Log.md (top row, 05:58, Caught, Rogue Ball) via _addrow_maractus.py; sprite pr_556s.png downloaded. Backup Shiny Log.md.bak_maractus_0602.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 49176, parent WmiPrvSE 113808). One instance; fighting w170 by 06:03.

## 2026-11-04 06:29-06:36 MST - watch run: Eternatus run ended w190 (wipe vs Trainer Red's Mega Blastoise), eggs, new run slot 2
- Farm ended 06:28:02 at w190 (all six fainted vs Red's Mega Blastoise, Mega Launcher). Run Log row written by the script (slot 2, w190, luck 3).
- to_title.py -> title -> _re2.py newgame (Classic). Eggs: Eternatus 3 (x5, candy 19 -> 4), Tynamo 3 (x20, candy 62 -> 2). Eggs 0 -> 6. Zacian 42, Sentret 33, Mudkip 26, Feebas 6 unspent. Vouchers 490/101/34 unspent.
- nr_pick.py 890,602,401,327,263,299; `_re2.py start` failed its startCursor assert, so key 4 -> key 5 -> slot 2 (empty). Verified Classic, wave 1, slot 2, party 890/602/401/327/263/299.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 72020, parent WmiPrvSE 113808). One instance; w4 by 06:35.

## 2026-11-04 07:17-07:20 MST - watch run: caught wild shiny Floatzel w79 (single, standard variant)
- Farm stopped 07:12:45 on shiny_enemy Floatzel (sid 419, Lv53, variant 1, not a boss) at w79. At 07:17 (past 2 min) unchanged: CommandPhase turn 1, Floatzel 164/164, balls Poke 5 / Rogue 5, no farm process, no other controller.
- No attack. catch_shiny.py Floatzel 1 3: Rogue Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party had 5, so Floatzel joined the party (slot 6).
- Logged in CHIE Shiny Log.md (top row, 07:12, Caught, Rogue Ball) via _addrow_floatzel.py; sprite pr_419s.png. Backup Shiny Log.md.bak_floatzel_0721.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 168316, parent WmiPrvSE). One instance; fighting w80 by 07:19.

## 2026-11-04 08:01-08:07 MST - watch run: caught wild shiny Amoonguss w136 (single, rare variant); Floatzel dropped from party
- Farm stopped 07:58:57 on shiny_enemy Amoonguss (sid 591, Lv103, variant 2, not a boss) at w136. At 08:01:30 (2.5 min) unchanged: CommandPhase turn 1, Amoonguss 370/370, balls Poke 5 / Rogue 9 / Master 1, no farm process.
- No attack. catch_shiny.py Amoonguss 1 3: Rogue Ball (9 -> 8) caught first throw. Party was full (Floatzel had joined at w79), and cap_rd.py's confirms answered the add-to-party prompt Yes, so the game swapped Amoonguss in for Floatzel (slot 3). Floatzel is still registered as caught; only its in-run party slot was lost. Dex shiny caught 847 -> 849.
- Logged in CHIE Shiny Log.md (top row, 07:58, Caught, Rogue Ball) via _addrow_amoonguss.py; sprite pr_591s.png. Backup Shiny Log.md.bak_amoonguss_0803.
- Relaunch clash: PokeFarmControl started its own pr_farm17.py (PID 114692) at 08:03:08, 8 s before my hidden launch (PID 1304). Killed 1304; one instance left (the app's).
- The clash left PartyUiHandler (MODIFIER mode) stuck with pendingPrompt=true, so X did nothing and the farm looped "reward Potion cannot be applied" at w137 (STALL x150). Cleared pendingPrompt once via _unstick_party.py; the farm went on to w138 at 08:06.
- TODO: catch flow should answer the add-to-party prompt itself (No when party is full) before cap_rd.py's confirms; farm could clear a stuck pendingPrompt after a STALL in PartyUiHandler.

## 2026-11-04 08:15 MT - XFERLEPPA
- XFER overflow -> configured secondary (fallback Milotic); Ether/Elixir rank -30 when primary PP low (<40% any move or <50% total). Master Ball/candy priority unchanged.
- Root cause: tiny max PP on Eternabeam/Dynamax Cannon; held Leppa capped stack, only +10 on a move at 0 PP.

## 2026-11-04 08:22-08:28 MST - watch run: caught wild shiny Meganium w141 (double with Nidoqueen, rare variant)
- Farm stopped 08:07:12 on shiny_enemy Meganium (sid 154, Lv113, variant 2, not a boss) in a double with Nidoqueen. At 08:22 (15 min) unchanged: CommandPhase turn 1, Meganium 303/303, balls Poke 5 / Rogue 8 / Master 1, no farm process; last other-session activity was the 08:09-08:15 XFERLEPPA patch.
- Turn 1: Eternatus Eternabeam single-target on Nidoqueen (KO); Eelektross switched out for Amoonguss (no damaging move). Turn 2 (Eternatus recharging): Amoonguss threw a Rogue Ball (8 -> 7), caught first throw. Meganium took no damage.
- Party was full; PokeFarmControl relaunched pr_farm17.py (PID 108360, parent PokeFarmControl 170576) at 08:25:21 during the capture prompt, and the release prompt ended with Meganium in the party in place of Spinda. Dex shiny caught 849 -> 852 (includes earlier pending ones).
- Logged in CHIE Shiny Log.md (top row, 08:07, Caught, Rogue Ball) via _addrow_meganium.py; sprite pr_154s.png downloaded. Backup Shiny Log.md.bak_meganium_0827.
- One farm instance (the app's), fighting w142 by 08:25.
- TODO (repeat): catch flow / farm should answer the full-party prompt No (storage) instead of releasing a helper.

## 2026-11-04 08:29 MST - watch run: wild shiny Kecleon w144 caught by another controller
- Farm (relaunched by PokeFarmControl) stopped 08:25:59 on shiny Kecleon (Lv114, variant 2, double with Tsareena). Within ~40 s another controller KO'd Tsareena and caught Kecleon (Rogue 7 -> 6, dex shiny caught 852 -> 853); I sent no input. Logged Caught (08:25, w144, Rogue Ball), sprite pr_352s.png. Farm relaunched by the app (PID 29076); Eternatus fainted at w145, others fighting, revive expected at next shop.

## 2026-11-04 08:34 MST - watch run: w145 wipe, then external page reload; save still at w145 (no input sent)
- Farm saw ALL-FAINT at 08:28:15 at w145 (trainer with shiny Rayquaza; bench fell one by one). At 08:28:17 the page was reloaded from outside (no farm/app reload code), so the game over was never saved; farm exited 08:28:53 "PRIMARY Eternatus MISSING".
- Game sits on Title (Continue/New Game). getSession(2) = w145 saved 08:27:06 MST, Classic, party 890/604/591/476/154/401 all with HP. So the run has NOT ended: no run-end steps, no eggs, no Run Log row yet. Candy Eternatus 15, Tynamo 30, eggs 0.
- Reload ~6 min ago counts as recent other-session activity, so no input this run. Next watch: if still on Title and untouched (~10+ min idle), Continue slot 2 (Load Game, like the 11/03 w140 precedent) and relaunch the farm hidden; if it wipes again the farm writes the Run Log row, then do run-end steps.

## 2026-11-04 08:39-08:46 MST - watch run: Continued slot 2 at w145, wiped again vs the same trainer (shiny Rayquaza), eggs, new run slot 2
- Title idle ~11 min after the 08:28 external reload; Title Continue loaded slot 2 directly (w145, all six alive). Relaunched hidden (PID 42800). Same trainer team (Polteageist/Armarouge/Hydrapple/Rayquaza): Eternatus fainted 08:40:44, all six fainted 08:41:34. Script wrote the Run Log row (w145, slot 2, luck 5).
- to_title.py -> title (slot 2 cleared) -> _re2.py newgame (Classic). Eggs: Eternatus 3 (x5, candy 15 -> 0), Tynamo 1 (x20, candy 30 -> 10). Eggs 0 -> 4. Zacian 42, Sentret 33, Mudkip 26, Feebas 6 unspent. Vouchers 500/103/34 unspent.
- nr_pick.py 890,602,401,327,263,299; key 4 -> key 5 -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2, party 890/602/401/327/263/299.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 139436, parent WmiPrvSE 113808). One instance; w5 by 08:46.
- New helper _cont_slot2.py (Title Continue; note Continue loads the last session directly, no slot picker).

## 2026-11-04 09:00 MT - t204u Eternatus moveset
- _re2.py `eternmoves` sets starterData[890].moveset=[Malignant Chain 919, Dragon Energy 820, Body Press 776, Poison Tail 342]; `eternverify` prints in-run moves. All 4 egg moves unlocked (eggMoves=15). Dragon Pulse is Lv40 level-up, not starter-eligible; "dragon power" mapped to Dragon Energy.
- eternatus.json: protected += Malignant Chain; drop_first=[Poison Tail].
- pr_farm17.py learn_score: drop_first replaced before weakest for damaging offers.

## 2026-11-04 09:29-09:35 MST - watch run: run ended w115 (Trainer Rose, Ferrothorn), eggs, new run slot 2
- Eternatus run wiped at w115 at 09:29 (Trainer Rose; Ferrothorn/Copperajah, bench fell one by one). Script wrote the Run Log row (w115, slot 2, luck 3).
- to_title.py -> title (slot 2 cleared) -> _re2.py newgame (Classic). Eggs: Eternatus 2 (x5, candy 10 -> 0), Tynamo 1 (x20, candy 26 -> 6). Eggs 0 -> 3. Zacian, Sentret, Mudkip 26, Feebas 6 unspent. Vouchers 507/103/34 unspent.
- nr_pick.py 890,602,401,327,263,299; `_re2.py eternmoves` (Malignant Chain, Dragon Energy, Body Press, Poison Tail); key 4 -> key 5 -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; eternverify OK.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 29572, parent WmiPrvSE 113808). One instance; w7 by 09:34.

## 2026-11-04 10:10 MT - TGTMOVES (Gavin t205u/t206u)
- Profile-driven, generic (no-op without fields): target_moveset, extra_type_caps, pp_up_pref in learn_score / pick_reward / PP item move menu. No global rank change; Master Ball untouched.
- eternatus.json: target Malignant Chain/Dragon Energy/Dynamax Cannon/Flamethrower; extra_type_caps {15:1}; pp_up_pref +3 in Great/Ultra when a target move max PP <=10; PP Up -> lowest-max-PP target move.

## 2026-11-04 10:31-10:38 MST - watch run: w184 wipe (Elite Four Olivia, Kabutops), page reloaded 2 s later; slot 2 still holds w184 save (no input sent)
- Farm (launched 10:27 by PokeFarmControl) wiped at w184 vs Elite Four Olivia (Gigalith/Probopass/Carbink/Lycanroc/Kabutops); Eternatus fainted, bench fell one by one; ALL-FAINT 10:30:53, Run Log row written (w184, slot 2, luck 3), DONE 10:30:58.
- Page performance.timeOrigin = 10:31:00 (reloaded 2 s after DONE, not by farm code), game on Title. getSession(2) = w184 saved 10:29:29 MST, Classic, party 890/604/401/327/476 all with HP, so the game over was NOT saved (same as the 08:28 w145 case). Candy Eternatus 10, Tynamo 49, eggs 0.
- No game input this run (to_title.py found Title at step 0, sent nothing). Next watch: if still Title and untouched ~10 min, Continue slot 2 (_cont_slot2.py) and relaunch hidden like 08:39; if it wipes and the slot clears, do run-end eggs + new run. If the Run Log ends up with a duplicate w184 row, keep only the final one.
- CONFIG FIX: agent-tools\pokerogue_farm_config.json had lost "primary" (PokeFarmControl save_cfg overwrote the whole file with only secondary_field/candy_target at 10:04 when candy_target was set to "secondary"); farm resolved primary by party slot. Restored "primary": 890, kept candy_target "secondary" (backup .bak_cfgmerge_20261104_1035).
- PokeFarmControl.pyw save_cfg now merges into the existing config instead of replacing it (backup .bak_cfgmerge_20261104_1035). The running app keeps the old code until it's restarted.

## 2026-11-04 10:50-10:58 MST - watch run: run ended w190 (Champion Hau), eggs, new run slot 2
- Farm (launched 10:42 by PokeFarmControl) wiped at w190 vs Champion Hau (Decidueye/Noivern); ALL-FAINT 10:44:29, Run Log row written (w190, slot 2, luck 1), DONE 10:44:34. Slot 2 cleared (game over saved this time).
- Game was already in Classic starter select with an empty party (someone else pressed New Game between 10:44 and 10:50); watched it 3+ min with no change before acting.
- Eggs: Eternatus 2 (x5, candy 11 -> 1), Tynamo 2 (x20, candy 50 -> 10). Eggs 0 -> 4. Zacian 42, Sentret 33, Mudkip 26, Feebas 6 unspent. Vouchers 523/106/36 unspent.
- nr_pick.py 890,602,401,327,263,299; `_re2.py eternmoves`; key 4 -> key 5 -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; eternverify Malignant Chain/Dragon Energy/Body Press/Poison Tail.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 44556, parent WmiPrvSE 113808). One instance; w9 by 10:58.

## 2026-11-04 11:17-11:21 MST - watch run: caught wild shiny Ursaring w61 (single, standard variant)
- Farm stopped 11:13:04 on shiny_enemy Ursaring (sid 217, Lv41, variant 1, not a boss) at w61. At 11:17 (4 min) unchanged: CommandPhase turn 1, Ursaring 130/130, balls Poke 5 only, no farm process, no other controller.
- No attack. catch_shiny.py Ursaring 1 0: Poke Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 11:13, Caught, Poke Ball) via _addrow_ursaring.py; sprite pr_217s.png downloaded. Backup Shiny Log.md.bak_ursaring_1122.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 92200). One instance; w63 by 11:20.
- Note: ball stock is low (Poke 4 only, no Rogue/Master).

## 2026-11-04 11:29-11:33 MST - watch run: caught wild shiny Sandslash w85 (double with Cacturne)
- Farm stopped 11:27:20 on shiny_enemy Sandslash (sid 28, Lv56, variant 1, not a boss) in a wild double with Cacturne (Lv63). At 11:29:11 unchanged: CommandPhase turn 1, full HP, balls Poke 4 only, no farm process, no other controller.
- _shatk.py: Eternatus Flamethrower (single-target) at Cacturne (bi 2) KO'd it; Eelektross Wild Charge aimed at Cacturne (would retarget to Sandslash, which is Ground and immune). Sandslash untouched (160/160).
- Poke Ball (4 -> 3) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 11:27, Caught, Poke Ball) via _addrow_sandslash.py; sprite pr_28s.png present. Backup Shiny Log.md.bak_sandslash_1133.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 64568, parent WmiPrvSE). One instance; w88 by 11:32.
- Note: ball stock is very low (Poke 3 only).

## 2026-11-04 11:39-11:47 MST - watch run: caught wild shiny Staraptor w101 (double with Swellow, rare variant)
- Farm stopped 11:35:58 on shiny_enemy Staraptor (sid 398, Lv73, variant 2, not a boss) in a wild double with Swellow (Lv74). At 11:40 unchanged: CommandPhase turn 1, full HP, balls Poke 8, no farm process, no other controller.
- Eelektross Wild Charge (single-target) at Swellow; Eternatus switched out to Kricketot (new _sw.py = _shatk.py + `sw FIELD PARTYIDX` via handleCommand(2,idx) and `js FILE` modes) so no second damaging move could retarget. Kricketot fainted to the foes, Wild Charge KO'd Swellow; Spinda sent in. Staraptor took only its own recoil (192/209).
- Poke Ball 1 broke free, Poke Ball 2 caught (8 -> 6). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 11:35, Caught, Poke Ball); sprite pr_398s.png downloaded. Backup Shiny Log.md.bak_staraptor_1145.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create. Kricketot fainted (farm revives at next shop); Eternatus benched alive.

## 2026-11-04 11:46-11:50 MST - watch run: caught wild shiny Swellow w103 (double with Pidgeot)
- Farm (relaunched 11:43 after Staraptor) stopped 11:44:12 on shiny_enemy Swellow (sid 277, Lv79, variant 1, not a boss), wild double with Pidgeot (Lv79). Waited ~2 min; at 11:46 unchanged (turn 1, full HP, Poke 6, no farm process).
- Eternatus switched out to Spinda (_sw.py sw 0 2); Eelektross Wild Charge at Pidgeot KO'd it. Swellow 164/208 after the turn (its own Guts-era attacks/recoil, not our hits).
- Poke Ball caught first throw (6 -> 5); "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 11:44, Caught, Poke Ball); sprite pr_277s.png. Backup Shiny Log.md.bak_swellow_1149.
- Cleared flag/reason, rotated stdout, relaunched hidden (PID 99868). Note: Eternatus is benched (Spinda/Eelektross on field); farm brings the primary back; Kricketot still fainted, revive at next shop.

## 2026-11-04 12:08-12:13 MST - watch run: caught wild shiny Mudsdale w166 (single, standard variant)
- Farm stopped 12:06:12 on shiny_enemy Mudsdale (sid 750, Lv141, variant 1, not a boss) at w166. At 12:09 (~3 min) unchanged: CommandPhase turn 1, Mudsdale 464/464, balls Poke 20 / Rogue 10, no farm process, no other controller.
- No attack. catch_shiny.py Mudsdale 1 3: Rogue Ball (10 -> 9) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 12:06, Caught, Rogue Ball) via _addrow_mudsdale.py; sprite pr_750s.png downloaded. Backup Shiny Log.md.bak_mudsdale_1215. New read-only helper _rdstate.py (phase/turn/party HP/balls/enemy).
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 109264, parent WmiPrvSE 113808). One instance; w169 by 12:12.

## 2026-11-04 12:16-12:21 MST - watch run: caught wild shiny Drapion w171 (double with Sandslash)
- Farm stopped 12:13:24 on shiny_enemy Drapion (sid 452, Lv141, variant 1, not a boss), wild double with Sandslash (Lv138, Ground). At 12:16 (~3 min) unchanged: CommandPhase turn 1, full HP, balls Poke 20 / Rogue 9, no farm process, no other controller.
- Eelektross can't hit Sandslash (Electric vs Ground), so Eternatus Flamethrower (single-target, _sw.py mv 0 2 + tgt 2) at Sandslash and Eelektross switched out to Probopass (_sw.py sw 1 5). Sandslash survived at 1 HP; turn 2 Flamethrower again + Probopass Harden KO'd it. Drapion untouched (352/352).
- Rogue Ball (9 -> 8) caught first throw (_sw.py ball, cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 12:13, Caught, Rogue Ball) via _addrow_drapion.py; sprite pr_452s.png. Backup Shiny Log.md.bak_drapion_1222.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 124244, parent WmiPrvSE 113808). One instance; w173 by 12:20. Eelektross benched (Probopass on field); farm brings it back.
## 2026-11-02 08:35 MST - TARGETFIX (pr_farm17.py)
- Bug: in doubles the TargetSelect screen just pressed Z, so single-target moves always hit the left foe. Wave 81 (Shedinja Wonder Guard + Lurantis): every hit went into immune Shedinja for ~8 turns; Lugia, Milotic and Linoone fainted (run survived via Kricketot's Stone Axe).
- Fix: remember foes ranked by the chosen move's effectiveness (immune dropped) and set the TargetSelect cursor to the best live foe before confirming. Logs 'TARGET pick ...'. Backup pr_farm17.bak_target_20261102_0835.py. Restarted hidden at w82; verified w83.

## 2026-11-03 12:46 MT - Mega Bracelet / Swampertite priority (Gavin t195u)
- item_priority.json specials: mega_bracelet -380, swampertite -370 (only while Swampert 260 alive); Master Ball -400 stays top. prio.py rank_item matches 'mega bracelet' / 'swampertite'.
- pr_farm17.py: swampert_in_party flag; Swampertite party target forced to Swampert slot; secondary only-candy guard allows Swampertite on Swampert; shop target override skips it.
- Backups: pr_farm17.bak_mega_20261103_1244.py, prio.bak_mega_20261103_1244.py, item_priority.json.bak_mega_20261103_1244. py_compile OK.
- Note: Mega Bracelet already owned this run (w163). Restarted hidden via Win32_Process Create (PID 163968). One instance, w168 by 12:46.



## 2026-11-04 21:12-21:20 MST - watch run: caught wild shiny Donphan w98 (double with Golem, epic variant)
- Farm stopped 21:11:42 on shiny_enemy Donphan (sid 232, Lv69, variant 3, not a boss), wild double with Golem (Lv72). At 21:13:46 (~2 min) unchanged: CommandPhase turn 1, full HP, balls Poke 5 / Great 5 / Rogue 5, no farm process, no other controller.
- Mewtwo Aura Sphere single-target at Golem (_sw.py mv 0 1 + tgt 3), Absol Leer (non-damaging); Golem KO'd, Donphan untouched (214/214). Hidden tab needs STEP: pass a steps arg (e.g. `_sw.py rd 150`, `_sw.py ack 25`) or phases stall.
- Turn 2 Rogue Ball (5 -> 4) caught first throw (_sw.py ball Donphan 60, cap_rd.py 80, catch_ack.py). Party was 5, so Donphan joined as slot 6.
- Logged in CHIE Shiny Log.md (top row, 21:11, Caught, Rogue Ball) via _addrow_donphan.py; sprite pr_232s.png downloaded. Backup Shiny Log.md.bak_donphan_2116.
- Cleared flag/reasons, rotated stdout, relaunched hidden via Win32_Process Create (PID 11628, parent WmiPrvSE 113808). One instance; w99 by 21:19, Mewtwo still has Thunderous Kick.

## 2026-11-04 21:29-21:35 MST - watch run: run ended w114 (Trainer Faba, Porygon-Z), new run slot 2
- Farm wiped at w114 vs Trainer Faba (Porygon-Z Adaptability, Hypno); ALL-FAINT 21:28:21, Run Log row written (w114, slot 2, luck 3), DONE 21:28:27. to_title.py -> title; getSession(2) empty (game over saved).
- Candy: `_re2.py reduce` found no option because Reduce Cost sits inside the "Use Candies" submenu (reduce mode needs a patch: pick "Use Candies" first, label "×N Reduce Cost to X"). Checked by hand: Mewtwo candy 14, "×15 Reduce Cost to 6" unaffordable, nothing bought (saving candy). Absol has no reduction left (vr 2): 1 egg (×12, candy 17 -> 5). Eggs 0 -> 1. Vouchers 568/115/42 unspent.
- Gotcha: `_re2.py cancel` on starter select with an empty party opens a "return to title?" confirm; answered No.
- nr_pick.py 150,359,263,327,401; key 4 -> key 5 -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; Mewtwo moves Thunderous Kick/Confusion/Life Dew/Disable.
- Cleared flag, rotated stdout, launched hidden via Win32_Process Create (PID 96028, parent WmiPrvSE 113808). One instance; w4 by 21:34.

## 2026-11-04 21:52-21:58 MST - watch run: caught wild shiny Beedrill w46 (single, rare variant)
- Farm stopped 21:52:09 on shiny_enemy Beedrill (sid 15, Lv28, variant 2, not a boss) at w46. At 21:54:36 (~2.5 min) unchanged: CommandPhase turn 1, full HP, balls Poke 20 only, no farm process, no other controller.
- No attack (no shield). catch_shiny.py Beedrill 1 0: two Poke Balls broke free (Mewtwo took 44), third caught (20 -> 17, "Gotcha!"). Party had 5, so Beedrill joined as slot 6.
- Logged in CHIE Shiny Log.md (top row, 21:52, Lv28, variant 2, Caught, w46, Poké Ball) via _addrow_beedrill.py + _fix_bee.py; sprite pr_15s.png downloaded. Backup Shiny Log.md.bak_beedrill_2156.
- Cleared flag/reason, rotated stdout, relaunched hidden via Win32_Process Create (PID 110660, parent WmiPrvSE 113808). One instance; fighting w50 by 21:58 with Thunderous Kick intact.

## 2026-11-04 22:22-22:27 MST - watch run: caught wild shiny Camerupt w107 (single, standard variant)
- Farm stopped 22:17:18 on shiny_enemy Camerupt (sid 323, Lv75, variant 1, not a boss) at w107. At 22:23 (~6 min) unchanged: CommandPhase turn 1, full HP, balls Poke 22 / Rogue 5, no farm process, no other controller.
- No attack (no shield). catch_shiny.py Camerupt 1 3: Rogue Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 22:17, Lv75, variant 1, Caught, w107, Rogue Ball) via _addrow_camerupt.py; sprite pr_323s.png already present. Backup Shiny Log.md.bak_camerupt_2226.
- GOTCHA: _restart_after_shiny.py clears flags AND launches the farm itself; a second manual Win32_Process Create made 2 instances for ~40 s. Killed the extra (117888). One instance left: PID 94880 (parent WmiPrvSE 113808); w111 by 22:26, Mewtwo still has Thunderous Kick. Don't launch again after that helper.

## 2026-11-04 22:29-22:35 MST - watch run: run ended w115; candy spent; another controller took over new-run setup
- Farm wiped at w115 (Pelipper/Wailord rain trainer; Mewtwo PP low). ALL-FAINT 22:29:56, Run Log row written (w115, slot 2, luck 2), DONE.
- to_title.py -> title -> _re2.py newgame (Classic). Candy by hand (reduce mode still unpatched; Reduce Cost is under "Use Candies"): `_re2.py open 150` + `pick "Use Candies"` + `pick "×15 Reduce Cost*"`: Mewtwo candy 18 -> 3, valueReduction 1 -> 2. Absol (vr 2, maxed): 2 eggs (×12, candy 25 -> 1). Eggs 0 -> 2. Vouchers 572/117/42 unspent. New read-only helpers _cand_mb.py (150/359 candy+vr, egg count) and _slot_rd.py (slot, mode, wave, party moves).
- nr_pick.py 150,359,263,327,401 OK; key 4 -> Confirm, key 5 -> back to StarterSelect (no save-slot screen). About 1 min later the game was at w2 CommandPhase with Mudkip added as slot 6 and 5 Poke Balls, then back at SelectStarterPhase with an empty party ~20 s later. No farm process; only PokeFarmControl running. Someone else (likely Gavin) is driving: stopped all input, farm NOT launched. Next watches: no input until ~10 min idle and state is understood.

## 2026-11-04 22:39-23:18 MST - watch runs: new run farmed; caught wild shiny Luxray w76 (double with Golbat)
- Gavin's hand-set slot 2 run (Mewtwo, Absol, Mudkip, Spinda, Zigzagoon, Kricketot) sat idle at w1 from ~22:35; at 22:48 cleared flags, rotated stdout, launched hidden (PID 74524, parent WmiPrvSE). Hatches w25: 2 Absol + 1 Lapras, none shiny.
- Farm stopped 23:10:21 on shiny_enemy Luxray (sid 405, Lv49, variant 1, not a boss), wild double with Golbat (Lv54). At 23:12:49 unchanged (turn 1, full HP, Poke 10 / Great 5, no farm process).
- Mewtwo Psybeam single-target at Golbat (_sw.py mv 0 2 + tgt 2) KO'd it; Swampert Shore Up. Luxray untouched (152/152).
- Great Balls: 3 broke free, 4th caught (5 -> 1; cap_rd.py, catch_ack.py). Party full: _optno.py "No" -> storage.
- Logged in CHIE Shiny Log.md (top row, 23:10, Lv49, variant 1, Caught, w76, Great Ball) via _addrow_luxray.py; sprite pr_405s.png downloaded. Backup Shiny Log.md.bak_luxray_2316.
- _restart_after_shiny.py relaunched hidden (PID 133320, parent WmiPrvSE 113808). One instance; w77 by 23:17, Mewtwo still has Thunderous Kick.

## 2026-11-04 23:31-23:37 MST - watch run: run ended w110 (Bug-type fight: Lokix/Shuckle/Kleavor/Yanmega), new run slot 2
- Farm wiped at w110 (Lokix, Shuckle, Kleavor, Yanmega; Kleavor finished the party). ALL-FAINT 23:28:02, Run Log row written (w110, slot 2, luck 3), DONE.
- to_title.py -> title; getSession(2) empty. _re2.py newgame (Classic).
- Candy: Mewtwo (vr 2) and Absol (vr 2) have no cost reduction left in "Use Candies" (only "Buy an Egg"), so reductions are maxed. Leftover candy to eggs: Mewtwo 1 egg (x6, candy 8 -> 2), Absol 1 egg (x12, candy 12 -> 0). Eggs 0 -> 2. Vouchers 578/119/42 unspent.
- nr_pick.py 150,359,263,327,401; key 4 -> key 5 -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; Mewtwo moves Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 157268, parent WmiPrvSE 113808). One instance; w5 by 23:36 with Thunderous Kick intact.

## 2026-11-04 23:47-23:51 MST - watch run: caught wild shiny Rattata w27 (single, rare variant)
- Farm stopped 23:42:10 on shiny_enemy Rattata (Lv17, variant 2, not a boss) at w27. At 23:47 (~5 min) unchanged: CommandPhase, full HP, balls Poke 15 / Rogue 10, no farm process, no other controller.
- No attack (no shield). catch_shiny.py Rattata 1 3: Rogue Ball (10 -> 9) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party had 5, so Rattata joined as slot 6.
- Logged in CHIE Shiny Log.md (top row, 23:42, Lv17, variant 2, Caught, w27, Rogue Ball) via _addrow_rattata.py; sprite pr_19s.png downloaded. Backup Shiny Log.md.bak_rattata_2350.
- _restart_after_shiny.py relaunched hidden (PID 127352, parent WmiPrvSE 113808). One instance; w30 by 23:50, Mewtwo still has Thunderous Kick.

## 2026-11-05 00:12-00:17 MST - watch run: run ended w80 (Carracosta, Sturdy), new run slot 2
- Farm wiped at w80 vs wild Carracosta (Sturdy); ALL-FAINT 00:07:46, Run Log row written (w80, slot 2, luck 2), DONE.
- to_title.py -> title; slot 2 empty. _re2.py newgame (Classic).
- Candy: Mewtwo 5 (egg x6) and Absol 6 (egg x12), reductions maxed, so nothing affordable; nothing bought. Eggs 1. Vouchers 582/119/42 unspent.
- nr_pick.py 150,359,263,327,401; gx.py p:4 (Confirm) -> p:5 -> SaveSlotSelect -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 153284, parent WmiPrvSE 113808). One instance; w6 by 00:16.

## 2026-11-05 00:27 MT
- Added Mudkip (258) to new_run_team in agent-tools config: [150,359,263,327,401,258]. No script changes.

## 2026-11-05 01:21-01:30 MST - watch run: run ended w115 (Sylveon, Pixilate), new run slot 2 with Mudkip
- Mega Mewtwo Y fainted w115 01:16:48; partners fell to Sylveon; ALL-FAINT 01:17:54, Run Log row (w115, slot 2, luck 3), DONE.
- to_title.py -> title -> _re2.py newgame (Classic). `_re2.py reduce 150,359`: no option (both maxed, vr 2). Eggs by hand via open/pick "Use Candies"/pick "×N Buy an Egg": Mewtwo 2 eggs (x6, candy 12 -> 0), Absol 2 eggs (x12, 26 -> 2). Eggs 0 -> 4. Vouchers 588/119/42 unspent.
- Gotcha: a PowerShell -match on the "×" label failed (encoding), call pick with the literal label directly.
- nr_pick.py 150,359,263,327,401,258 (Mudkip added). With 6 in party gx.py p:4 didn't open the confirm; handler.tryStart() via gx.py js: did ("Begin with these Pokémon?"), p:5 -> SaveSlotSelect -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Cleared flag, rotated stdout, launched hidden via Win32_Process Create (PID 70556, parent WmiPrvSE 113808). One instance; w2 by 01:29.

## 2026-11-05 01:44-01:51 MST - watch run: caught wild shiny Growlithe w30 (double with Petilil, both bosses)
- Farm stopped 01:43:51 on shiny_enemy Growlithe (Lv20, variant 1, boss 2 segments), wild double with Petilil (Lv20 boss, 1 segment). At 01:46:12 (>2 min) unchanged: CommandPhase, full HP, Poke 5 only, no farm process, no other controller.
- Turn 1: Mewtwo Psybeam single-target at Petilil (_sw.py mv 0 2 + tgt 2) KO'd it; Absol switched to Kricketot (_sw.py sw 1 4).
- Shield: Mewtwo Meteor Mash (Steel, 0.5x vs Fire) via _sw.py shatk 0 3 + stgt 3, twice: 57 -> 42 -> 29, shield broken (segment index 0). Kricketot Growl, then switched to Spinda.
- Poke Ball (5 -> 4) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 01:43, Lv20, variant 1, Caught, w30, Poké Ball) via _addrow_growlithe.py; sprite pr_58s.png downloaded; frontmatter updated 2026-11-05. Backup Shiny Log.md.bak_growlithe_0150.
- _restart_after_shiny.py relaunched hidden (PID 74344, parent WmiPrvSE 113808). One instance; w32 by 01:50.

## 2026-11-05 01:59-02:06 MST - watch run: caught wild shiny Nymble w41 (double with Vivillon)
- Farm stopped 01:55:42 on shiny_enemy Nymble (Lv27, variant 2, not a boss), wild double with Vivillon (Lv25). At ~01:59 (>2 min) unchanged: CommandPhase turn 1, full HP, Poke 9 only, no farm process, no other controller.
- Turn 1: Mewtwo Psybeam single-target at Vivillon (_sw.py mv 0 2 + tgt 2) KO'd it; Spinda Slack Off (non-damaging). Nymble untouched (62/62).
- Level-ups: Spinda offered Teeter Dance -> declined (_cfno.js). Absol offered Night Slash -> learned into slot 1 replacing Leer (LearnMovePhase.learnMove(0) via _ns.js); Absol now Night Slash/Spirit Break/Sacred Sword/Cross Poison (target moveset complete).
- Turn 2: Poke Ball (9 -> 8) caught first throw ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged in CHIE Shiny Log.md (top row, 01:55, Lv27, variant 2, Caught, w41, Poké Ball) via _addrow_nymble.py; sprite pr_919s.png downloaded. Backup Shiny Log.md.bak_nymble_0205.
- _restart_after_shiny.py relaunched hidden (PID 123416, parent WmiPrvSE 113808). One instance; w42 by 02:06.

## 2026-11-05 02:19-02:28 MST — wild shiny Vespiquen (w58, double with Thwackey)
- Shiny stop 02:19:25; state unchanged after 2+ min wait, took over at 02:22.
- Turn 1: Mewtwo Psybeam single-target at Thwackey (_sw.py mv 0 2 + tgt 3) KO'd it; Swampert Shore Up (non-damaging). Vespiquen untouched (94/94).
- Poke Balls (8 -> 5): two broke free, third caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in Shiny Log (sprite pr_416s.png downloaded).
- _restart_after_shiny.py relaunched hidden (PID 102536, parent WmiPrvSE 113808). One instance; w59 by 02:28, reviving Absol at the shop.

## 2026-11-05 02:37-02:43 MST — wild shiny Rabsca (w72, single)
- Shiny stop 02:37:30 (Rabsca Lv46, variant 1, not a boss). State unchanged through 02:39:42 (turn 1, full HP, Poke 5 only, no farm process); took over.
- No attack (no shield). catch_shiny.py Rabsca 1 0: first Poke Ball broke free, second caught (5 -> 3; cap_rd.py 80, catch_ack.py). Mewtwo took a hit (218 -> 112). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, 02:37, Lv46, variant 1, w72, Poké Ball) via _addrow_rabsca.py; sprite pr_954s.png downloaded. New read-only probe _rd_state.py (phase, turn, party HP, balls, enemy).
- _restart_after_shiny.py relaunched hidden (PID 138652, parent WmiPrvSE 113808). One instance; reward screen w72 by 02:42.

## 2026-11-05 02:49-02:56 MST — wild shiny Sandslash (w75, double with Cacturne, sandstorm)
- Shiny stop 02:43:19 (Sandslash Lv49, variant 1, not a boss) in a double with Cacturne (Lv49, Grass/Dark, Sand Veil). Unchanged at 02:49 (turn 1, full HP, Poke 3 only, no farm process); took over.
- Mewtwo Thunderous Kick single-target at Cacturne (_sw.py mv 0 0 + tgt 2), Swampert Shore Up. First kick missed (Sand Veil), second KO'd Cacturne. Absol offered Phantom Force at Lv60 -> declined (_cfno.js), moveset unchanged.
- Poke Ball 1 broke free; Sandslash + sandstorm took Mewtwo to 5/240. Turn 4: Mewtwo switch to Linoone queued (_sw.py sw 0 2), Swampert threw Poke Ball 2 -> caught (3 -> 1) before the switch happened. Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (02:43, Lv49, variant 1, w75, Poké Ball); sprite pr_28s.png.
- _restart_after_shiny.py relaunched hidden (PID 80600, parent WmiPrvSE 113808). One instance; shop healed Mewtwo to 240/240; w76 by 02:56.
- Note: only 1 Poké Ball left and no other balls.

## 2026-11-05 03:12-03:17 MST - watch run: w95 NextEncounterPhase stall fixed by reload + Continue
- Farm (PID 80600) stalled from 03:09 at w95 (Rival Ivy) on "Come back, Mewtwo!": NextEncounterPhase loaded=false, loader idle, frame stepping didn't help (likely an asset load lost during a brief PC network blip ~03:11).
- Killed the farm, reloaded the page, stepped frames past the loading scene (new helper %TEMP%\prfarm\_pump.py + `gx.py s:100`; the HOOK needs rendered frames in a hidden tab), Title Continue (_cont_slot2.py) loaded slot 2 at w95, Classic, full HP. Note: the farm aborts "not Classic" if launched on Title, so Continue first.
- Relaunched hidden via Win32_Process Create (PID 143756, parent WmiPrvSE 113808), one instance; fighting w95 at 03:17. Mewtwo now has Thunderous Kick, Psychic, Psystrike, Meteor Mash.

## 2026-11-05 04:44-04:49 MST - watch run: run ended w188 (Trainer Karen, Weavile), new run slot 2
- Party wiped at w188 vs Trainer Karen's Weavile; ALL-FAINT 04:42:48, Run Log row written (w188, slot 2, luck 3), DONE. Mega Mewtwo X held Mewtwonite X this run.
- to_title.py -> title -> _re2.py newgame (Classic). `_re2.py reduce 150,359`: no option (both maxed). Eggs by hand (open/pick "Use Candies"/buyegg): Mewtwo 2 eggs (x6, candy 16 -> 4), Absol 2 eggs (x12, 24 -> 0). Eggs 0 -> 4. Vouchers 606/121/42 unspent.
- nr_pick.py 150,359,263,327,401,258; gx.py js: tryStart() -> Confirm, p:5 -> SaveSlotSelect -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Cleared flag/reason, rotated stdout, launched hidden via Win32_Process Create (PID 17900, parent WmiPrvSE 113808). One instance; w2 by 04:48.

## 2026-11-05 05:49 MST — wild shiny Camerupt caught (wave 75, double with Torkoal)
- Took over after the 05:40 shiny stop (state unchanged >2 min). Turn 1: Mewtwo Psychic single-target at Torkoal (_sw.py mv 0 1 + tgt 2) KO'd it; Absol Leer (non-damaging, needed tgt 2 confirm). Camerupt untouched (135/135).
- Mewtwo hit Lv64 and was offered Power Swap then Guard Swap; both declined via ConfirmUi "No" (_lmno.js through _sw.py js). Protected moves kept.
- Turn 2: Poké Ball (15 -> 14; no Rogue/Ultra/Great left) caught first throw (_sw.py ball Camerupt 60, cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage. Logged in Shiny Log.
- Note: Camerupt's turn-1 attack left Mewtwo 122/227 and Absol 32/176. Relaunched hidden via _restart_after_shiny.py (pythonw PID 80792); wave 77 by 05:50.
- cap_rd.py can crash printing non-cp1252 chars; set PYTHONIOENCODING=utf-8 first.

## 2026-11-05 06:10-06:16 MST — wild shiny Tentacruel caught (wave 94, double with Starmie)
- Shiny stop 06:03:49 (Tentacruel Lv64, variant 1, not a boss). Unchanged at 06:09 (turn 1, full HP, Poké 14 only, no farm process); took over.
- Turn 1: Mewtwo Psychic single-target at Starmie (_sw.py mv 0 1 + tgt 3) KO'd it; Absol Leer (Absol has Leer, not Night Slash, this run). Tentacruel untouched.
- Mewtwo Lv79 offered Calm Mind (move 347) -> declined via _lmno347.js (copy of _lmno.js with the move-id guard set to 347). Protected moves kept.
- Poké Balls (14 -> 12): first broke free, second caught ("Gotcha!", catch_ack.py). Party full: _optno.py "No" -> storage. Logged Caught in Shiny Log (sprite pr_73s.png already present).
- _restart_after_shiny.py relaunched hidden (PID 12636, parent WmiPrvSE 113808). One instance; w95 by 06:15, Mewtwo 282/282.

## 2026-11-05 ~07:01-07:08 MST - run ended w145 (trainer w/ Rayquaza, Pidgeot last), new run slot 2
- Whole party fainted at wave 145 (06:58); Run Log row written by script (verified).
- Reduce 150,359: no cost-reduction options left (maxed). Eggs: Mewtwo x2 (14->2 candy), Absol x2 (29->5). Eggs 0->4. Vouchers untouched.
- New Classic run in slot 2 (slots 0/1 Endless untouched): Mewtwo, Absol, Zigzagoon, Spinda, Kricketot, Mudkip.
- Gotcha: tryStart must be called via window.__pr_cam.scene.ui.getHandler(), not __pr_cam.ui.
- Flags cleared, stdout rotated, launched hidden via Win32_Process Create: pythonw PID 40056 (parent WmiPrvSE). Wave 3 by 07:07, Mewtwo moves intact.

## 2026-11-05 07:43-07:50 MST — wild shiny Rotom caught (wave 57, double with Electrode)
- Shiny stop 07:40:12 (Rotom Lv40, variant 1, not a boss). Unchanged at 07:44 (turn 1, CommandPhase, Rotom/Electrode full HP, Poké 5 only, no farm process); took over.
- Turn 1: Mewtwo Psybeam single-target at Electrode (_sw.py mv 0 2 + tgt 2) KO'd it; Absol Leer (mv 1 0 + tgt 2). Rotom untouched (96/96); Rotom's hits left Absol 43/140, Mewtwo 153/183.
- Poké Balls (5 -> 3): first broke free, second caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, backup .bak_rotom_0748); sprite pr_479s.png downloaded.
- _restart_after_shiny.py relaunched hidden (PID 128312, parent WmiPrvSE 113808). One instance.

## 2026-11-05 08:15-08:20 MST — wild shiny Ninetales caught (wave 96, double with Parasect)
- Shiny stop 08:12:35 (Ninetales Lv69, variant 1, not a boss). Unchanged at 08:15 (turn 1, CommandPhase, full HP, Poké 2 / Great 5, no farm process); took over.
- Turn 1: Mewtwo Psychic single-target at Parasect (_sw.py mv 0 1 + tgt 2) KO'd it; Absol Leer (mv 1 0 + tgt 2). Ninetales untouched (196/196); Mewtwo took a hit (313 -> 204).
- Great Balls (5 -> 3): first broke free, second caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, backup .bak_ninetales_0820); sprite pr_38s.png downloaded.
- _restart_after_shiny.py relaunched hidden (PID 49916, parent WmiPrvSE 113808). One instance; w97 by 08:20.

## 2026-11-05 08:27-08:35 MST: wild shiny Ursaring caught (w107)
- Farm stopped 08:27:29 on shiny_enemy Ursaring (Lv80, variant 1, not a boss) in a double with Butterfree. At ~08:30 unchanged (turn 1, full HP, Poke 2 / Great 3), so took over.
- Turn 1: Mewtwo Psychic single-target at Butterfree (_sw.py mv 0 1 + tgt 2) KO'd it; Absol Leer (mv 1 0 + tgt 2). Ursaring untouched (258/258).
- Great Balls (3 -> 0): two broke free, third caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Absol took hits (254 -> 101). Party full: _optno.py "No" -> storage.
- Logged Caught in Shiny Log (08:27, Lv80, variant 1, w107, Great Ball) via _addrow_ursaring.py; sprite pr_217s.png downloaded. Farm relaunched hidden (PID 46424), fighting w108 by 08:35.

## 2026-11-05 08:46-08:54 MST - run end w115 -> new run
- Run ended w115 (whole party fainted, Trainer Guzma's Golisopod, slot 2); Run Log row written by script.
- to_title.py -> title -> _re2.py newgame (Classic). `_re2.py reduce 150,359`: no option (both maxed). Eggs by hand (open/pick "Use Candies"/buyegg): Mewtwo 4 eggs (x6, candy 28 -> 4), Absol 1 egg (x12, 21 -> 9). Eggs 0 -> 5. Vouchers 618/124/42 unspent.
- nr_pick.py 150,359,263,327,401,258; gx.py js: tryStart() -> Confirm, p:5 -> SaveSlotSelect (slot 2 Empty) -> `_re2.py slot 2`. Verified Classic, wave 1, slot 2. Farm launched hidden (pythonw PID 92700, parent WmiPrvSE).

## 2026-11-05 09:14-09:27 MST - wild shiny Steenee caught (w33, epic variant 3)
- Farm stopped 09:14:44 on shiny_enemy Steenee (Lv21, variant 3, not a boss) in a double with Seviper. Unchanged at ~09:17 (turn 1, CommandPhase, full HP, Poke 15), so took over.
- Turn 1: Mewtwo Psybeam single-target at Seviper (_sw.py mv 0 2 + tgt 2) KO'd it; Absol Leer (mv 1 0 + tgt 2). Steenee untouched (58/58). Hidden tab needed frame steps (`_sw.py rd 150` / `ack 25`).
- Marshtomp offered Take Down at Lv25: declined via new _lmno36.js (copy of _lmno.js guarded to moveId 36). New read-only helper _lmpeek.js shows the LearnMove prompt.
- Turn 2: Poke Ball (15 -> 14) caught first throw (_sw.py ball Steenee 60, cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, 09:14, Lv21, variant 3, w33, Poke Ball); sprite pr_762s.png downloaded; backup .bak_steenee_0925.
- _restart_after_shiny.py relaunched hidden (PID 121500, parent WmiPrvSE 113808). One instance; w34 by 09:27.

## 2026-11-05 09:31-09:40 MST - wild shiny Deerling caught (w43, variant 1)
- Farm stopped 09:31:11 on shiny_enemy Deerling (Lv30, variant 1, not a boss) in a double with Teddiursa. Unchanged at ~09:35 (turn 1, CommandPhase, full HP, Poke 14), so took over.
- Turn 1: Mewtwo Psybeam single-target at Teddiursa (_sw.py mv 0 2 + tgt 2) KO'd it; Absol Leer (mv 1 0 + tgt 2). Deerling untouched (85/85). Mewtwo Lv34.
- Turn 2: Poke Ball (14 -> 13) caught first throw (_sw.py ball Deerling 60, cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, 09:31, Lv30, variant 1, w43, Poke Ball); backup .bak_deerling_0940. Sprite: Deerling icons are form-suffixed (585s-spring.png), saved as pr_585s.png. Note: _lmpeek.js must run via `_sw.py js`, not node.
- _restart_after_shiny.py relaunched hidden (PID 42224, parent WmiPrvSE 113808). One instance; w44 by 09:39.

## 2026-11-05 09:43-09:53 MST - wild shiny Scyther caught (w53, epic variant 3)
- Farm stopped 09:43:49 on shiny_enemy Scyther (Lv33, variant 3, not a boss, single battle). Unchanged at ~09:50 (CommandPhase, Scyther 92/92, Poke 13), so took over. No attack.
- Poke Balls (13 -> 11): first broke free, second caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py "No" -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row, 09:43, Lv33, variant 3, w53, Poke Ball) via _addrow_scyther.py; sprite pr_123s.png downloaded; backup .bak_scyther_0952; frontmatter updated.
- _restart_after_shiny.py relaunched hidden (PID 62484, parent WmiPrvSE 113808). One instance; w55 by 09:52.

## 2026-11-05 10:06-10:09 MST - double-shiny stop w68 (Cofagrigus + Golett)
- Farm stopped 10:06:38 on shiny_enemy at w68: BOTH wild foes shiny (Cofagrigus Lv46 Ghost, Mummy, 111/111; Golett Lv49 Ground/Ghost, 122/122), variant 1, no bosses. Balls: Poke 11, Master 1 (reserved). Party full HP.
- No input sent. A ball cannot be thrown with two foes out, so catching one means KOing the other shiny; handed the choice to Gavin. Farm not restarted; stop flag kept.
- 10:17 MST: game moved from CommandPhase to MovePhase (turn being played) with no input from the watch, so someone else is handling the double shiny. Watch sends no input; later watches check party/storage/Pokedex and log Cofagrigus/Golett as Caught or Missed.
- Both handoff attempts (10:09 and 10:14) returned "Aborted"; not retried, since the event is in NOTIFIED_HANDOFFS.txt and Gavin is now acting.

## 2026-11-05 10:22 MST - wave 68 double shiny: Golett LOST
Psychic KOd shiny Cofagrigus (useMode must be 1, 0 stalls MovePhase). Blind Z presses at next CommandPhase used Meteor Mash/Spirit Break and KOd shiny Golett. No ball thrown. Farm relaunched, stopped on shiny Drapion w71 double.

## 2026-11-05 10:42-10:48 MST - shiny Archeops w84 caught
Epic (variant 3) shiny Archeops Lv61 in double with Tinkaton. Swampert Triple Dive KO'd Tinkaton, Absol Leer; 1st Ultra Ball (5->4) caught it; declined release -> storage. _sw.py ball takes SPECIES name, not ball index. Capture-full prompt options are Summary/Pokedex/Yes/No (No = storage). Shiny Log row + pr_567s.png (pokerogue.net/images/pokemon/shiny/567.png). Removed farm-written stop flag, relaunched hidden PID 146312, wave 86 by 10:47. Mewtwo revived (218/218).

## 2026-11-05 10:48-10:56 MST - shiny Xatu w89 caught
Rare (variant 2) shiny Xatu Lv61 in double with Claydol. Unchanged at 10:52 (CommandPhase, full HP), so took over. Swampert Triple Dive single-target KO'd Claydol, Absol Leer; Xatu untouched. 1st Ultra Ball (4 -> 3) caught it; party full, _optno.py No -> storage. Shiny Log row added (sprite pr_178s.png already present; backup .bak_xatu_1058). _restart_after_shiny.py relaunched hidden PID 36604 (parent WmiPrvSE 113808), one instance, wave 90 by 10:55.

## 2026-11-05 11:03-11:05 MST - watch: config BOM broke primary/candy_target
- agent-tools\pokerogue_farm_config.json now starts with a UTF-8 BOM (likely PokeFarmControl/PowerShell write), so json.loads(read_text("utf-8")) failed: since ~10:35 the farm resolved PRIMARY=Swampert (source=party slot) and CANDY_TARGET fell back to its default (secondary). Mewtwo fainted w108 and was not revived (script revived Swampert).
- pr_farm17.py: both CONFIG_FILE.read_text(encoding="utf-8") -> "utf-8-sig" (lines 79, 265). Backup %TEMP%\prfarm\pr_farm17.bak_bom_20261105_1105.py. py_compile OK.
- Restarted hidden mid w112: PID 151044 (parent WmiPrvSE 113808), one instance. Log: "PRIMARY resolved: Mewtwo (species 150) source=config", CANDY_TARGET=primary. Mewtwo learned Future Sight over Psybeam (protected moves kept).

## 2026-11-05 11:08-11:12 MST - run end w112 -> new run
- Run ended w112 at 11:05 (whole party fainted, Trainer Magma Grunts' Magcargo, slot 2); Run Log row written by script.
- to_title.py -> _re2.py newgame (Classic). reduce 150,359: no option (both maxed). Eggs: Mewtwo x2 (x6, 15 -> 3), Absol x2 (x12, 29 -> 5). Eggs 0 -> 4. Vouchers 622/125/43 unspent.
- nr_pick.py 150,359,263,327,401,258; tryStart via scene.ui.getHandler() -> Confirm, gx.py p:5 -> SaveSlotSelect (slot 2 empty) -> _re2.py slot 2. Verified Classic, wave 1, slot 2, party [150,359,263,327,401,258].
- Flags cleared, stdout rotated, launched hidden (pythonw PID 64552, parent WmiPrvSE 113808). One instance; w5 by 11:12; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.

## 2026-11-05 11:58-12:11 MST - run end w145 -> new run
- Run ended w145 (whole party fainted; trainer Mimikyu/Rayquaza/Talonflame/Goodra/Glimmora), slot 2, Run Log row written by script.
- reduce 150,359: none left (maxed). Bought 2 Mewtwo eggs (15 -> 3) and 1 Absol egg (22 -> 10); eggs 3. No vouchers.
- Note: double `_re2.py cancel` at StarterSelect opens return-to-title Confirm; answered `pick "No"`.
- New run: nr_pick 150,359,263,327,401,258 -> tryStart -> Confirm p:5 -> slot 2 (empty). Verified Classic w1 slot 2.
- Flags cleared, stdout rotated, launched hidden pythonw PID 67364; w9 by 12:10, Mewtwo has Thunderous Kick + Meteor Mash.

## 2026-11-05 12:21-12:24 MST - wild shiny Poliwag w39 MISSED (partner's Discharge KO'd it)
- Farm stopped 12:19:28 on shiny_enemy Poliwag (Lv24, variant 1, not a boss, 58/58) in a wild double with Stunfisk (Ground/Electric, Lv27). Unchanged at 12:21:42 (CommandPhase, full HP, Poke 20 only), so took over.
- Turn 1: Mewtwo Psybeam single-target at Stunfisk (99 -> 38), Absol Leer. Stunfisk used Discharge (move 435, spread, hits its own ally) and KO'd Poliwag ("Wild Poliwag fainted!"). Not recoverable.
- Logged Missed in CHIE Shiny Log.md (top row, 12:19, Lv24, variant 1, w39, ball —); sprite pr_60s.png downloaded; backup .bak_poliwag_1224.
- Lesson: an enemy partner with a spread move (Discharge/Earthquake/Surf etc.) can KO the shiny; KO the partner as fast as possible (both mons may need to hit it when one hit can't KO).
- _restart_after_shiny.py relaunched hidden (PID 66868, parent WmiPrvSE 113808). One instance; w41 by 12:23.

## 2026-11-05 12:26-12:33 MST - wild shiny Lokix w51 caught (rare variant 2)
- Farm stopped 12:26:36 on shiny_enemy Lokix (Lv34, variant 2, single, not a boss). Unchanged at 12:28:54, so took over. No attack.
- Poke Balls (25 -> 21): three broke free, 4th caught. Party full: _optno.py No -> storage. Mewtwo left at 18/154 from Lokix hits.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_945s.png downloaded; backup .bak_lokix_1232).
- _restart_after_shiny.py relaunched hidden (PID 159032, parent WmiPrvSE 113808). One instance; w53 by 12:31, Mewtwo healed to 150/168.
- Note: the 12:24 WakeParent for the missed Poliwag returned "Aborted"; it's in NOTIFIED_HANDOFFS, so the watch did not send it again.

## 2026-11-05 12:34-12:39 MST - run end w60 -> new run
- Run ended w60 at 12:34 (whole party fainted vs Gym Leader Burgh's bug team, Leavanny last), slot 2; Run Log row written by script.
- to_title.py -> _re2.py newgame (Classic). reduce 150,359: no option (both maxed). Candy Mewtwo 5 (egg costs 6, none bought), Absol 15: 1 egg (x12, 15 -> 3) via open/pick "Use Candies"/pick "x12 Buy an Egg". Eggs 6 -> 7. Vouchers 633/127/43 unspent.
- nr_pick 150,359,263,327,401,258 -> gx.py js tryStart -> p:5 -> SaveSlotSelect -> _re2.py slot 2. Verified Classic (mode 0), wave 1, slot 2, party [150,359,263,327,401,258]. Config primary 150 / secondary 359 / candy_target primary.
- Flags cleared, stdout rotated, launched hidden (pythonw PID 146220, parent WmiPrvSE 113808). One instance; w5 by 12:38; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.

## 2026-11-05 12:49-12:53 MST - wild shiny Grimer w43 caught (variant 1)
- Farm stopped 12:49:03 on shiny_enemy Grimer (Lv26, variant 1, single, not a boss). Unchanged at 12:51:21 (CommandPhase turn 1, full HP, balls same), so took over. No attack.
- _sw.py ball Grimer: 1st Great Ball (5 -> 4) caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py No -> storage.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_88s.png downloaded; backup .bak_grimer_1252). Also replaced the script's 12:44 "UNKNOWN x1 (candidates: #359x1)" egg row (w25) with an Absol Egg row (sprite pr_359s.png).
- _restart_after_shiny.py relaunched hidden (PID 83092, parent WmiPrvSE 113808). One instance; w45 by 12:53.

## 2026-11-05 13:12-13:16 MST - wild shiny Lurantis w109 caught (variant 1)
- Farm stopped 13:12:37 on shiny_enemy Lurantis (Lv78, variant 1, single, not a boss). Unchanged at 13:14:53 (CommandPhase turn 1, full HP, balls same), so took over. No attack.
- _sw.py ball Lurantis: 1st Rogue Ball (5 -> 4) caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py No -> storage.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_754s.png downloaded; backup .bak_lurantis_1316). Mewtwo now has Psystrike (TK/Psychic/Psystrike/Meteor Mash).
- _restart_after_shiny.py relaunched hidden (PID 110064, parent WmiPrvSE 113808). One instance; w110 by 13:16 (Mewtwo dropped to 4/371 vs Torterra under weather).

## 2026-11-05 13:17-13:23 MST - run ended w110 (trainer w/ Torterra/Roserade), new run slot 2
- Whole party fainted at wave 110 (13:17:11); Run Log row written by script.
- Reduce 150,359: no options (maxed). Eggs: Mewtwo x2 (15->3), Absol x2 (28->4). Eggs 0->4. Vouchers untouched.
- nr_pick 150,359,263,327,401,258 -> scene.ui.getHandler().tryStart() -> p:5 -> SaveSlotSelect (slot 2 empty) -> _re2.py slot 2. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Flags cleared, stdout rotated, launched hidden (pythonw PID 164784, parent WmiPrvSE 113808). One instance; w8 by 13:22.

## 2026-11-05 13:46-13:51 MST - run ended w66 (trainer w/ Gothitelle/Lopunny/Milotic/Tsareena), new run slot 2
- Whole party fainted at wave 66 (13:42:26, Swampert last vs Tsareena); Run Log row written by script.
- to_title.py -> _re2.py newgame (Classic). Reduce 150,359: no options (maxed). Candy Mewtwo 5 (egg costs 6, none), Absol 14 -> 1 egg (x12, 14 -> 2). Eggs 2 -> 3. Vouchers untouched.
- nr_pick 150,359,263,327,401,258 -> tryStart -> p:5 -> SaveSlotSelect (slot 2 empty) -> _re2.py slot 2. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Flags cleared, stdout rotated, launched hidden (pythonw PID 143408, parent WmiPrvSE 113808). One instance; w6 by 13:50.

## 2026-11-05 14:14-14:25 MST - wild shiny Simisage w76 caught (variant 1, double with Lokix)
- Farm stopped 14:14:02 on shiny_enemy Simisage (Lv53, variant 1, double with Lokix, not a boss). Unchanged at ~14:20 (CommandPhase turn 1, foes full HP, balls same), so took over.
- Turn 1: Mewtwo Meteor Mash (single-target, _sw.py mv 0 3 + tgt 2) at Lokix -> 6 HP; Linoone Tidy Up. Turn 2: Meteor Mash KO'd Lokix; Linoone Tidy Up. Simisage untouched (156/156).
- _sw.py ball Simisage: 1st Rogue Ball (5 -> 4) caught ("Gotcha!", cap_rd.py 80, catch_ack.py). Party full: _optno.py No -> storage; party unchanged.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_512s.png downloaded; backup .bak_simisage_1424).
- _restart_after_shiny.py relaunched hidden (PID 137776, parent WmiPrvSE 113808). One instance.

## 2026-11-05 14:31 MST — NOUSABLE fix (pr_farm17.py)
- Wave 89 Bug-Type Superfan trainer: Wonder Guard Shedinja KO'd Mewtwo and Swampert; Linoone burned all damaging PP and the FightUiHandler looped "no usable move - back" forever (only Tidy Up left).
- Patch: when no damaging move is pickable but some move still has PP, use it to pass the turn (logs `NOUSABLE`). Backup pr_farm17.py.bak_nousable_1431. Restarted hidden (PID 124948); loop cleared, fight continued.

## 2026-11-05 14:32-14:36 MST - run ended w89 (Bug-Type Superfan trainer: Wonder Guard Shedinja/Kleavor), new run slot 2
- Whole party fainted at wave 89 (14:32:47, Kleavor last); Run Log row written by script.
- to_title.py -> _re2.py newgame (Classic). Reduce 150,359: no options (maxed). Eggs: Mewtwo x2 (14 -> 2); Absol 9 candy (egg costs 12, none). Eggs 0 -> 2. Vouchers untouched.
- nr_pick 150,359,263,327,401,258 -> tryStart -> p:5 -> SaveSlotSelect (slot 2 empty) -> _re2.py slot 2. Verified Classic, wave 1, slot 2; Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash.
- Flags cleared, stdout rotated, launched hidden (pythonw PID 108320, parent WmiPrvSE 113808). One instance; w5 by 14:36.

## 2026-11-05 15:10-15:15 MST - run ended w115 (whole party fainted vs trainer Rhyperior/Nidoking); no reductions left; 2 Mewtwo eggs (14->2), 2 Absol eggs (24->0); new slot-2 Classic run, hidden PID 55332, wave 4 by 15:15

## 2026-11-05 15:57-16:07 MST - wild shiny Clawitzer w113 caught (rare variant 2, double with Wugtrio)
- Overnight watch ~15:59: farm process gone after shiny_enemy stop at 15:57:50 (PID 63560 gone); stop flag set; status wave 113 Clawitzer Lv88 variant 2 sid 693 doubles with Wugtrio.
- Gavin-first wait elapsed (~3.5 min); state unchanged (CommandPhase). Took over.
- Turn 1: Mewtwo Psystrike single-target at Wugtrio (KO), Absol Leer at Wugtrio. Clawitzer untouched 243/243.
- _sw.py ball Clawitzer: 1st Rogue Ball (4 -> 3) caught ("Gotcha!"); Master untouched. Party full: _optno.py No -> storage.
- Logged Caught in CHIE Shiny Log.md (top row; sprite pr_693s.png from PokeAPI shiny/693.png; backup .bak_clawitzer_1602).
- _restart_after_shiny.py relaunched hidden (pythonw PID 6328, parent WmiPrvSE 113808). One instance; wave 114 by 16:07 (Team Plasma Sage Zinzolin). No handoff.

## 2026-11-05 16:55-17:14 MST - wild shinies Litwick w31 + Shuppet w33 caught (overnight watch)

### Litwick w31 (singles, variant 1)
- Farm stopped 16:55:37 on shiny_enemy Litwick (Lv21, variant 1, singles). Process already exited; stop flag set. Unchanged at ~17:05 (~10 min, CommandPhase turn 1), so took over.
- _sw.py ball Litwick: 1st Rogue Ball (5 -> 4) caught; Master untouched. Party full: _optno.py No -> storage.
- Logged Caught in CHIE Shiny Log.md (sprite pr_607s.png from PokeAPI official-artwork shiny/607.png; backup .bak_litwick_1706).
- _restart_after_shiny.py relaunched hidden (pythonw launch PID 76748, parent WmiPrvSE 113808).

### Shuppet w33 (doubles with Pumpkaboo, variant 1)
- Immediately after restart, farm hit shiny_enemy Shuppet Lv22 variant 1 wave 33 doubles with Pumpkaboo at 17:08:24 and stopped again.
- Gavin-first wait elapsed (~2.5+ min); state unchanged (CommandPhase turn 1). Took over.
- Turn 1: Mewtwo Meteor Mash (single-target) at Pumpkaboo (58->32), Absol Leer at Pumpkaboo. Turn 2: Meteor Mash KO'd Pumpkaboo; Absol Leer. Shuppet untouched 52/52.
- _sw.py ball Shuppet: 1st Rogue Ball (4 -> 3) caught; Master untouched. Party full: _optno.py No -> storage.
- Logged Caught (sprite pr_353s.png; backup .bak_shuppet_1712).
- _restart_after_shiny.py relaunched hidden (pythonw launch PID 41648, parent WmiPrvSE 113808). No handoff.

## 2026-11-05 19:14-19:25 MST - run ended w115 (Team Skull Boss Guzma Scizor), new run slot 2
- Whole party fainted at wave 115 (~19:14:19 MST) vs Team Skull Boss Guzma (Golisopod/Yanmega/Araquanid then Scizor last); Mewtwo fainted mid-fight; partners wiped. Run Log row written by script (slot=2 luck=2). Process gone; stop flag absent. No new shiny at wipe (earlier Deerling catch + shiny Mewtwo egg hatch already logged).
- to_title.py -> _re2.py newgame (Classic). Reduce 150,359: no options (both maxed vr2). Eggs via _buyeggs_once.py: Mewtwo x3 (x6, candy 22 -> 4), Absol x1 (x12, 19 -> 7). Eggs 0 -> 4. Vouchers 681/135/45 untouched.
- nr_pick 150,359,263,327,401,258 -> gx tryStart -> p:5 -> SaveSlotSelect (slot 2 Empty) -> _re2.py slot 2. Verified Classic (mode 0), wave 1, slot 2, party [150,359,263,327,401,258]. Mewtwo Thunderous Kick/Confusion/Life Dew/Meteor Mash (protected TK+MM present; Psystrike later).
- Flags cleared, stdout rotated, launched hidden via _restart_after_shiny.py (pythonw PID 5640, parent WmiPrvSE 113808). One instance; WAVE UP 1->2 by 19:24.
