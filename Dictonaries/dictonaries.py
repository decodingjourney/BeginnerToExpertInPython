fruit = {"orange": "a sweet orange sytrus fruit",
         "apple": "good for making cidar",
         "lemon": "a sour yellow sytrus fruit",
         "lime": "another sytrus fruit"}

# print(fruit)
# print(fruit["orange"])
#
# fruit["pear"] = "an odd shaped fruit"
# print(fruit)
#
# del fruit["lemon"]
# fruit.clear()
# while True:
#     dict_key = input("Please enter the name of fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have fruit called "+dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("We don't have "+dict_key)
#
# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack+" is "+fruit[snack])
#     print("-" *40)


# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f+" - "+fruit[f])

# for f in sorted(fruit.keys()):
#     print(f +" - "+fruit[f])

# print(fruit.keys())
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not good with icecream"
#
# print(fruit_keys)

print(fruit.items())

f_tuple = tuple(fruit.items())

print(f_tuple)


for snack in f_tuple:
    item,description = snack
    print(item +" is " +description)

print(dict(f_tuple))