import sys
def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number ! Please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("This statement will be executed always")



first_number = getint("Please enter first number")
second_number = getint("please enter second number")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number // second_number))
except ZeroDivisionError:
    print("You can not divide by zero(0)")
    sys.exit(2)
else:
    print("Task completed successfully")
