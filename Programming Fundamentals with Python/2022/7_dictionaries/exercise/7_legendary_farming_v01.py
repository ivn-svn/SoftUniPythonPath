#
# shadowmourne ---> shards
# valanyr      ---> fragments
# dragonwrath  ---> motes
#
import string
user_input = input().lower()
user_input = user_input.split(' ')
print(user_input)
item_obt = ''
#
legendary_items = {'shards': 'shadowmourne', 'fragments': 'valanyr', 'motes': 'dragonwrath'}
junk = {}
resources = {'shards': 0, 'fragments': 0, 'motes': 0}
for x in user_input:
    if x in resources:
        resources[x] += int(user_input[user_input.index(x) - 1])
    else:
        if x in junk:
            junk[x] += int(user_input[user_input.index(x) - 1])
            print(junk)
        elif x not in junk and x.isalpha():
            junk[x] = int(user_input[user_input.index(x) - 1])
        # elif x not in resources:
        #     resources[x] = int(user_input[user_input.index(x) - 1])
for (keys, values) in resources.items():
    if values >= 250:
        item_obt = string.capwords(legendary_items[keys])
        print(f"\n{item_obt} obtained! -> {values}")
for (keys, values) in resources.items():
    print(f'{keys}: {values}')
