user_input = input().split(' ')
newletter_int = 0
new_output = []

for word in user_input:
    newletter_int = 0 
    newstr = ''

    for letter in word:
        if ord(letter) >= 97:
            newletter = (ord(letter) - 97 + 2) % 26 + 97 
        else:
            newletter = (ord(letter))
        newstr += chr(newletter)

    new_output.append(newstr)
print(" ".join(new_output))