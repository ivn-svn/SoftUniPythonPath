password = str(input())
data = str(input())
while len(password) >= 6 <= 10


def pass_validator():


    while data != password:
        data = input()
    print(f"Password is valid")

else:
    if len(password) < 6 or > 10:
        print(f"Password must be between 6 and 10 characters")
    elif ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] not in password:
        print(f"Password must have at least 2 digits")
    elif # check whether the pass has some other signs
        print("Password must consist only of letters and digits")