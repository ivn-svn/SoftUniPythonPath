record = float(input())
distance_meters = float(input())
meters_second = float(input())
# край на прочетеното от конзолата /\
# distance_meters_minus = distance_meters - 15    # Променлива, с която после в if-a да проверявам,
# дали дистанцията вече е поне 15 метра.
distance_divided = distance_meters // 15 # За да получа колко пъти Иван ще се забави, деля дистанцията, която трябва
distance_divided *= 12.5
ivan_time = float(distance_meters * meters_second + distance_divided)
seconds_needed = abs(record - ivan_time) # разликата между рекорда и времето на Иван са секундите, които няма да му стигат.
# -------->
if distance_meters_minus >= 0: # Проверяваме вече дали е минал първите 15 метра.
    # да измине и чета не остатъка, а произведението на делителя и делимото.
    if distance_divided >= 1: # Ако забавянето, което се случва на всеки 15 метра се съдържа поне веднъж
        # очаквани на всеки 15 метра.
        # в произведението, то го умножавам по секундите, с които Иван ще се забави \/
        if ivan_time < record:
            print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
        else:
            print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
else:
    print(f"No, he failed! He was {seconds_needed:.2f} seconds slower.")
# -------->