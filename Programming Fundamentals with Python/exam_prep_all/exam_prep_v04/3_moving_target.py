# https://judge.softuni.org/Contests/Practice/Index/2305#2
cmd_ = ""
init_str = input().split(" ")
init_ints_list = [int(x) for x in init_str]
stuff_to_remove = []
while cmd_ != "End":
    cmd = cmd_.split(" ")
    action = cmd[0]
    if action == "Shoot":
        idx = int(cmd[1])
        power = int(cmd[2])
        if idx < len(init_ints_list):
            if (init_ints_list[idx] - power) <= 0:
                init_ints_list.pop(idx)
            else:
                init_ints_list[idx] -= power
        else:
            pass

    elif action == "Add":
        idx = int(cmd[1])
        value = int(cmd[2])
        if idx < len(init_ints_list):
            init_ints_list.insert(idx, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        idx = int(cmd[1])
        radius = int(cmd[2])
        positive = idx + radius + 1
        negative = radius * -1
        rnegative = idx + negative
        if rnegative >= 0 and 0 <= rnegative < len(init_ints_list) and 0 <= positive < len(init_ints_list):
            stuff_to_remove = init_ints_list[rnegative:positive]
            init_ints_list = [ll for ll in init_ints_list if ll not in stuff_to_remove]
        else:
            print("Strike missed!")
    cmd_ = input()
init_ints_list = [str(z) for z in init_ints_list]
printable = "|".join(init_ints_list)
print(printable)
