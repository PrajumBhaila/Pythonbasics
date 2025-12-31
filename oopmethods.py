# 4 pillars of OOP
# Abstraction 
        #-> Hiding complexities 

from abc import ABC , abstractmethod
class Coffee(ABC):
    @abstractmethod
    def makeCoffee(self):
        print("coffee in progrss!")
    @abstractmethod
    def makingcoffeeprocess(self):
        print("preparing milk")
        print("preparing beans")
        print("preparing sugar")
        print("cooking!")
    
    def readytoseve(self):
        print("serving!")
        self.makeCoffee()
        self.makingcoffeeprocess()

customer1 = Coffee()
customer1.readytoseve()
# Encapsulation
        # ->> wrapping f data and methods
# class Car:
#     name="honda"
#     __model="2019" # private

#     def getmodel(self):
#         return self.__model

#     def setcarmodel(self,model)  :
#         self.__model=model


# obj = Car()
# print(obj.name)
# print(obj.getmodel()) 

# obj.setcarmodel("2025") 
# print(obj.getmodel())

# # wap using encapsulation like bank account need to have balance of 10k by default you can do withdrawal 
# # it canot be less than 10k deposit and check balance

# class Bank:
#     __acc_no = "102383930223323820"
#     def __init__(self):
#         self.balance = 10000
#     def deposit(self,depo):
#         self.balance += depo
#         print(f"{depo} added")

#     def withdraw(self,draw):
#         if(draw<=10000):
#             print("no withdrawl for less than 10k!")
#         else:
#             print(f"{draw} withdrawal succesful!")
#             self.balance -= draw
    
    # @classmethod
    # def checkbalance(clr):
    #     print(clr.balance)

#     def getacc(self):
#         return self.__acc_no
    
#     def checkbalance(self):
#         return self.balance

# obj1 = Bank()

# obj1.deposit(50000)
# obj1.withdraw(5000)
# print(obj1.checkbalance())
# obj1.withdraw(15000)
# print(obj1.checkbalance())
# obj1.getacc()

# # Inheritance
#         # -> properties, methods of parent class  inherited by child class 
# # class Parent:
# #     lastname = "Shrestha"

# # class Child(Parent):
# #     firstname = "Sangam"

# #     def getfullname(self):
# #         return f"{self.firstname} {self.lastname}" 
    

# # obj = Child()
# # print(obj.getfullname())
# class Parent:
#     def __init__(self,lastname):
#         self.lastnames = lastname 

# class Child(Parent):
#     def __init__(self,firstname,lastnames):
#         self.firstnames=firstname
#         super().__init__(lastnames)
#     def getfullname(self):
#         return f"{self.firstnames} {self.lastnames}" 
    

# obj = Child("Sangam","Shrestha")
# print(obj.getfullname())
# obj1 = Child("Hello","Shrestha")
# print(obj1.getfullname())
# Polymorphism 