# 	Sum Matrix Elements
# read a matrix
#  sum  all numbers in the matrix
# •	print the matrix & the sum
# 
# Output:
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
#
# Input
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
user_input = input()
matrix = []
rows, columns = int(user_input.split(', ')[0]), int(user_input.split(', ')[1])
thesum = 0
for i in range(rows):
    row = input().split(', ')
    row = [int(z) for z in row]
    thesum += sum(row)
    matrix.append(row)
print(thesum)
print(matrix)

