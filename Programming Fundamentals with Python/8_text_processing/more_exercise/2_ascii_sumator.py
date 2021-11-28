# Write a program that prints a sum of all characters between
# two given characters (their ascii code). On the first line
# you will get a character. On the second line you get another character.
# On the last line you get a random string. Find all the characters between the two given and print their ascii sum.
sum_all = 0
first_char = str(input())
second_char = str(input())
random_string = input()
index_first = 0
index_second = 0
for x in random_string:
    if x == first_char:
        index_first = random_string.index(x)
    elif x == second_char:
        index_second = random_string.index(x)
for y in range(index_first, index_second):
    sum_all += ord(random_string[y])
print(sum_all)
if index_first is not True:
    pass

