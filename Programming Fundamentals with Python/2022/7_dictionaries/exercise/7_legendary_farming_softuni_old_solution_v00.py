def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

key_materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0,

}
legendary_items = {
    "fragments": "Valanyr",
    "shards": "Shadowmourne",
    "motes": "Dragonwrath",

}

junks = {}
winner = ""
while winner == "":
    args = input().lower().split()
    for i in range(0, len(args), 2):
        quantity = int(args[i])
        material = args[i + 1]
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                winner = material
                break
        else:
            validate_key_existing(junks, material)
            junks[material] += quantity

key_materials[winner] -= 250
winner_item = legendary_items[winner]
print(f"{winner_item} obtained!")

key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junks = dict(sorted(junks.items()))

print_dict(key_materials, "{}: {}")
print_dict(junks, "{}: {}")