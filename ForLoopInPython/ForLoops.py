# for i in range(1, 12):
#     print("Value of i now is {0} " .format(i))
#
#
# number = "9,123,234,345,456,567,678,789"
# for i in range(0, len(number)):
#     print(number[i], end='')
#
# number = "9,123,234,345,456,567,678,789"
# print()
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The new number is {} " .format(newNumber))


# number = "9,123,234,345,456,567,678,789"
# cleanedNumber = ''
#
# for char in number:
#     if char in '123456789':
#         cleanedNumber = cleanedNumber + char
# newNumber = int(cleanedNumber)
# print("The new number is {}" .format(newNumber))


# for state in ["Rajasthan", "Madhya Pradesh", "Chhattishgadh"]:
#     print("BJP lost in " +state)


# for i in range(2, 21):
#     for j in range(1, 11):
#         print("{0} * {1} = {2} " .format(i, j, i*j))
#     print("#############")


# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# # for i in range(len(quote)):
# #     if quote[i] in "ASMEWPOIRFH":
# #         print(quote[i], end='')
#
# sentence = ''
# for char in quote:
#     if char in 'ASMEWPOIRFH':
#         sentence = sentence + char
#
# print("the sentence is " +sentence)

# for i in range(0,101):
#     if (i % 7) == 0:
#         print(i, end='')


number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number;

print(answer)


















