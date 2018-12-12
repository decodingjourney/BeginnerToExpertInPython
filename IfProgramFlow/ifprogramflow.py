# name = input("Please enter your name ")
# age = int(input("How old are you {0} " .format(name)))
# print("are you really {0} years old {1}?" .format(age, name))
#
# if age >= 21:
#     print("You are eligible to cast your Vote")
#     print("Plese put an X in the box")
# else:
#     print("Please come after {0} years to vote" .format(21 - age))


# print("Please enter the number between 1 to 10 ")
# num = int(input())
# if num < 5:
#     print("Please guess the number higher ")
#     num = int(input())
#     if num == 5:
#         print("Well Done ! you guessed it correctly")
#     else:
#         print("Sorry! You did not guessed it ")
# elif num > 5:
#     print("Please guess lower number")
#     num = int(input())
#     if num == 5:
#         print("Well Done ! you guessed it correctly")
#     else:
#         print("Sorry! you did not guessed it correctly")
# else:
#     print("Congratulations! you have guessed it on very first time")


# print("Please enter the number between 1 to 10 ")
# num = int(input())
# if num != 5:
#     if num < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#
#     num = int(input())
#     if num == 5:
#         print("Well Done! you got it ")
#     else:
#         print("Sorry you did not guessed it ")
# else:
#     print("You guessed it on first attempt")


# age = int(input("How old are you? "))
# # if (age >= 16) and (age <= 65):
# if 16 <= age <= 65:
#     print("Welcome to work and have a nice day at work")


# Coding on 12-12-2018
# Write a small program to enter the name and age
name = input("Please enter your name ")
age = int(input(" how old are you {0} " .format(name)))
if age > 18 and age < 31:
    print("welcome to the grand party")
elif age <= 18:
    print("I am sorry! you are allowed after {0} years " .format(18 - age))
else:
    print("You are too old to attend this party")






















