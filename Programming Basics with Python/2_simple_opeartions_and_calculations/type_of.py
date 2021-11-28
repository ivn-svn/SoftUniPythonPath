import math

num = float(input())
second_num = num % 2 # change division sign with // or /.
num_rounded = math.ceil(second_num)
print(num_rounded)
print(type(second_num))