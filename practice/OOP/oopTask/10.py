class Employee:
    total_employees = 0
    def __init__(self,name):
        self.name = name
        Employee.total_employees += 1

    @classmethod
    def show(cls):
        print(cls.total_employees)

e1 = Employee("Harsh")
e2 = Employee("Rahul")
e3 = Employee("Amit")

Employee.show()