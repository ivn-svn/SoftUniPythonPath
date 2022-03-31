# https://judge.softuni.org/Contests/Practice/Index/1773#1
import math
# Functions
def loot(ilst, cm):
    for i in cm:
        if i in ilst:
            pass
        else:
            ilst.insert(0, i)
    return ilst


def drop(ilst, idx):
    if len(ilst) < idx or idx < 0:
        pass
    else:
        item = ilst[idx]
        ilst.pop(idx)
        ilst.append(item)
    return ilst


def steal(ilst, ct):
    if len(ilst) == ct:
        start = 0
        end = len(ilst)
    else:
        start = len(ilst) - ct # + 1
        end = len(ilst)
    stolen_items = ilst[start:end]
    ilst = [z for z in ilst if z not in stolen_items]
    print_stolen = ", ".join(stolen_items)
    print(print_stolen)
    return ilst


def calc_avg_treasure_gain(ilst):
    treasure_items_lengths = [len(length) for length in ilst]
    treasure_items_len_sum = sum(treasure_items_lengths) / len(initial_treasure_chest)
    treasure_items_len_sum = float(round(treasure_items_len_sum, 1))
    return treasure_items_len_sum


#
command = ""
avg_treasure_gain = 0
#
# User inputs:
initial_treasure_chest = input().split("|")
#
while command != "Yohoho!":
    cmd = command.split(" ")
    if "Loot" in cmd:
        cmd = cmd[1:len(cmd)]
        initial_treasure_chest = loot(initial_treasure_chest, cmd)
    elif "Drop" in cmd:
        index = int(cmd[1])
        initial_treasure_chest = drop(initial_treasure_chest, index)
    elif "Steal" in cmd:
        count = int(cmd[1])
        if count > len(initial_treasure_chest):
            count = len(initial_treasure_chest)
        initial_treasure_chest = steal(initial_treasure_chest, count)
    command = input()

treasure_chest_joined = ", ".join(initial_treasure_chest)
#print(f"{treasure_chest_joined}")

if len(initial_treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    avg_treasure_gain = calc_avg_treasure_gain(initial_treasure_chest)
    print(f"Average treasure gain: {avg_treasure_gain:.2f} pirate credits.")
