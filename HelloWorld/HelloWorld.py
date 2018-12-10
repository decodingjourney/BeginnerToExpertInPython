# print("Hello World!")
# print(3+5)
# print()
# print(3 * 6)
# greeting = "Good Morning!"
# name = "Anand"
# print(greeting+name)
# print(greeting+' '+name)
# print('Hello Git')

# #nameOfPerson = input("Please enter your name")
# #print(greeting+' '+nameOfPerson)
# splitString = 'This string is\nsplit over\nmany different\nlines'
# print(splitString)
# tabbedString = '1\t2\t3\t4\t5'
# print(tabbedString)
#
# #Representation of single quotes or double quotes inside a string
# print('The pet shop owner said "No, no, \'e\' uh... he is resting"')
# print("The pet shop owner said \"No, no, 'e' uh... he is resting\"")
# print("""The pet shot owner said "No, no, 'e' uh... he is resting" """)
# print('''The pet shop owner said "No, no, 'e' uh... he is resting"''')
# splitedString = """This line is
# splited into
# several
# lines"""
# print(splitedString)


#                                       VARIABLE
# name of the variable
# name = "anand"
# _name = "anand"
# name_and_title = "annad jha"
# greeting = "Hello"
# Greeting = "Good morning"
# age = 24
# print(greeting+' '+_name+' and '+name_and_title+' '+Greeting)
# # print(name_and_title+' '+age)
#
# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# bun_price = 2.40
# money = 15
# no_of_buns = money//bun_price
# print(no_of_buns)


# parrot = "anand started to fly just like parrot"
# print(parrot[2])
# print(parrot[-1])
# print(parrot[1:10])
# print(parrot[-4:-1])
# print(parrot[0:10:3])
#
# number = "9,234,345,456,567,678,789"
# print(number[0::3])
# Number = "1, 2, 3, 4, 5, 6, 7"
# print(Number[0::3])
#
# string1 = "he's "
# string2 = "probably"
# print(string1+string2)
# print("He's " "probably" " the most genius")
# print("Hello " * (5 + 4))
# today = "saturday"
# print("day" in today)
# print("sat" in today)
# print("thr" in today)
# print("thrua" in "say")

# String formatting -- Displaying String and Number

age = 29
print("I am "+str(age)+" years old boy")

print("I am {0} Years old".format(age))
print("There are {0} days in {1},{2},{3},{4},{5},{6},{7}".format(31,"January", "March", "May", "July", "August", "October", "December"))
print("""January: {2}
February: {0}
Msrch: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("My age is %d %s, %d %s" % (29, "years", 9, "months"))
# for i in range(1,10):
#     print("No. %2d Square is %4d and the Cube is %4d"% (i, i ** 2, i ** 3))

print("PI is approximately %12.50f" % (22/7))
print("PI is approximately {0:12.50}" .format(22/7))


for i in range(1, 12):
    print("No. {0:2} square is {1:4} and cube is {2:4}" .format(i, i ** 2, i ** 3))

for i in range(1, 12):
        print("No. {0:2} square is {1:<4} and cube is {2:<4}" .format(i, i ** 2, i ** 3))



