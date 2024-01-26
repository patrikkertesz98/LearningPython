class Competition():
    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def __repr__(self):
        return '({}, {})'.format(self.__name, self.__prize)

archery = Competition('Archery', 1100)

print(archery)

print(repr(archery))
print(str(archery))

print(int.__add__(1,2))

#__add__ special method can be called on any number and string and can be redefined in class

class Savings:
    def __init__(self, amount):
        self.__amount = amount

    def __add__(self, other):
        return self.__amount + other.__amount

s1 = Savings(20100)
s2 = Savings(200)

# + operator calls __add__
print(s1 + s2)

class MethodSub:

    def __init__(self, number):
        self.__number = number
    
    def __sub__(self, other):
        return self.__number * other.__number

num_1 = MethodSub(10)
num_2 = MethodSub(4)

print(num_1 - num_2)




