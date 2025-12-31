# wap using abstraction for different shapes area calculation -> Shape
# ABC -> area() -> Circle, Rectangle, Square
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

square = Square(4)
print("Area of Square:", square.area())
circle = Circle(5)
print("Area of Circle:", circle.area()) 

class