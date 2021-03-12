#Michael Santoro
#COMP 3008 - Project 5

#Import

from math import pi
from math import sqrt

#Define a Class
class shape:
    def __init__(self, name):
        self.name = name  #Passing Through
        self.area = 0     #Over-Write
        self.perimeter = 0#Over-Write
    def __str__(self):
        return f'Shape {self.name} Area: {self.area}'

#Not Calculating an Area Here
class polygon(shape):
    def __init__(self,sides):
        self.sides = sides
        super(polygon,self).__init__(name='Polygon')
    def __str__(self):
        return f'Polygon'

#Not Calculating an Area Here
class parallelogram(polygon):
    def __init__(self):
        super(parallelogram,self).__init__(sides=4)
    def __str__(self):
        return f'Parallelogram'

class rectangle(parallelogram):
    def __init__(self, length, width):
        super(rectangle,self).__init__()
        self.length = length
        self.width = width
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        return self.length * self.width
    def calcperimeter(self):
        return 2 * self.length + 2 * self.width
    def __str__(self):
        return f'{self.name} has {self.sides} and area of {self.area} with a perimeter of {self.perimeter}'

class square(rectangle):
    def __init__(self,side):
        super(square,self).__init__(side,side)
        self.name = 'Square'
    def __str__(self):
        return f'{self.name} has {self.sides} and area of {self.area} with a perimeter of {self.perimeter}'

class oval(shape):
    def __init__(self, majorAxis, minorAxis):
        super().__init__('Oval')
        self.majorAxis = majorAxis
        self.minorAxis = minorAxis
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        a = pi*(self.majorAxis/2)*(self.minorAxis/2)
        return a
    def calcperimeter(self):
        p = pi*sqrt(2)*((self.majorAxis/2)**2)*((self.minorAxis/2)**2)
        return p
    def __str__(self):
        return f'{self.name} has major axis of {self.majorAxis} and minor axis of {self.minorAxis} and area of {round(self.area,2)} with a perimeter of {round(self.perimeter,2)}'

class triangle(polygon):
    def __init__(self,base,height,side1,side2,side3):
        super().__init__(3)
        self.name = 'Triangle'
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        a = (1/4)*self.base*self.height
        return a
    def calcperimeter(self):
        p = self.side1+self.side2+self.side3
        return p
    def __str__(self):
        return f'{self.name} has {self.sides} sides and area of {round(self.area,2)} with a perimeter of {self.perimeter}'

class pentagon(polygon):
    def __init__(self, side):
        super(pentagon,self).__init__(4)
        self.name = 'Pentagon'
        self.side = side
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        a = (1/4)*sqrt(5*(5+2*sqrt(5)))*self.side**2
        return a
    def calcperimeter(self):
        p = 5*self.side
        return p
    def __str__(self):
        return f'{self.name} has {self.sides} sides and area of {round(self.area,2)} with a perimeter of {self.perimeter}'

class circle(shape):
    def __init__(self, radius):
        super(circle,self).__init__('Circle')
        self.radius = radius
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        a = pi*self.radius**2
        return a
    def calcperimeter(self):
        p = 2*pi*self.radius
        return p
    def __str__(self):
        return f'{self.name} has radius {self.radius} and area of {round(self.area,2)} with a perimeter of {round(self.perimeter,2)}'

class rhombus(polygon):
    def __init__(self, diagonal1, diagonal2, side): #Constructor
        #Passing Through
        super(rhombus,self).__init__(sides=4)
        #Over-Write Objects
        self.name = 'Rhombus'
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.side = side
        self.area = self.calcarea()
        self.perimeter = self.calcperimeter()
    def calcarea(self):
        return (self.diagonal1*self.diagonal2)//2
    def calcperimeter(self):
        return 4*self.side
    def __str__(self):
        return f'{self.name} has {self.sides} number of sides and area of {self.area} with a perimeter of {self.perimeter}'

def main():
    shape1 = rhombus(4,4,4)
    circle1 = circle(4)
    pentagon1 = pentagon(4)
    triangle1 = triangle(3,4,3,3,3)
    oval1 = oval(5,3)
    square1 = square(4)
    rectangle1 = rectangle(4,6)

    print(shape1)
    print(circle1)
    print(pentagon1)
    print(triangle1)
    print(oval1)
    print(square1)
    print(rectangle1)

main()
