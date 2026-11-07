# Primary sweeper profiles
One JSON per primary (lead). The farm picks the profile whose `species` contains the primary's species id
(primary = config key `primary` if set, else party slot 1 at run start). Files are re-read when they change.
Folder order: `C:\Users\gavin\..PROJECT\pokerogue\profiles\` (edit here), then `%TEMP%\prfarm\profiles\`.
Fields: name, species, signature_items (ranked like Rusted Sword, given to primary), learn_moves, protected_moves,
wanted_moves, replaceable_moves, replace_normal_type, good_moves, primary_move, spread_moves.
No profile for a species -> defaults: decline new moves, no preferred move.
