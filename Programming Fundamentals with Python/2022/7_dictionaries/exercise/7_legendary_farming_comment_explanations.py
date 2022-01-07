import string # importing string to cast every obtained item's first letter to upper().
# Additionally, the incoming input should be casted to lower so that 'Shards' == 'shards'
user_input = input().lower() # the oneline of input {quantity} <space> {resource} shall come here
user_input = user_input.split(' ')
resvalues = [int(z) for z in user_input if user_input.index(z) % 2 == 0] # the values be indexed & ref
# to particular resource needed for each legendary item
resitself = [y for y in user_input if user_input.index(y) % 2 == 1] # the resources itself presented in a list
#
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'} # the legendary stuff
junk = {} # this collects * that isn't 'shards', 'fragments' or 'motes' and should come after the leg item resources
winermaterial = '' # I would ref here the material of which we reach the 250 barrier first
resources = {'shards': 0, 'fragments': 0, 'motes': 0} # the resource collector dict
for x in range(0, len(resvalues)): # for loop to index my resources
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
        print(f"{keys}: {values}")
    else:
        for (keys, values) in resources.items():
            print(f"{keys}: {values}")

for (keys, values) in resources.items():
    if legendary_items[keys] != item_obt.lower():
        print(f"{keys}: {values}")
    elif legendary_items[keys] == item_obt.lower():
        winermaterialint = (int(resources[winermaterial]) - 250)
        print(f"{winermaterial}: {winermaterialint}")
for (keys, values) in junk.items():
    print(f"{keys}: {values}")