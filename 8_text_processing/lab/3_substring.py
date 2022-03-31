sub_concat = ''
first_string = input()
second_string = input()
first_string_list = [x for x in first_string]
second_string_list = [z for z in second_string]
substring = [y for y in second_string_list if y not in first_string_list]
for l in substring:
    sub_concat += l
print(sub_concat)

