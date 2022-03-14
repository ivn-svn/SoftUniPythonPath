# https://judge.softuni.org/Contests/Practice/Index/2303#0
#
# First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings
# with commands split by a single space. The commands will be the following:

# "Cut {index} {length}"
#         ◦ Gets the substring with the given length starting from the given index from the password and removes its
# first occurrence, then prints the password on the console.
#         ◦ The given index and the length will always be valid.


init_str = input()


def take_odd(istr):
    takeodd = [istr[x] for x in range(0, len(istr)) if x % 2 == 1]
    return takeodd


def cut_it(a, b):
    b = a + b
    cuted = init_str[slice(a, b)]
    cut = init_str.replace(cuted, '')
    return cut


def subst(a, b, istr):
    istr = istr.replace(a, b)
    return istr


cmd = ''

while cmd != 'Done':
    cmd = input()
    if "TakeOdd" in cmd:
        todd = take_odd(init_str)
        init_str = ''.join(todd)
        print(init_str)
    elif "Cut" in cmd:
        splited = cmd.split()
        a = int(splited[1])
        b = int(splited[2])
        init_str = cut_it(a, b)
        print(init_str)
    elif "Substitute" in cmd:
        splited = cmd.split()
        a = splited[1]
        b = splited[2]
        if a in init_str:
            init_str = subst(a, b, init_str)
            print(init_str)
        elif a not in init_str:
            print("Nothing to replace!")

print(f"Your password is: {init_str}")