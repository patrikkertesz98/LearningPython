class Competition:

    __raise_amount = 1.04

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def raise_prize(self):
        self.__prize = self.__prize * self.__raise_amount
    
    def print_details(self):
        print("Name: {}, prize: {}".format(self.__name, self.__prize))

    @classmethod
    def get_raise_amount(cls):
        return cls.__raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.__raise_amount = amount

    @classmethod
    def from_str(cls, competition_str):
        name, prize = competition_str.split('-')

        return cls(name, prize)


sprint = Competition('Sprint', 10000)

print(sprint.get_raise_amount())

sprint.set_raise_amount(1.06)
print(sprint.get_raise_amount())

archery_str = 'Archery-8000'

archery = Competition.from_str(archery_str)

archery.print_details()

class Rectangle:

    def area(x,y):
        return x * y

Rectangle.area = staticmethod(Rectangle.area)

print(Rectangle.area(15,16))

class Rectangle:

    @staticmethod
    def area(x,y):
        return x * y
