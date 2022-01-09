

synonym_dict = {}
n = int(input())
word = ''
synonym = ''
for i in range(0, n):
    word = input()
    synonym = input()
    if word not in synonym_dict:
        synonym_dict[word] = [synonym]
    elif word in synonym_dict:
        synonym_dict[word].append(synonym)

    elif synonym not in synonym_dict[word]:
        synonym_dict[word].append([synonym])
for (keys, values) in synonym_dict.items():
    vallist = [x for x in values]
    vallist = ', '.join(vallist)
    printable = f'{keys} - {vallist}'
    print(printable)