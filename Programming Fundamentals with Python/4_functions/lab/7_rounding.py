# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().
num = input()
def rounding_func(a):
    num1 = num.split(" ")
    num_list = []
    for x in num1:
        z = float(x)
        z = round(z)
        num_list.append(z)
    return num_list
print(rounding_func(num))