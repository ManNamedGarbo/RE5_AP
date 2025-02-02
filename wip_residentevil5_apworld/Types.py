from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

class Re5Location(Location):
    game = "Resident Evil 5"

class Re5Item(Item):
    game = "Resident Evil 5"

class ChapterType(IntEnum):
    "1_1" = 1
    "1_2" = 2
    "2_1" = 3
    "2_2" = 4
    "2_3" = 5
    "3_1" = 6
    "3_2" = 7
    "3_3" = 8
    "4_1" = 9
    "4_2" = 10
    "5_1" = 11
    "5_2" = 12
    "5_3" = 13
    "6_1" = 14
    "6_2" = 15
    "6_3" = 16
    ALL = 17

class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1

class EventData(NamedTuple):
    name:       str
    ap_code:    Optional[int] = None

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
    key_type: Optional[ChapterType] = None
    key_requirement: Optional[int] = 0
    level_type: Optional[str] = None

episode_type_to_name = {
    EpisodeType.TOT:      "Tide of Terror",
    EpisodeType.SSE:      "Sunset Snake Eyes",
    EpisodeType.VV:       "Vicious Voodoo",
    EpisodeType.FITS:     "Fire in the Sky",
    EpisodeType.CHOH:     "Cold Heart of Hate",
    EpisodeType.ALL:      "All"
}

episode_type_to_shortened_name = {
    EpisodeType.TOT:    "ToT",
    EpisodeType.SSE:    "SSE",
    EpisodeType.VV:     "VV",
    EpisodeType.FITS:   "FitS",
    EpisodeType.CHOH:   "CHoH",
    EpisodeType.ALL:    "All"
}