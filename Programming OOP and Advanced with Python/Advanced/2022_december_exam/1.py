from collections import deque

food_supply_portions = input().split(", ")  # sum the quantity of the last daily food portion  
satmina_portions = input().split(", ") # with the quantity of the first daily stamina.
food_supply_portions_ints = [int(f) for f in food_supply_portions]  
satmina_portions_ints = deque([int(s) for s in satmina_portions]) 
peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
all_peaks = peaks.copy()
conquered = deque([])

while food_supply_portions_ints and satmina_portions_ints and peaks.keys():
    food = food_supply_portions_ints.pop()
    stamina = satmina_portions_ints.popleft()
    peaks_list = peaks.keys()
    peaks_list = deque(peaks_list)
    climbing = peaks_list.popleft()
    if food + stamina >= peaks[climbing]:
        conquered.append(climbing)
        del peaks[climbing]
        # print("Food: ", food, "Stamina: ", stamina)
        # print("Peak: ", climbing, "  Value: ",  all_peaks[climbing])
    else:
        peaks_list.appendleft(climbing)

if len(all_peaks.keys()) == len(conquered):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else: 
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if len(conquered) > 0: 
    print(f"Conquered peaks:")
    for peak in conquered:
        print(f"{peak}")
