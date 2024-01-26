from abc import ABC, abstractclassmethod, abstractmethod

class Nomi(ABC):

    @abstractmethod
    def diet(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass

    def behavior(self):
        print('Complex')

chimp = Nomi()

chimp.behavior()

class Human(Nomi):

    def diet(self):
        print('omnivorous')

    def walk(self):
        print('bipods')


paul = Human()

paul.diet()
paul.walk()