Links that may help people along the project

Arc File Identification: <https://residentevilmodding.boards.net/thread/3989/re5-ge-arc-list>

All Item IDs: <https://residentevilmodding.boards.net/thread/17341/all-resident-evil-5-items>

Useful Modding Resources: <https://www.mediafire.com/folder/kcz7vfu35nmpo/Resident_Evil_5_Public_Mods_Archive_-_RichardHafer>

RE5 Gold Edition Ultimate Trainer: <https://www.nexusmods.com/residentevil5goldedition/mods/2?tab=description>

File Path for Arc files `.\Resident Evil 5\nativePC_MT\Image\Archive`

----------------------Current Blockers for RE5 Minimal Viable Product----------------------
1. I have no idea how regions work in the apworld, even after having it explained by 3 people I just don't understand how to do it, so I'm just not.
2. I need to figure out where certain things are in memory. The absolutely crucial two for my minimal viable product is knowing when a player is in a specific level; the other being where Keys are stored in their story slots and how I can change them on the fly.
3. I need a way to figure out how each location is unique for identifying it for my rando program.

My current randomizer script expects an "input.json" that will be provided from AP upon generation, it'll be something like....
```json
[
  "uW1p3", 279
]
```
My rando program goes "Where is uW1p3 at?" checks another file, "Oh it's in s118.arc! Open that arc file, modify the item to 279 at that location, save and repack it. Boom it's modded now!"
The problem stems from non-unique items, like Gold being randomized. Cause now it's a generic value like "uIt0402", which not only can appear multiple times in a single arc file, but in nearly the exact same coords (up to 6 items in the same chest), but it can appear in MULTIPLE ARC FILES.
so I can't just have the json be like....
```json
[
  "uIt0402", 279
]
```
because then it'll replace some 30 locations across the game all with a Handgun.
that's no bueno.
and in that same Arc file, I can't find anything that could be used as a single unique identifier that wouldn't link to other arc files or items currently existing.

My CURRENT idea to tackle this would be assigning unique identifiers to locations in the apworld, so instead of outputting as the location ID "uIt0402" it'd be more specific. My current mapping files for the python script says `"uIt0402" = s118.arc` which isn't always true, cause of the duplicate locations issue. So since I'm having to be specific about locations to Archipelago anyways, like 2-1 Gold Chest #1, 2-1 Gold Chest #2, couldn't I just assign a unique ID to each of those, then tell it to output that location? Then in my mapping file, lets say `2-1 Gold Chest #1 = 21010402-1`, which my mapping file says `21010402-1 = s118.arc, line 80`, so it'll go straight to that location and modify that one instead of searching for the only result of uIt0402. I think that could work but I barely know how apworlds work, so who knows! I'm ranting at this point.

If I'm wrong in any of these assumptions, or you have better ideas, please let me know. I am by no means an experienced modder or programmer and I'm trying my best to figure things out and make this randomizer work, because I genuinely love this game.
