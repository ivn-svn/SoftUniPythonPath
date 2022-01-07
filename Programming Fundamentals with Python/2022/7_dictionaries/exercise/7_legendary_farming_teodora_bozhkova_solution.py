materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
KEY_MATERIAL_LIMIT = 250
is_obtained = False

while True:
    list_of_materials = input().lower().split()
    length = len(list_of_materials)

    for i in range(0, length, 2):
        material = list_of_materials[i + 1]
        quantity = int(list_of_materials[i])

        if material == "shards":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Shadowmourne obtained!")
                is_obtained = True
                break

        elif material == "fragments":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Valanyr obtained!")
                is_obtained = True
                break

        elif material == "motes":
            materials[material] += quantity

            if materials[material] >= KEY_MATERIAL_LIMIT:
                materials[material] -= KEY_MATERIAL_LIMIT
                print("Dragonwrath obtained!")
                is_obtained = True
                break

        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

    if is_obtained:
        break

sorted_key_materials = dict(materials.items())
for key, value in sorted_key_materials.items():
    print(f"{key}: {value}")

sorted_junk_materials = dict(junk.items())
for junk, value in sorted_junk_materials.items():
    print(f"{junk}: {value}")