# Write a program that prints part of the ASCII table characters on the console, separated by a single space. On the
# first line of input, you will receive the char index you should start with. On the second line - the index of the
# last character you should print.
start_input = int(input())
input_n = int(input())
for y in range(start_input, input_n + 1):
    print(chr(y), end=' ')
