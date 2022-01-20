str1 = input()
str2 = input()
str3 = input()
full_body = ['','','']
for str in [str1, str2, str3]:
    if "head" in str:
        full_body[0] = str
    elif "body" in str:
        full_body[1] = str
    elif "tail" in str:
        full_body[2] = str
print(full_body)