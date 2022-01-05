# Write a program that extracts all elements from a given sequence of words present
# in it an odd number of times (case-insensitive).
#     • Words are given on a single line, space-separated.
#     • Print the result elements in lowercase, in their order of appearance.
user_input = input().lower()
user_input = user_input.split(" ")


dictionary = {}
for word in user_input:
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1


for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")