from collections import deque
from collections import OrderedDict
time_taken = input().split(" ")  # Time taken to complete a single task
task_numbers = input().split(" ")   # Number of tasks given to programmers 
tasks_dict = OrderedDict({"Darth Vader Ducky": range(0, 61), "Thor Ducky": range(61, 121), "Big Blue Rubber Ducky": range(121, 181), "Small Yellow Rubber Ducky": range(181, 241)})
tasks_amounts = {x: 0 for x in tasks_dict.keys()}
tasks_list = tasks_dict.keys()
# time_taken = "10 15 12 18 22 6".split(" ")
# task_numbers = "12 16 5 6 9 1".split(" ")
time_taken = deque([int(tt) for tt in time_taken])
task_numbers = [int(tn) for tn in task_numbers]
max_val = tasks_dict["Small Yellow Rubber Ducky"]
maxx = list(max_val)[-1]

while time_taken and task_numbers:
    time = time_taken.popleft()
    task = task_numbers.pop()
    task_time_calculation = time * task
    for (award, award_item_range) in tasks_dict.items():
        
        if task_time_calculation in award_item_range:
            tasks_amounts[award] += 1
        else:            
            task -= 2
            if time_taken:
                time_taken.append(time_taken.pop())
            continue

    if not time_taken and not task_numbers:
        break


 #   print(task_time_calculation)
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
# print(tasks_dict)
# print(tasks_amounts)
# for task, value in tasks_dict.items():
for task in tasks_list:
        print(f"{task}: {tasks_amounts[task]}")

