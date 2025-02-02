import random

from BaseClasses import Item, ItemClassification
from .Types import ItemData, Re5Item, ChapterType, chapter_type_to_name, chapter_type_to_shortened_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Re5World

def create_itempool(world: "Re5World") -> List[Item]:
    itempool: List[Item] = []

    # Create all chapters except for the starting chapter as items, this will be used in the future for when starting with all chapters is an option.
    starting_chapter = (chapter_type_to_name[ChapterType(world.options.StartingChapter)])

    for chapter in re5_chapters.keys():
        if starting_chapter == "All":
            break
        if starting_chapter == chapter:
            continue
        itempool.append(create_item(world, chapter))

    for name in item_table.keys():
        item_type: ItemClassification = item_table.get(name).classification
        item_amount: int = item_table.get(name).count
    
        itempool += create_multiple_items(world, name, item_amount, item_type)

    victory = create_item(world, "Victory")
    world.multiworld.get_location("Complete Chapter 6-3", world.player).place_locked_item(victory)

    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - len(event_item_pairs) - 1)
    return itempool

def create_item(world: "Re5World", name: str) -> Item:
    data = item_table[name]
    return Re5Item(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "Re5World", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [Re5Item(name, item_type, data.ap_code, world.player)]

    return itemlist

def create_junk_items(world: "Re5World", count: int) -> List[Item]:
    trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    trap_list: Dict[str, int] = {}

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

        elif trap_chance > 0 and ic == ItemClassification.trap:
            if name == "Discard Random Slot Trap":
                trap_list[name] = world.options.DiscardTrapWeight.value
            elif name == "Siphon Gold Trap":
                trap_list[name] = world.options.SiphonTrapWeight.value

    for i in range(count):
        if trap_chance > 0 and world.random.randint(1,100) <= trap_chance:
            junk_pool.append(world.create_item(
                world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        else:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

re5_items = {
    # Weapons
    "AK-74": ItemData(34769900, ItemClassification.progression, 1),
    "Benelli M3": ItemData(34769900, ItemClassification.progression, 1),
    "Beretta M92F": ItemData(34769900, ItemClassification.progression, 1),
    "H&K MP5": ItemData(34769900, ItemClassification.progression, 1),
    "H&K P8": ItemData(34769900, ItemClassification.progression, 1),
    "H&K PSG-1": ItemData(34769900, ItemClassification.progression, 1),
    "Hydra": ItemData(34769900, ItemClassification.progression, 1),
    "Ithaca 37": ItemData(34769900, ItemClassification.progression, 1),
    "Jailbreaker": ItemData(34769900, ItemClassification.progression, 1),
    "L Hawk": ItemData(34769900, ItemClassification.progression, 1),
    "Longbow": ItemData(34769900, ItemClassification.progression, 1),
    "M40 GL": ItemData(34769900, ItemClassification.progression, 1),
    "M93R": ItemData(34769900, ItemClassification.progression, 1),
    "Minigun": ItemData(34769900, ItemClassification.progression, 1),
    "S&W M29": ItemData(34769900, ItemClassification.progression, 1),
    "S&W M500": ItemData(34769900, ItemClassification.progression, 1),
    "S75": ItemData(34769900, ItemClassification.progression, 1),
    "SIG 556": ItemData(34769900, ItemClassification.progression, 1),
    "SVD Dragunov": ItemData(34769900, ItemClassification.progression, 1),
    "VZ61": ItemData(34769900, ItemClassification.progression, 1),
    
    # Key Items
    "Beast Slate": ItemData(34765401, ItemClassification.progression, 1),
    "Bridge Keycard": ItemData(34765402, ItemClassification.progression, 1),
    "Crane Keycard": ItemData(34765403, ItemClassification.progression, 1),
    "Earth Emblem": ItemData(34765404, ItemClassification.progression, 1),
    "Furnace Key": ItemData(34765405, ItemClassification.progression, 1),
    "Guard's Key": ItemData(34765406, ItemClassification.progression, 1),
    "Hangar Keycard A": ItemData(34765407, ItemClassification.progression, 1),
    "Hangar Keycard B": ItemData(34765408, ItemClassification.progression, 1),
    "Old Building Key": ItemData(34769409, ItemClassification.progression, 1),
    "Port Key": ItemData(34769410, ItemClassification.progression, 1),
    "Raptor Slate": ItemData(34769420, ItemClassification.progression, 1),
    "Sea Emblem": ItemData(34769430, ItemClassification.progression, 1),
    "Shaman Slate": ItemData(34769440, ItemClassification.progression, 1),
    "Sky Emblem": ItemData(34769450, ItemClassification.progression, 1),
    "Tanker Keycard A": ItemData(34769460, ItemClassification.progression, 1),
    "Tanker Keycard B": ItemData(34769470, ItemClassification.progression, 1),
    "Warrior Slate": ItemData(34769480, ItemClassification.progression, 1),

#   # Treasures
#     "treasure item haha": ItemData(10020015, ItemClassification.progression, 7),
#
#   # Victory
#    "Victory": ItemData(6942042, ItemClassification.progression, 0)
}

re5_chapters = {
    "Chapter 1-1": ItemData(14450021, ItemClassification.progression, 0),
    "Chapter 1-2": ItemData(14450022, ItemClassification.progression, 0),
    "Chapter 2-1": ItemData(14450023, ItemClassification.progression, 0),
    "Chapter 2-2": ItemData(14450025, ItemClassification.progression, 0),
    "Chapter 2-3": ItemData(14450026, ItemClassification.progression, 0),
    "Chapter 3-1": ItemData(14450027, ItemClassification.progression, 0),
    "Chapter 3-2": ItemData(14450028, ItemClassification.progression, 0),
    "Chapter 3-3": ItemData(14450029, ItemClassification.progression, 0),
    "Chapter 4-1": ItemData(14450030, ItemClassification.progression, 0),
    "Chapter 4-2": ItemData(14450031, ItemClassification.progression, 0),
    "Chapter 5-1": ItemData(14450032, ItemClassification.progression, 0),
    "Chapter 5-2": ItemData(14450033, ItemClassification.progression, 0),
    "Chapter 5-3": ItemData(14450034, ItemClassification.progression, 0),
    "Chapter 6-1": ItemData(14450035, ItemClassification.progression, 0),
    "Chapter 6-2": ItemData(14450036, ItemClassification.progression, 0),
    "Chapter 6-3": ItemData(14450037, ItemClassification.progression, 0),
}

junk_items = {
#    # Junk
    "Handgun Ammo (10)": ItemData(19090711, ItemClassification.filler, 0),
#
#    # Traps
#    "Discard Random Slot Trap": ItemData(10250726, ItemClassification.trap, 0),
#    "Siphon Gold Trap": ItemData(10250727, ItemClassification.trap, 0),
}

#junk_weights = {
#    "Charm": 40,
#    "1-Up": 20
#}

item_table = {
    **re5_items,
    **re5_chapters,
    **junk_items
}

#event_item_pairs: Dict[str, str] = {
#    "Beat Raleigh": "Beat Raleigh",
#    "Beat Muggshot": "Beat Muggshot",
#    "Beat Mz. Ruby": "Beat Mz. Ruby",
#    "Beat Panda King": "Beat Panda King"
#}