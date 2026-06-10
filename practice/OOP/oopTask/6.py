class Dog:
    def sound(self):
        print("Dog -> Bark")
class Cat:
    def sound(self):
        print("Cat -> Meow")
class Cow:
    def sound(self):
        print("Cow -> Moo")

dog = Dog()
cat = Cat()
cow = Cow()

animal = [dog,cat,cow]

for animals in animal:
    animals.sound()