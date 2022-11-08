# Write a program that reads a number - N, 
# representing the rows and columns of a square matrix. 
# On the next N lines, you will receive rows of the matrix. 
# Each row consists of ASCII characters. 
#
# After that, you will receive a symbol. 
# Find the first occurrence of that symbol in the matrix and print its position 
# in the format: "({row}, {col})". You should start searching from the top left. 
# If there is no such symbol, 
# print the message "{symbol} does not occur in the matrix".
#
n = int(input())
rows = n
cols = 0
matrix = []
diagonal_sum = 0
occurrence = False
for item in range(rows): 
    therow = list(input())
    matrix.append([item for item in therow])
    
searchchar = input()
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == searchchar:
            occurrence = True
            print(f"({row}, {col})")
            
if not occurrence:
    print(f"{searchchar} does not occur in the matrix")


