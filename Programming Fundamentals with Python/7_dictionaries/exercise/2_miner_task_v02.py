str_seq = input()
resources_dict = {}
value = 0
resources_list = []
counter = 0


def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()


while str_seq != 'stop':
    str_seq = input()
    if str_seq.isdigit() != True:
        resources_list.append(str_seq)
        resources_dict[str_seq] = 0
    elif str_seq.isdigit() == True:
        print(counter)
        print(resources_list)
        resources_dict[resources_list[counter]] = int(str_seq)
        counter += 1

else:
    print(resources_dict)
