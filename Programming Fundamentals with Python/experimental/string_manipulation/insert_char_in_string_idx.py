# https://www.kite.com/python/answers/how-to-insert-a-character-into-a-string-at-an-index-in-python#:~:text=To%20insert%20a%20character%20into%20a%20string%20at%20index%20i,that%20held%20the%20original%20string.

# To insert a character into a string at index i, split the string using the slicing syntax a_string[:i] and a_string[i:].
#
# Between these two portions of the original string, use the concatenation operator + to insert the desired character.
#
# Assign the result to the variable that held the original string.
a_string = ''
print(a_string)
# OUTPUT
# ac
a_string = a_string[:1] + "b" + a_string[1:]
# Insert `"b"` in the middle of `a_string`

print(a_string)
# OUTPUT
# abc