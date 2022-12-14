from collections import deque
# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2
days = 0
mnt_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
food, stamina = deque([int(x) for x in input().split(", ")]), deque([int(z) for z in input().split(", ")])
climbed_peaks = list()
food_copy = food.copy()
stamina_copy = stamina.copy()
mnt_peaks_list = list(mnt_peaks.keys())
mnt_peaks_list_copy = deque(mnt_peaks_list.copy())
#print(mnt_peaks_list)
mnt_peak_ctr = 0 

while food_copy and stamina_copy and mnt_peaks_list_copy:
    current_peak = mnt_peaks_list[mnt_peak_ctr]
    current_day_res = food[len(stamina) - days - 1] + stamina[days]
    if mnt_peaks[current_peak] <= current_day_res and mnt_peak_ctr < len(mnt_peaks_list):
        food_copy.pop()
        stamina_copy.popleft()
        climbed_peaks.append(current_peak)
        mnt_peak_ctr += 1
        mnt_peaks_list_copy.popleft()
    else:
        food_copy.pop()
        stamina_copy.popleft()
    days += 1
    




if len(climbed_peaks) == len(mnt_peaks_list):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else: 
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if len(climbed_peaks) > 0:
    print("Conquered peaks:")
    for printpeak in climbed_peaks:
        print(printpeak, end="\n")



