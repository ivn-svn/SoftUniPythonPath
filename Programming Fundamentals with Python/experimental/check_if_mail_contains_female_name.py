import re
names = input()
regex = '\\w*\\.\\w*ova@\\w*\\.com'
regex1 = '\\w*\\.\\w*ov@\\w*\\.com'
girls = re.findall(regex, names)
boys = re.findall(regex1, names)
print(len(girls))
print(len(boys))