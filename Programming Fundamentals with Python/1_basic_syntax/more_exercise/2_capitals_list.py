
# Write a program that takes a single string and prints a list of all the capital letters indices.
# user_input = input()
# index_list = []
# for x in user_input:
#     if x.isupper():
        
#         index_list.append(user_input.index(x))
# print(index_list)

data_inp = input()
uppercase = []
for i in range(len(data_inp)):
    if data_inp[i].isupper():
        uppercase.append(i)
print(uppercase)