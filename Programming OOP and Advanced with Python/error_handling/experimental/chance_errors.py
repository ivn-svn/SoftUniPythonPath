def try_raise_exception():
    chance = 0.7
    value = random.random()
    if value < chance:
        raise ValueError ('Invalid value')
# elif value < 0.7:
#
# raise TypeError ('Invalid type')
for i in range (10):
    try:
        try_raise_exception()
        print (f'Try {i}: No exception')
    except ValueError as err:
        print (f'Try {i}: Yes exception: {err} ')
        