shadowmourne, valanyr, dragonwrath = "shadowmourne", "valanyr", "dragonwrath"
shards, fragments, motes = 'shards', 'fragments', 'motes'
legendary_item = ""
item_res_dict = {shards: shadowmourne, fragments: valanyr, motes: dragonwrath}
res_qty_dict = {shards: 0, fragments: 0, motes: 0}
key_res_list = [shards, fragments, motes]
junks_qty_dict = {}
item_obtained = False
line = input()
while not item_obtained:
    res_list = line.split(" ")
    for i in range(0, len(res_list), 2):
        amount = int(res_list[i])
        resource = res_list[i + 1]
        resource = resource.lower()
        if resource.lower() in key_res_list:
            if resource.lower() in res_qty_dict.keys():
                res_qty_dict[resource] += amount
                current_val = res_qty_dict[resource]
                if current_val >= 250:
                    legendary_item = item_res_dict[resource]
                    legendary_item = legendary_item.capitalize()
                    item_obtained = True
                    res_qty_dict[resource] = current_val - 250
                    break
            else:
                res_qty_dict[resource] = amount
                current_val = res_qty_dict[resource]
                if current_val >= 250:
                    legendary_item = item_res_dict[resource]
                    legendary_item = legendary_item.capitalize()
                    item_obtained = True
                    res_qty_dict[resource] = current_val - 250
                    break
        else:
            if resource.lower() in junks_qty_dict.keys():
                junks_qty_dict[resource] += amount
            else:
                junks_qty_dict[resource] = amount
    # for (k, v) in res_qty_dict.items():
    #     if v >= 250:
    #         res_leg_item = k
    #
    #         for (legitem, legres) in item_res_dict.items():
    #             if legres == k:
    #                 legendary_item = legitem.capitalize()

    if item_obtained == False:
        line = input()
    else:
        break
if item_obtained:
    print(f"{legendary_item} obtained!")

print(f"shards: {res_qty_dict[shards]}\nfragments: {res_qty_dict[fragments]}\nmotes: {res_qty_dict[motes]}")
for (junk, qty) in junks_qty_dict.items():
    print(f"{junk}: {qty}")
