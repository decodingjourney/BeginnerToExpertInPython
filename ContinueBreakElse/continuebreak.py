# shopping_list = ["milk", "bread", "pasta", "spam", "serelac"]
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print(item)


# breakfast = ["milk", "bread", "butter", "passta", "egg"]
# nasty_food = ''
# for item in breakfast:
#     if item == "pasta":
#         nasty_food = item
#         break
#
# if nasty_food:
#     print("I don't like " + nasty_food)



# for i in range(0, 100, 7):
#     print(i)
#     if (i > 0) and (i % 11) == 0:
#         break


for i in range(1, 21):
    if (i % 3) == 0 or (i % 5) == 0:
        continue
    print(i)

