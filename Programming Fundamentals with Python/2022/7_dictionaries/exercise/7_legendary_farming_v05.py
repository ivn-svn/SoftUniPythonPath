from collections import OrderedDict
import string

junk = {}

main_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

main_ordered = OrderedDict(main_materials)

legendary_items = {
    'fragments': 'Valanyr',
    'shards': 'Shadowmourne',
    'motes': 'Dragonwrath'
}

junk = OrderedDict(junk)

winner_material = ''
end_cycle = False

resource = ''
amount = 0
legendary_item = ''

user_input = input().lower().split(' ')

while not end_cycle:
    for i in range(0, len(user_input), 2):
        amount = int(user_input[i])
        resource = user_input[i + 1]
        if resource in main_ordered.keys():
            main_ordered[resource] += amount
            if main_ordered[resource] >= 250:
                legendary_item = string.capwords(legendary_items[resource])
                main_ordered[resource] -= 250
                winner_material = resource
                end_cycle = True
                print(f'{legendary_item} obtained!')
                break
        elif resource not in main_ordered.keys():
            if resource in junk.keys():
                junk[resource] += amount
            elif resource not in junk.keys():
                junk.setdefault(resource, 0)
                junk[resource] += amount

for (k, v) in main_ordered.items():
    print(f'{k}: {v}')
for (k, v) in junk.items():
    print(f'{k}: {v}')
