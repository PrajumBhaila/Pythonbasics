
#loops in python
# range datatype range()
for i in range(0,11):
    print (i)


#wap to check if odd or even using loop
# list = [1,2,3,4,5]
# size = len(list)
# for i in range (0,size):
#     if(list[i] % 2 == 0):
#         print(f"{list[i]} is even")
#     else:
#         print(f"{list[i]} is odd")


#while loop  in python
# a=0
# while(a<=10):
#     print(a)
#     a+=1

#using while loop for even or odd 
# i=0
# while(i<=10):
#     if(i % 2 == 0):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")
#     i+=1

#wap to print multiplication table of 1 to 10

# for j in range (1,11):
#     print(f"table of {j}")
#     for k in range(1,11):
#         print(f"{j} * {k} = {j*k}")

#wap to print the following pattern:
'''
*
**
***
****
*****
'''

for i in range (0,5):
    
    for j in range(i):
        print("*", end="")
    print()
    
#reverse
for i in range (6,0,-1):
    
    for j in range(i):
        print("*", end="")
    print()
    
