# Write a program that prints you a receipt for your new computer. You will receive the parts' ' \
#         'prices (without tax) until you receive what type of customer this is - ' \
#         'special or regular. Once you receive the type of customer you should print the receipt.

command = ''

end = False
total_price = 0
price_wo_tax = 0
taxes = 0
special = False


while end == False:
    command = input()
    price = 0
    tax = 0
    if command.lower() == "":
        print(f"Invalid order!")
    elif command.lower() == "special":
        special = True
        end = True
        break
    elif command.lower() == "regular":
        end = True
        break
    else:
        price = float(command)
        if price < 0:
            print("Invalid price!")
        else:
            tax = price * 0.20
            taxes += tax
            total_price += price + tax
            price_wo_tax += price

if special:
    total_price *= 0.90

if total_price == 0:
    print("Invalid order!")
else:
    receipt = "Congratulations you've just bought a new computer!\n"
    receipt += f"Price without taxes: {price_wo_tax:.2f}$\n"
    receipt += f"Taxes: {taxes:.2f}$\n"
    receipt += f"-----------\n"
    receipt += f"Total price: {total_price:.2f}$"
    print(receipt)