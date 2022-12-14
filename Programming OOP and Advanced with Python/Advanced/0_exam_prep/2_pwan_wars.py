from collections import deque



rows = deque(list())
cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
for row in range(1, 9):
    rows.appendleft([str(cols[i] + str(row)) for i in range(0, 8)])

print(rows)

# rev = list()
# #reverse_matrix = [rev.append(rows[r]) for r in range(-8, 0)]
# reverse_matrix = rows[::-1]
# print(reverse_matrix)