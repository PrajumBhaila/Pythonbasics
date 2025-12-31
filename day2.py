'''
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

num3 = num1 + num2
print(type(num1), type(num2))
print("The sum is: ", num3)
'''

num4 = "55"
num5 = float(num4)

print(type(num4), type(num5))


#string manipulation 
name=  " prajum Bhaila"
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("prajum", "Piyush"))

print(name.split())
print(name.capitalize())
print(name.title())

print(name.count("s"))
print(name.index("S"))

#isupper, islower, istitle for boolean return

#string slicing and indexing 

sample = "Hello, welcome to python programming"
print(sample[0])  # H
print(sample[7])  # w
print(sample[-1]) # g
print(sample[3:10]) # r
print(sample[:10]) # 0 to 9
print(sample[10:]) # 10 to end

#slicing start: end: step

print(sample[-7:0]) 
# print(sample[-7:-1]) 
# print(sample[::2])
# print(sample[::-1]) #reversing a string


#wap to print even index character of a string 
sample = "abcdefghijklmnopqrestuvwxyz"

print(len(sample))
rev = sample[::2]
print(rev)
print(rev[::-1])# even index characters

# Arithmetic operators // gives integers if no specifically divided by float ** gives power

print(5//2)
print(5/2)
print(2**3)

# assignment operators => =, +=, -=, *=, /=, //=, **=
a = 10
a += 5
print(a)    

a **= 2
print(a)
a //= 3
print(a)
a -= 4
print(a)
a *= 2
print(a)
a /= 2
print(a)

#logical operators -> and, or, not

a= True
b= False
print(a and b)
print(a or b)
print(not a)

