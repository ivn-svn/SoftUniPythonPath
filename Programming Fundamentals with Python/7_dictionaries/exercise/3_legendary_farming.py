# The possible items are:
# Shadowmourne – requires 250 Shards;
# Valanyr – requires 250 Fragments;
# Dragonwrath – requires 250 Motes;
# Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input,
# in the format:
# 2 motes 3 ores 15 stones
# Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to
# print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered
# by quantity in descending order, then by name in ascending order,
# each on a new line. Finally, print the collected junk
# items in alphabetical order.
# Input
# Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
# Output
# On the first line, print the obtained item in the format: {Legendary item} obtained!
# On the next three lines, print the remaining key materials in descending order by quantity
# If two key materials have the same quantity, print them in alphabetical order
# On the final several lines, print the junk items in alphabetical order
# All materials are printed in format {material}: {quantity}
# The output should be lowercase, except for the first letter of the legendary
legendary_items = {"Shards": "Shadowmourne", "Fragments": "Valanyr", "Motes": "Dragonwrath"}
#
junk = {} # Something to use as soon as I solve the other issues with задачата on lne 48
#
#
true_check = True # Truth checker to let the loop run till the wheels fall off
#
material_gathered = {} # dict variable to hold all gathered with the material_func()

# function to check gathered material
def material_func(a, b): # the most computational power intensive function in  the assignment!
    if a not in material_gathered:
        material_gathered[a] = b
    elif a in material_gathered:
        material_gathered[a] += b
    return material_gathered
#
data_input = input().split(" ")
while true_check ==  True:
    #
    material = [data_input[z] for z in range(len(data_input)) if z % 2 == 1]
    quantity = [data_input[j] for j in range(len(data_input)) if j % 2 == 0]
    for m in material: # for cycle to roam through the list of "material"/materials and list of "qunatity"/quantities
        # from below /\ | In "" you are seeing the variable names.
        for q in quantity:
            q = int(q)
            material_func(m, q)
    #
    for (key, value) in material_gathered.items() and legendary_items.items():
        if material_gathered[key] == legendary_items[value] and material_gathered[value] >= 250:
            print(f"{legendary_items[key]} obtained!")
            true_check = False
                #break
        else:
            junk[key] = value
            continue
        print(f"{material}: {quantity}")
        # {quantity} {material}

