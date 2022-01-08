res_amount_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'}
winner_material_boundary = 250
user_input = input().lower()
resource = ''
amount = 0
junk = {}
split_user_input = user_input.split(' ')
for i in range(0, len(split_user_input) - 1, 2):
    amount = int(split_user_input[i])
    resource = split_user_input[i + 1]

    if resource in res_amount_dict.keys() and res_amount_dict[resource] < 250:
        res_amount_dict[resource] += amount
        if res_amount_dict[resource] >= 250:
            break
    elif resource not in res_amount_dict.keys():
        if resource not in junk.keys():
            junk[resource] = amount
        elif resource in junk.keys():
            junk[resource] += amount
for item in split_user_input:
    if item in res_amount_dict.keys():
        if res_amount_dict[item] >= 250:
            res_amount_dict[item] -= 250
            legendary_item = legendary_items[item]
            capletter = legendary_item[0]
            legendary_item = legendary_item.replace(capletter, capletter.upper())
            print(f'{legendary_item} obtained!')
for main_resource in res_amount_dict.keys():
    print(f'{main_resource}: {res_amount_dict[main_resource]}')
for (junk_item, item_quantity) in junk.items():
    print(f'{junk_item}: {item_quantity}')