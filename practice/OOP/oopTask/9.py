from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started...")

class Bike(Vehicle):
    def start(self):
        print("Bike started...")

car = Car()
bike = Bike()

car.start()
bike.start()