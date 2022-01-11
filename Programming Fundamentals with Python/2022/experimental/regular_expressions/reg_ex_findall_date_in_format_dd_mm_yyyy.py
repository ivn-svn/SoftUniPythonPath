# Regular expression:
# \b(\d{2})([-.\/])(\d{2})([-.\/])(\d{4})

# example input:
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
import re

pattern = "\\b(\d{2})([-.\/])(\d{2})([-.\/])(\d{4})"
user_input = input()
output = re.findall(pattern, user_input)
print(output)