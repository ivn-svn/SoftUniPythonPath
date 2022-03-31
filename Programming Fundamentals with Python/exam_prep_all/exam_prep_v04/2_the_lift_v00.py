# link to task: https://judge.softuni.org/Contests/Practice/Index/2517#1
# https://pastebin.com/i7KrzpRK
queue_waiting = int(input())
current_state = input().split(' ')
queue_var = queue_waiting
changed_state = current_state
max_capacity = len(current_state) * 4


def take_seats(cstate, qvar):
    counter = 0
    for seats in cstate:
        diff = 4 - int(seats)
        if int(seats) < 4 and qvar - diff >= 0:
            qvar -= diff
            cstate[counter] = str(4)
            counter += 1
        elif qvar - diff < 0:
            cstate[counter] = str(qvar)
            counter += 1
            qvar -= qvar
    pr = ' '.join(cstate)
    return pr, qvar


onboarded = 0
for x in current_state:
    onboarded += int(x)

if max_capacity - onboarded > queue_waiting:
    places_left = max_capacity - onboarded
    printable, queue_var = take_seats(current_state, queue_var)
    print("The lift has empty spots! ")  # There will be free seats.
    print(printable)
elif max_capacity - onboarded < queue_waiting:
    people_waiting = queue_waiting + onboarded - max_capacity
    # There won't be free seats.
    printable, queue_var = take_seats(current_state, queue_var)
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{printable}")
elif onboarded + queue_waiting == max_capacity:
    printable, queue_var = take_seats(current_state, queue_var)
    print(printable)
elif queue_waiting == 0:
    printable, queue_var = take_seats(current_state, queue_var)
    print(printable)
elif max_capacity - (onboarded + queue_waiting) == 0:
    printable, queue_var = take_seats(current_state, queue_var)
    print(printable)