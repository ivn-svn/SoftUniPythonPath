# 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
century_input = int(input())
years = century_input * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f'{century_input} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')