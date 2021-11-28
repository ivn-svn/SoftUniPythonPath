# Да се напише програма, която чете число n, въведено от потребителя,
# и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.
n = int(input())
for powerof in range(n + 1):
    if powerof % 2 == 0:
        value = pow(2, powerof)
        print(value)