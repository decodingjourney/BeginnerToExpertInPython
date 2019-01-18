myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
newString = ''

#for c in myList:
  #  newString += c +", "
newString = ", ".join(letters)

print(newString)