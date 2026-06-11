class Employee:
    total_employees = 0

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary

        Employee.total_employees += 1

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.__salary}")
        print("-" * 30)

    @classmethod
    def show_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")

    @staticmethod
    def company_rules():
        print("\nCompany Rules:")
        print("1. Be punctual")
        print("2. Complete your tasks on time")
        print("3. Maintain professionalism")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.get_salary()}")
        print(f"Department: {self.department}")
        print("-" * 30)


employees = []
managers = []

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Show Employees")
    print("4. Show Managers")
    print("5. Show Total Employees")
    print("6. Show Company Rules")
    print("7. Polymorphism Demo")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter Salary: "))

        emp = Employee(name, emp_id, salary)
        employees.append(emp)

        print("Employee Added Successfully!")

    elif choice == "2":
        name = input("Enter Name: ")
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, emp_id, salary, department)
        managers.append(manager)

        print("Manager Added Successfully!")

    elif choice == "3":
        if not employees:
            print("No Employees Found!")
        else:
            print("\n===== EMPLOYEES =====")
            for emp in employees:
                emp.show_info()

    elif choice == "4":
        if not managers:
            print("No Managers Found!")
        else:
            print("\n===== MANAGERS =====")
            for manager in managers:
                manager.show_info()

    elif choice == "5":
        Employee.show_total_employees()

    elif choice == "6":
        Employee.company_rules()

    elif choice == "7":
        print("\n===== POLYMORPHISM DEMO =====")

        items = []

        if employees:
            items.append(employees[0])

        if managers:
            items.append(managers[0])

        if not items:
            print("Add at least one Employee or Manager first.")
        else:
            for item in items:
                item.show_info()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")