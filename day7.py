
#encapsulation meaning -> wrapping up of data and methods
# #class car:
# #__->private
# #__v=brand = "volvo
# # model = "2019"

# def get_carbrand(self):
#     return self.__brand

# class car:
# # __->private
#  def __inti__(self, brand, model):
#      self.__brand = brand #private variable
    

# def get_carbrand(self):
#     return self.__brand
#WAP using encapsulation like bank account need to have
class Bank:
    def __init__(self):
        self.__balance = 10000
    
    def add_balance(self, amount):
        self.__balance = self.__balance + amount
    
    def withdrawl(self, amount):
        if(self.__balance >= 10000):
            if(self.__balance >= amount):
                self.__balance = self.__balance-amount
                print(f"your withdrawl {amount}")
            else:
                print("You don't have sufficient balance ")
                
    def chechbalance(self):
        return self.__balance
    
myaccount = Bank()
myaccount.add_balance(5000)
myaccount.withdrawl(2000)
print(myaccount.chechbalance())

#3. inheriance -> properties, methods of parent class inherited by child class
class Parent:
    def __init__(self, lastname):
        self.lastnames = lastname
        
        def lastname(self):
            return self.lastnames
    
class Child(Parent):
    def __init__(self, firstname, lastnames):
        self.first_name = firstname
        super().__init__(lastnames)
    
    def fullname(self):
        return f"{self.first_name} {self.lastnames}"
    
user1 = Child("prabhat", "tuladhar")
print(user1.fullname())
print(user1.lastname())

user2 = Child("ram", "hapa")
print(user2.fullname())
print(user2.lastname())

#from abc import ABC, abstractionmethod

# class Coffee(ABC):
    # @abstracionmethod
    # def makeCoffee(self):
    # print("user is asking for coffee")
    
    # abstractmethod
    # def makeCoffeeProcess(self):
    # print ("making ready of utinsels")
    # print("taking milk, coffee and sugar")
    # print("pour coffee in cup")
    # print("serve to the user")
    
    # def readytoserver(self):
    # self.makeCoffee()
    # self.makeCoffeeProcess()
    
    # coffee1 = Coffee()
    # coffee1.readytoserver() 


