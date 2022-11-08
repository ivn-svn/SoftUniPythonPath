# 2.	Even Matrix
# Write a program that receives a matrix of numbers 
# and prints a new one only with the numbers that are even. 
# Use nested comprehension for that problem. 
# On the first line, you will receive the rows of the matrix. 
# On the next rows, you will get elements for each column separated 
# with a comma and a space ", ".  
#
# 2
# 1, 2, 3
# 4, 5, 6
#
rows = int(input())
matrix = []
for i in range(rows):
    row = input().split(', ')
    matrix.append([int(even) for even in row if int(even) % 2 == 0])
print(matrix)