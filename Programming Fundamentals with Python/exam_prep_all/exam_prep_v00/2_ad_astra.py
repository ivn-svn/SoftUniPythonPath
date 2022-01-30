# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#1.
#
# You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a
#     long time, you have packed a lot of food with you. Create a program, which helps you identify how much food you
#     have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. You must extract the information about the food and
# calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
# It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# The item name will contain only lowercase and uppercase letters and whitespace
# The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be
# exactly two digits long
# The calories will be an integer between 0-10000
# Calculate the total calories of all food items and then determine how many days you can last with the food you have.
# Keep in mind that you need 2000kcal a day.
import re



total_calories = 0
def split_items(lstp, tcal):
    pri = []
    for item in lstp:
        item_splited = item.strip("#|")
        item_splited = re.split("\#|\|", item_splited)
        item_name = item_splited[0]
        date = item_splited[1]
        calories = int(item_splited[2])
        tcal += calories
        pri.append(f"Item: {item_name}, Best before: {date}, Nutrition: {calories}")
    days = tcal // needed_kcal
    days = int(days)
    print(f"You have food to last you for: {days} days!")
    for p in pri:
        print(p)
    return pri, tcal, days

text_string = input()


item_name = ''
expiration_date = ''
calories = 0
days = 0
# Operation vars:
date = ''

#
needed_kcal = 2000
#
# The solution should consist of 2 parts:
# 1. Regex to find the relevant data
# 2. Algorithm to calculate food supply per day

#
txt = text_string
list_products = re.findall(r"\#\w*\#\d*\/\d*\/\d*\#\d*\#|\|\w*\|\d*\/\d*\/\d*\|\d*\||\#\w*\s\w*\#\d*\/\d*\/\d*\#\d*\#", txt)


printable, total_calories, days_ = split_items(list_products, total_calories)
#print(total_calories)

# print(f"You have food to last you for: {days} days!")
#
#
# print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
