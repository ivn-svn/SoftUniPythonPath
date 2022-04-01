# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
train_ticket = 150
#
maximum_clothes, maximum_shoes, maximum_accessories = 50.00, 35.00, 20.50
maximum_list = [maximum_clothes, maximum_shoes, maximum_accessories]
#
clothes, shoes, accessories = 'Clothes', 'Shoes', 'Accessories'
items_list = [clothes, shoes, accessories]
# Input variables:
collection = input().split('|')
budget = float(input())
list_bought_items = []
markup_list = []
# For cycle to iterate over the list:
for iterable in collection:
    iterable = iterable.split('->')
    item = iterable[0]
    price = float(iterable[1])
    for maximum in items_list:
        if item == maximum:
            idx = items_list.index(item)
    maximum_price = maximum_list[idx]
    if price > maximum_price:
        pass
    else:
        if budget >= price:
            budget -= price
            new_price = float(price + price * 0.40)
            markup_list.append(new_price - price)
            list_bought_items.append(item)
            list_bought_items.append(new_price)
            # budget += new_price
        else:
            pass
final_prices = []
for i in range(0, len(list_bought_items), 2):
    it = list_bought_items[i]
    final_price = float(list_bought_items[i + 1])
    final_prices.append(final_price)
    print(f'{final_price:.2f}', end=' ')

profit = sum(markup_list)
budget += sum(final_prices)
print(f"\nProfit: {profit:.2f}")

if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")