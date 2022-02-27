# Write a program that finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full,
# you should direct the people to the next one with space available.
# 15
# 0 0 0 0
#
def filled(wag):
    counter = 0
    for passenger in wag:
        if passenger == 4:
            counter += 1
    if counter == len(wag):
        fil = True
    else:
        fil = False
    return fil


people = int(input())
current_state = input()
#
initial_wagons = current_state.split(" ")
wagons = [int(x) for x in initial_wagons]
tofill = len(wagons) * 4
placestaken = 0
for taken in wagons:
    placestaken += int(taken)

if tofill >= people:
    free = tofill - people
else:
    queue = people - tofill
#
place_taken = 0

for place in wagons:
    place_taken += int(place)

for i in range(people):
    while filled(wagons) == False:
        for x in wagons:
            if x < 4:
                wagons[x] += 1
                free -= 1
    else:
        break


print(f"The lift has empty spots! {free}")
print(f"There isn't enough space! {queue} people in a queue!\n {wagons}")