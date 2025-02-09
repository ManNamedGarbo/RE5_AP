from typing import TypedDict, List
from .Regions import Stages


class LocationDict(TypedDict):
    name: str
    chapter: Chapters
    arc_file: str
    unique_id: str


class EventDict(TypedDict):
    name: str
    chapter: str
    item: str


# Make a unique ID for each location generated like the following "Chapter, Line of ItemID, ItemType" so "115_426_3" would mean "Arc File 115, Line 426", ItemType 3 for briefcase.
# The reason the unique ID includes the Arc file number at the beginning is in case there is somehow an overlap in line/filetype in another file. If s115 has 426_3, and s100 also has 426_3, the arc randomizer wouldn't know the differece otherwise, so it's there as backup.
# Gonna need to make the apworld generate a json on generation that outputs a Location, Arc file, Which line to replace, and what item ID.
# Heres an example for Chapter 1-1 M92F Briefcase being replaced with a green herb;
# [
# "s115.arc", 426, 769, 3
# ]
# This is saying to the Arc Randomizer "Unpack s115.arc, in the item lot xml file go to line 426, replace the itemid value with 769 to place a green herb there, ensure itemtype for that same classref is 3 since it's in a briefcase location.
# Each line in this output json would denote a different item, as pulled from Archipelago's slot data (probably).
location_table: List[LocationDict] = [
    {'name': "Chapter 1-1 M92F Briefcase",
        'chapter': c11_alley1,
        'arc_file': "s115.arc",
        'unique_id': "115_426_3"},
    {'name': "Chapter 1-1 Butcher Shop Crate",
        'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_96_2"},
    {'name': "Chapter 1-1 Butcher Shop Barrel",
         'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_151_2"},
    {'name': "Chapter 1-1 Carcass House Barrel 1",
         'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_206_2"},
    {'name': "Chapter 1-1 Carcass House Barrel 2",
         'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_481_2"},
    {'name': "Chapter 1-1 Carcass House Box",
         'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_41_2"},
    {'name': "Chapter 1-1 Carcass House Shelf Herb",
         'chapter': c11_alley1,
         'arc_file': "s115.arc",
         'unique_id': "115_316_0"},
    {'name': "1-1 Handgun Ammo after First Zombie",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_41_4"},
    {'name': "1-1 Barricade Safehouse Shelf Herb",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_206_0"},
    {'name': "1-1 Barricade Safehouse Shelf Grenade",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_536_0"},
    {'name': "1-1 Barricade Safehouse Shelf Handgun Ammo",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_261_0"},
# Locations are missing valid unique_id that would allow randomization. Basically I can't find out how to assign unique numbers to them cause of how the arc file lays out breakables.
#    {'name': "1-1 Barricade Safehouse Barrel 1",
#         'chapter': c11_alley2,
#         'arc_file': "s116.arc",
#         'unique_id': "116_"},
#    {'name': "1-1 Barricade Safehouse Barrel 2",
#         'chapter': c11_alley2,
#         'arc_file': "s116.arc",
#         'unique_id': "116_"},
#    {'name': "1-1 Barricade Safehouse Barrel 3",
#         'chapter': c11_alley2,
#         'arc_file': "s116.arc",
#         'unique_id': "116_"},
    {'name': "1-1 After Tunnel Shelf Handgun Ammo",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_426_0"},
# Two handgun ammos side by side, but not enough appearances of Handgun Ammo in the arc file. Might be a shared location?
#    {'name': "1-1 After Tunnel Shelf Handgun Ammo 2",
#         'chapter': c11_alley2,
#         'arc_file': "s116.arc",
#         'unique_id': "116_"},
    {'name': "1-1 After Tunnel Shelf Herb",
         'chapter': c11_alley2,
         'arc_file': "s116.arc",
         'unique_id': "116_151_0"},
    {'name': "1-1 VZ61 Briefcase",
         'chapter': c11_assembly,
         'arc_file': "s114.arc",
         'unique_id': "114_96_3"},
    {'name': "1-1 Executioner Gold Ring",
         'chapter': c11_assembly,
         'arc_file': "s114.arc",
         'unique_id': "114_41_4"},
]