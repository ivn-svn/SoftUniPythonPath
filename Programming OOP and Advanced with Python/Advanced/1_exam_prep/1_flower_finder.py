from collections import deque
from copy import deepcopy

# v = "o e a o e a i"
# c = "p r s x r"
# vowels = input().split()
# consonants = input().split()
vowels = deque(input().split())
consonants = input().split()
words = ["rose", "tulip", "lotus", "daffodil"]
words_copy = deepcopy(words)
found = ""


def wordFoundCheck(words, copy):
    idx = 0
    for w in words:
        if w == "":
            found = copy[idx]
            return found
        idx += 1


while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for i in range(len(words)):
        word = words[i]
        if v in word:
            word = word.replace(v, "")
        if c in word:
            word = word.replace(c, "")
        words[i] = word

    found = wordFoundCheck(words, words_copy)

    if found != "" and found in words_copy:
        print(f"Word found: {found}")
        break
 
if found == None or found not in words_copy:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
