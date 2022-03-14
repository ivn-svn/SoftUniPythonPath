# Write a program finds a place for the tourist on a lift.
# Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct
# the people to the next one with space available.
# Input
#     • On the first line, you will receive how many people are waiting to get on the lift
#     • On the second line, you will receive the current state of the lift separated by a single space: " ".
# Output

# When there is no more available space left on the lift, or there are no more people in the queue, you should print
# on the console the final state of the lift's wagons separated by " " and one of the following messages:
#     • If there are no more people and the lift have empty spots, you should print:
# "The lift has empty spots!
# {wagons separated by ' '}"
#     • If there are still people in the queue and no more available space, you should print:
# "There isn't enough space! {people} people in a queue!
# {wagons separated by ' '}"
#     • If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "

people_q = int(input())
lift_state = input().split(' ')

capacity = len(lift_state) * 4
# print(capacity)
final_state = []

for seats in lift_state:
    free = 4 - int(seats)
    if free > 0:
        if people_q - free > 0:
            people_q -= free
            fs_append = int(seats) + free
            final_state.append(str(fs_append))
            # print(people_q)
            pplleft = capacity - people_q
            print(f"The lift has empty spots! {pplleft}")
        elif people_q - free == 0:
            final_state.append(str(0))

        elif people_q - free < 0:
            final_state.append(str(people_q))
            pplleft = people_q - capacity
            print(f"There isn't enough space! {pplleft} people in a queue! {final_state}")


wagoons_print = ' '.join(final_state)
print(wagoons_print)