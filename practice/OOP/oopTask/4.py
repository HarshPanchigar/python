class Animal:
    def eat(self):
        print("Eat from mouth & drink by lick")

class Dog(Animal):
    def bark(self):
        print("Bark.... Bark....")

dog = Dog()
dog.eat()
dog.bark()