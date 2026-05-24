class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluct = False

    def car_start(self):
        self.acc = True
        self.brk = True
        self.cluct = True
        print("Car start....")

car = Car()
car.car_start()