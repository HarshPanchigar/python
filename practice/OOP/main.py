#methods = methods is a function associated with class
class nameAge:
    # name = "Harsh Panchigar"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # print(f"Hello From INIT... {self.name}")
    def Pname(self):
        print(f"Hello From function... {self.name} and age is {self.age}")

obj = nameAge("Harsh",20)
obj.Pname()