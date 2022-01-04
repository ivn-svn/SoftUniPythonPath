# 	Capitals
# Using a dictionary comprehension, write a program that receives country names on the first line, 
# separated by comma and space ", ", and their corresponding capital cities on the second line 
# (again separated by comma and space ", "). Print each country with their capital on a separate 
# line in the following format: "{country} -> {capital}".
country = input().split(', ')
capital = input().split(', ')
capitals_countries = zip(country, capital)
for (keys, values) in capitals_countries:
    print(f"{keys} -> {values}")
#