# Slicing or substring with start-index, end-index and step.
s = 'This is to demonstrate substring functionality in python.'
print(s[12:22:2])
# Output: ‘eosrt’

# Slicing or substring with start-index, end-index and --> w i t h o u t <-- step.
s = 'This is to demonstrate substring functionality in python.'
print(s[12:22])
# Output: ‘emosntrate’
# print only EVENS in the list:
print(s[::2])
# print only ODDS in the list:
print(s[1::2])
