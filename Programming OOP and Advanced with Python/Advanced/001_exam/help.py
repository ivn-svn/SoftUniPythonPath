import pprint


def ThreeD(a, b, c):
    lst = [[['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst


# Driver Code
col1 = 5
col2 = 3
row = 2
# used the pretty printed function
pprint.pprint(ThreeD(col1, col2, row))

#

from collections import deque
# x for x in reversed(name) reverse a list called name

# python code to implement the approach

if __name__ == "__main__":

    # Considering 2-D array having 3 rows and 3 columns
    n = 3
    m = 3
    arr = [[3, 2, 7], [2, 6, 8], [5, 1, 9]]

    # Iterating over all 1-D arrays in 2-D array
    for i in range(0, n):

        # Printing all elements in ith 1-D array
        for j in range(0, m):
            # Printing jth element of ith row
            print(arr[i][j], end=" ")

        print()

    # This code is contributed by rakeshsahni # https://www.geeksforgeeks.org/how-to-iterate-a-multidimensional-array/

# Python code
# Consider 3-D array of dimensions 2*2*2
x = 2
y = 2
z = 2
arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Iterating over each 2-D array in 3-D array
for i in range(0, x):
    print("Inside " + str(i + 1) + " 2D array in 3-D array")

# Iterating over each 1-D array
for j in range(0, x):
    print("Inside " + str(j + 1) + " 1D array of the 2-D array")

    # Iterating over each element in 1-D array
    for k in range(0, x):
        print(arr[i][j][k], end=" ")
    print("")

print("")

# This code is contributed by akashish__ # https://www.geeksforgeeks.org/how-to-iterate-a-multidimensional-array/
#




