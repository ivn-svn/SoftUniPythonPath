# https://judge.softuni.org/Contests/Practice/Index/1773#0
# Main calculus function:
def pirate_plunder(total, day, daily, target):
    for d in range(1, day + 1):
        total += daily
        if d % 3 == 0:
            total += (daily * 0.5)
        if d % 5 == 0:
            total *= 0.7

    return total, day, daily, target


def checks(perc, total, target):
    if total >= target:
        print(f"Ahoy! {total:.2f} plunder gained.")
    else:
        perc = (total / target_plunder) * 100
        print(f"Collected only {perc:.2f}% of the plunder.")
    return perc, total, target


#
target_plunder = 0
total_plunder = 0
# User inputs:
days = int(input())  # you will receive how many days the pirating lasts.
daily_plunder = int(input())  # how much the pirates plunder for a day
target_plunder = int(input())  # expected plunder at the end
# Main calculus


#
percentage = 0  # should be edited to reflect the formula for percentage
#

total_plunder, days, daily_plunder, target_plunder = pirate_plunder(total_plunder,
                                                                    days, daily_plunder,
                                                                    target_plunder)
#
percentage, total_plunder, target_plunder = checks(percentage, total_plunder, target_plunder)

# Example inputs:
# 5
# 40
# 100
