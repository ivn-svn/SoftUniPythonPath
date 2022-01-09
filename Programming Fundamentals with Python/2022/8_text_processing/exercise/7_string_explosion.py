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
explosions_list = []
damage = []
reduced_list = ''
for char in user_input:
    if char == '>':
        explosion = True
        explosions_list.append(index)
        damage.append([])
    index += 1