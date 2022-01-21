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
enter = input()

new_list = ""
explosion = 0
lenght = 0

while lenght < len(enter):
    for i in range(len(enter)):
        if not enter[i] == ">" and explosion > 0:
            explosion -= 1
        elif enter[i] == ">":
            explosion += int(enter[i + 1])
            new_list += enter[i]
        else:
            new_list += enter[i]
        lenght += 1
print(new_list)