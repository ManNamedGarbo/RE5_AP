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


# Make a unique ID for each location generated like the following "Chapter, Line of ItemID, ItemType" so "11_426_3" would mean Chapter 1-1, Line 426 of the corresponding arc file, ItemType 3 for briefcase. Chapter data is unneeded, but helps prevent non-unique IDs. 
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
        'unique_id': "11_426_3"},