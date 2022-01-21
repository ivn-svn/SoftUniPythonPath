n = list(map(int, input().split(' ')))
k = int(input())
list_result = []
counter = 0

index = 0
while len(n) > 0:
    counter += 1

    if counter % k == 0:
        list_result.append(n.pop(index))
    else:
        index += 1

    if index >= len(n):
        index = 0

print(str(list_result).replace(' ', ''))
