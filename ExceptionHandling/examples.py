def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)
try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program can not calculate that large")
# except ZeroDivisionError:
#     print("what are you doing dividing by zero ????")

print("program terminating")