# Write a program, which keeps a dictionary with synonyms.
# The key of the dictionary will be the word.
# The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words.
# After each word, you will be given a synonym, so the count of lines you have to read from the console is 2 * n.
# You will be receiving a word and a synonym each on a separate line like this:
# {word}
# {synonym}
n = int(input())
synonyms = {}
for i in range(n):
    word = input()  # .split(" ")
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym) # Не може да се апендва на dictionary, само на списък! Апендвайки към стринг,
    # променливата очевидно автоматично се превръща в списък.
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
