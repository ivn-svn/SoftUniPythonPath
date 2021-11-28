n2 = int(input())
n1 = int(input())
n0 = int(input())
prime = [2, 3, 5, 7]
for i in range(1, n2 + 1):
    for j in range(1, n1 + 1):
        for k in range(1, n0 + 1):
            if j in prime:
                if i % 2 == 0 and k % 2 == 0:
                    print(f'{i} {j} {k}')