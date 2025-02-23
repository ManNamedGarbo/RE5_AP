from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import CollectionState
from typing import Dict, TYPE_CHECKING
import Options
from .Regions import Chapters
from .Items import ItemDict, item_table, group_table, RE5Type
from .Locations import LocationDict, EventDict, location_table
from .Options import RE5Options, slot_data_options, RE5_option_groups, StartingChapter, ExcludeDriving

if TYPE_CHECKING:
    from . import RE5World

# Region connection rules, what region goes to where, and what you need to do so.
def set_chapter_rules(player, multiworld, world: "RE5World"):
   # Chapter 1-1
   # Not required, player starts with 1-1 and level has no keys or otherwise outstanding requirements.
   if not StartingChapter == 1:
       set_rule(multiworld.get_entrance("Menu -> 1-1 Civilian Checkpoint", player), lambda state:
           state.has("Chapter 1-1", player, 1))
   # Chapter 1-2
   if not StartingChapter == 2:
       set_rule(multiworld.get_entrance("Menu -> 1-2 Public Assembly", player), lambda state:
           state.has("Chapter 1-2", player, 1))
       set_rule(multiworld.get_entrance("1-2 Public Assembly -> 1-2 Urban District", player), lambda state:
           state.has("Chapter 1-2", player, 1))
       set_rule(multiworld.get_entrance("1-2 Urban District -> 1-2 Abandoned Building", player), lambda state:
           state.has("Chapter 1-2", player, 1))
       set_rule(multiworld.get_entrance("1-2 Abandoned Building -> 1-2 Furnace Facility", player), lambda state:
           state.has("Chapter 1-2", player, 1))
   # Chapter 2-1
   set_rule(multiworld.get_entrance("2-1 The Port -> 2-1 Shanty Town", player), lambda state:
	   state.has("Guard's Key", player, 1))
   if not StartingChapter == 3:
       set_rule(multiworld.get_entrance("Menu -> 2-1 Storage Facility", player), lambda state:
           state.has("Chapter 2-1", player, 1))
       set_rule(multiworld.get_entrance("2-1 Storage Facility -> 2-1 The Bridge", player), lambda state:
           state.has("Chapter 2-1", player, 1))
       set_rule(multiworld.get_entrance("2-1 The Bridge -> 2-1 The Port", player), lambda state:
           state.has("Chapter 2-1", player, 1))
       add_rule(multiworld.get_entrance("2-1 The Port -> 2-1 Shanty Town", player), lambda state:
           state.has("Chapter 2-1", player, 1))
       set_rule(multiworld.get_entrance("2-1 Shanty Town -> 2-1 Train Yard", player), lambda state:
           state.has("Chapter 2-1", player, 1))
   # Chapter 2-2
   if not StartingChapter == 4:
       set_rule(multiworld.get_entrance("Menu -> 2-2 Train Station", player), lambda state:
           state.has("Chapter 2-2", player, 1))
       set_rule(multiworld.get_entrance("2-2 Train Station -> 2-2 The Mines", player), lambda state:
           state.has("Chapter 2-2", player, 1))
       set_rule(multiworld.get_entrance("2-2 The Mines -> 2-2 Mining Area", player), lambda state:
           state.has("Chapter 2-2", player, 1))
   # Chapter 3-1
   set_rule(multiworld.get_entrance("3-1 Marshlands -> 3-1 Village", player), lambda state:
      (state.has("Beast Slate", player, 1) and
       state.has("Raptor Slate", player, 1) and
       state.has("Warrior Slate", player, 1) and
       state.has("Shaman Slate", player, 1)))
   if not StartingChapter == 5:
       set_rule(multiworld.get_entrance("Menu -> 3-1 Marshlands", player), lambda state:
           state.has("Chapter 3-1", player, 1))
       add_rule(multiworld.get_entrance("3-1 Marshlands -> 3-1 Village", player), lambda state:
	       state.has("Chapter 3-1", player, 1))
   # Chapter 3-2
   if not StartingChapter == 6:
       set_rule(multiworld.get_entrance("Menu -> 3-2 Execution Ground", player), lambda state:
           state.has("Chapter 3-2", player, 1))
       set_rule(multiworld.get_entrance("3-2 Execution Ground -> 3-2 Oil Field Refinery", player), lambda state:
           state.has("Chapter 3-2", player, 1))
       set_rule(multiworld.get_entrance("3-2 Oil Field Refinery -> 3-2 Oil Field Control Facility", player), lambda state:
           state.has("Chapter 3-2", player, 1))
       set_rule(multiworld.get_entrance("3-2 Oil Field Control Facility -> 3-2 Oil Field Dock", player), lambda state:
           state.has("Chapter 3-2", player, 1))
   # Chapter 3-3
   if not StartingChapter == 7:
       set_rule(multiworld.get_entrance("Menu -> 3-3 Oil Field - Drilling Facilities", player), lambda state:
           state.has("Chapter 3-3", player, 1))
       set_rule(multiworld.get_entrance("3-3 Oil Field - Drilling Facilities -> 3-3 Irving's Patrol Boat", player), lambda state:
           state.has("Chapter 3-3", player, 1))
   # Chapter 4-1
   if not StartingChapter == 8:
       set_rule(multiworld.get_entrance("Menu -> 4-1 Caves", player), lambda state:
           state.has("Chapter 4-1", player, 1))
       set_rule(multiworld.get_entrance("4-1 Caves -> 4-1 Ancient Village", player), lambda state:
           state.has("Chapter 4-1", player, 1))
       set_rule(multiworld.get_entrance("4-1 Ancient Village -> 4-1 Labyrinth", player), lambda state:
           state.has("Chapter 4-1", player, 1))
   # Chapter 4-2
   set_rule(multiworld.get_entrance("4-2 Worship Area -> 4-2 Pyramid", player), lambda state:
      (state.has("Earth Emblem", player, 1) and
       state.has("Sea Emblem", player, 1) and
       state.has("Sky Emblem", player, 1)))
   if not StartingChapter == 9:
       set_rule(multiworld.get_entrance("Menu -> 4-2 Worship Area", player), lambda state:
           state.has("Chapter 4-2", player, 1))
       add_rule(multiworld.get_entrance("4-2 Worship Area -> 4-2 Pyramid", player), lambda state:
           state.has("Chapter 4-2", player, 1))
       set_rule(multiworld.get_entrance("4-2 Pyramid -> 4-2 Underground Garden", player), lambda state:
           state.has("Chapter 4-2", player, 1))
   # Chapter 5-1
   if not StartingChapter == 10:
       set_rule(multiworld.get_entrance("Menu -> 5-1 Underground Garden", player), lambda state:
           state.has("Chapter 5-1", player, 1))
       set_rule(multiworld.get_entrance("5-1 Underground Garden -> 5-1 Progenitor Virus House", player), lambda state:
           state.has("Chapter 5-1", player, 1))
       set_rule(multiworld.get_entrance("5-1 Progenitor Virus House -> 5-1 Experimental Facility U-8", player), lambda state:
           state.has("Chapter 5-1", player, 1))
   # Chapter 5-2
   if not StartingChapter == 11:
       set_rule(multiworld.get_entrance("Menu -> 5-2 Experimental Facility", player), lambda state:
           state.has("Chapter 5-2", player, 1))
       set_rule(multiworld.get_entrance("5-2 Experimental Facility -> 5-2 Power Station", player), lambda state:
           state.has("Chapter 5-2", player, 1))
       set_rule(multiworld.get_entrance("5-2 Power Station -> 5-2 Experimental Facility Passage", player), lambda state:
           state.has("Chapter 5-2", player, 1))
       set_rule(multiworld.get_entrance("5-2 Experimental Facility Passage -> 5-2 Missile Area 1st Floor", player), lambda state:
           state.has("Chapter 5-2", player, 1))
       set_rule(multiworld.get_entrance("5-2 Missile Area 1st Floor -> 5-2 Uroboros Research Facility", player), lambda state:
           state.has("Chapter 5-2", player, 1))
   # Chapter 5-3
   set_rule(multiworld.get_entrance("5-3 Monarch Room Entrance -> 5-3 Monarch Room Jill & Wesker", player), lambda state:
      state.has_group("precise", player, 1))
   if not StartingChapter == 12:
       set_rule(multiworld.get_entrance("Menu -> 5-3 Uroboros Research Facility", player), lambda state:
           state.has("Chapter 5-3", player, 1))
       set_rule(multiworld.get_entrance("5-3 Uroboros Research Facility -> 5-3 Missile Area 2nd Floor", player), lambda state:
           state.has("Chapter 5-3", player, 1))
       set_rule(multiworld.get_entrance("5-3 Missile Area 2nd Floor -> 5-3 Moving Platform", player), lambda state:
           state.has("Chapter 5-3", player, 1))
       set_rule(multiworld.get_entrance("5-3 Moving Platform -> 5-3 Monarch Room Entrance", player), lambda state:
           state.has("Chapter 5-3", player, 1))
       add_rule(multiworld.get_entrance("5-3 Monarch Room Entrance -> 5-3 Monarch Room Jill & Wesker", player), lambda state:
           state.has("Chapter 5-3", player, 1))
   # Chapter 6-1
   set_rule(multiworld.get_entrance("6-1 Ship Deck -> 6-1 Ship Hold", player), lambda state:
      (state.has("Crane Keycard", player, 1) and
       state.has("Tanker Keycard A", player, 1) and
       state.has("Tanker Keycard B", player, 1)))
   if not StartingChapter == 13:
       set_rule(multiworld.get_entrance("Menu -> 6-1 Ship Deck", player), lambda state:
           state.has("Chapter 6-1", player, 1))
       add_rule(multiworld.get_entrance("6-1 Ship Deck -> 6-1 Ship Hold", player), lambda state:
           state.has("Chapter 6-1", player, 1))
   # Chapter 6-2
   set_rule(multiworld.get_entrance("6-2 Bridge -> 6-2 Bridge Deck", player), lambda state:
       state.has("Bridge Keycard", player, 1))
   if not StartingChapter == 14:
       set_rule(multiworld.get_entrance("Menu -> 6-2 Main Deck", player), lambda state:
           state.has("Chapter 6-2", player, 1))
       set_rule(multiworld.get_entrance("6-2 Main Deck -> 6-2 Bridge", player), lambda state:
           state.has("Chapter 6-2", player, 1))
       add_rule(multiworld.get_entrance("6-2 Bridge -> 6-2 Bridge Deck", player), lambda state:
           state.has("Chapter 6-2", player, 1))
   # Chapter 6-3
   set_rule(multiworld.get_entrance("Menu -> 6-3 Bridge Deck", player), lambda state:
	  (state.has("Chapter 6-3", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
   set_rule(multiworld.get_entrance("6-3 Bridge Deck -> 6-3 Bridge Interior", player), lambda state:
      (state.has("Chapter 6-3", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
   set_rule(multiworld.get_entrance("6-3 Bridge Interior -> 6-3 Engine Room", player), lambda state:
      (state.has("Chapter 6-3", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
   set_rule(multiworld.get_entrance("6-3 Engine Room -> 6-3 Hangar", player), lambda state:
	  (state.has("Chapter 6-3", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has("Hangar Keycard A", player, 1) and
       state.has("Hangar Keycard B", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
   set_rule(multiworld.get_entrance("6-3 Hangar -> 6-3 Volcano", player), lambda state:
      (state.has("Chapter 6-3", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has("Hangar Keycard A", player, 1) and
       state.has("Hangar Keycard B", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
   if ExcludeDriving == 1:
       add_rule(multiworld.get_entrance("Menu -> 6-3 Bridge Deck", player), lambda state:
           state.has("Chapter 2-3 Complete", player, 1))
       add_rule(multiworld.get_entrance("6-3 Bridge Deck -> 6-3 Bridge Interior", player), lambda state:
           state.has("Chapter 2-3 Complete", player, 1))
       add_rule(multiworld.get_entrance("6-3 Bridge Interior -> 6-3 Engine Room", player), lambda state:
           state.has("Chapter 2-3 Complete", player, 1))
       add_rule(multiworld.get_entrance("6-3 Engine Room -> 6-3 Hangar", player), lambda state:
           state.has("Chapter 2-3 Complete", player, 1))
       add_rule(multiworld.get_entrance("6-3 Hangar -> 6-3 Volcano", player), lambda state:
           state.has("Chapter 2-3 Complete", player, 1))
       
# Setup events for each level completion, assign "Complete Chapter X-Y" to them, require all completion for c63_volcano
##########################
##### LOCATION RULES #####
##########################
   set_rule(multiworld.get_location("1-1 Executioner Gold Ring", player), lambda state:
       state.has_group("heavywep", player, 1))
   set_rule(multiworld.get_location("1-2 Ithaca M37", player), lambda state:
       state.has("Old Building Key", player, 1))
   set_rule(multiworld.get_location("1-2 Ivory Relief from Allyson", player), lambda state:
       state.has("weapons", player, 1))
   set_rule(multiworld.get_location("2-1 Guard's Treasure Chest 1", player), lambda state:
       state.has("Guard's Key", player, 1))
   set_rule(multiworld.get_location("2-1 Guard's Treasure Chest 2", player), lambda state:
       state.has("Guard's Key", player, 1))
   set_rule(multiworld.get_location("2-1 Guard's Treasure Chest 3", player), lambda state:
       state.has("Guard's Key", player, 1))
   set_rule(multiworld.get_location("2-1 Guard's Treasure Chest 4", player), lambda state:
       state.has("Guard's Key", player, 1))
   set_rule(multiworld.get_location("3-1 Giant Majini Blue Enigma", player), lambda state:
       state.has_group("heavywep", player, 1))
   set_rule(multiworld.get_location("6-3 Defeat Wesker", player), lambda state:
      (state.has("Chapter 6-3", player, 1) and
       state.has("Hangar Keycard A", player, 1) and
       state.has("Hangar Keycard B", player, 1) and
       state.has("Chapter 1-1 Complete", player, 1) and
       state.has("Chapter 1-2 Complete", player, 1) and
       state.has("Chapter 2-1 Complete", player, 1) and
       state.has("Chapter 2-2 Complete", player, 1) and
       state.has("Chapter 3-1 Complete", player, 1) and
       state.has("Chapter 3-2 Complete", player, 1) and
       state.has("Chapter 3-3 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 4-1 Complete", player, 1) and
       state.has("Chapter 5-1 Complete", player, 1) and
       state.has("Chapter 5-2 Complete", player, 1) and
       state.has("Chapter 5-3 Complete", player, 1) and
       state.has("Chapter 6-1 Complete", player, 1) and
       state.has("Chapter 6-2 Complete", player, 1) and
       state.has_group("weapons", player, 3) and
       state.has_group("heavywep", player, 1)))
        
   world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
        
def set_driving_rules(player, multiworld):
# Adds the on-rails driving sequence 2-3, assuming the player wishes to do so.
# Note: This adds no items. Just a level and a boss with no locations.
    set_rule(multiworld.get_entrance("Menu -> 2-3 Savanna", player), lambda state:
	    state.has("Chapter 2-3", player, 1))
    set_rule(multiworld.get_entrance("2-3 Savanna -> 2-3 Night Port", player), lambda state:
	    state.has("Chapter 2-3", player, 1))

def set_rules(re5_world: "RE5World", ExcludeDriving):
    player = re5_world.player
    multiworld = re5_world.multiworld
    world = re5_world

    set_chapter_rules(player, multiworld, world)
    if ExcludeDriving == 1:
        set_driving_rules(player, multiworld)
