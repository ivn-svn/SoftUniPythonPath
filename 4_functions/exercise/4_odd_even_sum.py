char_split = str(input())
odd_sum = 0
even_sum = 0
# defines 3 variables, char_split is for user input to put the characters

def chrs_split(char_split):  # a function to split the characters from the char_split variable
    return [char for char in char_split]


char_collection = chrs_split(char_split)
for char in char_collection:
    if int(char) % 2 == 0:
        even_sum += int(char)

    else:
        odd_sum += int(char)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
