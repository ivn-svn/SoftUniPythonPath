
# first_line = input().split(" ")
# second_line = input()
# final_message = ""
# for number in first_line:
#     digits = 0
#     for digit in number:
#         digits += int(digit)
#     final_message += chr(digits)



# print(final_message)

user_input = input().split(' ')
newletter_int = 0
newstr = ''
new_output = []

for word in user_input:
    newletter_int = 0 
    for letter in word:
        newletter = ord(letter) + 2
        newstr = chr(newletter)
    new_output.append(newstr)
print(" ".join(new_output))