# Write a program that receives a list of numbers (string containing integers separated by ", ")
# and prints lists with the numbers them into lists of 10's.
# Examples:
#     • The numbers 2 8 4 3 fall into the group under 10
#     • The numbers 13 19 14 15 fall into the group under 20
# For more details, see the examples below
n = input()
num_list = n.split(', ')
num_list_ints = [int(x) for x in num_list]
new_numdict = {}
group_of = ''
listof = ''
max_value = max(num_list_ints)
groups = {}
for i in range(1, max_value + 1):
    group_of = str(((i // 10) * 10) + 10)
    listof = f'Group of {group_of}\'s: '
    groups[listof] = []
    if i in num_list_ints:
        groups[listof] = groups[listof].append(str(i))
        #print(listof + f'{groups[listof]}')
    else:
        pass
# for keys in groups:
for keys in groups:
    print(keys, groups[keys])