factor = int(input())
count = int(input())
length = factor * count
el_list = []
for x in range(length, 0, -factor):
    el_list.append(x)
el_list.reverse()
print(el_list)