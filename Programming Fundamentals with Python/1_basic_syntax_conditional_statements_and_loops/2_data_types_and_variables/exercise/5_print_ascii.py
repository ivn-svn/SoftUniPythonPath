# https://judge.softuni.bg/Contests/Compete/Index/1722#4
# write a program that prints part of the ASCII table of characters on the console.
# On the first line of input you will receive the char index you should start
# with and on the second line - the index of the last character you should print
start_char = int(input())
end_char = int(input())
#
for x in range(start_char, end_char + 1):
    print(chr(x), end=' ')
