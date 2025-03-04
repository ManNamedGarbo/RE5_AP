See the AP Arc Randomizer, required for file mod randomization https://github.com/ManNamedGarbo/RE5_Arc_Rando

# Current to-do (updated March 3rd)
- Locations.py has been reworked and requires more fields be filled out than ever. There is a cheat engine table included in this repo that can be used to find coordinates of item locations in game, this needs to be done for every single location, logging it's ItemID (the first number), then the X, Y, Z coordinates, then name the location. Do this for every single location in the game which is around 900 if you include all guns, keys, treasures, ammo/herbs/loose items, and so on.
- Option to includetreasure currently doesn't do anything, flag locations that are treasures for such
- Option to includebreakables should PROBABLY be made a thing, cause holy shit that's a ton of locations if you don't. Locations like crates, barrels and fruit should be included for such an option.
- Figure out BSAA Emblems, Keys, and Chapter Unlocks as Memory Addresses/Offsets so they can be randomized. Without Keys/Chapter Unlocks being able to be randomized then randomization would become quite linear.
- Use ArsonAssassin's AP Memory Library client to read/write memory and handle the connection between the game and Archipelago (this is a different undertaking entirely than the apworld, but both need each other to function so it's listed here.)

Links that may help people who wish to contribute to the project
File Path for Arc files `.\Resident Evil 5\nativePC_MT\Image\Archive`
Arc File Identification: <https://residentevilmodding.boards.net/thread/3989/re5-ge-arc-list>
All Item IDs: <https://residentevilmodding.boards.net/thread/17341/all-resident-evil-5-items>
Useful Modding Resources: <https://www.mediafire.com/folder/kcz7vfu35nmpo/Resident_Evil_5_Public_Mods_Archive_-_RichardHafer>
RE5 Gold Edition Ultimate Trainer: <https://www.nexusmods.com/residentevil5goldedition/mods/2?tab=description>
