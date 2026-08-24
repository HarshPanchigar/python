class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    
    def __init__(self, name,roll):
        super().__init__(name)
        self.roll = roll

    def roll_no(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
    
std = Student("Harsh" , 101)
std.roll_no()