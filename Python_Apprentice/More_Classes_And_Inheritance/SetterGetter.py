class Wrestler:
    def __init__(self):
        self.__name = ''

    def set_name(self, name):
        print('setter method called')
        self.__name = name

    def get_name(self):
        print('getter method called')
        print(self.__name)

    def del_name(self):
        print('deleter method called')
        del self.__name

    name = property(get_name, set_name, del_name)

w =  Wrestler()

w.name = 'Kart'

w.name

del w.name

class Boxer:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        print('getter method called')
        return self.__name

    @name.setter
    def name(self, name):
        print('setter method called')
        self.__name = name

    @name.deleter
    def name(self):
        print('deleter method called')
        del self.__name

    @property
    def age(self):
        print('getter called')
        return self.__age
    
    @age.setter
    def age(self, value):
        print('setter called')
        self.__age = value

    @age.deleter
    def age(self):
        print('deleter called')
        del self.__age        

b = Boxer("orbán", 52)
print(b.name)

b.name = "Putyin"
b.age = 15
del b.age
