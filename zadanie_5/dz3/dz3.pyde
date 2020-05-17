class Shape():
    def __init__(self):
        print('Shape created')
        
    def draw(self):
        print('Drawing a shape')
        
    def area(self):
        print('Calc area')
        
    def perimeter(self):
        print('Calc perimeter')
        
import math
class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)
        
        self.a = a
        self.b = b
        self.c = c
        
        print('Triangle created')
        
    def draw(self):
        print('Drawing triangle whith sides={self.a}, {self.b}, {self.c}')
        
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c
    
triangle = Triangle(12,10,12)

triangle.draw()
print(triangle.area())
print(triangle.perimeter())
