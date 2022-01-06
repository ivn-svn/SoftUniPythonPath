def collect_material(key_materials_dict: dict , junk_materials: dict, material: str, qty: int):
    if material == 'shards' or material == "fragments" or material == "motes":
        key_materials_dict[material] += qty
    else:
        if material not in junk_materials.keys():
            junk_materials[material] = qty
        else:
            junk_materials[material] += qty
 
 
key_materials = {"shards": 0, "fragments": 0,"motes": 0}
junk = {}
item_obtained = ''
 
while item_obtained == '':
    current_line = input().split()
    for i in range(0,len(current_line),2):
        material_qty = int(current_line[i])
        material_name = current_line[i + 1].lower()
 
        collect_material(key_materials,junk,material_name,material_qty)
 
        if key_materials['shards']>= 250:
            item_obtained = 'Shadowmourne'
            key_materials['shards'] -= 250
            break
 
        elif key_materials['fragments']>= 250:
            item_obtained = 'Valanyr'
            key_materials['fragments'] -= 250
            break
 
        elif key_materials['motes']>= 250:
            item_obtained = 'Dragonwrath'
            key_materials['motes'] -= 250
            break
 
print(f"{item_obtained} obtained!")
for key_m,qty_m in key_materials.items():
    print(f"{key_m}: {qty_m}")
for key_j, qty_j in junk.items():
    print(f"{key_j}: {qty_j}")