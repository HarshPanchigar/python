class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return f"Area of rectangle is : {self.length * self.width}"

    def perimeter(self):
        return f"Perimeter of rectangle is : {2 * (self.length + self.width)}"
    

length = int(input("Enter length: "))
width = int(input("Enter width: "))
obj = Rectangle(length,width)
print(obj.area())
print(obj.perimeter())
