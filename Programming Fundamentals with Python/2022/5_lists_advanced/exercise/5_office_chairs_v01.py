n = int(input())
chairs_needed = 0
room_number = 0
eachroom = 0
total_free_chairs = 0
visitors = 0
splited_str = [input() for x in range(1, n + 1)]
for y in splited_str:
    chairs = len(y.split(' ')[0])
    visitors = int(y.split(' ')[1])
    room_number += 1
    if visitors > chairs:
        chairs_needed = (visitors - chairs)
        print(f"{chairs_needed} more chairs needed in room {room_number}")
    elif chairs >= visitors:
        eachroom += 1
        total_free_chairs += (chairs - visitors)
if total_free_chairs > 0 and eachroom == n:
    print(f"Game On, {total_free_chairs} free chairs left")