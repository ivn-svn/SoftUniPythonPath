user_input = input()
matrix = []
rows, columns = int(user_input.split(', ')[0]), int(user_input.split(', ')[1])
colsum = 0
list_col_sums = []
for i in range(rows):
    row = input().split(' ')
    row = [int(z) for z in row]
    matrix.append(row)
for col in range(columns):
    for idx in range(rows):
        colsum += matrix[idx][col]
    list_col_sums.append(colsum)
    print(colsum)
    colsum = 0 