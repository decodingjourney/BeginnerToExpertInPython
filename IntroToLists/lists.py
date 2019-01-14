# ipAddress = input("Please enter the ipAddress of the system ")
# print(ipAddress.count('.'))

# parrot_list = ["non pinin'", "no more", "a stif", "berift of live", "Green"]
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# # numbers.sort()
# number_in_order = sorted(numbers)
# print(number_in_order)
#
# if numbers == number_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if number_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")


# list_1 = []
# list_2 = list()
#
# print("List 1 {}".format(list_1))
# print("List 2 {}".format(list_2))
#
# if list_1 == list_2:
#     print("Both the lists are equal")
#
# even = [2, 4, 6, 8]
# another_even = even
#
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(even)
#
#
# even = [2, 4, 6, 8]
# another_even = list(even)
#
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(even)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = [even, odd]
print(number)

for number_set in number:
    print(number_set)

    for value in number_set:
        print(value)


menu = []

menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', ' sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])

for iteam in menu:
    if not 'spam' in iteam:
        print(iteam)
        for item in iteam:
            print(item)

