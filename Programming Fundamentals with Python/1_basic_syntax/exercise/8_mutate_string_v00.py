# Input
# bubble gum
# turtle hum


# Output
# tubble gum
# turble gum
# turtle gum
# turtle hum
first_str = input()
second_str = input()
mutate_str = ""
for i in range(len(first_str)):
    if first_str[i] == second_str[i]:
        mutate_str += first_str[i]
    elif first_str[i] != second_str[i]:
        mutate_str += second_str[i]
        mutate_plus = ""
        length_sub = len(mutate_str)
        len_first = len(first_str)
        mutate_plus += mutate_str
        for m in range(length_sub, len_first):
            mutate_plus += first_str[m]
        print(mutate_plus)