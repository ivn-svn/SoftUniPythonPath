numlist = input()
numsplit = numlist.split(', ')
listofints = [int(x) for x in numsplit]
groups_of = {f'List of ' + str(((((z - 1) // 10) * 10) + 10)) + f'\'s':z for z in listofints}
print(groups_of)