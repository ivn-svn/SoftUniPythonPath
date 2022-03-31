input_data = input().split(' ')
odd_occurence_counter = 0
#
lower_input_data = [x.lower() for x in input_data]
unique_items = [z for z in lower_input_data if lower_input_data.count(z) % 2 == 1]
set_apart = set(unique_items)
print(list(set_apart))