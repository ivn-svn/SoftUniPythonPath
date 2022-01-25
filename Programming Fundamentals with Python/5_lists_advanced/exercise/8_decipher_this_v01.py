#     • the second and the last letter are switched (e.g., Holle means Hello)
#     • the first letter is replaced by its character code (e.g., 72 means H)
# Input:
# 82yade 115te 103o
#
# Output:
# Ready set go

# Useful link for reference & help:
# https://docs.python.org/3/tutorial/datastructures.html
#
user_input = input().split(" ")
first_letter = ''
second_letter = ''
last_letter = ''
printable_list = []
ord_char = ''
final_str = ''
concat_str = ''


for word in user_input:
    final_str = ''
    first_letter = ''
    last_letter = ''
    ord_char = ''
    concat_str = ''
    for idx in range(0, len(word)):
        if word[idx].isdigit():
            first_letter = word[idx]
            ord_char += first_letter
        else:
            final_str += word[idx]
    concat_str = chr(int(ord_char)) + final_str
    second_letter = concat_str[1]
    last_letter = concat_str[len(concat_str) - 1]
    # placeholder = '^'
    # concat_str = concat_str.replace(last_letter, placeholder)
    # concat_str = concat_str.replace(second_letter, last_letter)
    # concat_str = concat_str.replace(placeholder, second_letter)
    fst = [concat_str[x] for x in range(2, len(concat_str) -1)]
    #scd = [fst[y] for y in range(1, len(fst) -1)]
    trd = list(chr(int(ord_char))) + list(last_letter) + list(fst) + list(second_letter)
    trd = ''.join(trd)
    printable_list.append(trd)
print(' '.join(printable_list))