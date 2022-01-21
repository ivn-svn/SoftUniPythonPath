# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list. Use abs()
# Example input: 1 2.5 -3 -4.5
seq_num = input()
absval = []
def abs_val(a):
    for x in seq_num.split(" "):
        z = abs(float(x))
        absval.append(z)
    return absval
print(abs_val(seq_num))