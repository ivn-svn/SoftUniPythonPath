string_input = input().split(" ")
opposite_num = []
for x in string_input:
    x = int(x)
    powered = x * 2
    x = x - powered
    opposite_num.append(x)
print(opposite_num)