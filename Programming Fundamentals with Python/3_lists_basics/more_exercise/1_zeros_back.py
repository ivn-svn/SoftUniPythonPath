# https://judge.softuni.bg/Contests/Practice/Index/1726#1
list_str = str(input()).split(", ")
zeros_str = [x for x in list_str if int(x) == 0]
list_str_sep = [y for y in list_str if int(y) != 0]
combined_list = list_str_sep + zeros_str
int_list = []
for i in combined_list:
    int_list.append(int(i))
print(int_list)
