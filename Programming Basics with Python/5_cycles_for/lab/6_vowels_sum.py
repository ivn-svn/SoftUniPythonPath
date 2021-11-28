# буква | стойност
# a     |    1  |
# e     |    2  |
# i     |    3  |
# o     |    4  |
# u     |    5  |
# --------------
user_string = str(input())
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_calc = 0
for vowels in user_string:
    if vowels == 'a':
        vowel_calc += 1
    elif vowels == 'e':
        vowel_calc += 2
    elif vowels == 'i':
        vowel_calc += 3
    elif vowels == 'o':
        vowel_calc += 4
    elif vowels == 'u':
        vowel_calc += 5
    else:
        pass
print(vowel_calc)