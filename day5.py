# # print("hello world!!!!")
# # for i in range(50):
# #     print("Hello moktan!!!!!!!")

# # statements -> break, continue, pass
# # break terminates the loop
# # continue skips the current iteration and move to next iteration
# # pass is a statement used to skip the current task and move onto the next one without giving error

# # print all even
# # for i in range(0,11,2):
# #     if i == 6:
# #         continue
# #     print(i)

# # for i in range(0,11):
# #     pass

# # if 2 % 2 == 0:
# #     print('hello ')

# #q1 
# # i = 0
# # while i < 11:
# #     if i == 5:
# #         continue
# #     print(i)
# #     i += 1
# # print()
# # # q2 
# # i = 0 
# # while i < 11:
# #     if i == 5:
# #         break
# #     print(i)
# #     i += 1
# # prime_no = 0
# # for i in range(1,100):
# #     count = 0
# #     for j in range(i):
# #         if i % j == 0:
# #             count += 1
# #     if count == 1:
# #         prime_no += 1
# #         print(i)

# # else in for loop
# # for i in range(5):
# #     print(i)
# # else:
# #     print("looop finished....")



# # list comprehension 
# # syntax -> [expression for item in iterable] without if condition

# # list_1 = [a**2 for a in range(0,11)]
# # print(type(list_1))
# # print(list_1)

# # # syntax -> [expression for item in iterable if condition] with if condition


# # list_1 = [a**2 for a in range(0,11) if a%2 == 0]
# # print(type(list_1))
# # print(list_1)

# # list comp 
# # to print which day is today
# # list_2 = ["sunday","monday", "tuesday","wednesday", "thursday", "friday", "saturday"]
# # user_inpu = input("Enter the day: ").strip().lower()
# # day_list = [a for a in list_2 if a == user_inpu]
# # print(type(day_list))
# # print(day_list)
# import datetime as date
# print(date.datetime.now())
# print(date.datetime.now().strftime("%A"))

# # list_2 = ["sunday", "monday", "tuesday","wednesday", "thursday", "friday", "saturday"]
# # user_inpu = datetime.datetime.now().strftime("%A").lower()
# # day_list = [a for a in list_2 if a == user_inpu]
# # print(type(day_list))
# # print(day_list)
# # print(user_inpu)

# # functions
# # block of code which performs the specific task when it is called


# # def college_name(a,b):
# #     print(f"sum is of {a}, {b} is {a+b}")

# # for i in range(5):
# #     college_name(i, i+1)
# # else:
# #     print("loop finished..")

# # functions types
# # 1 positional arguments

# # def namepri(name, age):
# #     print(f"name is {name} and age {age}....")

# # namepri("moktan", 22)
# # namepri(22, "moktan")
# # # 2 keyword arguments

# # def ka(name, age):
# #     print(f"name is {name} and age {age}....")

# # ka("moktan", 22)
# # ka(age = 22, name = "moktan")
# # 3 default arguments
# def ka(name="Prajum", age=15):
#    print(f"name is {name} and age {age}....")

# ka()
# ka("Hello",20)
# # 4 variable length arguments -> *args -> tuple

# def variablelenarg(a,b,*arg):
#    print(arg)

# variablelenarg(1,2,3,4)
# # 5 variable length keyword arguments -> **kwargs -> dictationary
# def variablelenargkey(**kwarg):
#    print(kwarg)

# variablelenargkey(name = "Prajum", age="17")




