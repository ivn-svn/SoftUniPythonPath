import re

text_input = input()
pattern = r"(:[A-z])|(:\D)"

matches = re.findall(pattern, text_input)
for match in matches:
    for emoticon in match:
        if emoticon:
            print(emoticon, end="\n")
