# Create three decorators: make_bold, make_italic, make_underline, 
# which will have to wrap a text returned from a function 
# in <b></b>, <i></i> and <u></u> respectively.


def make_bold(func_ref):  
    def wrapper(*args):
        return "<b>" + func_ref(*args) + "</b>"
    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        return "<i>" + func_ref(*args) + "</i>"
    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        return "<u>" + func_ref(*args) + "</u>"
    return wrapper


@make_bold
@make_italic
@make_underline


def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
#print(greet_all("Peter", "George"))
