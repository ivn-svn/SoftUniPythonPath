# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
vowels_list = ['a', 'o', 'u', 'e', 'i']
vowelstext = str(input())
#
vowelstextlist = [z for z in vowelstext if z.lower() not in vowels_list]
# finaltext = ''
# for x in vowelstextlist:
#     y = x.lower()
#     if y in vowels_list:
#         if x.isupper() == True:
#             vowelstextlist.remove(x)
#         else:
#             vowelstextlist.remove(x)
# finaltext = ''.join(vowelstextlist)
print(''.join(vowelstextlist))