class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"My name is {self.name} and I am {self.age} years old"

s1 = Student("Harsh",20)
print(s1.introduction())