#
#   https://pynative.com/python-class-method/#:~:text=Delete%20Class%20Methods-,What%20is%20Class%20Method%20in%20Python,can%20access%20only%20class%20variables
#


from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

# jessa = Student('Jessa', 20)
# jessa.show()
#
# # create new object using the factory method
# joy = Student.calculate_age("Joy", 1995)
# joy.show()

class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student1('Peter', 20)
jessa.show()

# create new object using the factory method
joy = Student1.calculate_age("Joy", 1995)
joy.show()