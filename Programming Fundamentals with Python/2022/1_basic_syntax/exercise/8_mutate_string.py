#     8. * Mutate Strings
# You will be given two strings. Transform the first string into the second one, 
# letter by letter. Print only the unique strings.
# Note: the strings will have the same lengths.


first_str = input()

second_str = input()
#
mutated_str = first_str
for letter in range(len(first_str)):
    if mutated_str[letter] != second_str[letter]:
        mutated_str = mutated_str.replace(mutated_str[letter], second_str[letter], 1)
        print(mutated_str)