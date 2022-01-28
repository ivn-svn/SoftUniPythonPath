n = int(input())
# Two dicts: 1 for rarity integers, 2nd with list value to store the ratings and iterate over them later on.
plant_rarity_dict = {}
# =======> FUNCTIONS:


def plant_raings_func(pl_rar_d):
    pass

# TODO: Implement the missing functionality for //  pl_rat_d, pl_rar_d:

def do_what(com, pl_rat_d, pl_rar_d):
    rate = "Rate: "
    update = "Update: "
    reset = "Reset: "
    rating = 0
    if rate in com:
        com = com.strip(rate)
        plant = com.split(" - ")[0]
        rating = com.split(" - ")[1]
        return plant, rating
    elif update in com:
        com = com.strip(update)
        plant = com.split(" - ")[0]
        rarity = com.split(" - ")[1]
        return plant, rarity
    elif reset in com:
        com = com.strip(reset)
        plant = com
        return plant




    # =======> FOR CYCLE:
for i in range(0, n):
    plant_rarity = input()
    plant = plant_rarity.split('-')[0]
    rarity = plant_rarity.split('-')[1]
    plant_rarity_dict[plant] = int(rarity) # if I receive plant > 1 I have to update the rarity.
    # Hence, assignm. op is ok.

command = input()
do_what(command)
plant_ratings_dict = plant_raings_func(plant_rarity_dict)
plant, action = do_what(command, plant_ratings_dict, plant_rarity_dict)