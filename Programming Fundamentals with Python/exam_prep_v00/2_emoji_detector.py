# https://judge.softuni.org/Contests/Practice/Index/2302#1
import re

pattern = r"(?<=::)([A-Z][a-z][a-z]+)(?=::)|(?<=\*\*)([A-Z][a-z][a-z]+)(?=\*\*)"
originals_pattern = r"(\:\:[A-Z][a-z][a-z]+\:\:)|(\*\*[A-Z][a-z][a-z]+\*\*)"
patternd = r"(\d)"
output = []
cool_threshold = []
originals_list = []
sum_cool_threshold = 1
user_input = input()

matches = re.findall(pattern, user_input)
num_matches = re.findall(patternd, user_input)
originals_matches = re.findall(originals_pattern, user_input)
for m in matches:
    for mm in m:
        if mm:
            # print(mm)
            output.append(mm)


for num in num_matches:
    for n in num:
        # if num:
        # print(n)
        cool_threshold.append(int(n))
        sum_cool_threshold *= int(n)
# sum_cool_threshold = math.prod(cool_threshold)

for original in originals_matches:
    for theoriginal in original:
        if theoriginal:
            # print(theoriginal)
            originals_list.append(theoriginal)

print(f"Cool threshold: {sum_cool_threshold}")
cool_ones = "\n".join(output)
printoriginals = "\n".join(originals_list)
print(f"{len(output)} emojis found in the text. The cool ones are: \n{printoriginals}")
