def wrapThis(a):
    a = str(a).upper()
    return a 

@wrapThis
def msgReturnAsList(msg):
    msg = list(msg)
    return msg

b = "Convert to upper and output it as a list of letters."
print(msgReturnAsList(b))

`TypeError: 'str' object is not callable` when a decorator function is caleld

I get a `TypeError: 'str' object is not callable` when a decorator function is caleld. E.g. I
call the function `msgReturnAsList`, which is actually meant to return a list and therefore I do not understand why is it throwing an error that a `str object is not callable`.

I read at [FreeCodeCamp](https://www.freecodecamp.org/news/typeerror-str-object-is-not-callable-how-to-fix-in-python/) that this TypeError occurs mainly in two occasions, neither of which has anything to do with my case:
    1."If You Use str as a Variable Name in Python"
    2. "If You Call a String Like a Function in Python"

Can somebody clarify what is the logic behind this and how do I get `msgReturnAsList` to return the string converted to upper by `wrapThis` and then converted to a list by the problematic decorator function `msgReturnAsList`?
