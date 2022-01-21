num_list = input().split(' ')
k = int(input())
new_list = [num_list[x] for x in range(0, len(num_list) -1) if x % (k -1) == 0 and x > 0]
print(new_list)