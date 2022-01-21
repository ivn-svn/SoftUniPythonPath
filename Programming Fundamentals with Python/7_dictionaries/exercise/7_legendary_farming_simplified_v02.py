
import string

user_input = input().lower()
user_input = user_input.split(' ')
resvalues = [int(z) for z in user_input if user_input.index(z) % 2 == 0]
resitself = [y for y in user_input if user_input.index(y) % 2 == 1]
#
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'}
junk = {}
winermaterial = ''
resources = {'shards': 0, 'fragments': 0, 'motes': 0}
item_obt = ''
for x in range(0, len(resvalues)):
    if resitself[x] in resources:
        resources[resitself[x]] += int(resvalues[x])
    elif resitself[x] not in resources:
        if resitself[x] not in junk:
            junk[resitself[x]] = int(resvalues[x])
        else:
            junk[resitself[x]] += int(resvalues[x])

for (keys, values) in resources.items():
    if values >= 250:
        winermaterial = keys
        item_obt = string.capwords(legendary_items[keys])
        print(f"{item_obt} obtained!")
for (keys, values) in resources.items():
    if legendary_items[keys] != item_obt.lower() and item_obt != '':
        print(f"{keys}: {values}")
    elif item_obt == '':
        print(f"{keys}: {values}")
    else:
        winermaterialint = (int(resources[winermaterial]) - 250)
        print(f"{winermaterial}: {winermaterialint}")
for (keys, values) in junk.items():
    print(f"{keys}: {values}")
