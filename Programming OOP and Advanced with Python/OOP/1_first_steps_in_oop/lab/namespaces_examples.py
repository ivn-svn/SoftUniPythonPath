# Pretty good explanation of Namespaces in the below link: 
# https://www.programiz.com/python-programming/namespace
#
# To simply put it, a namespace is a collection of names.
#
# In Python, you can imagine a namespace as a mapping of every
#  name you have defined to corresponding objects.
#
# Pretty good examples of namnespaces in below link
# https://code.tutsplus.com/tutorials/what-are-python-namespaces-and-why-are-they-needed--cms-28598
def outer_func():
    c_num = 12
    def inner_func():
        d_num = 13
        print(dir(), ' - names in inner_func')
    e_num = 14
    inner_func()
    print(dir(), ' - names in outer_func')
     
outer_func()
# ['d_num']  - names in inner_func
# ['c_num', 'e_num', 'inner_func']  - names in outer_func

a_num = 10
b_num = 11
 
def outer_func():
    global a_num
    a_num = 15
    b_num = 16
    def inner_func():
        global a_num
        a_num = 20
        b_num = 21
        print('a_num inside inner_func :', a_num)
        print('b_num inside inner_func :', b_num)
    inner_func()
    print('a_num inside outer_func :', a_num)
    print('b_num inside outer_func :', b_num)
     
outer_func()
print('a_num outside all functions :', a_num)
print('b_num outside all functions :', b_num)
 
# a_num inside inner_func : 20
# b_num inside inner_func : 21
 
# a_num inside outer_func : 20
# b_num inside outer_func : 16
 
# a_num outside all functions : 20
# b_num outside all functions : 11