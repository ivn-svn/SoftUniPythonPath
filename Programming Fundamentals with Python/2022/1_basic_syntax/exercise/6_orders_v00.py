order_num = int(input())
#
total_price = 0
price = 0
per_capsule = 0
days = 0
caps_count = 0 
#
price_list = []
for i in range(0, order_num):
    per_capsule = float(input())
    days = int(input())
    caps_count = int(input())
#
    price = days * per_capsule * caps_count
    price_list.append(price)
    total_price += price
    
for p in price_list:
    print(f"The price for the coffee is: ${p:.2f}")
print(f"Total: ${total_price:.2f}")