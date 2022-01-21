# Theme: Exercise Dictionaries: Legendary Farming

# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However,
# it's a tedious process, and it requires quite a bit of farming. The possible items are:
#     • "Shadowmourne" - requires 250 Shards
#     • "Valanyr" - requires 250 Fragments
#     • "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials  (case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that
# the corresponding legendary item is obtained.

# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_ fragments}
# motes: {number_of_ motes}"

# Finally, print the collected junk items in the order of appearance.
# ....................................................................
# Input
#     • Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2}" \
#                                                " … {quantityN} {materialN}"
# Output
#     • On the first line, print the obtained item in the format: "{Legendary item} obtained!"
#     • On the next three lines, print the remaining key materials
#     • On the several final lines, print the junk items
#     • All materials should be printed in the format: "{material}: {quantity}"
#     • The output should be lowercase, except for the first letter of the legendary
# Example Input:
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards
#
# _______________________________
# Example Output
# Valanyr obtained!
# shards: 5  # or 12 ???????????????????????????????????????????????????????????????????????????????
# fragments: 5
# motes: 3
# stones: 5
# leathers: 6

# # #
# Theme_2.25 Exercise Dictionaries: 03. Legendary Farming
from collections import OrderedDict


def print_dict(dictionary, template):
    # prints the dictionary keys & values in specific format !
    for k, v in dictionary.items():  # k - key, v - value
        print(template.format(k, v))


key_materials_1 = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
key_materials = OrderedDict(key_materials_1)


legendary_items = {
    'fragments': 'Valanyr',
    'shards': 'Shadowmourne',
    'motes': 'Dragonwrath'
}

junks = OrderedDict()
win_material = ''
while win_material == '':
    args = input().lower().split()  # converts to lower case letters
    # args = '3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards'.lower().split()
    # args = '123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver'.lower().split()

    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                win_material = material  # The win_material is NOT the winner !
                break
        else:  # junk dictionary
            junks.setdefault(material, 0)  # sets the key values = 0 by default
            junks[material] += quantity

key_materials[win_material] -= 250
print(f'{legendary_items[win_material]} obtained!')

# key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))  # sorted acc. to the problem
# print_dict(key_materials, "{}: {}")  # calls function print_dict(...)
for k, v in key_materials.items():  # k - key, v - value
    print(f'{k}: {v}')

# junks = dict(sorted(junks.items()))
# print_dict(junks, "{}: {}")  # calls function print_dict(...)
for k, v in junks.items():  # k - key, v - value
    print(f'{k}: {v}')
