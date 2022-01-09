#     5.  Emoticon Finder
# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

# Input
# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
#
# Output
# :P
# :O
# :)
user_input = input()
splited_input = user_input.split(' ')
special_character = []
joined = ''
second_character = ''
emo_list = []
first_char = ''
for word in splited_input:
    if ':' in word:
        first_char = ':'
        second_character = word[1]
        emoticon = first_char + second_character
        emo_list.append(emoticon)
for each in emo_list:
    print(each, end='\n')

