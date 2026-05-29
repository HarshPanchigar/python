# Class inheritance 

class Car:
    @staticmethod
    def start():
        print("Car Start...")

    @staticmethod
    def stop():
        print("Car stop...")

class Toyota(Car):
    def __init__(self,name):
        self.name = name
        print(self.name)

c1 = Toyota("Fortuner")
print(c1.start())
print(c1.stop())