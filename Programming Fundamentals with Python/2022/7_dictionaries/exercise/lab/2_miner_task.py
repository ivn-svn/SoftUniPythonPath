# You will be given a sequence of strings, each on a new line. Every odd line on the console represents a resource
# (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources
# and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
# Gold -> 155
# Silver -> 10
# Copper -> 17
def resource_collector(cmd, ln):
    if cmd.isnumeric():
        resources_dict[len(resources_dict)] += int(cmd)
        ln += 1
    elif cmd.isalpha():
        resources_dict[cmd] = 0
        commands_list.append(cmd)
    return resources_dict


command = input()
line = 0
commands_list = []
resource = ''
amount = 0
resources_dict = {}
while command != 'stop':
    command = input()
    resources_dict = resource_collector(command, line)
else:
    print(resources_dict)
