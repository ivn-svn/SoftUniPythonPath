first_line = input().split(" ")
second_line = input()
final_message = ""
char_remove = ''
lsecond = len(second_line) -1
for number in first_line:
    digits = 0
    for digit in number:
        digits += int(digit)
    if digits > lsecond:
        digits = digits - lsecond - 1
        char_remove = second_line[digits]
        final_message += second_line[digits]
        second_line = second_line.replace(char_remove, '')
    else:
        final_message += second_line[digits]
        char_remove = second_line[digits]
        second_line = second_line.replace(char_remove, '')
print(final_message)