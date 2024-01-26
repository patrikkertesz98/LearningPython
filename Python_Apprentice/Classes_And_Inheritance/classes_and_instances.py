class Student:
    pass


print(type(Student))

object_1 = Student()
object_2 = Student()

print(object_1)
print(isinstance(object_2, Student))

object_1.name = "Patrik"
object_1.email = "Patrik@citromail.hu"

print(object_1.name, object_1.email)

object_2.name = "Dori"
object_2.email = "Dori@citromail.hu"

# redifining a class
class Student:
    name = ""
    score = 0
    active = True


object_3 = Student()
print(object_3.active)
