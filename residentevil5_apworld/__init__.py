import random, json, os
from typing import List, Dict, Any, TYPE_CHECKING, TypedDict, Set
from BaseClasses import MultiWorld, Region, Location, Item, Tutorial, ItemClassification, CollectionState
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import PerGameCommonOptions, World, WebWorld
from dataclasses import dataclass

import Options
from Options import Choice, OptionGroup, Toggle, OptionSet, Range
from enum import Enum
from .Items import RE5Type, item_table, group_table, base_id
from .Locations import LocationDict, EventDict, location_table, base_id, event_table
from .Regions import Chapters, region_exits
from .Options import create_option_groups, RE5Options, RE5_option_groups, slot_data_options
from .Rules import set_rules, set_chapter_rules

class RE5Web(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Resident Evil 5 Randomizer and connecting to an Archipelago Multiworld. ",
        "English",
        "setup_en.md",
        "setup/en",
        ["Garbo"]
    )]

class RE5World(World):
    """Resident Evil 5 is a survival horror game packed with hordes of fast-moving, quick-thinking enemies that represent a whole new breed of unimaginable undead evil."""

    game = "Resident Evil 5"
    web = RE5Web()

    item_name_to_id = {item["name"]: (base_id + index) for index, item in enumerate(item_table)}
    item_name_to_type = {item["name"]: item["type"] for item in item_table}
    location_name_to_id = {loc["name"]: (base_id + index) for index, loc in enumerate(location_table)}

    item_name_groups = group_table
    options_dataclass = RE5Options
    options: RE5Options

    def __init__(self, multiworld: MultiWorld, player: int):
        super(RE5World, self).__init__(multiworld, player)

        self.item_classification: Dict[RE5Type, ItemClassification] = {
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
        set_rules(self, self.options.ExcludeDriving.value)

    def create_item(self, name: str) -> "Re5Item":
        item_id: int = self.item_name_to_id[name]
        item_type: RE5Type = self.item_name_to_type[name]
        classification = self.get_item_classification(item_type)

        return Re5Item(name, classification, item_id, self.player)
        
    def get_item_classification(self, item_type: RE5Type) -> ItemClassification:
        classification = ItemClassification.filler
        if item_type in self.item_classification.keys():
            classification = self.item_classification[item_type]

        return classification
        
    def create_event(self, event: str) -> "Re5Item":
        return Re5Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        item = self.random.choice(item_table)

        while self.get_item_classification(item["type"]) == ItemClassification.progression:
            item = self.random.choice(item_table)

        return item["name"]
       
    def create_items(self):
        options = self.options
        itempool = []
        for item in item_table:
            itempool.append(self.create_item(item["name"]))
            if item["name"] == "Chapter 2-3" and options.ExcludeDriving.value == 0:
                itempool.remove(self.create_item(item["name"]))

            else:
                continue



        self.multiworld.itempool += itempool

    def create_junk_items(world: "RE5World", count: int) -> List[Item]:
        trap_chance = world.options.TrapChance.value
        junk_pool: List[Item] = []
        junk_list: Dict[str, int] = {}
        trap_list: Dict[str, int] = {}
        ic: RE5Type

        for item in item_table:
            name = item["name"]
            ic = item["type"]
            print(ic)
            if ic == RE5Type.Filler:
                junk_list[name] = 100

            for i in range(count):
                junk_pool.append(world.create_item(
                    world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))
        return junk_pool


    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)

        for n in region_exits:
            multiworld.regions += [Region(n, player, multiworld)]

        menu.add_exits({"1-1 Civilian Checkpoint": "New Game"})

        for n in region_exits:
            self.get_region(n).add_exits(region_exits[n])

        for index, loc in enumerate(location_table):
            Chapters: Region = self.get_region(loc["chapter"])
            Chapters.add_locations({loc["name"]: base_id + index})

        for e in event_table:
            Chapters: Region = self.get_region(e["chapter"])
            event = Re5Location(player, e["name"], None, Chapters)
            event.show_in_spoiler = False
            event.place_locked_item(self.create_event(e["item"]))
            Chapters.locations += [event]

        multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
        
    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options
        
        slot_data: Dict[str, Any] = {
            "locations": {loc["unique_id"]: (base_id + index) for index, loc in enumerate(location_table)},
            "StartingChapter": int(options.StartingChapter.value),
            "IncludeTreasures": bool(options.IncludeTreasures.value),
            "ExcludeDriving": bool(options.ExcludeDriving.value),
            "TrapChance": options.TrapChance.value,
            "DiscardTrapWeight": options.DiscardTrapWeight.value,
            "SiphonTrapWeight": options.SiphonTrapWeight.value
        }

        return slot_data

def client_data(self):
    # Find the corresponding location and item from the tables
    location = next((loc for loc in location_table if loc['name'] == self.chapter), None)
    item = next((itm for itm in item_table if itm['name'] == self.xml_id), None)

    if location and item:
        return {
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
