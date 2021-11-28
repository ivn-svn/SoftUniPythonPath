# https://stackoverflow.com/questions/36544824/getting-only-integers-from-a-list-of-tuples-python-3
from operator import itemgetter
l = [(a, 3), (b, 4), (c, 5), (d, 1), (e,2)]
r = map(itemgetter(1), l)
print(r)