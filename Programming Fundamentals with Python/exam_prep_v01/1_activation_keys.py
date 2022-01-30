# Submit @ https://judge.softuni.org/Contests/Practice/Index/2302#0.
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.


def do_what_func(cmd, dow):
    global swaped

    global raw_activation_key
    if dow == contains:
        substr = cmd[1]
        if substr in raw_activation_key:
            appendix = f"{raw_activation_key} contains {substr}"
            events.append(appendix)
        else:
            appendix = f"Substring not found!"
            events.append(appendix)

    elif dow == flip:

        letters_case = cmd[1]
        start = int(cmd[2])
        end = int(cmd[3])
        slicable = slice(start, end)
        replacable = raw_activation_key[slicable]
        if letters_case.lower() == 'lower':
            swaped = replacable.lower()
        elif letters_case.lower() == 'upper':
            swaped = replacable.upper()
        raw_activation_key = raw_activation_key.replace(replacable, swaped)
        appendix = raw_activation_key
        events.append(appendix)
    elif dow == sliced:
        start = int(cmd[1])
        end = int(cmd[2])
        slicable = slice(start, end)
        replacable = raw_activation_key[slicable]
        raw_activation_key = raw_activation_key.replace(replacable, '')
        appendix = raw_activation_key
        events.append(appendix)
    return raw_activation_key, events


events = []

raw_activation_key = input()
gen = False
contains = "Contains"
flip = "Flip"
sliced = "Slice"
while gen == False:
    command = input()
    if command == "Generate":
        gen = True
        break
    else:
        command = command.split('>>>')
        do_what = command[0]
        raw_activation_key, events = do_what_func(command, do_what)

for event in events:
    print(event)
print(f"Your activation key is: {raw_activation_key}")