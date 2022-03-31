# You will be given a sequence of strings, each on a new line.
# Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on)
# and every even – quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]
resources_gathered = {}
true_check = True

def seq_string(a, b):
    if a not in resources_gathered:
        resources_gathered[a] = b
    elif a in resources_gathered:
        resources_gathered[a] += b
    return resources_gathered


while true_check:
    resource = str(input())
    if resource.lower() == "stop":
        for (key, value) in resources_gathered.items():
            print(f"{key} -> {value}")
        true_check = False
        #break
    else:
        amount_resource = int(input())
        seq_string(resource, amount_resource)




