# what is exception handling?

# It prevents the program from crashing when an error happens.

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero")