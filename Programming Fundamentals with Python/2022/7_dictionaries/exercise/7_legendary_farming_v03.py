import string
from collections import OrderedDict
#
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'}
junk = {}
junk = OrderedDict(junk)
winermaterial = ''
resources = {'shards': 0, 'fragments': 0, 'motes': 0}
item_obt = ''
endcycle = False
while winermaterial == '' or endcycle == False:
    user_input = input().lower()
    user_input = user_input.split(' ')
    resvalues = [int(z) for z in user_input if user_input.index(z) % 2 == 0]
    resitself = [y for y in user_input if user_input.index(y) % 2 == 1]
    for x in range(0, len(resvalues)):
        if resitself[x] in resources.keys():
            resources[resitself[x]] += int(resvalues[x])
            if resources[resitself[x]] >= 250:
                winermaterial = resitself[x]
                item_obt = string.capwords(legendary_items[resitself[x]])
                winermaterialint = (int(resources[winermaterial]) - 250)
                print(f"{item_obt} obtained!")
                endcycle = True
                break
        elif resitself[x] not in resources:
            if resitself[x] not in junk:
                junk[resitself[x]] = int(resvalues[x])
            else:
                junk[resitself[x]] += int(resvalues[x])



for (keys, values) in resources.items():
    if legendary_items[keys] != item_obt.lower():
        print(f"{keys}: {values}")
    else:
        print(f"{winermaterial}: {winermaterialint}")
for (keys, values) in junk.items():
    print(f"{keys}: {values}")

    #
    # Да се изясни какво става, ако стойността на сумата на който и да е от ресурсите не достига до 250...
