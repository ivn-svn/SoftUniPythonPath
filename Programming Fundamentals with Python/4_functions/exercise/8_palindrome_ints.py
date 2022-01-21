incomingdata = input().split(', ')
userinput = [x for x in incomingdata]
#print(userinput)
rev = False
for z in userinput:
    reversedinput = list(reversed(z))
    #print(reversedinput)
    if list(z) == reversedinput:
        rev = True
        print(f"{rev}")
    else:
        rev = False
        print(f"{rev}")

# FOR REFERENCE: reddit answer by @synthphreak:
# Question: What does 'list_reverseiterator' object is not scriptable mean?
#
# Answer: That the list_reverseiterator object is not scriptable. Lol.
#
# (Semi-)jokes aside, this means that you can't index into a list_reverseiterator object. listtoreturn is a ' \
#                                            'list_reverseiterator, therefore listtoreturn[0] doesn't work.
# This is because a list_reverseiterator object is an iterator, not a list.
#
# To make it a list so you can index into it, change
#
# listtoreturn= reversed(listofstates)
# to
#
# listtoreturn = list(reversed(listofstates))
# or
#
# listtoreturn = listofstates[::-1]
# There are other methods, and you don't even need to stick to lists (e.g., a tuple would also work). ' \
#                                     'It all just depends on what you're trying to do.
# https://www.reddit.com/r/learnpython/comments/nwjdhg/why_am_i_getting_typeerror_list_reverseiterator/