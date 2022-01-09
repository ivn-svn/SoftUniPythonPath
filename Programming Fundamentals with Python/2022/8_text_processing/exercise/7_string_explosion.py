#      String Explosion
# Write a program that reads a string from the console that contains:
#     • Explosions marked with '>'
#     • Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
#     • Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark
#      ('>') while deleting characters, you should add the strength to your previous explosion.
#      You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
#     • You will always receive strength for the explosions
#     • The path will consist only of letters from the Latin alphabet, integers, and the char '>'
#     • The strength of the punches will be in the interval [0…9]
user_input = input()
explosion = False
index = 0
damage = 0
explosion_int_at_index = {}
pass_this_index = []
additional = 0
unwanted = ''
for char in range(0, len(user_input)):
    if user_input[char] == '>':
        damage = user_input[index + 1]
        explosion_int_at_index[index] = int(damage)
    index += 1


for key, value in explosion_int_at_index.items():

    for item in range(key, value):
        if user_input[item] == '>':
            unwanted = user_input[value + 1]
            print(unwanted)
        else:
            unwanted = user_input[item]
            print(unwanted)
        pass_this_index.append(unwanted)

reduced_list = [ele for ele in user_input if ele not in pass_this_index]
print(reduced_list)
print(explosion_int_at_index)
