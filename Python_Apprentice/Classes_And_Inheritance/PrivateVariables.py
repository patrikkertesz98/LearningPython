class Dog:

    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    def print_details(self):

        print('My name is %s and I am a %s' %(self.__name, self.__breed))

d1 = Dog('Kevin', 'Bischon')
d1.print_details()
#can't change an instance variables if the have __ before them
# (private variables the python way) if you want you can change the value
# just use _Dog__name for assigning 
d1.name = 'Nemo'
d1.print_details()

d1._Dog__name = 'Nemo'
d1.print_details()
print(d1.__dict__)



