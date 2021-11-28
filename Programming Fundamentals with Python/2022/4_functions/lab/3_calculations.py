# Create a function that receives three parameters and calculates a result depending on operator. The operator can be
# 'multiply', 'divide', 'add', 'subtract' .
# The input comes as three parameters – two integers and an operator as a string.
op = input() #c
int1 = int(input()) #a
int2 = int(input()) #b
operators = ['multiply', 'divide', 'add', 'subtract']
def calc_func(c, a, b):
    result = None
    if c == operators[0]:
        result = a * b
    if c == operators[1]:
        result = a / b
    if c == operators[2]:
        result = a + b
    if c == operators[3]:
        result = a - b
    return result
    print(int(result))

print(calc_func(op, int1, int2))
