from collections import deque
from math import dist

n_petrol_pumps = int(input())
petrol_tank = 0 
thestation = 1
petrol_amounts = []
distances = []
filler = 0 
counter = 1
for pump in range(n_petrol_pumps):
    cmd = input()
    petrol_amount = int(cmd.split(' ')[1])
    distance_pump = int(cmd.split(' ')[0])
    petrol_amounts.append(petrol_amount)
    distances.append(distance_pump)


capacity = sum(petrol_amounts)
therange = sum(distances)

lengthy = len(petrol_amounts)

petrol_amounts = deque(petrol_amounts)
distances = deque(distances)

while petrol_amounts:
    pamount = petrol_amounts.popleft()
    distance = distances.popleft()
    filler += pamount
    if filler >= therange:
        thestation = counter
        break
    else: 
        counter += 1 


print(thestation)
