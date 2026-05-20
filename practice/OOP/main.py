#methods = methods is a function associated with class
class nameAge:
    # name = "Harsh Panchigar"
    def __init__(self,name):
        self.name = name
        # print(f"Hello From INIT... {self.name}")
    def Pname(self):
        print(f"Hello From function... {self.name}")

obj = nameAge("Harsh")
obj.Pname()