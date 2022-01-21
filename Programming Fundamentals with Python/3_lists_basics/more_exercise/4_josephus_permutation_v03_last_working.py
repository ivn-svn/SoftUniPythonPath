soldiers_list = input().split(' ')
k = int(input())
alive_soldiers_list = soldiers_list
death_soldiers_list = [] # printable
#
counter = 0
#
while len(death_soldiers_list) - 1 < len(soldiers_list) -2:
    for soldier in soldiers_list:
        if soldier in alive_soldiers_list and counter % (k - 1) == 0 and counter > 0:
            death_soldiers_list.append(soldier)
            alive_soldiers_list.remove(soldier)
        counter += 1

        print(f"Alive: {alive_soldiers_list}")
print(f"Death: {death_soldiers_list}")
