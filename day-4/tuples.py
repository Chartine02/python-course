# A tuple is a series of comma separated values
names = ("John", "Sarah", "Alice")

movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]

# The comma are what makes tuples, tuples. You can just write:
name = ("John")

# rather
name = "John",
name = ("John",)

# Accessing values in tuples
# tuples are ordered collections, where each item can be accessed by index based on their position in the collection.

# Why Tuples
# tuples are immutable, once created you cannot modify them. Which means there is no pop or append methods
# Accessing values in nested collections

# movies = [
#     ("Eternal Sunshine of the Spotless Mind", 2004),
#     ("Memento", 2000),
#     ("Requiem for a Dream", 2000)
# ]

movies[0] #("Eternal Sunshine of the Spotless Mind", 2004)
movies[0][0]  # "Eternal Sunshine of the Spotless Mind"



