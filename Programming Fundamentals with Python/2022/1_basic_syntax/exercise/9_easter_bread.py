#     9. * Easter Bread
# Create a program that calculates how many loaves you can make with the budget you have.

# You will receive your budget. 
# Then, you will receive the price for 1 kg flour. 

# Recipe:
# Eggs: 1 pack
# Flour: 1 kg
# Milk: 0.25 l

# The price for 1 pack of eggs is 75% of the price for 1 kg flour. 

# The price for 1l milk is 25% more than the price for 1 kg flour. 

# Notice that you need 0.250l milk for one bread, and the calculated price is for 1l.

# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
#     • For every bread that you make, you will receive 3 colored eggs. 
#     • For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread. 
# 
# The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves – ({current_bread_count} – 2)
# In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have left, formatted to the 2nd decimal place, in the following format:

# "You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."

loaves = 0
budget = 0
#
current_bread_count = 0
# Counter
counter = 0


# Input by the user:
budget_input = input()
flour_price_kg = input()

# Basic calculus:
eggs = flour_price_kg * 0.75
milk_price = (0.25 * flour_price_kg) + flour_price_kg

# What is needed to cook the bread?
milk_needed_for_bread = milk_price * 0.25 

# 0.25 milk is needed for 1 bread! **********
number_of_bread = 0
colored_eggs = 0
money_left = 0

# Start cooking:
while True:
    for i in range():
        pass
else:
    print(f"You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")

#
recipe = eggs + flour_price_kg + milk_price


({current_bread_count} – 2)