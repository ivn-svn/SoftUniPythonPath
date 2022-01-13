# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". 

# # Use capturing groups in your regular expression.
# # Every valid date has the following characteristics:
#     • It always starts with two digits, followed by a separator
#     • After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
#     • After that, it has a separator and exactly 4 digits (for the year).
#     • The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
#     • The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a group backreference to check for this.
import re
pattern = r"(\d{2}[/][A-Z]{1}[a-z]{2}[/]\d{4})|(\d{2}[.][A-Z]{1}[a-z]{2}[.]\d{4})|(\d{2}[-][A-Z]{1}[a-z]{2}[-]\d{4})"
user_input = input()
matches = re.findall(pattern, user_input)
final_list = []
for match in matches: 
    
    for x in match:
        if x != '':

            if "/" in x and len(x) > 0:
                x = x.split("/")
            elif "." in x and len(x) > 0:
                x = x.split(".")
            elif "-" in x and len(x) > 0:
                x = x.split("-")
            x = tuple(x)

            final_list.append(x)


for z in final_list:
    print(f"Day: {z[0]}, Month: {z[1]}, Year: {z[2]}")