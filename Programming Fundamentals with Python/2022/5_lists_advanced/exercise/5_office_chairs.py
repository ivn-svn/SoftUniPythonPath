n = int(input())
needed_chairs_in_room = 0
number_of_room = 0
total_free_chairs = 0
visitors = ''
chairs = ''
splited_str = []
#
for i in range(0, n):
    string_test = input()
    splited_str = string_test.split(' ')
    chairs = splited_str[0]
    visitors = int(splited_str[1])
    if visitors > len(chairs):
        needed_chairs_in_room += (int(visitors) - int(len(chairs)))
    elif visitors <= len(chairs):
        total_free_chairs += (int(len(chairs)) - int(visitors))
    number_of_room += 1
if needed_chairs_in_room > 1:
    print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
elif needed_chairs_in_room < 1 and total_free_chairs >= 1:
    print(f"Game On, {total_free_chairs} free chairs left")
