# import re
# password = input()
# only_letters = True
# pattern = ''
# letters = ''
# result = re.findall(pattern, password)
# if 10 > len(password) > 6:
#     pass

import re
password = input()
y = []
numcheck = [y.append(x) for x in list(password) if x.isnumeric()]
def check_pass(p):
    printable = ''
    if re.fullmatch(r'[A-Za-z0-9]{6,10}', p):
        # match
        printable += '\nPassword is valid'
    if not 10 >= len(p) >= 6:
    #     # no match
        printable += '\nPassword must be between 6 and 10 characters'
    if password.isalnum() == False:
    #     # no match
         printable += '\nPassword must consist only of letters and digits'
    if len(numcheck) < 2:
        # no match
        printable += '\nPassword must have at least 2 digits'
    return printable
print(check_pass(password))
