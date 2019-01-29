import shelve

books = shelve.open("books")

books["recipes"] = {"blt" : ["bacon", "lattus", "tomato", "bread"],
                    "beans_on_toast" : ["beans", "bread"],
                    "scrambled_eggs" : ["eggs", "butter", "milk"],
                    "soup" : ["tin_of_soup"],
                    "pasta" : ["pasta", "cheese"]}
books["maintenance"] = {"stuck" : ["oil"],
                        "loose" : ["gaffer_tape"]}

print(books["recipes"])

books.close()




# books = {"recipes" : {"blt" : ["bacon", "lattus", "tomato", "bread"],
#                       "beans_on_toast" : ["beans", "bread"],
#                       "scrambled_eggs" : ["eggs", "butter", "milk"],
#                       "soup" : ["tin_of_soup"],
#                       "pasta" : ["pasta", "cheese"]},
#          "maintenance" : {"stuck" : ["oil"],
#                           "loose" : ["gaffer_tape"]
#                           }}
#
# print(books["recipes"]["soup"])
# print(books["maintenance"]["loose"])