class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} Your AVG is : {sum/3:.2f}")

s1 = Students("Harsh",[80,85,83])
s1.get_marks()
s1.hello()