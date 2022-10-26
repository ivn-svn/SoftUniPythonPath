# def print_rhombus(n):
#     [print(get_line(i, n)) for i in range (n)]
#     [print(get_line(i, n)) for i in range (n - 2, -1, -1)]
# print_rhombus(3)
def print_row(size, star_count):
    for row in range (size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")

size = int(input())

for star_count in range(1, size):
    print_row(size, star_count)
for star_count in range(size, 0, -1):
    print_row(size, star_count)

