from typing import List, Dict, Any, TYPE_CHECKING
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, OptionSet, Range

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in RE5_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class StartingChapter(Choice):
    """
    Determines which chapter you will start with in Chapter Select or upon starting a new game cycle.
    Choosing to start with Chapter 2-3 will result in instant BK and will fail solo generation.
    NOTE THIS OPTION CURRENTLY DOES NOT WORK. DO NOT CHANGE THE VALUE FROM CHAPTER 1-1
    """
    display_name = "Starting Chapter"
    option_chapter1_1 = 1
    option_chapter1_2 = 2
    option_chapter2_1 = 3
    option_chapter2_2 = 4
#   option_chapter2_3 = -1 # Why would you do this to yourself? This would require someone else to send you a chapter, since you'd BK with zero checks in sphere 1.
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
#   option_all = 15 # I don't think this does what I think it does, so I'm going to comment it out and hope I don't need it later.
    default = 1

class StartingWeapon(Choice):
    """
    Determines whether the first sphere of the multiworld will guarantee a weapon or not.
    Pistol means it will guarantee any pistol is in Sphere 1.
    Random means it will guarantee any weapon is in Sphere 1.
    None means it will be entirely random when you obtain your first weapon. Good luck!

    Note: Only BSAA emblems, Bosses, and Breakables that cannot be broken with your knife will require a weapon in logic.
    """
    display_name = "Guarantee Early Starting Weapon"
    option_Early = 1
    option_Early_Local = 2
    option_Early_Pistol = 3
    option_Early_Local_Pistol = 4
    option_None = 5
    default = 3

class IncludeTreasures(Toggle):
    """
    If enabled, Treasures are shuffled into the pool. This includes treasures found in terrain, in chests, standalone, or dropped by enemies. 
    This does NOT include RNG treasure drops such as the Lion Heart from Lickers.
    """
    display_name = "Include Treasures"

#There is currently no reasonable way to randomize BSAA emblems with how I randomize the game. This will require finding memory addresses and offsets for these regions, then figuring out how to grant an item based on that.

#class IncludeEmblems(Toggle):
#    """
#    If enabled, BSAA Emblems are shuffled into the pool. This includes adds 30 locations to the pool, if not filled, this will generate filler.
#    """
#    display_name = "Include BSAA Emblems"

class ExcludeDriving(Toggle):
    """
    Choose if you wish to disable Chapter 2-3 Savanna from appearing in the randomizer.
    Note that no checks are in this level besides level completion, which currently isn't implemented anyways
    
    Disabling this setting will expect you to play 2-3 to goal.
    Enabling this setting will remove Chapter 2-3 from the pool, no longer expecting you to complete the level to goal.
    """
    display_name = "Exclude Driving Level"

class TrapChance(Range):
    """
    Determines the chance for any junk item to become a trap.
    Set it to 0 for no traps, 100 would make all filler items Traps.

    THIS SETTING CURRENTLY DOES NOTHING TO THE ITEM POOL, AS TRAPS ARE NOT IMPLEMENTED.
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

    THIS SETTING CURRENTLY DOES NOTHING TO THE ITEM POOL, AS TRAPS ARE NOT IMPLEMENTED.
    """
    display_name = "Discard Slot Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class SiphonTrapWeight(Range):
    """
    The weight of Siphon Gold traps in the trap pool.
    This trap will remove half of your current gold count when obtained.

    THIS SETTING CURRENTLY DOES NOTHING TO THE ITEM POOL, AS TRAPS ARE NOT IMPLEMENTED.
    """
    display_name = "Siphon Gold Trap Weight"
    range_start = 0
    range_end = 100
    default = 10

@dataclass
class RE5Options(PerGameCommonOptions):
# add IncludeEmblems whenever BSAA Emblems are able to be randomized in the future.
    StartingChapter:     StartingChapter
    StartingWeapon:      StartingWeapon
    IncludeTreasures:    IncludeTreasures
    ExcludeDriving:      ExcludeDriving
    TrapChance:          TrapChance
    DiscardTrapWeight:   DiscardTrapWeight
    SiphonTrapWeight:    SiphonTrapWeight

RE5_option_groups: Dict[str, List[Any]] = {
# add IncludeEmblems whenever BSAA Emblems are able to be randomized in the future.
    "General Options": [StartingChapter, IncludeTreasures, ExcludeDriving],
    "Trap Options": [TrapChance, DiscardTrapWeight, SiphonTrapWeight]
}

slot_data_options: List[str] = [
# add IncludeEmblems whenever BSAA Emblems are able to be randomized in the future.
    "StartingChapter",
    "IncludeTreasures",
    "ExcludeDriving"
]