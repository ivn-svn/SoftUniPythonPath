from collections import deque

# caffeine_mgs = "34, 2, 3".split(", ") # take the last caffeine portion
# energy_drinks = deque(int(y) for y in  "40, 100, 250".split(", ")) # take 1st energy drink
caffeine_mgs = input().split(", ") # take the last caffeine portion
caffeine_mgs = [int(z) for  z in caffeine_mgs]
energy_drinks = deque(int(y) for y in  input().split(", ")) # take 1st energy drink

# energy_drinks= deque(input().split(", ")) # take 1st energy drink

total_caffeine = 0
caffeine_in_drink = 0 
while caffeine_mgs and energy_drinks and 0 <= caffeine_in_drink <= 300:
    caffeine = caffeine_mgs.pop()
    drink = energy_drinks.popleft()
    caffeine_in_drink = caffeine * drink

    if total_caffeine + caffeine_in_drink <= 300:
        total_caffeine += caffeine_in_drink 
        
    else:
        total_caffeine -= 30
        energy_drinks.append(drink)


drinks = ""

for d in range(len(energy_drinks)):
    drinks += str(energy_drinks[d]) 
    if d < len(energy_drinks) - 1:
        drinks += ", "


if energy_drinks:
    print(f'Drinks left: {drinks}')
else:
    print(f'At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')
