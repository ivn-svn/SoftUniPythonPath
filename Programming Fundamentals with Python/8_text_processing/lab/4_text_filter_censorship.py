banned_words = input().split()
text = input()
for word in text:
    text = text.replace(word, "*" * len(word))
print(text)