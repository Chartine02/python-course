# Accepting an arbitrary number of positional arguments

# Here it's better to use *names for clarity, and always this parameter comes last like a rest parameter in js
def multigreet(*args):
    for name in args:
        print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne")

# Accepting an arbitrary number of keyword arguments
def pretty_print(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}:{val}")

pretty_print(title="The matrix", director="Wachowski", year=1999)

# if using both in a function kwargs has to come last after args

numbers = [1, 2, 3, 4, 5, 5]

print(*numbers, sep=" | ")

def print_movie(*args):
    for value in args:
        print(value)

# Other uses for * and **, it's used for unpacking an iterable
numbers = [1, 2, 3, 4, 5]

print(*numbers, sep=" | ")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())

#
def print_movie(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(studio="Warner Bros", **movie) # adding ** changes the object into keywords arguments

# studio: Warner Bros
# title: The Matrix
# director: Wachowski
# year: 1999

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print("{title}, by {author} ({year})".format(**book))

    print()


