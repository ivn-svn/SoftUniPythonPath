from collections import OrderedDict
import string

material = ''
amount = 0
main_items = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
legendary_items = {
    'fragments': 'Valanyr',
    'shards': 'Shadowmourne',
    'motes': 'Dragonwrath'
}
junk = {}
junk = OrderedDict(junk)
main_items = OrderedDict(main_items)
win_material = ''
legendary_item = ''
while win_material == '':
    user_input = input().lower().split(' ')

    for index in range(0, len(user_input), 2):
        material = user_input[index + 1]
        amount = int(user_input[index])
        if material == 'shards':
            main_items['shards'] += amount
            if main_items[material] >= 250:
                win_material = legendary_items[material]
                main_items[material] -= 250
                print(f'{win_material} obtained!')
                break
        elif material == 'fragments':
            main_items['fragments'] += amount
            if main_items[material] >= 250:
                win_material = legendary_items[material]
                main_items[material] -= 250
                print(f'{win_material} obtained!')
                break
        elif material == 'motes':
            main_items['motes'] += amount
            if main_items[material] >= 250:
                win_material = legendary_items[material]
                main_items[material] -= 250
                print(f'{win_material} obtained!')
                break
        elif material not in main_items.keys():
            junk.setdefault(material, 0)
            junk[material] += amount
for (k, v) in main_items.items():
    print(f'{k}: {v}')
for (k, v) in junk.items():
    print(f'{k}: {v}')