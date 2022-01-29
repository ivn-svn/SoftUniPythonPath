# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# create a list
# Source: https://www.programiz.com/python-programming/methods/list/extend
prime_numbers = [2, 3, 5]

# create another list
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]


#  C O P Y

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()


print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]