import random

from typing import List, Dict, Any, TYPE_CHECKING, TypedDict, Set
from BaseClasses import MultiWorld, Region, Location, Item, Tutorial, ItemClassification, CollectionState
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import PerGameCommonOptions, World, WebWorld
from dataclasses import dataclass
from Options import Choice, OptionGroup, Toggle, OptionSet, Range
from enum import Enum
from .Items import RE5Type, ItemDict, item_table, group_table
from .Locations import LocationDict, EventDict, location_table
from .Regions import Chapters, region_exits
from .Options import create_option_groups, Re5Options, Re5_option_groups, slot_data_options
from .Rules import set_rules, set_driving_rules, set_chapter_rules, rules, 

class RE5Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Resident Evil 5 Randomizer and connecting to an Archipelago Multiworld. "
        "English",
        "setup_en.md",
        "setup/en",
        ["Garbo"]
    )]

class RE5World(World):
    """
    Resident Evil 5 is a survival horror game packed with hordes of fast-moving, quick-thinking enemies that represent a whole new breed of unimaginable undead evil.
    """

    game = "Resident Evil 5"
    web = RE5Web()

    item_name_to_id = {item["name"]: (base_id + index) for index, item in enumerate(item_table)}
    item_name_to_type = {item["name"]: item["type"] for item in item_table}
    location_name_to_id = {loc["name"]: (base_id + index) for index, loc in enumerate(location_table)}

    item_name_groups = group_table
    options_dataclass = Re5Options
    options: Re5Options

    def __init__(self, multiworld: MultiWorld, player: int):
        super(RE5World, self).__init__(multiworld, player)
        self.item_classification: Dict[BRCType, ItemClassification] = {
            RE5Type.Chapter: ItemClassification.progression,
            RE5Type.Key: ItemClassification.progression,
            RE5Type.Assault: ItemClassification.progression,
            RE5Type.Magnum: ItemClassification.progression,
            RE5Type.Explosive: ItemClassification.progression,
            RE5Type.Special: ItemClassification.progression_skip_balancing, # I don't want it to rely on special weapons like the Minigun and Longbow for progression, but they are here in case you do get them.
            RE5Type.Treasure: ItemClassification.useful,
            RE5Type.Handgun: ItemClassification.progression,
            RE5Type.SMG: ItemClassification.progression,
            RE5Type.Shotgun: ItemClassification.progression,
            RE5Type.Rifle: ItemClassification.progression,
            RE5Type.Healing: ItemClassification.filler,
            RE5Type.Ammo: ItemClassification.filler,
            RE5Type.Filler: ItemClassification.filler
        }

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)

    def set_rules(self):
        rules(self)

    def get_item_classification(self, item_type: Re5Type) -> ItemClassification:
        classification = ItemClassification.filler
        if item_type in self.item_classification.keys():
            classification = self.item_classification[item_type]

        return classification

    def create_item(self, name: str) -> "Re5Item":
        item_id: int = self.item_name_to_id[name]
        item_type: Re5Type = self.item_name_to_type[name]
        classification = self.get_item_classification(item_type)
        
        return Re5Item(name, classification, item_id, self.player)

    def create_event(self, event: str) -> "Re5Item":
        return Re5Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        item = self.random.choice(item_table)

        while self.get_item_classification(item["type"]) == ItemClassification.progression:
            item = self.random.choice(item_table)

        return item["name"]

    def generate_early(self):
        generate_early(self)
        
    def set_rules(self):
        set_rules(self)

    def create_items(self):
        create_items(self)
    
    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)

        for n in region_exits:
            multiworld.regions += [Region(n, player, multiworld)]

        menu.add_exits({"c11_checkpoint", "c12_assembly", "c21_storage", "c22_station", "c23_car", "c31_marsh", "c32_exegrounds", "c33_oilboat", "c41_caves", "c42_worship", "c51_garden", "c52_experiment", "c53_uroboros", "c61_deck", "c62_deck", "c63_aheri"})

        for n in region_exits:
            self.get_region(n).add_exits(region_exits[n])

        for index, loc in enumerate(location_table):
            stage: Region = self.get_region(loc["stage"])
            stage.add_locations({loc["name"]: base_id + index})

        for e in event_table:
            stage: Region = self.get_region(e["stage"])
            event = Re5Location(player, e["name"], None, stage)
            event.show_in_spoiler = False
            event.place_locked_item(self.create_event(e["item"]))
            stage.locations += [event]

        multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
        
    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options
        
        slot_data: Dict[str, Any] = {
            "locations": {loc["game_id"]: (base_id + index) for index, loc in enumerate(location_table)},
            "StartingChapter": options.StartingChapter.value,
            "IncludeTreasures": options.IncludeTreasures.value,
            "ExcludeDriving": options.ExcludeDriving.value,
            "TrapChance": options.TrapChance.value,
            "DiscardTrapWeight": options.DiscardTrapWeight.value,
            "SiphonTrapWeight": options.SiphonTrapWeight.value
        }

        return slot_data

# Figure out how, on generation, to pull the slot data and figure out "Hey, X item is placed on Y location"
# Then using that info, grab Chapter, Arc File, and Unique ID from the location, and the xml_ID of the item in that location, print it in a single string in the json.
# Example would be M92F in 2-1 H&5 MP5 Briefcase would output as....
#[
#    {
#      "c21_storage", "s118.arc", "118_282_3", 258
#    }
#]
# 
#        
#    def generate_output(self, output_directory: str):
#        data = self.client_data()
#        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.json"
#       with open(os.path.join(output_directory, filename), 'wb') as f:
#           f.write(json.dumps(data))   

#def client_data(self):
#    return {
#        "chapter": location_table(self.chapter)
#        "arc_file": location_table(self.arc_file)
#        "unique_id": location_table(self.unique_id)
#        "xml_id": item_table(self.xml_id)
#     }
#
#def generate_output(self, output_directory: str):
#  # pull the data from our dict
#    data = self.client_data()
#  # create the json file named after the player slot
#    filename = f"{self.multiworld.get_out_file_name_base(self.player)}.json"
#    with open(os.path.join(output_directory, filename), 'wb') as f:
#  # put all that sweet sweet data into the file and save it please
#        f.write(bytes(json.dumps(data)))

def client_data(self):
    # Find the corresponding location and item from the tables
    location = next((loc for loc in location_table if loc['name'] == self.chapter), None)
    item = next((itm for itm in item_table if itm['name'] == self.xml_id), None)

    if location and item:
        return {
            "chapter": location['chapter'],
            "arc_file": location['arc_file'],
            "unique_id": location['unique_id'],
            "xml_id": item['xml_id'],
        }
    else:
        return {}  # In case the location or item isn't found, just break out of it.

def generate_output(self, output_directory: str):
    data = self.client_data()

    if data:  # Assuming we actually have the data, then print to json based after player slot
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.json"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f, indent=4)
        
class Re5Item(Item):
    game: str = "Resident Evil 5"
    
class Re5Location(Location):
    game: str = "Resident Evil 5"
