# Define four functions: add, subtract, divide, and multiply.
def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def divide(x,y):
    if y == 0:
        print("You can't divide by zero")
    return x/y


def multiply(x,y):
    return x * y

#  Define a function called print_show_info that has a single parameter.
def print_show_info(show):
    print(f"{show['title']} {show['initial_release']} - {show['seasons']} seasons")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(tv_show)

# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary.
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
for show in series:
    print_show_info(show)

# Create a function to test if a word is a palindrome.
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

print(is_palindrome("was it a car or a cat I saw"))
