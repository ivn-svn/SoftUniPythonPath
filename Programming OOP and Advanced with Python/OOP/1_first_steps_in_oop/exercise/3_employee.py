# Create class Employee. Upon initialization, it should receive id (number), 
# first_name (string), last_name (string) and salary (number). Create 3 additional instance methods:
# -	get_full_name() - returns "{first_name} {last_name}"
# -	get_annual_salary() - returns the total salary for 12 months
# -	raise_salary(amount) - increases the salary by the given amount and returns the new salary
class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = int(id)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.salary = int(salary)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_annual_salary(self):
        return self.salary * 12
    def raise_salary(self, amount):
        self.amount = int(amount)
        self.salary += self.amount
        return self.salary