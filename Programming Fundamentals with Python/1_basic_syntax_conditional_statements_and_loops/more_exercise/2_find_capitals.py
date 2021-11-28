# Write a program that takes a single string and prints a list of all the indices of all the capital letters
data_inp = input()
uppercase = []
for i in range(len(data_inp)):
    if data_inp[i].isupper():
        uppercase.append(i)
print(uppercase)


