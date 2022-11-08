# Write a program that finds the sum of all numbers 
# in a matrix's primary diagonal 
# (runs from top left to bottom right). 
# On the first line, you will receive an integer N – 
# the size of a square matrix. 
# 
# The next N lines holds the values 
# for each column - N numbers, separated by a single space. 
n = int(input())
rows = n
cols = n
matrix = []
diagonal_sum = 0
for idx in range(rows): 
    therow = input().split(' ')
    matrix.append([int(item) for item in therow])
    diagonal_sum += matrix[idx][idx]
print(diagonal_sum)


