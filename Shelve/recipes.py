import shelve

# blt = ["bacon", "lettus", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_egg = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_egg"] = scrambled_egg
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # ordered_key = list(recipes.keys())
    # ordered_key.sort()
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    recipes["soup"].append("creaton")

    for snack in recipes:
        print(snack, recipes[snack])








