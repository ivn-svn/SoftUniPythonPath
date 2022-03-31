# Your task here is to define how much coffee you need to stay awake after your night. Until you receive the command
# "END", you need to read a single command, according to this command you will print the number of coffee you need
# to stay awake during day time.
# Note: If the count exceed 5 please return 'You need extra sleep'.
# The list of events can contain the following:
# You have homework to do ('coding').
# You have a dog or a cat that just decide to wake up too early ('dog' or 'cat').
# You just watch a movie ('movie').
# Other events can be present and it will be represent by arbitrary string, just ignore this one.
# Each event can be lowercase, or uppercase. If it is lowercase you need 1 coffee by events and
# if it is uppercase you need 2 coffees.
#
#
activities = ['dog', "cat", "coding", "movie"]
#
#
command = ''
#
coffees = 0
#
counter = 0
while command.lower() != "end":
    command = input()
    counter += 1
    if counter > 5:
        print("You need extra sleep")
        break
    else:
        if command.lower() in activities:
            if command.isupper():
                coffees += 2
            elif command.islower():
                coffees += 1
        elif command not in activities:
            continue
else:
    print(f"{coffees}")
