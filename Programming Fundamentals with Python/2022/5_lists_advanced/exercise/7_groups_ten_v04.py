numlist = input()
numsplit = numlist.split(', ')
listofints = [int(x) for x in numsplit]
#groups_of = {f'List of ' + str(((((z - 1) // 10) * 10) + 10)) + f'\'s':z for z in listofints}
groups_of1 = {}
listofsth = ''
for z in listofints:
    zzz = str(((((z - 1) // 10) * 10) + 10))
    listofsth = f'Group of ' + zzz + f'\'s'
    if listofsth in groups_of1:
      # groups_of1[listofsth] += (f', ' + str(z))
        groups_of1[listofsth].append(z)
    elif listofsth not in groups_of1:
     #   groups_of1[listofsth] = str(z)
        groups_of1[listofsth] = []
        groups_of1[listofsth].append(z)
for values in groups_of1:
    print(f'{values}: {groups_of1[values]}')