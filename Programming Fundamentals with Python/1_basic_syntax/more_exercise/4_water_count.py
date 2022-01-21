# Beaches are filled with sand, water, fish, and sun. Given a string, 
# calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

user_input = input()
keywords = ["Sand", "Water", "Fish", "Sun"]
wordcounter = 0
for word in keywords:
    wordcounter += user_input.lower().count(word.lower())
print(wordcounter)