char_split = str(input())
# defines char_split variable. It is for user input to put the characters which are going to be checked
x = char_split.split(', ')
# defines an x variable to hold a list of integers actually as strings. They won't get converted to ints anyweay.
for integer in x:


    def chrs_split(integer):  # a function to split the characters from the char_split variable
        return [char for char in integer]


    splitted = chrs_split(integer)
    first_reverse = []


    def reversing_num(splitted):
        for i in reversed(splitted):
            first_reverse.append(i)
        return first_reverse


    if reversing_num(splitted) == chrs_split(integer):
        print("True")
    elif first_reverse != chrs_split(integer):
        print("False")
