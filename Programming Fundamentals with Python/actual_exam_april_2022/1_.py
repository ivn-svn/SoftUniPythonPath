init_str = input()
line = input()
while line != "End":
    line_split = line.split(" ")
    cmd = line_split[0]
    if cmd == "Translate":
        character = line_split[1]
        replacement = line_split[2]
        occ_count = init_str.count(character)
        init_str = init_str.replace(character, replacement, occ_count)
        print(init_str)
    elif cmd == "Includes":
        substr = line_split[1]
        splited_init_str = init_str.split(" ")
        if substr in splited_init_str:
            print("True")
        else:
            print("False") # To check if False as a content is the same as false as a str
    elif cmd == "Start":
        substr = line_split[1]
        splited_init_str = init_str.split(" ")
        if substr in splited_init_str[0]:
            print("True")
        else:
            print("False")
    elif cmd == "Lowercase":
        for letter in init_str:
            if letter.isalnum():
                replacable = letter.lower()
                init_str = init_str.replace(letter, replacable)
        print(init_str)
    elif cmd == "FindIndex":
        found_char = line_split[1]
        idx = init_str.rfind(found_char)
        print(idx)
    elif cmd == "Remove":
        start = int(line_split[1])
        end = start + int(line_split[2])
        # num_to = end - start
        # end = num_to + start + 1
        # init_str = init_str[end+1:len(init_str)]
        # notincl = init_str[start:end]
        # for letter in range(start, end):
        #     list_init = list(init_str)
        #     new_list = list_init.pop(letter)
        repl = init_str[start:end]
        init_str = init_str.replace(repl, '')
        # removable = init_str[start:end]
        # print('Rem : ' + removable)
        # init_str = init_str.replace(removable, '')
        print(init_str)
    line = input()
