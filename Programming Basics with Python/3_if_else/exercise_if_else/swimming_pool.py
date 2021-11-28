record = float(input())
distance_meters = float(input())
meters_second = float(input())
# край на прочетеното от конзолата /\
# дали дистанцията вече е поне 15 метра.
distance_divided = distance_meters // 15 # За да получа колко пъти Иван ще се забави, деля дистанцията, която изминава
distance_divided *= 12.5 # умножавам по забавянето
ivan_time = float(distance_meters * meters_second + distance_divided)
seconds_needed = abs(record - ivan_time) # разликата между рекорда и времето на Иван са секундите,
# които няма да му стигат.
if ivan_time < record:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
