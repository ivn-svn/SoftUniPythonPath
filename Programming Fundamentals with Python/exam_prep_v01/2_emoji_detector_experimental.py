import re
#
user_input = input()
emoji = ''
#
coolness = 0
#
count_of_all_emojis = 0
#
pattern = r'\s\*{2}[A-Z][a-z]*\*{2}|\s\:{2}[A-Z][a-z]*\:{2}'
pattern_digits = r'\d'
#
found = re.findall(pattern, user_input)
digits_found = re.findall(pattern_digits, user_input)
#
cool_threshold_sum = 1
# Cool nums list \/
cool_nums_list = []

for num in digits_found:
    cool_threshold_sum *= int(num)


print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(found)} emojis found in the text. The cool ones are:")


for word in found:
    coolness = 0
    if len(word) - 4 >= 3:
        for character in word:
            coolness += ord(character)

        if coolness >= cool_threshold_sum:
            print(word, end='\n')