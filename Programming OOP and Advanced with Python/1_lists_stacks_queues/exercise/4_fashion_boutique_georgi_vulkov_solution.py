# Python Advanced, Theme 3.04. Stacks and Queues - Exercise: 04. Fashion Boutique

clothes = [int(x) for x in input().split()]  # a sequence of integers, representing the clothes in the box
# print(f"clothes: {clothes} ; type: {type(clothes)}")
capacity = int(input())  # the capacity of a rack (integer)
# print(f"Sum of clothes = {sum(clothes)}")
rack = []
current_capacity = capacity
counter = 1
while clothes:
    pack_num = clothes.pop()

    if pack_num < current_capacity:
        current_capacity -= pack_num

    elif pack_num == current_capacity and clothes:
        counter += 1
        current_capacity = capacity

    elif pack_num > current_capacity:
        counter += 1
        current_capacity = capacity - pack_num
    # print(f"current_capacity = {current_capacity}")
    # print(f"counter = {counter}")

print(counter)
