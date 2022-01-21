# The code should match all dates that are given in the following format: "dd{separator}MMM{separator}yyyy"

# example input:
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
import re

pattern = "\\b(\\d{2})([-.\/])([A-Z][a-z]{2})\\2(\\d{4})\\b"
#user_input = "13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016"
user_input = input()

matches = re.findall(pattern, user_input)
def out_func():
    for match in matches:
        print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")


out_func()
