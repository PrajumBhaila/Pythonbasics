
#conditions in python
# if, elif, else, match(switch case)

# num = int(input("Enter a number: "))
# if (num % 2 == 0):
#      print(f"{num} is an even number.")
# else:
#      print(f"{num} is an odd number.")     
     
# # wap to check is given number is odd using if statement only?

# num1 = int(input("Enter a number: "))

# if (num1 % 2 != 0):
#      print(f"{num1} is an odd number.")

#wap to check if a given grade falls in which A,B,C,D,E,F using if  else statements

# grade = int(input("Enter the grade of the student: [0-100] "))  
# if grade >= 90:
#     print("Grade A")
# if (grade >= 80 and grade < 90):
#     print("Grade B")
# if (grade >= 70 and grade < 80):
#     print("Grade C")
# if (grade >= 60 and grade < 70):
#     print("Grade D")
# if (grade >= 50 and grade < 60):
#     print("Grade E")
# if grade < 50:
#     print("Grade F , failed")
    

#WAP TO CHECK THE GIVEN LETTER IS VOWEL OR NOT

# vowel = str(input("Enter a character of alphabtets: "))

# def isvowel():
#     if(vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'):
#         print(f"{vowel} is a vowel" )
#     else:
#          print(f"{vowel} is not a vowel" )
         
# isvowel()
        
# # if(isvowel()):
# #     print(f"{vowel} is a vowel" )
    
# # if(vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u'):
# #     print(f"{vowel} is a vowel" )
# # else:
# #     print(f"{vowel} is not a vowel")

# #match {similar to switch case}

# character = input("Enter any character: ")

# match(character):
#     case "a":
#         print("Vowel")
#     case "e":
#         print("Vowel")
#     case "i":
#         print("Vowel")
#     case "o":
#         print("Vowel")
#     case "u":
#         print("Vowel")
#     case default:
#         print("Not vowel")
        
# wap using match to check if given number is negative, positive or zero

num = int(input("Enter any number: "))


match(num):
    case num if num >0:
        print("positive")
    case num if num<0:
        print("negative")
    case num if num==0:
        print("zero")    
    case default :
        print("notnumber")