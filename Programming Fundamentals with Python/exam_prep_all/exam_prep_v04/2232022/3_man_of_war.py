# https://judge.softuni.org/Contests/Practice/Index/1773#2
# Functions, fire, defend, repair, status
def fire(idx, dmg, warship_status, v):
    if 0 <= idx < len(warship_status):
        warship_status[idx] -= dmg
        if warship_status[idx] <= 0:
            v = True
            print("You won! The enemy ship has sunken.")
    return v


def defend(sidx, eidx, dmg, pirate_status, v):
    if 0 <= sidx <= len(pirate_status) and 0 <= eidx <= len(pirate_status):
        for sec in range(sidx, eidx):
            pirate_status[sec] -= dmg
            if pirate_status[sec] <= 0:
                print("You lost! The pirate ship has sunken.")
                v = True
                break
    else:
        pass
    return v


def repair(idx, health, pirate_status):
    if 0 <= idx < len(pirate_status):
        if pirate_status[idx] + health <= max_health_cap:
            pirate_status[idx] += health
        elif pirate_status[idx] + health > max_health_cap:
            pirate_status[idx] = max_health_cap


def count_repairs(lst, low):
    need_repair_lst = [repneed for repneed in lst if repneed < low]
    need_repair_count = len(need_repair_lst)
    return need_repair_count


# Inputs go below:
pirate_ship_status = [int(num) for num in input().split(">")]
warship_status = [int(numw) for numw in input().split(">")]
max_health_cap = int(input())
low_health_alert = max_health_cap * 0.2
# End inputs
pirate_ship_sum = 0
warship_sum = 0
#
stalemate = False
victory = False
# < / >
command = ""
#
while command != "Retire":
    cmd = command.split(" ")
    if "Fire" in cmd:
        idx = int(cmd[1])
        dmg = int(cmd[2])
        victory = fire(idx, dmg, warship_status, victory)
    elif "Defend" in cmd:
        start_idx = int(cmd[1])
        end_idx = int(cmd[2]) + 1
        dmg = int(cmd[3])
        victory = defend(start_idx, end_idx, dmg, pirate_ship_status, victory)
    elif "Repair" in cmd:
        idx = int(cmd[1])
        health = int(cmd[2])
        repair(idx, health, pirate_ship_status)
    elif "Status" in cmd:
        repair_needed_warship = count_repairs(warship_status, low_health_alert)
        repair_needed_pirateship = count_repairs(pirate_ship_status, low_health_alert)
        print(f"{repair_needed_pirateship} sections need repair.")
    command = input()

#
if not victory:
    pirate_ship_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
