n = int(input())
# Two dicts: 1 for rarity integers, 2nd with list value to store the ratings and iterate over them later on.
plant_rarity_dict = {}
plant_ratings_dict = {}
# =======> FUNCTIONS:
# TODO: Make print out function.


def calc_avg_ratings(pl_rat_d):
    for key in pl_rat_d.keys():
        avg = 0
        for idx in range(0, len(pl_rat_d[key])):
            avg += int(pl_rat_d[key][idx])
        avg = avg // len(pl_rat_d[key])
        pl_rat_d[key].clear()
        pl_rat_d[key] = f"{avg:.2f}"
    return pl_rat_d

# def validate_plant(plnt, pl_dict):
#     if plnt in pl_dict.keys():
#         return True
#     else:
#         return False


def do_what(com, pl_rat_d, pl_rar_d):
    rate = "Rate: "
    update = "Update: "
    reset = "Reset: "
    #
    if rate in com:  # add the given rating to the plant (store all ratings)
        com = com.strip(rate)
        pl = com.split(" - ")[0]
        rating = int(com.split(" - ")[1])
        if pl in pl_rar_d.keys():
            if pl in pl_rat_d.keys():
                pl_rat_d[pl].append(rating)
            else:
                pl_rat_d[pl] = list()
                pl_rat_d[pl].append(rating)
        else:
            print("error")
    elif update in com: #  update the rarity of the plant with the new one
        com = com.strip(update)
        pl = com.split(" - ")[0]
        rar = int(com.split(" - ")[1])
        if pl in pl_rar_d.keys():
            pl_rar_d[pl] = rar
        else:
            print("error")
    elif reset in com:   # remove all the ratings of the given plant
        com = com.strip(reset)
        pl = com
        if pl in pl_rar_d.keys():
            pl_rat_d[pl].clear()
            pl_rat_d[pl] = 0
        else:
            print("error")

#
    return pl_rat_d, pl_rar_d



    # =======> FOR CYCLE:
for i in range(0, n):
    plant_rarity = input()
    plant = plant_rarity.split('<->')[0]
    rarity = plant_rarity.split('<->')[1]
    plant_rarity_dict[plant] = int(rarity) # if I receive plant > 1 I have to update the rarity.
    # Hence, assignm. op is ok.

# =======> WHILE LOOP:

command = ''
while command != "Exhibition":
    if command == "Exhibition":
        break
    else:
        command = input()
        plant_ratings_dict, plant_rarity_dict = do_what(command, plant_ratings_dict, plant_rarity_dict)

plant_ratings_dict = calc_avg_ratings(plant_ratings_dict)
print(f"{plant_ratings_dict}, \n {plant_rarity_dict}")
