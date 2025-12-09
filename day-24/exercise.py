def get_num():
    num = int(input("Choose a number between 1 and 10: "))

    try:
        if num not in range(1,11):
            raise ValueError("The number must be between 1 and 10")

get_num()

# 2

def divide(a, b):
    try:
        print(a / b)

    except ZeroDivisionError:
        print("you can not divide a number by 0")
    except TypeError:
        print("you can do this calculations with numbers")
    except ArithmeticError:
        print("there was an arithmetic error")


def itemgetter(collection, identifier):
    try:
        return collection[identifier]

    except KeyError or IndexError:
        return "The key/index is unavailable"


