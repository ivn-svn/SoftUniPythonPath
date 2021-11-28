# 4. Sum of Chars
# Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
# Input
# On the first line, you will receive n – the number of lines, which will follow
# On the next n lines – you will receive letters from the Latin alphabet
# Output
# Print the total sum in the following format:
# The sum equals: {total_sum}
# Constraints
# n will be in the interval [1…20].
# The characters will always be either upper or lower-case letters from the English alphabet
# You will always receive one letter per line
n = int(input())
char_sum = 0
for x in range(0, n):
    latin_chars = str(input())
    if latin_chars not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        char_sum += ord(latin_chars)
    else:
        pass
print(f"The sum equals: {char_sum}")
