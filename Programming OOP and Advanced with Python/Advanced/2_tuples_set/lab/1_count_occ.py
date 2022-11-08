# The right way to solve Occurences Count assignment
# Not preferrable to solve 1_count_occ.py this way

#numbers_string = '-2.5 4 3 2.5 -5.5 4 3 3 -2.5 3'
numbers_string = input()

occurences_counts = {}

numbers = [float(x) for x in numbers_string.split(' ')]

for number in numbers:
    if number in occurences_counts:
        occurences_counts[number] += 1
    else: 
        occurences_counts[number] = 1

#print(occurences_counts)

for numb, counts in occurences_counts.items():
    print(f"{numb} - {counts} times")

