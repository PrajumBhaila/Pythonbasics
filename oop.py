#oop => object class 4 pllars , methods

#class => blueprint (Methods, cosntructor, properties)
#object  => instance of class

# class Students:
#     name = "Ram"
#     age = 17

#     # this -> self in python 
#     def __init__(self,number):
#         self.number=number

#     def show(self):
#         return f"name : {self.name} age: {self.age}"   
    
    
# Obj = Students(98096161)

# print(Obj.name,Obj.number)
# print(Obj.show())

# Obj2 = Students(98484843)
# print(Obj2.name,Obj.number)
# print(Obj2.show())

# Calculator using OOP in Python 

# class Calculator:

#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b

#     def add(self):
#         return self.num1+self.num2

#     def sub(self):
#         return self.num1-self.num2

#     def mul(self):
#         return self.num1*self.num2

#     def div(self):
#         if self.num2 == 0:
#             return "Cannot divide by zero"
#         return self.num1/self.num2


# c = int(input("Enter a number1: "))
# d = int(input("Enter a number2: "))

# obj = Calculator(c,d)

# print("Options for operation: \n 1. Add \n 2.Sub \n 3. Multiply \n 4. Division")

# input1 = input("Enter what you want: ")

# match(input1):
#     case "1":
#         print(f"Sum is: ", obj.add())

#     case "2":
#         print(f"Diff is: ", obj.sub())

#     case "3":
#         print(f"Product is: ", obj.mul())

#     case "4":
#         print(f"Division is: ", obj.div())
    
#     case _:
#         print("Error")


#types of methods:
# instance methods = need object to call 
# class methods = can be called uisng class name
# static methods = independent 

class methodsinpy:
    @classmethod
    def name(cls,a,b):
        return a+b
    
    @staticmethod
    def name1(a,b):
        return a+b
x=methodsinpy.name(6,7)
print(x)

y=methodsinpy.name1(7,8)
print(y)

