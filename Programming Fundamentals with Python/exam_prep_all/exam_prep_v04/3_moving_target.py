# https://judge.softuni.org/Contests/Practice/Index/2305#2
cmd_ = ""
init_str = input().split(" ")
init_ints_list = [int(x) for x in init_str]
while cmd_ != "End":
    stuff_to_remove = []
    cmd = cmd_.split(" ")
    action = cmd[0]
    if action == "Shoot":
        idx = int(cmd[1])
        power = int(cmd[2])
        if idx < len(init_ints_list):
            # print(init_ints_list)
            if init_ints_list[idx] - (pow(init_ints_list[idx], power)) <= 0:
                init_ints_list.pop(idx)
            else:
                init_ints_list[idx] -= (pow(init_ints_list[idx], power))
            # print(init_ints_list)
        else:
            pass

    elif action == "Add":
        idx = int(cmd[1])
        value = int(cmd[2])
        if idx < len(init_ints_list):
            # print(init_ints_list)
            init_ints_list.insert(idx, value)
            # print(init_ints_list)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        idx = int(cmd[1])
        radius = int(cmd[2])
        if idx < len(init_ints_list):
            # print(init_ints_list)
            for i in range(1, radius):
                stuff_to_remove.append(init_ints_list[idx + i])
                stuff_to_remove.append(init_ints_list[idx + (i * -1)])
                stuff_to_remove.append(init_ints_list[idx])
            for removable in stuff_to_remove:
                init_ints_list.remove(removable)
            # print(init_ints_list)
        else:
            print("Strike missed!")
    cmd_ = input()
init_ints_list = [str(z) for z in init_ints_list]
printable = "|".join(init_ints_list)
print(printable)

