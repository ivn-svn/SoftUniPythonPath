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
# The difference between 3_legendary_farming and 3_legendary_farming_v_1:
#
junk = {}
material_gathered = {}


def material_func(a, b):
    if a not in material_gathered:
        material_gathered[a] = b
    elif a in material_gathered:
        material_gathered[a] += b
    return material_gathered, a, b



def junk_func(a, b):
    if a not in junk:
        junk[a] = b
    elif a in junk:
        junk[a] += b
    return junk


data_input = input().split(" ")
material_dict = {data_input[i + 1]: data_input[i] for i in range(0, len(data_input), 2)}
while True:
    for (key,
         value) in material_dict.items():
        material_func(key, value)
        calc_value = int(material_gathered[key])
        if calc_value >= 250:
            print(f"{key} obtained!")
            break
        else:
            junk_func(key, value)
    #
