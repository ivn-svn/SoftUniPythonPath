numbers_count = int(input())
sum_number = 0
for counter in range(numbers_count):  # Така диапазонът започва от 0 до крайно число numbers_count
    current_number = int(input())
    sum_number += current_number
print(sum_number)
