
times = int(input())
names = list()
for i in range(0, times):
    user_input = input()
    names.append(user_input)

uniques_list = set(names)

for name in uniques_list:
    print(name, end="\n")