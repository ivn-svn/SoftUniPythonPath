from functools import wraps
def uppercase(func): # The **Decorator**
    @wraps(func)
    def wrapper():
        result = func()
        return result.upper()
    return wrapper