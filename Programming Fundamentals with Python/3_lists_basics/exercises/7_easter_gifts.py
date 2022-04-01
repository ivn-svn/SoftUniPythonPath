initial_gifts_list = input().split(" ")
cmd = input()

while cmd != "No Money":
    inp_lst = cmd.split(" ")
    gift = inp_lst[1]
    if "OutOfStock" in inp_lst:
        for item in initial_gifts_list:
            if item == gift:
                idx = initial_gifts_list.index(item)
                initial_gifts_list[idx] = None
    elif "Required" in inp_lst:
        idx = int(inp_lst[2])
        if 0 <= idx < len(initial_gifts_list):
            initial_gifts_list[idx] = gift
    elif "JustInCase" in inp_lst:
        initial_gifts_list[len(initial_gifts_list) - 1] = gift

    cmd = input()

printable_list = [it for it in initial_gifts_list if it is not None]
print(" ".join(printable_list))
