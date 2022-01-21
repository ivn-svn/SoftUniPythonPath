# Print only unique values from a list:
a = [1, 2, 20, 6, 210]
b = set([6, 20, 1])
c = [x for x in a if x not in b]
print(c)