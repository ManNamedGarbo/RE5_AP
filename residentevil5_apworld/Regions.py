from typing import Dict

class Chapters:
    Menu = "Menu"
    # Chapter 1-1
    c11_checkpoint = "1-1 Civilian Checkpoint"            #s100.arc
    c11_alley1 = "1-1 Back Alley First Half"              #s115.arc
    c11_alley2 = "1-1 Back Alley Second Half"             #s116.arc
    c11_assembly = "1-1 Public Assembly"                  #s114.arc
    # Chapter 1-2
    c12_assembly = "1-2 Public Assembly"                  #s114.arc
    c12_urban = "1-2 Urban District"                      #s102.arc
    c12_abandoned = "1-2 Abandoned Building"              #s117.arc
    c12_furnace = "1-2 Furnace Facility"                  #s103.arc
    # Chapter 2-1
    c21_storage = "2-1 Storage Facility"                  #s118.arc
    c21_bridge = "2-1 The Bridge"                         #s104.arc
    c21_port = "2-1 The Port"                             #s113.arc
    c21_shanty = "2-1 Shanty Town"                        #s105.arc
    c21_train = "2-1 Train Yard"                          #s106.arc
    # Chapter 2-2
    c22_station = "2-2 Train Station"                     #s119.arc
    c22_mines = "2-2 The Mines"                           #s107.arc
    c22_popokarimu = "2-2 Mining Area"                    #s108.arc
    # Chapter 2-3
    c23_car = "2-3 Savanna"                               #s109.arc, no items
    c23_ndesu = "2-3 Night Port"                          #s111.arc, no items
    # Chapter 3-1
    c31_marsh = "3-1 Marshlands"                          #s200.arc
    c31_village = "3-1 Village"                           #s202.arc
    # Chapter 3-2
    c32_exegrounds = "3-2 Execution Ground"               #s201.arc
    c32_refinery = "3-2 Oil Field Refinery"               #s207.arc
    c32_control = "3-2 Oil Field Control Facility"        #s203.arc
    c32_docks = "3-2 Oil Field Dock"                      #s209.arc
    # Chapter 3-3
    c33_oilboat = "3-3 Oil Field - Drilling Facilities"   #s204.arc
    c33_irving = "3-3 Irving's Patrol Boat"               #s205.arc, no items
    # Chapter 4-1
    c41_caves = "4-1 Caves"                               #s313.arc
    c41_ancient = "4-1 Ancient Village"                   #s300.arc
    c41_labyrinth = "4-1 Labyrinth"                       #s301.arc
    # Chapter 4-2
    c42_worship = "4-2 Worship Area"                      #s302.arc
    c42_pyramid = "4-2 Pyramid"                           #s303.arc
    c42_garden = "4-2 Underground Garden"                 #s312.arc
    # Chapter 5-1
    c51_garden = "5-1 Underground Garden"                 #s312.arc
    c51_progenitor = "5-1 Progenitor Virus House"         #s305.arc
    c51_u8 = "5-1 Experimental Facility U-8"              #s304.arc
    # Chapter 5-2
    c52_experiment = "5-2 Experimental Facility"          #s304.arc
    c52_power = "5-2 Power Station"                       #s310.arc
    c52_facpassage = "5-2 Experimental Facility Passage"  #s316.arc
    c52_missile1 = "5-2 Missile Area 1st Floor"           #s307.arc
    c52_mkono = "5-2 Uroboros Research Facility"          #s308.arc
    # Chapter 5-3
    c53_uroboros = "5-3 Uroboros Research Facility"       #s308.arc
    c53_missile2 = "5-3 Missile Area 2nd Floor"           #s314.arc
    c53_platform = "5-3 Moving Platform"                  #s315.arc
    c53_monarch = "5-3 Monarch Room Entrance"             #s311.arc
    c53_jill = "5-3 Monarch Room Jill & Wesker"           #s309.arc
    # Chapter 6-1
    c61_deck = "6-1 Ship Deck"                            #s500.arc
    c61_hold = "6-1 Ship Hold"                            #s501.arc
    # Chapter 6-2
    c62_deck = "6-2 Main Deck"                            #s503.arc
    c62_bridge = "6-2 Bridge"                             #s504.arc
    c62_aheri = "6-2 Bridge Deck"                         #s511.arc
    # Chapter 6-3
    c63_aheri  = "6-3 Bridge Deck"                        #s511.arc
    c63_bridge = "6-3 Bridge Interior"                    #s512.arc
    c63_engine = "6-3 Engine Room"                        #s505.arc
    c63_hangar = "6-3 Hangar"                             #s506.arc
    c63_volcano = "6-3 Volcano"                           #s508.arc

# I'm sorry for the crimes against python I must commit.  
region_exits: Dict[str, str] = {
    Chapters.Menu: [Chapters.c11_checkpoint,
                    Chapters.c12_assembly,
                    Chapters.c21_storage,
                    Chapters.c22_station,
                    Chapters.c23_car,
                    Chapters.c31_marsh,
                    Chapters.c32_exegrounds,
                    Chapters.c33_oilboat,
                    Chapters.c41_caves,
                    Chapters.c42_worship,
                    Chapters.c51_garden,
                    Chapters.c52_experiment,
                    Chapters.c53_uroboros,
                    Chapters.c61_deck,
                    Chapters.c62_deck,
                    Chapters.c63_aheri],
    Chapters.c11_checkpoint: [Chapters.c11_alley1],
    Chapters.c11_alley1: [Chapters.c11_alley2],
    Chapters.c11_alley2: [Chapters.c11_assembly],
    Chapters.c11_assembly: [Chapters.Menu,
                            Chapters.c12_assembly],
    Chapters.c12_assembly: [Chapters.c12_urban],
    Chapters.c12_urban: [Chapters.c12_abandoned],
    Chapters.c12_abandoned: [Chapters.c12_furnace],
    Chapters.c12_furnace: [Chapters.Menu,
                           Chapters.c21_storage],
    Chapters.c21_storage: [Chapters.c21_bridge],
    Chapters.c21_bridge: [Chapters.c21_port],
    Chapters.c21_port: [Chapters.c21_shanty],
    Chapters.c21_shanty: [Chapters.c21_train],
    Chapters.c21_train: [Chapters.Menu,
                         Chapters.c22_station],
    Chapters.c22_station: [Chapters.c22_mines],
    Chapters.c22_mines: [Chapters.c22_popokarimu],
    Chapters.c22_popokarimu: [Chapters.Menu,
                              Chapters.c23_car],
    Chapters.c23_car: [Chapters.c23_ndesu],
    Chapters.c23_ndesu: [Chapters.Menu,
                         Chapters.c31_marsh],
    Chapters.c31_marsh: [Chapters.c31_village],
    Chapters.c31_village: [Chapters.Menu,
                           Chapters.c32_exegrounds],
    Chapters.c32_exegrounds: [Chapters.c32_refinery],
    Chapters.c32_refinery: [Chapters.c32_control],
    Chapters.c32_control: [Chapters.c32_docks],
    Chapters.c32_docks: [Chapters.Menu,
                         Chapters.c33_oilboat],
    Chapters.c33_oilboat: [Chapters.c33_irving],
    Chapters.c33_irving: [Chapters.Menu,
                          Chapters.c41_caves],
    Chapters.c41_caves: [Chapters.c41_ancient],
    Chapters.c41_ancient: [Chapters.c41_labyrinth],
    Chapters.c41_labyrinth: [Chapters.Menu],
    Chapters.c42_worship: [Chapters.c42_pyramid],
    Chapters.c42_pyramid: [Chapters.c42_garden],
    Chapters.c42_garden: [Chapters.Menu,
                          Chapters.c51_garden],
    Chapters.c51_garden: [Chapters.c51_progenitor],
    Chapters.c51_progenitor: [Chapters.c51_u8],
    Chapters.c51_u8: [Chapters.Menu,
                      Chapters.c52_experiment],
    Chapters.c52_experiment: [Chapters.c52_power],
    Chapters.c52_power: [Chapters.c52_facpassage],
    Chapters.c52_facpassage: [Chapters.c52_missile1],
    Chapters.c52_missile1: [Chapters.c52_mkono],
    Chapters.c52_mkono: [Chapters.Menu,
                         Chapters.c53_uroboros],
    Chapters.c53_uroboros: [Chapters.c53_missile2],
    Chapters.c53_missile2: [Chapters.c53_platform],
    Chapters.c53_platform: [Chapters.c53_monarch],
    Chapters.c53_monarch: [Chapters.c53_jill],
    Chapters.c53_jill: [Chapters.Menu,
                        Chapters.c61_deck],
    Chapters.c61_deck: [Chapters.c61_hold],
    Chapters.c61_hold: [Chapters.Menu,
                        Chapters.c62_deck],
    Chapters.c62_deck: [Chapters.c62_bridge],
    Chapters.c62_bridge: [Chapters.c62_aheri],
    Chapters.c62_aheri: [Chapters.Menu,
                         Chapters.c63_aheri],
    Chapters.c63_aheri: [Chapters.c63_bridge],
    Chapters.c63_bridge: [Chapters.c63_engine],
    Chapters.c63_engine: [Chapters.c63_hangar],
    Chapters.c63_hangar: [Chapters.c63_volcano],
    Chapters.c63_volcano: [Chapters.Menu]
}