data = input() # дефинира и събира входните данни
dictionary = {} # дефинира празен речник
#
for char in data:
    if char == " ": # проверява дали има разстояние,
        continue # ако има, продължава към следващия ред от кода, като го прескача
    if char not in dictionary:
        dictionary[char] = 0

    dictionary[char] += 1

for (key, value) in dictionary.items():
    print(f"{key} -> {value}")