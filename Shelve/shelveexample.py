import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, Yellow, citrus fruit"
    fruit['grape'] = "a small sweet fruit growing in bunches"
    fruit['lime'] = "a sour green citrus fruit"

    # print(fruit["orange"])
    # print(fruit["lemon"])
    #
    # for key in fruit:
    #     print(key)
    #
    # fruit['lime'] = "great with Taquila"
    # for snack in fruit:
    #     print(snack+" : "+fruit[snack])
    while True:
        shelf_key = input("Please enter the name of fruit ")
        if shelf_key == "Quit":
            break

        if shelf_key in fruit:
            description = fruit[shelf_key]
            print(description)
        else:
            print("We don't have a "+shelf_key)
        # description = fruit.get(shelf_key, "We don't have a "+shelf_key)
        # print(description)






# #with shelve.open('ShelfTest') as fruit:
# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, Yellow, citrus fruit"
# fruit['grape'] = "a small sweet fruit growing in bunches"
# fruit['lime'] = "a sour green citrus fruit"
#
# print(fruit["orange"])
# print(fruit["lemon"])
# fruit.close()
#
# print(fruit)