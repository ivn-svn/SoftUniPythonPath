import re
txt = "The rain in Spain"
str = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("ai", str)
print(x, y)