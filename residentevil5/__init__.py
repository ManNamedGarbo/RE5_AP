import random, json, os
from typing import List, Dict, Any, TYPE_CHECKING, TypedDict, Set
from BaseClasses import MultiWorld, Region, Location, Item, Tutorial, ItemClassification, CollectionState
from worlds.generic.Rules import set_rule
from worlds.AutoWorld import PerGameCommonOptions, World, WebWorld
from dataclasses import dataclass

import Options
from Options import Choice, OptionGroup, Toggle, OptionSet, Range
from enum import Enum
from .Items import RE5Type, item_table, group_table, ItemDict
from .Locations import LocationDict, EventDict, location_table, event_table
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

    item_name_to_id = {item["name"]: item["ap_id"] for item in item_table}
    item_name_to_type = {item["name"]: item["type"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["ap_id"] for loc in location_table}

    item_name_groups = group_table
    options_dataclass = RE5Options
    options: RE5Options

    def __init__(self, multiworld: MultiWorld, player: int):
        super(RE5World, self).__init__(multiworld, player)
        self.multiworld = multiworld
        self.player = player
        self.item_table: List[ItemDict] = item_table
        self.location_table: List[LocationDict] = location_table
        self.item_classification: Dict[RE5Type, ItemClassification] = {
            RE5Type.Chapter: ItemClassification.progression,
            RE5Type.Key: ItemClassification.progression,
            RE5Type.Explosive: ItemClassification.progression,
            RE5Type.Special: ItemClassification.progression_skip_balancing, # I don't want it to rely on special weapons like the Minigun and Longbow for progression, but they are here in case you do get them.
            RE5Type.Assault: ItemClassification.progression,
            RE5Type.Magnum: ItemClassification.progression,
            RE5Type.Handgun: ItemClassification.progression,
            RE5Type.SMG: ItemClassification.progression,
            RE5Type.Shotgun: ItemClassification.progression,
            RE5Type.Rifle: ItemClassification.progression,
            RE5Type.Treasure: ItemClassification.useful,
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

    def generate_early(self):
        if Options.StartingWeapon == 1:
            weapon = random.choice(list(self.multiworld.group_table["weapons"]))
            self.multiworld.early_items[self.player][weapon] = 1
        elif Options.StartingWeapon == 2:
            weapon = random.choice(list(self.multiworld.group_table["weapons"]))
            self.multiworld.local_early_items[self.player][weapon] = 1
        if Options.StartingWeapon == 3:
            weapon = random.choice(list(self.multiworld.group_table["pistol"]))
            self.multiworld.early_items[self.player][weapon] = 1
        elif Options.StartingWeapon == 4:
            weapon = random.choice(list(self.multiworld.group_table["pistol"]))
            self.multiworld.local_early_items[self.player][weapon] = 1

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


    def create_junk_items(self, count: int) -> List[Item]:
        junk_pool: List[Item] = []
        junk_list: Dict[str, int] = {}

        # Identify all filler items
        for item in self.item_table:
            name = item["name"]
            item_type = item["type"]
        
            # Check if the item is classified as filler (any of RE5Type.Filler, RE5Type.Healing, or RE5Type.Ammo)
            if item_type in [RE5Type.Filler, RE5Type.Healing, RE5Type.Ammo]:
                junk_list[name] = 100  # Assign weight of 100 for each filler item
    
        # Create exactly 'count' junk items
        for i in range(count):
            if junk_list:  # Make sure we have junk items to choose from
                chosen_item = self.random.choices(
                    list(junk_list.keys()), 
                    weights=list(junk_list.values()), 
                    k=1
                )[0]
                junk_pool.append(self.create_item(chosen_item))
    
        return junk_pool

       
    def create_items(self):
        options = self.options
        itempool = []
    
        # Create all your main items
        for item in item_table:
            # Skip Chapter 2-3 if driving is excluded
            if item["name"] == "Chapter 2-3" and options.ExcludeDriving.value == 0:
                continue
        
            itempool.append(self.create_item(item["name"]))
    
        # Add the items to the multiworld's itempool
        self.multiworld.itempool += itempool
    
        # Calculate how many locations need to be filled
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        current_items = len([item for item in self.multiworld.itempool if item.player == self.player])
    
        # If we need more items, create junk to fill the gap
        if total_locations > current_items:
            junk_needed = total_locations - current_items
            print(f"Adding {junk_needed} junk items to fill all locations")
        
            # Call create_junk_items to add junk items to the pool
            junk_items = self.create_junk_items(junk_needed)
        
            # Add junk items to the itempool
            self.multiworld.itempool += junk_items


    def create_regions(self):
        multiworld = self.multiworld
        player = self.player

        # Create the Menu region and add it to the multiworld
        menu = Region("Menu", player, multiworld)
        multiworld.regions.append(menu)

        # Add all other regions to multiworld
        for n in region_exits:
            multiworld.regions += [Region(n, player, multiworld)]

        # Add exits for the Menu region
        menu.add_exits({"1-1 Civilian Checkpoint": "New Game"})

        # Now, add exits to all other regions
        for n in region_exits:
            region = self.get_region(n)  # Make sure this returns a valid region
            if region:
                region.add_exits(region_exits[n])
            else:
                print(f"Warning: Region {n} not found!")

        # Add locations from location_table
        for loc in location_table:
            Chapter: Region = self.get_region(loc["chapter"])
            # Use the static ID directly from loc["ap_id"] instead of the dynamic ID calculation
            Chapter.add_locations({loc["name"]: loc["ap_id"]})

        # Add events from event_table
        for e in event_table:
            chapter_region = self.get_region(e["chapter"])
            if chapter_region:
                event = Re5Location(player, e["name"], None, chapter_region)
                event.show_in_spoiler = False
                event.place_locked_item(self.create_event(e["item"]))
                chapter_region.locations += [event]
            else:
                print(f"Warning: Event chapter {e['chapter']} not found!")

        # Set the completion condition
        multiworld.completion_condition[player] = lambda state: state.has("Victory", player)

        
    def fill_slot_data(self) -> Dict[str, Any]:
        options = self.options
        
        slot_data: Dict[str, Any] = {
            "locations": {loc["ap_id"]: loc["ap_id"] for loc in location_table},
            "StartingChapter": int(options.StartingChapter.value),
            "StartingWeapon": int(options.StartingWeapon.value),
            "IncludeTreasures": bool(options.IncludeTreasures.value),
            "ExcludeDriving": bool(options.ExcludeDriving.value),
            "TrapChance": options.TrapChance.value,
            "DiscardTrapWeight": options.DiscardTrapWeight.value,
            "SiphonTrapWeight": options.SiphonTrapWeight.value
        }

        return slot_data

    def get_xml_id(self, item_name):
        for item_entry in self.item_table:
            if item_entry.get("name") == item_name:
                return item_entry.get("xml_id", 1543)  # Default to 1543 if xml_id is not found
        return 1543  # Default if item not found in item_table


    def generate_output(self, output_directory):
        output_data = []

        # Assuming location_table is available and contains location data
        # Assuming item_table is available and contains item data
        for location in self.multiworld.get_filled_locations(self.player):
            if location.player != self.player:
                continue

            # If location has an item
            item = location.item
            if item:
                # Retrieve xml_id from the item_table (Items.py)
                item_xml_id = self.get_xml_id(item.name)

                # If the xml_id is negative or not found, set it to 1543
                if item_xml_id is None or item_xml_id < 0:
                    item_xml_id = 1543

                # Retrieve corresponding location data from location_table (Locations.py)
                location_data = next((loc for loc in self.location_table if loc['name'] == location.name), None)
                
                if location_data:
                    arc_file = location_data['arc_file']
                    ap_id = location_data['ap_id']
                else:
                    # Handle cases where location data is missing
                    print(f"Warning: No location data found for {location.name}")
                    continue

                # Append the data for this location and item pairing
                output_data.append({
                    "arc_file": arc_file,
                    "ap_id": ap_id,
                    "item_xml_id": item_xml_id  # Item xml_id (item_xml_id)
                })
            else:
                # If location has no item, log or handle it as necessary
                print(f"Warning: Location {location.name} is empty or unfilled.")

        # Output the data to a JSON file
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.json"
        json_file_path = os.path.join(output_directory, filename)

        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4)

        self.multiworld.output_path = json_file_path


class Re5Item(Item):
    game: str = "Resident Evil 5"
    
class Re5Location(Location):
    game: str = "Resident Evil 5"
