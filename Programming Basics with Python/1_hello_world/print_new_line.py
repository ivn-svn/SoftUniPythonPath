# x = 1
# for x in range(10):
#     x + 1
# print(x)
# -------------------------------------------------> this is not working. WHY?! <---------------------------------------
for x in range (10):
    counter = x + 1
    print(counter)
#---------------------------------> add as an argument to the print function in order to print newline : |,  end = '\n'|
# You can use the optional named argument end to explicitly mention the string that should be appended
# at the end of the line.
#
# Whatever you provide as the end argument is going to be the terminating string.
#
# So if you provide an empty string, then no newline characters, and no spaces will be appended to your input.
# for c in 'хелло':
#     print(c)
# -------------------------------------------------> this is working. WHY the fck?! <-----------------------------------
