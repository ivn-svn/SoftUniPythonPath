budget = float(input())
season = input()
#
destination = ""
type = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        type = "Camp"
    elif budget >= 100 and budget <= 1000:
        destination = "Balkans"
        price = budget * 0.7
        type = "Hotel"
    elif budget >= 1000:
        destination = "Europe"
        if season == "summer":
            price = budget * 0.4
    else:
        price = budget * 0.8
        type = "Hotel"
else:
    destination = "Europe"
    price = budget * 0.9
    type = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type} - {price:.2f}")
#