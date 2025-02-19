Links that may help people along the project

Arc File Identification: <https://residentevilmodding.boards.net/thread/3989/re5-ge-arc-list>

All Item IDs: <https://residentevilmodding.boards.net/thread/17341/all-resident-evil-5-items>

Useful Modding Resources: <https://www.mediafire.com/folder/kcz7vfu35nmpo/Resident_Evil_5_Public_Mods_Archive_-_RichardHafer>

RE5 Gold Edition Ultimate Trainer: <https://www.nexusmods.com/residentevil5goldedition/mods/2?tab=description>

File Path for Arc files `.\Resident Evil 5\nativePC_MT\Image\Archive`

----------------------Current Blockers for RE5 Minimal Viable Product----------------------
# Current to-do (updated feb 9th)
- Finish getting the list of all locations assigned correctly to the apworld (lot more draining than I expected, due to how RE5 formats it's locations and item data.)
- Create a parsing tool inside of the apworld that will create the input json needed for the arc randomizer program to function.
- Figure out where BSAA Emblems, Keys, and Chapter Unlocks are in the games memory so they can be randomized.
- Once the above is found, then figure out a way the client will be able to watch these locations, and grant items on the fly when interacting with them. Currently I'm only familiar with game file modification so this probably won't be done by me unfortunately.
- Get some kind of AP client? Not sure where to start with this. Maybe ArsonAssassin's Memory Library will help act as a client and a memory address tracker tool? I don't have the current know-how to do this myself, so someone would absolutely need to help with this.
- Update the Arc Rando script to accept new information as provided through `items_table` "xml_id", alongside `locations_table` "unique_id" and "arc_file" information. (tl;dr
(tl;dr print `"arc_file", "unique_id", "xml_id"` into a json on apworld generation)
