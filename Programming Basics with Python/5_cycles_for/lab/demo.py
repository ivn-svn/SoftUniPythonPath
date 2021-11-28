# # How to check the length of a string?
# text = 'rapoo'
# text_length = len(text)
# print(text_length)
# # How to go through a string with a for cycle? Here it is:
# text = input()
# text_length = len(text)
# for letter_index in range(text_length): # Пайтън гледа какво седи след in оператора.
#    # print(letter_index)
#     print(text[letter_index]) # To print every letter of the string.
#
# text = input()
# text_length = len(text)
# for index, letter in enumerate(text):
#    # print(letter_index)
#     print(index)
#     print(letter)
n = int(input())
for counter in range(n, 0, -1): # Намалява стойността на counter всеки път с 1 заради -1
    # Това се нарича for цикъл със стъпка.
    print(counter)
# for counter in range(1, 10, -2): # Няма да работи, понеже след първия цикъл поради
#     # изваждането на -2, не влизаме в цикъла.
#     print(counter)