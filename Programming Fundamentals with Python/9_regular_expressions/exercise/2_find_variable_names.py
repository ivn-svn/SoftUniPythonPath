# Write a program that finds all variable names in each string. A variable name starts with an underscore ("_")
# and contains only capital and non-capital letters and digits. Extract only their names without the underscore.
# Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.
# Input
# The _id and _age variables are both integers.
# Calculate the _area of the _perfectRectangle object.
# __invalidVariable _evenMoreInvalidVariable_ _validVariable
#
# Output
# id,age
# area,perfectRectangle
# validVariable
import re
# pattern = r"(?<!_)\w+"
pattern = r"((?<=_)[A-z]+(?=_))|((?<=__)[A-z]+)|((?<=_)[A-z]+)|([A-z]+(?=_))"

user_input = input()
matches = re.finditer(pattern, user_input)
lstmap = []


for match in matches:
    lstmap.append(match.group(0))
print(",".join(lstmap))

