# function
#3. default arguments
def details(name = "rojal", age ="23"):
    print(f"name is {name}, age is {age}")

details()
details("ram", "23")
# 4.variable length arguments -> *arg -> tuple
def var_l(a,b,*one):
    print(one)
    print(a,b)
var_l(1,2,3,4)
# 5. varibale length keyword arguments -> **kwargs ->dict
def fa(**here):
    print(here)
    
fa(name="rojal", age ="25")

#wap to function to use all parameter type in function
#pass
def all_funstion(a,b,c,*args,**kwargs):
    print(a,b,c,args,kwargs)
all_funstion(1,2,3,name="here", age="23")
print("this is pass keyword which lets us to pass the function's body")

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
#recursion in python function -> function calling itself

# def add(n):
#     if n==0:
#         return
#     print(n)
#     return add(n-1)
    
# add(4)
#factorial of number using recursion 5!
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print("the factorial of 5 is",fact(5))

# type hinting in python
# def ac(a:int , b:int):
#     print(a+b)
    
# ac(1,5)
# #lamda function ->
# one = lambda x,y : x+y
# print(one(1,7))
# #multiply 2 values
# p = lambda a,b: a*b
# print(p(5,4))

#global and local variable
# global -> if we make a varible outside a function we can 
# use it inside a function and outside it

#global variable
global_var = "23"
print(global_var)
 
def abc():
    local_var = 34
    print(local_var)
    print(global_var)
    
abc()
# function lambda function

list1=[1,2,3,4,5]
list2= list[map(lambda x : x*2 , list1)]
print(list2())