# a = int(input())
# b = int(input())
# c = int(input())
#
#
# def three_ints(a, b, c):
#     minimal = min(a, b, c)
#     return minimal
#
#
# print(three_ints(a, b, c))

# -----------------  Another solution: ----------------- #

a = int(input())
b = int(input())
c = int(input())


def three_ints(a, b, c):
    # compare_num = three_ints(a, b, c)
    # for i in compare_num:
    #     return i
    min_found = 0
    if a < b and a < c:
        min_found = a
    elif b < a and b < c:
        min_found = b
    elif c < b and c < a:
        min_found = c
    return min_found
print(three_ints(a, b, c))
