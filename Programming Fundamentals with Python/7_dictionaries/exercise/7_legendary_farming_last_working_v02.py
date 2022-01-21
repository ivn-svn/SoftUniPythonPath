# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However,
# it's a tedious process, and it requires quite a bit of farming. The possible items are:
#     • "Shadowmourne" - requires 250 Shards
#     • "Valanyr" - requires 250 Fragments
#     • "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that
# the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_ fragments}
# motes: {number_of_ motes}"
# Finally, print the collected junk items in the order of appearance.
#
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
# shards: 5
# fragments: 5
# motes: 3
# stones: 5
# leathers: 6

import string

user_input = input().lower()
user_input = user_input.split(' ')
resvalues = [int(z) for z in user_input if user_input.index(z) % 2 == 0]
resitself = [y for y in user_input if user_input.index(y) % 2 == 1]
#
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'}
junk = {}
winermaterial = ''
resources = {'shards': 0, 'fragments': 0, 'motes': 0}
for x in range(0, len(resvalues)):
    if resitself[x] in resources:
        resources[resitself[x]] += int(resvalues[x])
    elif resitself[x] not in resources:
        if resitself[x] not in junk:
            junk[resitself[x]] = int(resvalues[x])
        else:
            junk[resitself[x]] += int(resvalues[x])

for (keys, values) in resources.items():
    if values >= 250:
        winermaterial = keys
        item_obt = string.capwords(legendary_items[keys])
        print(f"{item_obt} obtained!")
for (keys, values) in resources.items():
    if legendary_items[keys] != item_obt.lower():
        print(f"{keys}: {values}")
    else:
        winermaterialint = (int(resources[winermaterial]) - 250)
        print(f"{winermaterial}: {winermaterialint}")
for (keys, values) in junk.items():
    print(f"{keys}: {values}")
