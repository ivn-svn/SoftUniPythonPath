current = 1
is_current_bigger_than_n = False
n = int(input())
for row in range(1, n + 1):
    for col in range(1, row + 1):
#
        if current > n:
            is_current_bigger_than_n = True
            break
        print(str(current) + ' ', end='')
        current += 1 # Увеличава настоящото число current да е по-голямо от n
    if is_current_bigger_than_n: # Връща цикъла на ред 4, когато настоящото число current стане по-голямо от n.
        break
    print()