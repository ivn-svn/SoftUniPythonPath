area = float(input())
square_meter_cost = float(7.61)
final_price = float(area * square_meter_cost)
discount = float((square_meter_cost * area) * 0.18)
final_price = float(final_price - discount)
print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
# [] Входни данни: Само кв. метри за озеленяване
# [] 7.61 кв. м. цена
# [] отстъпка 18%








































