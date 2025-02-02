from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, OptionSet, Range

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in Re5_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class StartingChapter(Choice):
    """
    Determines which chapter you will start with in Chapter Select or upon starting a new game cycle.
    """
    display_name = "Starting Chapter"
    option_chapter1_1 = 1
    option_chapter1_2 = 2
    option_chapter2_1 = 3
    option_chapter2_2 = 4
#   option_chapter2_3 = 5 # Why would you do this to yourself? I don't know, but it's an option I guess.
    option_chapter3_1 = 5
    option_chapter3_2 = 6
    option_chapter3_3 = 7
    option_chapter4_1 = 8
    option_chapter4_2 = 9
    option_chapter5_1 = 10
    option_chapter5_2 = 11
    option_chapter5_3 = 12
    option_chapter6_1 = 13
    option_chapter6_2 = 14
    option_all = 15
    default = 1

class IncludeTreasures(Toggle):
    """
    If enabled, Treasures are shuffled into the pool. This includes treasures found in terrain, in chests, standalone, or dropped by enemies. 
    This does NOT include RNG treasure drops such as the Lion Heart from Lickers.
    """
    display_name = "Include Treasures"

class ExcludeDriving(Toggle):
    """
    If enabled, this will disable Chapter 2-3 Savanna from appearing in the randomizer.
    Disabling this may require you to play a level that has no checks besides the level completion itself.
    """
    display_name = "Exclude Driving Level"

class TrapChance(Range):
    """
    Determines the chance for any junk item to become a trap.
    Set it to 0 for no traps.
    """
    display_name = "Include Traps"
    range_start = 0
    range_end = 100
    default = 0

class DiscardTrapWeight(Range):
    """
    The weight of Discard Slot traps in the trap pool.
    This trap will choose a slot in the players inventory at random, and delete the item contained within it.
    Any items deleted in this way are expected to be able to be purchased again, or picked up again from the level of origin.
    """
    display_name = "Discard Slot Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class SiphonTrapWeight(Range):
    """
    The weight of Siphon Gold traps in the trap pool.
    This trap will remove half of your current gold count when obtained.
    """
    display_name = "Siphon Gold Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

@dataclass
class Re5Options(PerGameCommonOptions):
    StartingChapter:                StartingChapter
    IncludeTreasures:               IncludeTreasures
    ExcludeDriving:                 ExcludeDriving
    TrapChance:                     TrapChance
    DiscardTrapWeight:              DiscardTrapWeight
    SiphonTrapWeight:               SiphonTrapWeight

Re5_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartingChapter, IncludeTreasures, ExcludeDriving],
    "Trap Options": [TrapChance, DiscardTrapWeight, SiphonTrapWeight]
}

slot_data_options: List[str] = {
    "StartingChapter",
    "IncludeTreasures",
    "ExcludeDriving",
}