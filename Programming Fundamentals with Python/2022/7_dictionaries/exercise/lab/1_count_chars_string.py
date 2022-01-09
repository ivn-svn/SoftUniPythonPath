# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
# Examples
# Input
# text
# Output
# t -> 2
# e -> 1
# x -> 1
text_input = list(input())
tdict = dict()
for i in text_input:
    if i in tdict:
        pass
    elif i != " ":
        tdict[i] = text_input.count(i)
for (key, value) in tdict.items():
    print(f"{key} -> {value}")