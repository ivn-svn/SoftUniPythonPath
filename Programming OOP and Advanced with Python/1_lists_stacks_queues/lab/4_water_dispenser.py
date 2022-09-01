# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".

'''
# PSEUDO



'''

from collections import deque

def refill_water(starting_qty, refill_val):
    starting_qty += refill_val
    return starting_qty

starting_qty = int(input())
#cmd = input()
cmd = "2\nPeter\nAmy\nStart\n2\nrefill 1\n1\nEnd\n".split("\n")

ppl_q = []
for line in cmd:
    while line !=  "End": # Replace with ifs when testing real input data
        while line != "Start": # Replace with ifs when testing real input data
            ppl_q.append(line)
        for person in ppl_q:
            if "refill" in line:
                refill_val = int(line)
                starting_qty = refill_water(starting_qty, refill_val)
            else:
                if line.isnumeric():
                    if starting_qty - int(line) > 0:
                        starting_qty -= int(line)
                        person_name = line
                        ppl_q.popleft(person_name)
                        print("{person_name} got water")
                    else:
                        person_name = line
                        ppl_q.popleft(person_name)
                        print("{person_name} must wait")

print("{starting_qty} liters left")
    #cmd = input()
