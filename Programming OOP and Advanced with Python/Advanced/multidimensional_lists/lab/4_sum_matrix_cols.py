# Write a program that reads a matrix from the console and 
# prints the sum for each column on separate lines. 
# On the first line, you will get matrix sizes in format 
# "{rows}, {columns}". On the next rows, you will get elements for each column 
# separated with a single space. 
#
user_input = input()
matrix = []
rows, columns = int(user_input.split(', ')[0]), int(user_input.split(', ')[1])
colsum = 0
list_col_sums = []
matrix = []
matrix = [matrix.append([int(y) for y in input().split(' ')]) for row in range(rows)]
for col in range(columns):
    for idx in range(rows):
        colsum += matrix[idx][col]
    list_col_sums.append(colsum)
    print(colsum)
    colsum = 0 
