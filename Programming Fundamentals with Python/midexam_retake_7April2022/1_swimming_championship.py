pts_won = 0
daily_pts = 0


def calc_sponsorship(sponshorship_percentage, all_costs):
    discount = all_costs * sponshorship_percentage
    money = all_costs - discount
    return money


champ_days = int(input())
pts_cover = int(input())
swimmers_count = int(input())
hotel_room_price = float(input())
participation_fee = float(input())

hotel_exp = swimmers_count * hotel_room_price * champ_days
participation_cost = participation_fee * swimmers_count
all_costs = hotel_exp + participation_cost

for day in range(0, champ_days):
    if day >= 1:
        pts_won += daily_pts * 0.05
    daily_pts = float(input())
    pts_won += daily_pts

if pts_won >= pts_cover:
    sponshorship_percentage = 0.25
    money = calc_sponsorship(sponshorship_percentage, all_costs)
    print(f"Money left to pay: {money:.2f} BGN.\nThe championship was successful!")
elif pts_won < pts_cover:
    sponshorship_percentage = 0.10
    money = calc_sponsorship(sponshorship_percentage, all_costs)
    print(f"Money left to pay: {money:.2f} BGN.\nThe championship was not successful.")