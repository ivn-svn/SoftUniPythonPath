# https://pythonexamples.org/python-dictionary-methods/#10

# fromkeys()

# Dictionary fromkeys() method creates a new dictionary from the keys of given dictionary and an optional default value for the key-value pairs.
#
# Python Program

dictionary = {"a": 4, "b": 5, "c": 6}
dictionary_1 = dict.fromkeys(dictionary, 1)
print(dictionary_1)