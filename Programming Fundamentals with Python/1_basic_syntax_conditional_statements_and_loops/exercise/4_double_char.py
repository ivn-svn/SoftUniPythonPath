text = ''
given_string = str(input())
for letter in given_string:
    text += f'{letter}{letter}'
print(text)