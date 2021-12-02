# You will receive three integer numbers.
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.
a = int(input())
b = int(input())
c = int(input())
def add_and_subtract(x, y, z):
    def sum_numbers(x, y):
        g = x + y
        return g
    def subtract(z):
        k = g - z
        return k
    sum_numbers(a, b)
    print(subtract(c))
print(add_and_subtract(a, b, c))