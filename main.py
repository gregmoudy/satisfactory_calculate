import json

# ITEMS
ITEM_CABLE                  = "Cable"
ITEM_COPPER_INGOT           = "Copper Ingot"
ITEM_COPPER_ORE             = "Copper Ore"
ITEM_COPPER_SHEET           = "Copper Sheet"
ITEM_IRON_INGOT             = "Iron_Ingot"
ITEM_IRON_ORE               = "Iron Ore"
ITEM_IRON_PLATE             = "Iron Plate"
ITEM_IRON_ROD               = "Iron Rod"
ITEM_MODULAR_FRAME          = "Modular Frame"
ITEM_REINFORCED_IRON_PLATE  = "Reinforced Iron Plate"
ITEM_ROTOR                  = "Rotor"
ITEM_SCREW                  = "Screw"
ITEM_SMART_PLATING          = "Smart Plating"
ITEM_WIRE                   = "Wire"

# MACHINES
MACHINE_ASSEMBLER           = "Assembler"
MACHINE_CONSTRUCTOR         = "Constructor"
MACHINE_MINER_MK1           = "Miner Mk.1"
MACHINE_MINER_MK2           = "Miner Mk.2"
MACHINE_SMELTER             = "Smelter"

# LOOKUP KEYS
KEY_INPUT_ITEMS             = "Input Items"
KEY_MACHINE                 = "Machine"
KEY_OPM                     = "Output Per Minute"
KEY_RECIPES                 = "Recipes"

# Input item tuple is (<item_type>, <input_per_minute>)
LOOKUP = { 
    ITEM_CABLE : { 
        KEY_MACHINE : MACHINE_CONSTRUCTOR, 
        KEY_RECIPES : [ 
            { 
                KEY_OPM : 30, 
                KEY_INPUT_ITEMS : [ 
                    ( ITEM_WIRE, 60 ), 
                ], 
            }, 
        ], 
    },
    ITEM_COPPER_INGOT : { 
        KEY_MACHINE : MACHINE_SMELTER, 
        KEY_RECIPES : [ 
            { 
                KEY_OPM : 30, 
                KEY_INPUT_ITEMS : [ 
                    ( ITEM_COPPER_ORE, 30 ), 
                ], 
            }, 
        ], 
    },
    ITEM_COPPER_ORE : { 
        KEY_MACHINE : MACHINE_MINER_MK2, 
        KEY_RECIPES : [ 
            { 
                KEY_OPM : 120, 
                KEY_INPUT_ITEMS : [], 
            }, 
        ], 
    },
    ITEM_WIRE : { 
        KEY_MACHINE : MACHINE_CONSTRUCTOR, 
        KEY_RECIPES : [ 
            { 
                KEY_OPM : 30, 
                KEY_INPUT_ITEMS : [ 
                    ( ITEM_COPPER_INGOT, 15 ), 
                ], 
            }, 
        ], 
    },
}


ore_per_minute_needed = dict()
item_to_make = ITEM_CABLE

item_dict = LOOKUP.get(item_to_make)
print("Item: {0}".format(item_to_make))
print("\tRecipes:")
for recipe in item_dict[KEY_RECIPES]:
    print("\t\t{0}: {1}".format(KEY_OPM, recipe[KEY_OPM]))
    print("\t\tInput Items:")
    for item in recipe[KEY_INPUT_ITEMS]:
        print("\t\t\t{0}: {1}".format(item[0], item[1]))


# TODO:
# Input we will need from the user:
# What do you want to make?
# Miner Level?
# Ore Purity?
# Or
# Do we need all that, what if we just said "What do you want to make?" and then we calculate how much ore input it would need and 
# then generate a table that shows how much ore we can get out of combinations of different miner levels and ore purity levels.

# TODO:
# We will need to calculate remaining item waste when things don't break even. User might want to collect it, trash, or feed it to another production line.
