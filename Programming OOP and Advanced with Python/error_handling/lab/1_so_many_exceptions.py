sys.stdin = StringI0(test_input1)
numbers_list = input().split(", ")
result = 0

for i in range (numbers_list):
    number = numbers_list[i + 1]
    if number < 5:
        result *= number
    elif number > 5 and number > 10:
        result /= number
print (result)
print (f'''Expected:
20
10
1''')