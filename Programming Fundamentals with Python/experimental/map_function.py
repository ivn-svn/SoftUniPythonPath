def square(number):
     return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(list(squared))
# [1, 4, 9, 16, 25]


list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))
# [1, 1, 1]

list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))
# [10, 15]


# Capitalization or to Lower:
list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))
# [1, 1, 1]

list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))
# [10, 15]


# Remove whitespaces:
with_spaces = ["processing ", "  strings", "with   ", " map   "]

list(map(str.strip, with_spaces))
# ['processing', 'strings', 'with', 'map']
#
# Remove dots from lists of strings:
with_dots = ["processing..", "...strings", "with....", "..map.."]

list(map(lambda s: s.strip("."), with_dots))
# ['processing', 'strings', 'with', 'map']

