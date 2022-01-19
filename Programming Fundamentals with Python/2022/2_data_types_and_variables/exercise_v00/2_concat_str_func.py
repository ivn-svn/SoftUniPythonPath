#     2. Chars to String
# Write a function that receives 3 characters. 
# Concatenate all the characters into one string and print it on the console.
def thrree_chars():
    inp1 = input()
    inp2 = input()
    inp3 = input()
    onestr = inp1 + inp2 + inp3
    return onestr
newstr = thrree_chars()

print(newstr)