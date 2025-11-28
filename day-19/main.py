import json
import math


with open('books.json', 'r') as read_file:
    books = json.load(read_file)
    print(books)

while True:
    try:
        number = int(input('Enter a whole number'))
        break
    except ValueError:
        print("You didn't enter a valid number")

# handling multiple exceptions
def average(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")

# or
import math

def average2(numbers):
    try:
        mean = math.fsum(numbers) / len(numbers)
        print(mean)
    except (ZeroDivisionError, TypeError):
        print("An average cannot be calculated for the values you provided.")
