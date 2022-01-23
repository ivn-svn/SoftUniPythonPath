#     4. Palindrome Strings
# On the first line, you will receive words separated by a single space.
#     On the second line, you will receive a palindrome. First, you should print a list containing all
#     the found palindromes in the sequence. Then, you should print the number of occurrences of the given
#     palindrome in the format: "Found palindrome {number} times".


first_line = input().split(" ")
second_line = input()
palindromes = []
for word in first_line:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(second_line)} times")