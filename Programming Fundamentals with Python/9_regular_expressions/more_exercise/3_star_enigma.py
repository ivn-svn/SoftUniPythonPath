import re

letters_count = 0
lines = int(input())

for i in range(0, lines):
    user_input = input()
    usr_ct = user_input.count('s')
    for character in user_input:
        decrypted_str = ''
        old_char = character
        new_char = chr(ord(old_char) - usr_ct)
        decrypted_str += new_char



planet_name_pattern = r"\@[A-z]+"
planet_population_pattern = r"\:d+"
attack_type_pattern = r"\![A-Z]\!"
solder_count_pattern = r"->[0-9]+"

planet_names_matches = re.findall(planet_name_pattern, user_input)
planet_population_matches = re.findall(planet_population_pattern, user_input)
attack_type_matches = re.findall(attack_type_pattern, user_input)

# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except:
# '@', '-', '!', ':' and '>'.

print(attack_type_matches)
