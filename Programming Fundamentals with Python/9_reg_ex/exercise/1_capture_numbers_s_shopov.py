import re

numbers = []

while True:
    text = input()
    if not text:
        break
    number = re.findall('\d+', text)
    [numbers.append(x) for x in number if number]

for number in numbers:
    print(number, end=' ')

    #Source: https://pastebin.com/u/simeonshopov