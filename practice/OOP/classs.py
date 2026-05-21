class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"Congratulations {self.name} you scored {self.marks} marks")

all_students = []
for i in range(3):
    name = input("Enter students name: ")
    marks = input("Enter students marks: ")

    obj = Students(name,marks)
    all_students.append(obj)
    
print("\n--- Student Details ---\n")

for i in all_students:
    i.show()