# print(3+5)
#
# tabbedString = '1\t2\t3\t4\t5'
# print(tabbedString)
# print('The pet shop owner said "No, no, \'e\' uh... he is resting"')
# print("The pet shot owner said \"No, no, 'e' uh.. he is resting\"")
# print("""The pet shop owner said "No, no, 'e' uh... he is resting" """)
# print('''The pet shop owner said "No, no, 'e' uh... he is resting" ''')
#
# age = 28
# print("his age is "+age)

# parrot = "anand started to fly just like parrot"
# print(parrot[2])
# print(parrot[-1])
# print(parrot[1:10])
# print(parrot[-4:-1])
# print(parrot[0:10:3])


# number = "9,234,345,456,567,678,789"
# # print(number[0::3])
# # Number = "1, 2, 3, 4, 5, 6, 7"
# # print(Number[0::3])

# string1 = "he's "
# # string2 = "probably"
# # print(string1+string2)
# # print("He's " "probably" " the most genius")
# # print("Hello " * (5 + 4))
# # today = "saturday"
# # print("day" in today)
# # print("sat" in today)
# # print("thr" in today)
# # print("thrua" in "say")

# print("There are {} days in {},{},{},{},{},{},{}".format(31,"January", "March", "May", "July", "August", "October", "December"))

# print("""January: {2}
# February: {0}
# Msrch: {2}
# April: {1}
# May: {2}
# June: {1}
# July: {2}
# August: {2}
# September: {1}
# October: {2}
# November: {1}
# December: {2}""".format(28, 30, 31))


# print("My age is %d %s, %d %s" % (29, "years", 9, "months"))
# print("My age is {} years, {} months".format(29, 9))

# for i in range(1, 10):
#     print("No. {0:2}, square is {1:4}, cube is {2:4}".format(i, i ** 2, i ** 3))

# for i in range(1, 21):
#     if (i % 3) == 0 or (i % 5) == 0:
#         continue
#     print(i)


# number = "9,123,234,345,456,567,678,789"
# cleanNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '01234':
#         cleanNumber = cleanNumber +number[i]
#
# print(cleanNumber)

even = [2,4,6,8]
odd = [1, 3, 5, 7, 9]

number = even + odd
print(number)
# number.sort()
# print(number)

number_in_order = sorted(number)
print(number_in_order)

if number == number_in_order:
    print("The list is equal")
else:
    print("The list is not equal")