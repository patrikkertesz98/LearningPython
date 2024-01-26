import math

class Shape:
    pass

class Shape():
    pass

class Shape(object):
    pass

class Shape:

    def __init__(self, shape_type):
        self.__type = shape_type
    
    def get_type(self):
        return self.__type

circle = Shape("circle")
square = Shape("square")
print(square.get_type())

class Shape:

    def __init__(self, shape_type, color='Red'):
        self.__color = color
        self.__type = shape_type
    
    def get_type(self):
        return self.__type
    def get_color(self):
        return self.__color

circle = Shape("circle", color="Blue")
print(circle.get_color())
print(circle.get_type())

class Circle(Shape):
    pass

class Square(Shape):

    def __init__(self, side):
        Shape.__init__(self, 'square')
        self.__side = side
    def get_area(self):
        return self.__side * self.__side
    def get_perimeter(self):
        return 4 * self.__side


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, 'circle')

        self.__radius = radius
    def get_area(self):
        return math.pi * self.__radius * self.__radius
    def get_perimeter(self):
        return 2 * math.pi * self.__radius

circle = Circle(14)
square = Square(10)

print(circle.get_type())
print(square.get_type())
print(square.get_color())
print(circle.get_color())

print('Circle______')
print(circle.get_area())
print(circle.get_perimeter())

print('Square______')

print(square.get_area())
print(square.get_perimeter())

#more subclasses and inheritance

class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def get_name(self):
        return self.__name
    
    def get_prize(self):
        return self.__prize

    def raise_prize(self):
        self.__prize = self.__prize * self.__raise_amount

race = Competition('Race', 100)

print(type(race))

class Sprint(Competition):
    pass

sprint = Sprint('100m', 700)

class Cycling(Competition):

    def __init__(self, name, prize, country):
        #import the init method of the parent class
        super().__init__(name, prize)

        self.__country = country

    def get_country(self):
        return self.__country

cycling = Cycling('10km', 7500, 'USA')

print(issubclass(Cycling, Competition))
