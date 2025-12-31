#wap to create a calculator using oop ask 2 input from user 
#need to have add, sub, multiply, divide 

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero is not allowed"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
calc= Calculator(num1,num2)
print("Addition:", calc.add())
print("Subtraction:", calc.sub())  
print("Multiply:",calc.multiply())
print("Divide:",calc.divide())