input_data = input().split(' ')
odd_occurence_counter = 0
#
lower_input_data = [x.lower() for x in input_data]
unique_items = [z for z in lower_input_data if lower_input_data.count(z) % 2 == 1]
#for h in range(0, len(unique_items), len(unique_items) -1):
for y in unique_items:#unique_items:
    if unique_items.count(y) > 1:
        unique_items.remove(y)
print(unique_items)
