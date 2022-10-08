matrix = [
[1, 2, 3, 4],
[2, 3, 4, 5],
[3, 4, 5, 6]
]
# Wrong
print([[x for x in row if x % 2 == 0] for row in matrix])

def remove_even (ll):
    return [x for x in ll if x % 2 == 0]
print([remove_even (row) for row in matrix])