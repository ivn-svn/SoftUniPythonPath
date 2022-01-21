# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.
smallest = 0
x = int(input())
y = int(input())
z = int(input())
listed = [x, y, z]
def smallestnum():
    newlisted = sorted(listed)
    return newlisted[0]
print(smallestnum())
#
# Using for loop for multiple numbers:
#
# ls1 = []
# total_ele = int(input(" How many elements you want to enter? "))
#
# # getting list from the user
# for i in range(total_ele):
#     n = int(input("Enter a number:"))
#     ls1.append(n)
# print(ls1)
# min = ls1[0]
#
# # finding smallest number
# for i in range(len(ls1)):
#     if ls1[i] < min:
#         min = ls1[i]
# print("The smallest element is ", min)
# https://www.askpython.com/python/examples/smallest-number-in-python