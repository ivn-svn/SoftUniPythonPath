# Create a program that checks if inputs are valid and decrypt it. On the first line you will receive a number that
# indicates how many inputs you will receive on the next lines
#|GEORGI|:#Lead architect#
n = int(input())
data_input = ''
data_input1 = ''
for x in range(0, n):
    data_input1 = input()
    data_input = data_input1.split(":")
    boss_name = data_input[0].replace("|", "")
    title = data_input[1].replace("#", "")
    name_len = len(boss_name)
    title_len = len(title)
    p = title.split(" ")
    lower = p[1]
    if name_len >= 4 and boss_name.isupper():
        if "|" in data_input[0] and len(p) <= 2:
            if not lower[0].isupper():
                print(f"\n{boss_name}, The {title}"
                      f"\n>> Strength: {name_len}\n"
                      f">> Armour: {title_len}")
            else:
                print("Access denied!")
        else:
            print("Access denied!")
    else:
        print("Access denied!")



        #     if data_input1.count("|") == 1: