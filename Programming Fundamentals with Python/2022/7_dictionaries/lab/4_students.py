# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.

name = ''
id = ''
course = ''
user_input = ':'
endread = False
students_dict = {}
printin = ''
def printable_func(useri):
    getc = useri.replace("_", " ")
    # for (key, value) in students_dict:
    #     return f"{value[0]}-{value[1]}"
    j = students_dict.keys()
    x = [z for z in j if getc in students_dict[z]]
    for i in x:
        names = students_dict.get(i)
        print(f"{names[0]} - {i}")
    return x
while endread != True:

    if ':' not in user_input:
        endread = True
        printin = printable_func(user_input)
        print(printin)

        break
    else:
        user_input = input()
        if ':' not in user_input:
            printin = printable_func(user_input)
            print(printin)
            break
        else:
            name = user_input.split(':')[0]
            id = user_input.split(':')[1]
            course = user_input.split(':')[2]
            students_dict[id] = [name, course]
