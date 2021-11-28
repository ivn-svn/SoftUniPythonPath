number = int(input())
product = 0
if number in range(111, 999) and number > 0:
    number_str = str(number)
    # number_length = len(number_str)
    reverse_num0 = number_str[2]
    reverse_num1 = number_str[1]
    reverse_num2 = number_str[0]
    # TO INTEGER!
    reverse_num0int = int(reverse_num0)
    reverse_num1int = int(reverse_num1)
    reverse_num2int = int(reverse_num2)
    # number_int = int(number_str)
    for x in range(1, reverse_num2int + 1):
        for y in range(1, reverse_num1int + 1):
            for z in range(1, reverse_num0int + 1):
                product = x * y * z
                print(f"{x} * {y} * {z} = {product}")

        #print(reverse_num0, reverse_num1, reverse_num2)
else:
    print('Number not in range!')

    # # Sort Algorithm
    # if reverse_num0 > reverse_num1 and reverse_num2:
    # elif reverse_num1 > reverse_num0 and reverse_num2:
    # elif reverse_num2 > reverse_num1 and reverse_num0: