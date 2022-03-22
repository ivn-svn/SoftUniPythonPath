# https://judge.softuni.org/Contests/Practice/Index/1773#2
# Functions, fire, defend, repair, status
def fire(idx, dmg, pirate_status, warship_status):
    if idx < len(warship_status) -1:
        warship_status[idx] -= dmg
        if warship_status[idx] <= 0:
            print("You won! The enemy ship has sunken.")


def defend(sidx, eidx, dmg, pirate_status, warship_status):
    if sidx < len(pirate_status) -1 or eidx < len(pirate_status) -1:
        pass
    else:
        for sec in range(sidx, eidx):
            pirate_status[sec] -= dmg
            if pirate_status[sec] <= 0:
                print("You lost! The pirate ship has sunken.")
                break
def repair():
    pass


def status():
    pass

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

# < / >
command = ""
#
while command != "Retire":
    cmd = command.split(" ")
    if "Fire" in cmd:
        idx = int(cmd[1])
        dmg = int(cmd[2])
        fire(idx, dmg, pirate_ship_status, warship_status)
    elif "Defend" in cmd:
        start_idx = int(cmd[1])
        end_idx = int(cmd[2])
        dmg = int(cmd[3])
    elif "Repair" in cmd:
        pass
    elif "Status" in cmd:
        repair_needed_warship = count_repairs(pirate_ship_status, low_health_alert)
        repair_needed_pirateship = count_repairs(warship_status, low_health_alert)
        #print(f"{repair_needed_warship} sections need repair.")
        print(f"{repair_needed_pirateship} sections need repair.")

if stalemate:
    pirate_ship_sum = sum(pirate_ship_status)
    warship_sum = sum(warship_status)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {warship_sum}")
