# Create a program that checks if inputs are valid and decrypt it. On the first line you will receive a number that
# indicates how many inputs you will receive on the next lines
#|GEORGI|:#Lead architect#
import re
n = int(input())
boss_name = ''
title = ''
name_len = ''
title_len = ''
pattern = "[^#:|]"
name_pattern = ''
title_pattern = ''
for x in range(0, n):
    data_input = input()
    boss_name = re.findall(pattern, data_input)
    print("".join(boss_name))
print(f"\n{boss_name}, The {title}"
      f"\n>> Strength: {name_len}\n"
      f">> Armour: {title_len}")