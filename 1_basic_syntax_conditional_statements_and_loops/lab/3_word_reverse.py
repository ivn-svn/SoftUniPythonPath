word_reverse = str(input())
reverse_string = ''
for i in range(len(word_reverse) - 1,  -1, -1): # where 1st
    # -1 е частно,
    # второто е крайната цел, а третото стъпката.
    # print(word_reverse[i])
    reverse_string += word_reverse[i]
print(reverse_string)
