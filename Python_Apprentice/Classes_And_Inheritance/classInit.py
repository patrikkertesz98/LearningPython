class Student:
    def __init__(self):
        print('init called')


s1 = Student()
s2 = Student()

#initial arguments

class Student:
    def __init__(self, name):
        print('init called')
        self.name = name
        self.mail = name +'@'+'gmail.com'

s2 = Student('Dori')
print(s2.name, s2.mail)

class Worker:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

w1 = Worker('Patrik', 'Kertész')

print(w1.fullname())
