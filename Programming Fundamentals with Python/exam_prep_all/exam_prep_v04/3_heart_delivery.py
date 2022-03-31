#  https://judge.softuni.org/Contests/Practice/Index/2031#2
houses = input().split("@")
houses = [int(x) for x in houses]
neighbourhoud = ""
jump = 0
house_index = 0
house_count = len(houses)
current_pos = 0
#
cmd = input()
while cmd != "Love!":
    cmdspl = cmd.split(" ")
    if "Jump" in cmdspl:
        jump = int(cmdspl[1])
        current_pos += jump
        if current_pos >= house_count:
            current_pos = 0
        house_index = current_pos
        if houses[current_pos] > 0:
            houses[current_pos] -= 2
            if houses[current_pos] == 0:
                print(f"Place {house_index} has Valentine's day.")
        elif houses[current_pos] == 0:
            print(f"Place {house_index} already had Valentine's day.")
    cmd = input()

fails_count = [int(fail) for fail in houses if fail > 0]
hearts_needed = len(fails_count)
print(f"Cupid's last position was {house_index}.")

if hearts_needed == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {hearts_needed} places.")
