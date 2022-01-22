# Source: https://www.geeksforgeeks.org/python-itertools/

# Python code to demonstrate the working of
# repeat()

# importing "itertools" for iterator operations
import itertools

# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

#


# import the product function from itertools module
from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))