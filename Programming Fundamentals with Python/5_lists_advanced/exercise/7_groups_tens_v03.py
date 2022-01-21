n = input()
num_list = n.split(', ')
num_list_ints = [int(x) for x in num_list]
new_numdict = {}
group_of = ''
listof = ''
max_value = max(num_list_ints)
groups = {'': []}
for i in range(1, max_value + 1):
    group_of = str(((i // 10) * 10) + 10)
    listof = f'Group of {group_of}\'s: '
    if int(group_of) - 10 > max_value:
        break
    else:
        if i in num_list_ints:
            if listof in groups:
                groups[listof].append(int(i))
            else:
                groups[listof] = []
                groups[listof].append(int(i))
        else:
            pass
for keys in groups:
    print(keys, groups[keys])