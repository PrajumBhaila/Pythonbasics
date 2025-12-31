#oop -> Object Oriented Programming
# class, object, method, inheritance, encapsulation, polymorphism, abstraction

# class ClassName:
# methods, constructor, properties

#class -> blueprint
#object -> instance of class

class Student:
    name="Ram"
    age=20

    # DENDER METHODS/MAGIC METHODS
    #_init_ -> constructor

    # def __init__(self):
    #     print("auto run when object is created")

    def __init__(self,name,age):
        self.name=name
        self.age=age

    #class -> methods
    #this -> self
    def details(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("Ram",20)
print(student1.name,student1.age)
print(student1.details())
#WAP using OOP to need to have a class name Kist and properties like building, classes, 
# teachers and other your wish.

class Kist:
    building = "Main Building"
    classes = 10
    teachers = 30
    principal = "Mr. Sharma"
    location = "Kamalpokhari"
kist1 = Kist()
print(kist1.building)
print(kist1.classes)
print(kist1.teachers)
print(kist1.principal)
print(kist1.location)

