data_input = input().split(" ")
material_gathered = {}
material_dict = {data_input[i + 1]: int(data_input[i]) for i in range(0, len(data_input), 2)}
legendary_items = {"Shards": "Shadowmourne", "Fragments": "Valanyr", "Motes": "Dragonwrath"}
junk = {}
item_obtained = False

def material_func(a, b):
    if a not in material_gathered:
        material_gathered[a] = b
    elif a in material_gathered:
        material_gathered[a] += b
    return material_gathered


def junk_func(a, b):
    if a not in junk:
        junk[a] = b
    elif a in junk:
        junk[a] += b
    return junk


while item_obtained == False:
    for (key,
         value) in material_dict.items():
        material_func(key, value)
        calc_value = int(material_gathered[key])
        if calc_value >= 250:
            for (key, value) in material_gathered.items():
                if value >= 250:
                    item_obtained = True
                    print(f"{key} obtained!")
        else:
            junk_func(key, value)

