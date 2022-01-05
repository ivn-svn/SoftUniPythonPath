# Legendary Farming
# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. 
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# 	•	"Shadowmourne" - requires 250 Shards
# 	•	"Valanyr" - requires 250 Fragments
# 	•	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk. 
# You will be given lines of input in the format: 
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, 
# you have to print that the corresponding legendary item is obtained. 
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_ fragments}
# motes: {number_of_ motes}"
# Finally, print the collected junk items in the order of appearance.
user_input = input()
number_of_shards = 0
number_of_fragments = 0
number_of_motes = 0 
junk_items = {}
#
legendary_items = {"shadowmourne": [0, "shards"], "valanyr": [0, "fragments"], "dragonwrath": [0, "motes"]}

def item_collector(leg_i, j_i, us_in):
    us_in = us_in.split(" ")

    for i in range(0, len(us_in)):
        if us_in[i] in leg_i:
            if i % 2 == 1:
                leg_i[us_in[i]] += int(us_in[i]) 
        else:
            if i % 2 == 0 and us_in[i] not in j_i:
                j_i[us_in[i]] = 0
            elif i % 2 == 1 and us_in[i - 1] in j_i:    
                j_i[us_in[i]] += int(us_in[i])          
    return leg_i, j_i, us_in


race_finish = False
material = 0
while material < 250 and race_finish == False:
    
    legendary_items, junk_items, user_input = item_collector(legendary_items, junk_items, user_input)
    for (keys, values) in legendary_items:
        material = values[1] 
        if material >= 250:
            race_finish = True
            break
else:
    print(f"{legendary_items} obtained.")
    print(f"shards: {number_of_shards}")
    print(f"fragments: {number_of_fragments}")
    print(f"motes: {number_of_motes}")
    print(f"{junk_items}")