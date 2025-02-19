from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import Dict, TYPE_CHECKING
from .Regions import Chapters
from .Items import ItemDict, item_table, group_table, RE5Type
from .Locations import LocationDict, EventDict, location_table

if TYPE_CHECKING:
    from . import RE5World

# Making sure the world can draw data from the proper location
def rules(RE5World):
    multiworld = RE5World.multiworld
    player = RE5World.player

# Region connection rules, what region goes to where, and what you need to do so.
def set_chapter_rules(player, multiworld):
   # Chapter 1-1
    set_rule(multiworld.get_entrance("Menu -> c11_checkpoint", player), lambda state:
	    state.has("Chapter 1-1", player, 1))
    set_rule(multiworld.get_entrance("c11_checkpoint -> c11_alley1", player), lambda state:
	    state.has("Chapter 1-1", player, 1))
    set_rule(multiworld.get_entrance("c11_alley1 -> c11_alley2", player), lambda state:
	    state.has("Chapter 1-1", player, 1))
    set_rule(multiworld.get_entrance("c11_alley2 -> c11_assembly", player), lambda state:
	    state.has("Chapter 1-1", player, 1))
   # Chapter 1-2
    set_rule(multiworld.get_entrance("Menu -> c12_assembly", player), lambda state:
	    state.has("Chapter 1-2", player, 1))
    set_rule(multiworld.get_entrance("c12_assembly -> c12_urban", player), lambda state:
	    state.has("Chapter 1-2", player, 1))
    set_rule(multiworld.get_entrance("c12_urban -> c12_abandoned", player), lambda state:
	    state.has("Chapter 1-2", player, 1))
    set_rule(multiworld.get_entrance("c12_abandoned -> c12_furnace", player), lambda state:
	    state.has("Chapter 1-2", player, 1))
   # Chapter 2-1
    set_rule(multiworld.get_entrance("Menu -> c21_storage", player), lambda state:
	    state.has("Chapter 2-1", player, 1))
    set_rule(multiworld.get_entrance("c21_storage -> c21_bridge", player), lambda state:
	    state.has("Chapter 2-1", player, 1))
    set_rule(multiworld.get_entrance("c21_bridge -> c21_port", player), lambda state:
	   (state.has("Chapter 2-1", player, 1) and
        state.has("Port Key", player, 1)))
    set_rule(multiworld.get_entrance("c21_port -> c21_shanty", player), lambda state:
	   (state.has("Chapter 2-1", player, 1) and
        state.has("Guard's Key", player, 1)))
    set_rule(multiworld.get_entrance("c21_shanty -> c21_train", player), lambda state:
	    state.has("Chapter 2-1", player, 1))
   # Chapter 2-2
    set_rule(multiworld.get_entrance("Menu -> c22_station", player), lambda state:
	    state.has("Chapter 2-2", player, 1))
    set_rule(multiworld.get_entrance("c22_station -> c22_mines", player), lambda state:
	    state.has("Chapter 2-2", player, 1))
    set_rule(multiworld.get_entrance("c22_mines -> c22_popokarimu", player), lambda state:
	    state.has("Chapter 2-2", player, 1))
   # Chapter 2-3
       set_rule(multiworld.get_entrance("Menu -> c23_car", player), lambda state:
	    state.has("Chapter 2-3", player, 1))
    set_rule(multiworld.get_entrance("c23_car -> c23_ndesu", player), lambda state:
	    state.has("Chapter 2-3", player, 1))
   # Chapter 3-1
    set_rule(multiworld.get_entrance("Menu -> c31_marsh", player), lambda state:
	    state.has("Chapter 3-1", player, 1))
    set_rule(multiworld.get_entrance("c31_marsh -> c31_village", player), lambda state:
	   (state.has("Chapter 3-1", player, 1) and
        state.has("Beast Slate", player, 1) and
        state.has("Raptor Slate", player, 1) and
        state.has("Warrior Slate", player, 1) and
        state.has("Shaman Slate", player, 1)))
   # Chapter 3-2
    set_rule(multiworld.get_entrance("Menu -> c32_exegrounds", player), lambda state:
	    state.has("Chapter 3-2", player, 1))
    set_rule(multiworld.get_entrance("c32_exegrounds -> c32_refinery", player), lambda state:
	    state.has("Chapter 3-2", player, 1))
    set_rule(multiworld.get_entrance("c32_refinery -> c32_control", player), lambda state:
	    state.has("Chapter 3-2", player, 1))
    set_rule(multiworld.get_entrance("c32_control -> c32_docks", player), lambda state:
	    state.has("Chapter 3-2", player, 1))
   # Chapter 3-3
    set_rule(multiworld.get_entrance("Menu -> c33_oilboat", player), lambda state:
	    state.has("Chapter 3-3", player, 1))
    set_rule(multiworld.get_entrance("c33_oilboat -> c33_irving", player), lambda state:
	    state.has("Chapter 3-3", player, 1))
   # Chapter 4-1
    set_rule(multiworld.get_entrance("Menu -> c41_caves", player), lambda state:
	    state.has("Chapter 4-1", player, 1))
    set_rule(multiworld.get_entrance("c41_caves -> c41_ancient", player), lambda state:
	    state.has("Chapter 4-1", player, 1))
    set_rule(multiworld.get_entrance("c41_ancient -> c41_labyrinth", player), lambda state:
	    state.has("Chapter 4-1", player, 1))
   # Chapter 4-2
    set_rule(multiworld.get_entrance("Menu -> c42_worship", player), lambda state:
	    state.has("Chapter 4-2", player, 1))
    set_rule(multiworld.get_entrance("c42_worship -> c42_pyramid", player), lambda state:
	    (state.has("Chapter 4-2", player, 1) and
         state.has("Earth Emblem", player, 1) and
         state.has("Sea Emblem", player, 1) and
         state.has("Sky Emblem", player, 1)))
    set_rule(multiworld.get_entrance("c42_pyramid -> c42_garden", player), lambda state:
	    state.has("Chapter 4-2", player, 1))
   # Chapter 5-1
    set_rule(multiworld.get_entrance("Menu -> c51_garden", player), lambda state:
	    state.has("Chapter 5-1", player, 1))
    set_rule(multiworld.get_entrance("c51_garden -> c51_progenitor", player), lambda state:
	    state.has("Chapter 5-1", player, 1))
    set_rule(multiworld.get_entrance("c51_progenitor -> c51_u8", player), lambda state:
	    state.has("Chapter 5-1", player, 1))
   # Chapter 5-2
    set_rule(multiworld.get_entrance("Menu -> c52_experiment", player), lambda state:
	    state.has("Chapter 5-2", player, 1))
    set_rule(multiworld.get_entrance("c52_experiment -> c52_power", player), lambda state:
	    state.has("Chapter 5-2", player, 1))
    set_rule(multiworld.get_entrance("c52_power -> c52_facpassage", player), lambda state:
	    state.has("Chapter 5-2", player, 1))
    set_rule(multiworld.get_entrance("c52_facpassage -> c52_missile1", player), lambda state:
	    state.has("Chapter 5-2", player, 1))
    set_rule(multiworld.get_entrance("c52_missile1 -> c52_mkono", player), lambda state:
	    state.has("Chapter 5-2", player, 1))
   # Chapter 5-3
    set_rule(multiworld.get_entrance("Menu -> c53_uroboros", player), lambda state:
	    state.has("Chapter 5-3", player, 1))
    set_rule(multiworld.get_entrance("c53_uroboros -> c53_missile2", player), lambda state:
	    state.has("Chapter 5-3", player, 1))
    set_rule(multiworld.get_entrance("c53_missile2 -> c53_platform", player), lambda state:
	    state.has("Chapter 5-3", player, 1))
    set_rule(multiworld.get_entrance("c53_platform -> c53_monarch", player), lambda state:
	    state.has("Chapter 5-3", player, 1))
    set_rule(multiworld.get_entrance("c53_monarch -> c53_jill", player), lambda state:
	    state.has("Chapter 5-3", player, 1))
   # Chapter 6-1
    set_rule(multiworld.get_entrance("Menu -> c61_deck", player), lambda state:
	    state.has("Chapter 6-1", player, 1))
    set_rule(multiworld.get_entrance("c61_deck -> c61_hold", player), lambda state:
	    (state.has("Chapter 6-1", player, 1) and
         state.has("Crane Keycard", player, 1) and
         state.has("Tanker Keycard A", player, 1) and
         state.has("Tanker Keycard B", player, 1)))
   # Chapter 6-2
    set_rule(multiworld.get_entrance("Menu -> c62_deck", player), lambda state:
	    state.has("Chapter 6-2", player, 1))
    set_rule(multiworld.get_entrance("c62_deck -> c62_bridge", player), lambda state:
	    state.has("Chapter 6-2", player, 1))
    set_rule(multiworld.get_entrance("c62_bridge -> c62_aheri", player), lambda state:
	    (state.has("Chapter 6-2", player, 1) and
         state.has("Bridge Keycard", player, 1)))
   # Chapter 6-3
    set_rule(multiworld.get_entrance("Menu -> c63_aheri", player), lambda state:
	    state.has("Chapter 6-3", player, 1))
    set_rule(multiworld.get_entrance("c63_aheri -> c63_bridge", player), lambda state:
	    state.has("Chapter 6-3", player, 1))
    set_rule(multiworld.get_entrance("c63_bridge -> c63_engine", player), lambda state:
	    state.has("Chapter 6-3", player, 1))
    set_rule(multiworld.get_entrance("c63_engine -> c63_hangar", player), lambda state:
	   (state.has("Chapter 6-3", player, 1) and
        state.has("Hangar Keycard A", player, 1) and
        state.has("Hangar Keycard B", player, 1)))
    set_rule(multiworld.get_entrance("c63_hangar -> c63_volcano", player), lambda state:
	    state.has("Chapter 6-3", player, 1))
   ##################
   # Location Rules #
   ##################
    set_rule(multiworld.get_location("1-1 Handgun Ammo after First Zombie", player), lambda state:
        state.has("weapons", player, 1))
    set_rule(multiworld.get_location("1-1 VZ61 Briefcase", player), lambda state:
        state.has("weapons", player, 1))
    set_rule(multiworld.get_location("1-1 Executioner Gold Ring", player), lambda state:
        state.has("weapons", player, 1))
    set_rule(multiworld.get_location("1-2 Ithaca M37", player), lambda state:
        state.has("Old Building Key", player, 1))
    set_rule(multiworld.get_location("1-2 Ivory Relief from Allyson", player), lambda state:
        state.has("weapons", player, 1))
    set_rule(multiworld.get_location("1-2 HG Ammo Case 1", player), lambda state:
        state.has("Furnace Key", player, 1))
    set_rule(multiworld.get_location("1-2 HG Ammo Case 2", player), lambda state:
        state.has("Furnace Key", player, 1))
    set_rule(multiworld.get_location("1-2 HG Ammo Case 3", player), lambda state:
        state.has("Furnace Key", player, 1))