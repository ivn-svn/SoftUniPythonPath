# input_data = input().split(' ')
# odd_occurence_counter = 0
# unique_items = [x.lower() for x in list(set(input_data))]
# odd_occured_items = []
# print(unique_items)
# for unique_item in unique_items:
#     if unique_item.lower() in input_data:
#         odd_occurence_counter += 1
#     if odd_occurence_counter % 2 == 1:
#         odd_occured_items.append(unique_item)
# print(odd_occured_items)
#
input_data = input().split(' ')
odd_occurence_counter = 0
lower_items = [x.lower() for x in input_data]
unique_items = list(set(lower_items))
print(unique_items)
lower_input_data = [z.lower() for z in input_data]

#
# def odd_occ_func():
#     if odd_occurence_counter % 2 == 1:
#         odd_occured_items.append(unique_item)
#         return odd_occ_func()


print(f"{lower_input_data} * ")

odd_occured_items = {}
for unique_item in unique_items:
    #for x in lower_input_data:
    odd_occurence_counter = lower_input_data.count(unique_item)

    if odd_occurence_counter % 2 == 1:
        odd_occured_items[unique_item] = odd_occurence_counter
print(odd_occured_items)
