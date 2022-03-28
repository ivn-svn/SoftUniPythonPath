import re


def find_name_age(usr_inp, pagd):
    name_pattern = r"@([A-z][a-z]+)\||@([a-z]+)\||@[a-z]\||@[A-z]\|"
    age_pattern = r"#(\d+)*|#(\d)*"

    name_match = re.findall(name_pattern, usr_inp)

    age_match = re.findall(age_pattern, usr_inp)
    for item in name_match:
        for item0 in item:
            if item0 != "":
                name = item0
                pagd[name] = 0

    for item1 in age_match:
        # for item0 in item1:
        for item2 in item1:
            # print(item2)
            if item2 != "":
                age = int(item2)
                pagd[name] = age

    return pagd


name = ''
age = 0
n = int(input())
person_age_dict = {}

for index in range(1, n + 1):
    user_input = input()
    person_age_dict = find_name_age(user_input, person_age_dict)

# print(person_age_dict)
for (name, age) in person_age_dict.items():
    print(f"{name} is {age} years old.")