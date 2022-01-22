keys = ("name", "surname")
values = ("John", "Doe")
zipped = list(zip(keys, values))
print(zipped)
d = dict(zipped); d
print(d)