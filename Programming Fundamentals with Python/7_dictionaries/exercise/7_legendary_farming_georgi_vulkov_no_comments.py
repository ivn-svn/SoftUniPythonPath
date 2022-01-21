from collections import OrderedDict


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
    args = input().lower().split()

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

for k, v in key_materials.items():  # k - key, v - value
    print(f'{k}: {v}')


for k, v in junks.items():  # k - key, v - value
    print(f'{k}: {v}')