class Teacher(Person):


    def teach (self):
        print (f'mr. {self. name} is teaching')
    def __str__(self):      #     self: Name: Doncho; Age: 47; Subject:
        return f' {super().__str__()}; Subject: Python 00P'