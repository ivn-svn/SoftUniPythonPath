# Charity Campaign Задача 6 Simple Operations and Calculations
days_of_the_campaign = int(input())
confectioner_number = int(input())
cake_number = int(input())
waffle_number = int(input())
pancake_number = int(input())
#
cake = float(45)
waffle = float(5.80)
pancake = float(3.20)
#
final_sum = (((cake_number * cake)
            + (waffle_number * waffle)
            + (pancake_number * pancake)) * days_of_the_campaign) * confectioner_number
product_expense = final_sum / 8
final_final_sum = final_sum - product_expense
print(f'{final_final_sum:.2f}')