class Class:
    def __init__(self, class_name: str):
        self.average_grade = 0
        self.class_name = class_name
        self.students = []
        self.grades = []
        self.__students_count = 22

    def add_student(self, name: str, grade: float):
        self.name = name
        self.grade = grade
        self.students.append(self.name)
        self.grades.append(grade)

    def get_average_grade(self):
        grades_sum = sum(self.grades)
        average_grade = grades_sum / len(self.grades)
        return average_grade

    def __repr__(self):
        if len(self.students) < self.__students_count and self.name != '' and self.class_name != '':

            studs_output = ', '.join(self.students)
            self.average_grade = Class.get_average_grade(self)
            return "The students in {}: {}. Average grade: {:0.2f}".format(self.class_name, studs_output, self.average_grade)


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)

# a_class = Class("11B")
# a_class.add_student("", 0)
# # a_class.add_student("George", 6.00)
# # a_class.add_student("Amy", 3.50)

print(a_class)

# Ref link:
# https://www.studytonight.com/python-howtos/how-to-round-floating-value-to-two-decimals-in-python
