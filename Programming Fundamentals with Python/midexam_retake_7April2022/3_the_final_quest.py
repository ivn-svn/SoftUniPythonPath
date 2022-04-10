words = input().split(' ')
cmd = input()
words_gathered = []

while cmd != 'Stop':
    cmd_list = cmd.split(' ')
    if 'Delete' in cmd_list:
        index = int(cmd_list[1]) + 1
        if index in range(0, len(words) - 1):
            words.pop(index)
    elif 'Swap' in cmd_list:
        word1 = cmd_list[1]
        word2 = cmd_list[2]
        if word1 in words and word2 in words:
            idx1 = words.index(word1)
            idx2 = words.index(word2)
            words[idx2] = words[idx1]
            words[idx1] = word2 # Check for errors
    elif 'Put' in cmd_list:
        word = cmd_list[1]
        index = int(cmd_list[2])
        if index == len(words):
            words.append(word)
        elif index < len(words):
            if index == 0:
                pass
            else:
                index = index - 1
                words.insert(index, word)
    elif 'Sort' in cmd_list:
        words.sort(reverse=True)
    elif 'Replace' in cmd_list:
        word1 = cmd_list[1]
        word2 = cmd_list[2]
        if word2 in words:
            first = words.index(word2)
            words[first] = word1
    cmd = input()
printable = ' '.join(words)
print(printable)