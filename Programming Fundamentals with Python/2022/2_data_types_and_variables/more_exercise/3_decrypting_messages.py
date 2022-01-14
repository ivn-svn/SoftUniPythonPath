#     3. Decrypting Messages
# On the first line, you will receive a key (integer). 
# On the second line, you will receive n – the number of lines, which will follow. On the next n lines 
# – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message. 
key_int = int(input())
n_int = int(input())
letter = ""
letter_list = []
replacement = ""
#
for line in range(0, n_int):
    letter = input()
    letter_list.append(ord(letter) + key_int)
for this in letter_list:
    replacement += chr(this)
print(replacement)
