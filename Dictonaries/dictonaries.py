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
while True:
    dict_key = input("Please enter the name of fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have "+dict_key)
