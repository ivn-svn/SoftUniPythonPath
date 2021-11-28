count_numbers = int(input())
counter = 0
biggest_number = 0
while counter < count_numbers:
    curr_number = int(input())
    if counter == 0:
        biggest_number = curr_number
    elif curr_number > biggest_number:
        biggest_number = curr_number
    counter += 1
print(biggest_number)