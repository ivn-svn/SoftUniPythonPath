# 1 Input data
sea = input()
cabin_type = input()
#
nights_count = int(input())
# 2. Where to sail | Check sea
price_per_night = 0
if sea == 'Mediterranean':
    if cabin_type == 'standard cabin':
        price = 27.5
    elif cabin_type == 'cabin with balcony':
        price = 30.2
    elif cabin_type == 'apartment':
        price = 40.5
elif sea == 'Adriatic':
    # standard
    # balcony
    # apartment
    pass
elif sea == 'Aeggean':
    pass
total_cost = price * 4 * nights_count
print(total_cost)
# 2.2. Define price per night
# 3. Calculate price without discount
# 4. Check night count > 7 -> discount
# 5. Print
if nights_count > 7:
    total_cost *= 0.75
print(f'Annie\'s holiday in the {sea} costs {total_cost:.2f} lv.')

