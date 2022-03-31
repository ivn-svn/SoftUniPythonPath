# https://judge.softuni.org/Contests/Practice/Index/2517#1
inp = None
num_moves_now = 0
el_seq = [str(num) for num in input().split(" ")]
match_el = ""
while inp != "end":
    len_el_seq = len(el_seq)
    if inp is not None and inp != "end":
        inp_ = [int(i) for i in inp.split(" ")]
        inp0 = int(inp_[0])
        inp1 = int(inp_[1])
        middle = len(el_seq) // 2
        if len_el_seq > 0:
            if inp0 == inp1 or inp0 >= len_el_seq or inp1 >= len_el_seq:
                match_el = el_seq[inp1]
                el_seq.insert(middle, match_el)
                el_seq.insert(middle, match_el)
                num_moves_now += 1
                # print(f"-{num_moves_now}a")
                print("Invalid input! Adding additional elements to the board")
            elif inp0 < 0 or inp1 < 0:
                num_moves_now += 1
                match_el = f"-{num_moves_now}a"
                el_seq.insert(middle, match_el)
                el_seq.insert(middle, match_el)
                # print(f"-{num_moves_now}a")
                print("Invalid input! Adding additional elements to the board")

            elif inp0 < len_el_seq and inp1 < len_el_seq:
                if el_seq[inp0] == el_seq[inp1]:
                    element = el_seq[inp0]
                    el_seq.pop(inp0)
                    idx = el_seq.index(element)
                    el_seq.pop(idx)
                    print(f"Congrats! You have found matching elements - {element}!")
                    num_moves_now += 1
                else:
                    print("Try again!")

        else:
            break
    inp = input()

el_seq = [str(zz) for zz in el_seq]
el_seq_joined = " ".join(el_seq)

if len_el_seq > 0:
    print(f"Sorry you lose :(\n{el_seq_joined}")
elif len_el_seq == 0:
    print(f"You have won in {num_moves_now} turns!")
