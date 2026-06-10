from abc import ABC , abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,value):
        self.value = value

    def area(self):
        return self.value * self.value


class Circle(Shape):
    def __init__(self,value):
        self.value = value

    def area(self):
        return math.pi * self.value * self.value

square = Square(4)
circle = Circle(3)
print(square.area())
print(circle.area())