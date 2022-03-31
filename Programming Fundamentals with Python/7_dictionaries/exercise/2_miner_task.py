# You will be given a sequence of strings, each on a new line.
# Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on)
# and every even – quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]
#resource = input()


def print_dict(dictionary, template):
    for k, v in dictionary.items():  # k - key, v - value
        print(template.format(k, v))


my_dict = {}
while True:
    command = input()
    if command == 'stop':
        break
    quantity = int(input())
    my_dict.setdefault(command, 0)
    my_dict[command] += quantity
    # print(f'my_dict: {my_dict}')

print_dict(my_dict, "{} -> {}")