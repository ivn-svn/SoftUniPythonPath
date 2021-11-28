# Изпитна задача
length = int(input())
width = int(input())
height = int(input())
percent_volume_taken = float(input())

total_volume = length * width * height
total_volume = total_volume / 1000
percent = percent_volume_taken * 0.01
volume_taken = total_volume * percent
volume_left = total_volume - volume_taken
print(f'{volume_left:.3f}')