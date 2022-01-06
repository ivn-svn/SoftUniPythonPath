# Solution by Deyan Altanov
# Source: https://softuni.bg/forum/34892/legendary-farming

all_materials = input().split()
value = False

key_materials = {'motes': 0, 'shards': 0, 'fragments': 0}
junk = {}

while value is False:
    for i in range(0, len(all_materials), 2):
        quantity = int(all_materials[i])
        item = all_materials[i + 1].lower()
        if item in key_materials:
            key_materials[item] += quantity
            if item == 'motes':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Dragonwrath obtained!')
                    value = True
                    break
            elif item == 'fragments':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Valanyr obtained!')
                    value = True
                    break
            elif item == 'shards':
                if key_materials[item] >= 250:
                    key_materials[item] -= 250
                    print('Shadowmourne obtained!')
                    value = True
                    break
        else:
            if item in junk:
                junk[item] += int(all_materials[i])
            else:
                junk[item] = int(all_materials[i])
    if value is True:
        break
    all_materials = input().split()

ordered_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
ordered_junk = sorted(junk.items(), key=lambda x: x[0])

for material, quantity in ordered_key_materials:
    print(f"{material}: {quantity}")
for material, quantity in ordered_junk:
    print(f"{material}: {quantity}")