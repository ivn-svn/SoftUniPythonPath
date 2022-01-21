string_int = input().split(', ') # single string of integers, separated by a comma
string_int1 = []
beggars_count = int(input())  # a count of beggars.
# Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns,
# from the first to the last number in the list.
index = 0
for x in string_int:
    string_int1.append(int(x))
beggars_list = []
for y in range(beggars_count):
    beggars_list.append(0)
for str in string_int1:
    beggars_list[index] += str
    index += 1
    if index == beggars_count:
        index = 0
print(beggars_list)



