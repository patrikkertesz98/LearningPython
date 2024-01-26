from os import name
from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME


class Father:
    def height(self):
        print('I have inherited my height from daddy!')

class Mother:
    def intelligence(self):
        print('I have inherited my intelli from momma!')

class Child1(Father, Mother):
    def experience(self):
        print('My experiences are my own')

class Child2(Mother, Father):
    pass

#print(help(Child1))
#print(help(Child2))

ch = Child1()

ch.height()
ch.experience()

##########################
#Complex example

class Employee:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def show_name(self):
        print(self.__name)

    def show_age(self):
        print(self.__age)

class Salary:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        print(self.__salary)

class Database(Employee, Salary):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age)
        Salary.__init__(self, salary)

emp1 = Database('Robin', 26, 98000)

emp1.show_age()
emp1.get_salary()
emp1.show_name()

######
#multilevel inheritance

class Grandparent():
    def height(self):
        print('Grandparent inheritance is height')

class Parent(Grandparent):
    def intelligance(self):
        print('intelligance from my parents')

class Child(Parent):
    def experience(self):
        print('These are my own experiences')

ch2 = Child()

ch2.height()
ch2.intelligance()
ch2.experience()
help(Child)