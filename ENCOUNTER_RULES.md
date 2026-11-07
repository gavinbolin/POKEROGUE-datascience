# Encounter rules

Version `encounter-rules-v1`. Content hash `08a83b9bf28e8a1b69694a02a0b04ec53680dc12e474abadeda354e9f742b990`.

Each encounter stores a chosen option and a fallback, as option keys (`option_1` is the first button). There is no preference ranking. `leave` takes the last option and ignores the chosen option. A fallback is used when the chosen option's requirements are not met, or when a simple condition fails.

The farm editor writes the live `encounter_rules.json` next to `item_priority.json` and reloads it when the file changes. The simulator keeps its own pinned copy and does not read this file.

## Mystery encounters

| Encounter | Tier | Waves | Choice | Fallback | Leave | Follow-up | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mysterious Challengers | GREAT | 10–180 | A Clever, Mindful Foe | The Mightiest Foe | no |  | Farm takes the top option (A Clever, Mindful Foe). If that option's requirements are not met, use The Mightiest Foe. |
| The Mysterious Chest | COMMON | 10–180 | Open It | Too Risky, Leave | no |  | Farm opens the chest. |
| Dark Deal | ROGUE | 30–180 | Refuse | Refuse | yes |  | Farm leaves. This encounter is on the party-change block list (trade, weird dream, or dark deal). |
| Fight or Flight | COMMON | 10–180 | Battle the Pokémon | Leave | no |  | Farm takes the top option (Battle the Pokémon). If that option's requirements are not met, use Leave. |
| Slumbering {{snorlaxName}} | GREAT | 15–150 | Battle It | Steal Its Item | no |  | Farm takes the top option (Battle It). If that option's requirements are not met, use Steal Its Item. |
| Training Session | ULTRA | 10–180 | Leave | Leave | yes | Which Pokémon: Lowest-index unfainted; Nature to train: Hardy; Ability to train: First offered ability | Farm opts out. Heavy training teaches an ability, which the farm declines. |
| Department Store Sale | COMMON | 10–100 | TM Counter | Poké Ball Counter | no |  | Farm takes the top option (TM Counter). If that option's requirements are not met, use Poké Ball Counter. |
| The Vitamin Dealer | COMMON | 10–180 | The Pricey Deal | Leave | no | Which Pokémon: Lowest-index unfainted | Farm picks The Pricey Deal when its requirements are met, otherwise Leave. |
| Field Trip | COMMON | 10–100 | A Physical Move | A Status Move | no | Which Pokémon: Lowest-index unfainted; Move to demonstrate: First move matching the chosen category | Farm takes the top option (A Physical Move). If that option's requirements are not met, use A Status Move. |
| The Safari Zone | GREAT | 10–180 | Enter | Leave | no | Safari action: Throw a Poké Ball | Farm takes the top option (Enter). If that option's requirements are not met, use Leave. |
| Lost at Sea | COMMON | 10–180 | {{option1PrimaryName}} Might Help | Wander Aimlessly | no |  | Farm takes the top option ({{option1PrimaryName}} Might Help). If that option's requirements are not met, use Wander Aimlessly. |
| Fiery Fallout | COMMON | 40–180 | Find the Source | Your Fire Resistant Pokémon Help | no |  | Farm takes the top option (Find the Source). If that option's requirements are not met, use Your Fire Resistant Pokémon Help. |
| The Strong Stuff | COMMON | 10–180 | Approach the {{shuckleName}} | Battle the {{shuckleName}} | no |  | Farm takes the top option (Approach the {{shuckleName}}). If that option's requirements are not met, use Battle the {{shuckleName}}. |
| The Pokémon Salesman | ULTRA | 10–180 | Accept | Refuse | no |  | Farm takes the top option (Accept). If that option's requirements are not met, use Refuse. |
| An Offer You Can’t Refuse | GREAT | 10–180 | Accept the Deal | Leave | no |  | Farm takes the top option (Accept the Deal). If that option's requirements are not met, use Leave. |
| Delibir-dy | GREAT | 10–180 | Give Money | Give an Item | no | Which Pokémon: Lowest-index unfainted; Food to give: Berry, Reviver Seed; Held item to give: First transferable held item (not a berry, Reviver Seed, or vitamin) | Farm takes the top option (Give Money). If that option's requirements are not met, use Give an Item. |
| Absolute Avarice | GREAT | 20–180 | Battle It | Let It Have the Food | no |  | Farm takes the top option (Battle It). If that option's requirements are not met, use Let It Have the Food. |
| A Trainer’s Test | ROGUE | 100–180 | Accept the Challenge | Refuse the Challenge | no |  | Farm takes the top option (Accept the Challenge). If that option's requirements are not met, use Refuse the Challenge. |
| Trash to Treasure | ULTRA | 100–180 | Investigate Further | Dig for Valuables | no |  | Farm takes the top option (Investigate Further). If that option's requirements are not met, use Dig for Valuables. |
| Berries Abound | COMMON | 10–180 | Battle the Pokémon | Leave | no |  | Farm takes the top option (Battle the Pokémon). If that option's requirements are not met, use Leave. |
| Clowning Around | ULTRA | 80–180 | Battle the Clown | Return the Insults | no | Which Pokémon: Lowest-index unfainted; Ability offered after the battle: Decline | Farm takes the top option (Battle the Clown). If that option's requirements are not met, use Return the Insults. |
| Part-Timer | COMMON | 10–180 | Make Deliveries | Sales Assistant | no | Which Pokémon: Lowest-index unfainted | Farm takes the top option (Make Deliveries). If that option's requirements are not met, use Sales Assistant. |
| Dancing Lessons | GREAT | 30–180 | Battle It | Show It a Dance | no | Which Pokémon: Lowest-index unfainted; Dance move to show: First Dance move the party knows | Farm takes the top option (Battle It). If that option's requirements are not met, use Show It a Dance. |
| ??? | ROGUE | 30–140 | Quickly Leave | Quickly Leave | yes |  | Farm leaves. This encounter is on the party-change block list (trade, weird dream, or dark deal). |
| The Winstrate Challenge | ROGUE | 100–180 | Accept the Challenge | Refuse the Challenge | no |  | Farm takes the top option (Accept the Challenge). If that option's requirements are not met, use Refuse the Challenge. |
| Teleporting Hijinks | COMMON | 10–180 | Put Money In | Inspect the Machine | no |  | Farm takes the top option (Put Money In). If that option's requirements are not met, use Inspect the Machine. |
| The Bug-Type Superfan | GREAT | 30–180 | Offer to Battle | Gift a Bug Item | no | Which Pokémon: Lowest-index unfainted; Bug move to teach after the battle: Decline (Cancel); Bug item to gift: Quick Claw, Grip Claw, Bug-type booster | Farm takes the top option (Offer to Battle). If that option's requirements are not met, use Gift a Bug Item. |
| Fun And Games! | GREAT | 10–180 | Play the Game | Leave | no | Which Pokémon: Lowest-index unfainted | Farm takes the top option (Play the Game). If that option's requirements are not met, use Leave. |
| Uncommon Breed | COMMON | 10–180 | Battle the Pokémon | Befriend It | no |  | Farm takes the top option (Battle the Pokémon). If that option's requirements are not met, use Befriend It. |
| The GTS | COMMON | 10–180 | Leave | Leave | yes | Which Pokémon: Lowest-index unfainted | Farm leaves. This encounter is on the party-change block list (trade, weird dream, or dark deal). |
| The Expert Pokémon Breeder | ULTRA | 25–180 | {{pokemon1Name}} | {{pokemon3Name}} | no |  | Farm takes the top option ({{pokemon1Name}}). If that option's requirements are not met, use {{pokemon3Name}}. |

## Options

### Mysterious Challengers

`mysteriousChallengers` · GREAT · waves [10, 180]

- `option_1` **A Clever, Mindful Foe**. Requirements: none.
- `option_2` **A Strong Foe**. Requirements: none.
- `option_3` **The Mightiest Foe**. Requirements: none.

### The Mysterious Chest

`mysteriousChest` · COMMON · waves [10, 180]

- `option_1` **Open It**. Requirements: mode:DEFAULT.
- `option_2` **Too Risky, Leave**. Requirements: none.

### Dark Deal

`darkDeal` · ROGUE · waves [30, 180]

- `option_1` **Accept**. Requirements: mode:DEFAULT.
- `option_2` **Refuse**. Requirements: none.

### Fight or Flight

`fightOrFlight` · COMMON · waves [10, 180]

- `option_1` **Battle the Pokémon**. Requirements: none.
- `option_2` **Steal the Item**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(new MoveRequirement(STEALING_MOVES, true).
- `option_3` **Leave**. Requirements: none.

### Slumbering {{snorlaxName}}

`slumberingSnorlax` · GREAT · waves [15, 150]

- `option_1` **Battle It**. Requirements: none.
- `option_2` **Wait for It to Move**. Requirements: none.
- `option_3` **Steal Its Item**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(new MoveRequirement(STEALING_MOVES, true).

### Training Session

`trainingSession` · ULTRA · waves [10, 180]

- `option_1` **Light Training**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_2` **Moderate Training**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_3` **Heavy Training**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_4` **Leave**. Requirements: none.

### Department Store Sale

`departmentStoreSale` · COMMON · waves [10, 100]

- `option_1` **TM Counter**. Requirements: none.
- `option_2` **Vitamin Counter**. Requirements: none.
- `option_3` **Battle Item Counter**. Requirements: none.
- `option_4` **Poké Ball Counter**. Requirements: none.

### The Vitamin Dealer

`shadyVitaminDealer` · COMMON · waves [10, 180]

- `option_1` **The Cheap Deal**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withSceneMoneyRequirement(0, VITAMIN_DEALER_CHEAP_PRICE_MULTIPLIER).
- `option_2` **The Pricey Deal**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withSceneMoneyRequirement(0, VITAMIN_DEALER_EXPENSIVE_PRICE_MULTIPLIER).
- `option_3` **Leave**. Requirements: none.

### Field Trip

`fieldTrip` · COMMON · waves [10, 100]

- `option_1` **A Physical Move**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_2` **A Special Move**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_3` **A Status Move**. Selects a Pokémon. Requirements: mode:DEFAULT.

### The Safari Zone

`safariZone` · GREAT · waves [10, 180]

- `option_1` **Enter**. Requirements: mode:DISABLED_OR_DEFAULT, withSceneRequirement(new MoneyRequirement(0, SAFARI_MONEY_MULTIPLIER).
- `option_2` **Leave**. Requirements: mode:DEFAULT.

### Lost at Sea

`lostAtSea` · COMMON · waves [10, 180]

- `option_1` **{{option1PrimaryName}} Might Help**. Requirements: mode:DISABLED_OR_DEFAULT, withPokemonCanLearnMoveRequirement(OPTION_1_REQUIRED_MOVE).
- `option_2` **{{option2PrimaryName}} Might Help**. Requirements: mode:DISABLED_OR_DEFAULT, withPokemonCanLearnMoveRequirement(OPTION_2_REQUIRED_MOVE).
- `option_3` **Wander Aimlessly**. Requirements: none.

### Fiery Fallout

`fieryFallout` · COMMON · waves [40, 180]

- `option_1` **Find the Source**. Requirements: none.
- `option_2` **Hunker Down**. Requirements: none.
- `option_3` **Your Fire Resistant Pokémon Help**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(CombinationPokemonRequirement.Some( new TypeRequirement(PokemonType.FIRE, true, 1), AbilityRequirement(FIRE_RESISTANT_ABILITIES, true).

### The Strong Stuff

`theStrongStuff` · COMMON · waves [10, 180]

- `option_1` **Approach the {{shuckleName}}**. Requirements: none.
- `option_2` **Battle the {{shuckleName}}**. Requirements: none.

### The Pokémon Salesman

`thePokemonSalesman` · ULTRA · waves [10, 180]

- `option_1` **Accept**. Requirements: mode:DISABLED_OR_DEFAULT, withSceneMoneyRequirement(0, MAX_POKEMON_PRICE_MULTIPLIER).
- `option_2` **Refuse**. Requirements: none.

### An Offer You Can’t Refuse

`anOfferYouCantRefuse` · GREAT · waves [10, 180]

- `option_1` **Accept the Deal**. Requirements: mode:DEFAULT.
- `option_2` **Extort the Kid**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(CombinationPokemonRequirement.Some( new MoveRequirement(EXTORTION_MOVES, true), AbilityRequirement(EXTORTION_ABILITIES, true).
- `option_3` **Leave**. Requirements: none.

### Delibir-dy

`delibirdy` · GREAT · waves [10, 180]

- `option_1` **Give Money**. Requirements: mode:DISABLED_OR_DEFAULT, withSceneMoneyRequirement(0, DELIBIRDY_MONEY_PRICE_MULTIPLIER).
- `option_2` **Give Food**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withPrimaryPokemonRequirement(new HeldItemRequirement(OPTION_2_ALLOWED_MODIFIERS).
- `option_3` **Give an Item**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withPrimaryPokemonRequirement(new HeldItemRequirement(OPTION_3_DISALLOWED_MODIFIERS, 1, true).

### Absolute Avarice

`absoluteAvarice` · GREAT · waves [20, 180]

- `option_1` **Battle It**. Requirements: mode:DEFAULT.
- `option_2` **Reason with It**. Requirements: mode:DEFAULT.
- `option_3` **Let It Have the Food**. Requirements: mode:DEFAULT.

### A Trainer’s Test

`aTrainersTest` · ROGUE · waves [100, 180]

- `option_1` **Accept the Challenge**. Requirements: none.
- `option_2` **Refuse the Challenge**. Requirements: none.

### Trash to Treasure

`trashToTreasure` · ULTRA · waves [100, 180]

- `option_1` **Investigate Further**. Requirements: mode:DEFAULT.
- `option_2` **Dig for Valuables**. Requirements: mode:DEFAULT.

### Berries Abound

`berriesAbound` · COMMON · waves [10, 180]

- `option_1` **Battle the Pokémon**. Requirements: none.
- `option_2` **Race to the Bush**. Requirements: mode:DEFAULT.
- `option_3` **Leave**. Requirements: none.

### Clowning Around

`clowningAround` · ULTRA · waves [80, 180]

- `option_1` **Battle the Clown**. Requirements: mode:DEFAULT.
- `option_2` **Remain Unprovoked**. Requirements: mode:DEFAULT.
- `option_3` **Return the Insults**. Selects a Pokémon. Requirements: mode:DEFAULT.

### Part-Timer

`partTimer` · COMMON · waves [10, 180]

- `option_1` **Make Deliveries**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_2` **Warehouse Work**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_3` **Sales Assistant**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(new MoveRequirement(CHARMING_MOVES, true).

### Dancing Lessons

`dancingLessons` · GREAT · waves [30, 180]

- `option_1` **Battle It**. Requirements: mode:DEFAULT.
- `option_2` **Learn Its Dance**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_3` **Show It a Dance**. Selects a Pokémon. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(new MoveRequirement(DANCING_MOVES, true).

### ???

`weirdDream` · ROGUE · waves [30, 140]

- `option_1` **“I See Them”**. Requirements: mode:DEFAULT.
- `option_2` **“Show Them To Me”**. Requirements: none.
- `option_3` **Quickly Leave**. Requirements: none.

### The Winstrate Challenge

`theWinstrateChallenge` · ROGUE · waves [100, 180]

- `option_1` **Accept the Challenge**. Requirements: none.
- `option_2` **Refuse the Challenge**. Requirements: none.

### Teleporting Hijinks

`teleportingHijinks` · COMMON · waves [10, 180]

- `option_1` **Put Money In**. Requirements: mode:DISABLED_OR_DEFAULT, withSceneMoneyRequirement(0, MONEY_COST_MULTIPLIER).
- `option_2` **A Pokémon Helps**. Requirements: mode:DISABLED_OR_SPECIAL, withPokemonTypeRequirement(MACHINE_INTERFACING_TYPES, true, 1).
- `option_3` **Inspect the Machine**. Requirements: none.

### The Bug-Type Superfan

`bugTypeSuperfan` · GREAT · waves [30, 180]

- `option_1` **Offer to Battle**. Requirements: none.
- `option_2` **Show Your Bug-types**. Requirements: mode:DISABLED_OR_DEFAULT, withPrimaryPokemonRequirement(new TypeRequirement(PokemonType.BUG, false, 1).
- `option_3` **Gift a Bug Item**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withPrimaryPokemonRequirement(CombinationPokemonRequirement.Some( // Meets one or both of the below reqs new HeldItemRequirement(["BypassSpeedChanceModifier", "ContactHeldItemTransferChanceModifier"], 1), AttackTypeBoosterHeldItemTypeRequirement(PokemonType.BUG, 1).

### Fun And Games!

`funAndGames` · GREAT · waves [10, 180]

- `option_1` **Play the Game**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withSceneRequirement(new MoneyRequirement(0, 1.5).
- `option_2` **Leave**. Requirements: none.

### Uncommon Breed

`uncommonBreed` · COMMON · waves [10, 180]

- `option_1` **Battle the Pokémon**. Requirements: none.
- `option_2` **Give It Food**. Requirements: mode:DISABLED_OR_SPECIAL, withSceneRequirement(new PersistentModifierRequirement("BerryModifier", 4).
- `option_3` **Befriend It**. Requirements: mode:DISABLED_OR_SPECIAL, withPrimaryPokemonRequirement(new MoveRequirement(CHARMING_MOVES, true).

### The GTS

`globalTradeSystem` · COMMON · waves [10, 180]

- `option_1` **Check Trade Offers**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withSceneRequirement(new PartySizeRequirement([2, 6], true).
- `option_2` **Wonder Trade**. Selects a Pokémon. Requirements: mode:DISABLED_OR_DEFAULT, withSceneRequirement(new PartySizeRequirement([2, 6], true).
- `option_3` **Trade an Item**. Selects a Pokémon. Requirements: mode:DEFAULT.
- `option_4` **Leave**. Requirements: none.

### The Expert Pokémon Breeder

`theExpertPokemonBreeder` · ULTRA · waves [25, 180]

- `option_1` **{{pokemon1Name}}**. Requirements: mode:DEFAULT.
- `option_2` **{{pokemon2Name}}**. Requirements: mode:DEFAULT.
- `option_3` **{{pokemon3Name}}**. Requirements: mode:DEFAULT.

## Other encounters

These are not mystery encounters. The catch switch and ball cap refine the global catching setting.

| Encounter | Catch | Ball cap | Note |
| --- | --- | --- | --- |
| Wild shiny | no | none | The farm stops for a human on a wild shiny. The simulator cannot wait, so catch is off: fight with the normal move rules and do not make a special shiny catch. |
| Wild boss | yes | rogue | Catch when a party slot is empty, shields are down, and the enemy BST is above the weakest party member. Ball cap rogue means the best non-Master ball. |
| Trainer | no | none | Trainers are fought like a normal wave. No catch. |
| Eternatus (wave 200) | no | none | The Classic final boss is never a catch target. |
