n = input()
num_list = n.split(', ')
num_list_ints = [int(x) for x in num_list]
group_of = ''
listof = ''
max_value = max(num_list_ints)
groups = {}
for i in range(1, max_value + 1):
    group_of = str(((i // 10) * 10) + 10)
    listof = f'Group of {group_of}\'s: '
    if int(group_of) - 10 > max_value:
        break
    else:
        if i in num_list_ints:
            groups[listof] = str(i)
            if listof in groups[listof]:
                groups[listof] = groups[listof].append(str(i))
                print(listof + f'{groups[listof]}')
            else:
                groups[listof] = str(i)
                print(listof + f'{groups[listof]}')
        else:
            pass