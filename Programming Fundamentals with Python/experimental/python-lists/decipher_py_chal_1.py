user_input = input().split(' ')
newletter_int = 0
new_output = []

for word in user_input:
    newletter_int = 0 
    newstr = ''

    for letter in word:
        newletter = ord(letter) + 2
        newstr += chr(newletter)
    new_output.append(newstr)
print(" ".join(new_output))