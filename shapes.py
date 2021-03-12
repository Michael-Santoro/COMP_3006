#Michael Santoro
#COMP 3008 - Project 5

#Import

from math import pi
from math import sqrt

#Define a Class
class shape:
    def __init__(self,name,area,perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter
    def area(self):
        print(f'Area is: {self.area}')
    def __str__(self):
        return f'Shape {self.name} Area: {self.area}'

class polygon(shape):
    def __init__(self,sides):
        super(polygon,self).__init__(name='Polygon',area=0,perimeter=1)
        self.sides = sides
    def __str__(self):
        return f'Polygon Shape has sides: {self.sides}'

class parallelogram(polygon):
    def __str__(self):
        return f'Parallelogram Shape has sides: {self.sides}'
class rectangle(parallelogram,polygon,shape):
    def __init__(self, length, width):
        super(rectangle,self).__init__(4)
        self.length = length
        self.width = width
        self.area = self.area
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class square(rectangle,parallelogram,polygon,shape):
    def __init__(self,side):
        super(square,self).__init__(side,side)
        self.name = 'Square'
        self.side = side
    def __str__(self):
        return f'{self.name} has {self.sides} and area of {self.area} with a perimeter of {self.perimeter}'

class oval(shape):
    def __init__(self, majorAxis, minorAxis):
        super().__init__()
        self.name = 'Oval'
        self.majorAxis = majorAxis
        self.minorAxis = minorAxis
        self.area = self.area(majorAxis,minorAxis)
        self.perimeter = self.perimeter(majorAxis,minorAxis)
    def area(self):
        a = pi*(self.majorAxis//2)*(self.minorAxis//2)
        return a
    def perimeter(self):
        p = pi*sqrt(2)*((self.majorAxis//2)**2)*((self.minorAxis//2)**2)
    def __str__(self):
        return f'{self.name} has major axis of {self.majorAxis} and minor axis of {self.minorAxis} and area of {self.area} with a perimeter of {self.perimeter}'

class triangle(polygon):
    def __init__(self,base,height,side1,side2,side3):
        super().__init__(3)
        self.name = 'Triangle'
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area()
        self.perimeter()
    def area(self):
        a = (1//4)*self.base*self.height
        return a
    def perimeter(self):
        p = self.side1+self.side2+self.side3
        return p
    def __str__(self):
        return f'{self.name} has {self.sides} and area of {self.area} with a perimeter of {self.perimeter}'

class pentagon(polygon):
    def __init__(self,side):
        super().__init__(4)
        self.name = 'Pentagon'
        self.side = side
        self.area()
        self.perimeter()
    def area(self):
        a = (1//4)*sqrt(5*(5+2*sqrt(5)))*self.side**2
        return a
    def perimeter(self):
        p = 5*self.side
        return p
    def __str__(self):
        return f'{self.name} has {self.sides} and area of {self.area} with a perimeter of {self.perimeter}'

class circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.name = 'Circle'
        self.radius = radius
        self.area = self.area
        self.perimeter = self.area
    def area(self):
        a = pi*self.radius**2
        return a
    def perimeter(self):
        p = 2*pi*self.radius
        return p
    def __str__(self):
        return f'{self.name} has radius {self.radius} and area of {self.area} with a perimeter of {self.perimeter}'

class rhombus(polygon,shape):
    def __init__(self, diagonal1, diagonal2, side):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.side = side
        area = self.area()
        perimeter = self.perimeter()
        super(rhombus,self).__init__(sides=4,name='Rhombus',area=area,perimeter=perimeter)

    def area(self):
        return (self.diagonal1*self.diagonal2)//2
    def perimeter(self):
        return 4*self.side


    def __str__(self):
        return f'{self.name} has {self.sides} number of sides and area of {self.area} with a perimeter of {self.perimeter}'

def main():
    shape1 = rhombus(4,4,4)

    print(shape1)

main()
