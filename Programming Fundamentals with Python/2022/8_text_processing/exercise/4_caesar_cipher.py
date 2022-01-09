# 4.  Caesar Cipher
# Write a program that returns an encrypted version of the same text. Encrypt the
# text by replacing each character with the corresponding character three positions forward
# in the ASCII table. For example, A would be replaced with D, B would become E, and so on.
# Print the encrypted text.
#
# Input
# Programming is cool!
# One year has 365 days.
#
# Output
# Surjudpplqj#lv#frro$
# Rqh#|hdu#kdv#698#gd|v1
user_input = input()
replacement_str = ''
letter_id = 0
replacement_id = 0

for letter in user_input:
    letter_id = ord(letter)
    replacement_id = letter_id + 3
    replacement_str += chr(replacement_id)
print(replacement_str)