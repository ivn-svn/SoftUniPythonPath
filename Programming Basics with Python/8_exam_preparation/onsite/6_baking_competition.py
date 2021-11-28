num_bakers = 0
baker = str(input())
type_sweet = str(input())
#
# 1. Read count of competitors
competitors_count = int(input())
# 2. For each competitor
for competitor in range(competitors_count):
    name = input()
    cookies_counter = 0
    cakes_counter = 0
    waffles_counter = 0
    # 2.1. Until stop baking!
    command = input()
    while command != 'Stop baking!':
        pastry_type = command
# 2.1.1. Read pastry count
        int(input())
# 2.1.2. Read pastry type
    pastries_count = int(input())
    if pastry_type == 'cookies':
        cookies_counter = pastries_count
    elif pastry_type == 'cookies':
        cookies_counter += pastries_count
    elif pastry_type == 'cakes':
        cakes_counter += pastries_count
    elif pastry_type == 'waffles':
        waffles_counter += pastries_count
# 2.3. Add count of each pastry to total
    print(f'{name} baked {cookies_counter} cookies, {cakes_counter} cakes and {waffles_counter} waffles.')
    # 3. Calculate total money
    total_pastries_made = cookies_counter + cakes_counter + waffles_counter
    total_cookies_counter += cookies_counter
    total_cakes_counter += cakes_counter
    total_waffles_counter += waffles_counter
total_pastries_made += total_cookies_counter + total_cakes_counter + total_waffles_counter
cookies_money = total_cookies_counter * 1.5
cakes_money = total_cakes_counter * 7.80
waffles_money = total_waffles_counter * 2.3
total_money = cookies_money + cakes_money + waffles_money
print(f'All bakery sold: {total_pastries_made}')
print(f'Total sum for charity: {total_money:.2f}')