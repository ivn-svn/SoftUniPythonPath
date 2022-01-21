# You will be given a sequence of strings, each on a new line.
# Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on)
# and every even – quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]
#resource = input()

# Решението само от 2_miner_task_v_1 работи.
line_count = 1
resources = {}
resource_amount = 0
print(line_count)
resource = ''
def resource_input():
    resource = input()

def resource_check(resources, resource_amount):
    if line_count % 2 == 1:
        if resource in resources:
            pass
        else:
            resources[resource] = []
    elif line_count % 2 == 0:
        resource_amount = input()
        resources[resource] += resource_amount


while True:
    if resource == "stop":
        break
    else:
        line_count += 1
        resource_check(resource, resource_amount)
        # resource_check()
    print(line_count)
print(f'{resource} -> {resource_amount}')