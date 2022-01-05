# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value.
# Try solving that problem using comprehension.
# Input
# a, b, c, a
# d, c, m, h
# Output
# {'a': 97, 'b': 98, 'c': 99}
# {'d': 100, 'c': 99, 'm': 109, 'h': 104}
user_input = input().split(', ')
chars_dict = {}
for i in user_input:
    chars_dict[i] = int(ord(i))
print(chars_dict)
