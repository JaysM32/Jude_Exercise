import math

class Shape:
    def __init__(self, color = "Green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color
    def isFilled(self):
        return self.__filled

    def setColor(self, warna):
        self.__color = warna
    def setFilled(self, filled = True):
        self.__filled = filled

    def toString(self):
        if self.__filled == True:
            return (f"A Shape with color of {self.color} and filled")
        else:
            return (f"A Shape with color of {self.color} and NOT filled")


class Circle(Shape):
    def __init__(self, rad = 1.0, color = "Green", filled = True):
        super().__init__(color, filled)
        self.__radius = rad

    def getRadius(self):
        return self.__radius

    def setRadius(self, rad):
        self.__radius = rad


    def getPeri(self):
        return 2*math.pi*self.__radius
    def getArea(self):
        return math.pi*(self.__radius**2)

    def toString(self):
        return f"A Circle with radius {self.__radius}, which is a subclass of Shape class"

class Rectangle(Shape):
    def __init__(self, width = 5.0, length = 9.0, color = "Green", filled = True):
        super().__init__(color, filled)
        self.__width = width
        self.__length = length


    def getWidth(self):
        return self.__width
    def getLength(self):
        return self.__length


    def setWidth(self, width):
        self.__width = width
    def setLength(self, length):
        self.__length = length

    def getArea(self):
        return self.__width * self.__length
    def getPeri(self):
        return 2 * (self.__width + self.__length)

    def toString(self):
        return f'A Rectangle with width {self.__width} and length {self.__length}, which is a subclass of Shape class.'

class Square(Rectangle):
    def __init__(self, side = 1.0, color = "Green", filled = True, width = 5.0, length = 9.0):
        super().__init__( width, length, color, filled)
        self.__side = side

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def setWidth(self, side):
        super().setWidth(side)
        super().setLength((side))
    def setLength(self, side):
        super().setWidth(side)
        super().setLength((side))

    def getArea(self):
        return self.__side**2
    def getPeri(self):
        return 4*self.__side

    def toString(self):
        return (f"A Square with side={self.__side}, which is a subclass of {super().toString()}")


square1 = Square(9.0,"Blue", False)
print(square1.toString())
print(square1.getArea())
print(square1.getPeri())
square1.setSide(30.0)
print(square1.toString())
print(square1.getArea())
print(square1.getPeri())
