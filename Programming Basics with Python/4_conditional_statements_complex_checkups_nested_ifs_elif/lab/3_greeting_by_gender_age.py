age = float(input())
gender = input()
#
gender_char = gender.lower() [0]
#
if gender_char == "f" and age < 16:
    print("Miss")
elif gender_char == "f" and age >= 16:
    print("Ms.")
elif gender_char == "m" and age < 16:
    print("Master")
elif gender_char == "m" and age >= 16:
    print("Mr.")