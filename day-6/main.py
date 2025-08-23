# Loops allow performing an operation on all items of an iterable
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
      print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

# break, stops the loop
for movie in movies:
      # Check the title of the current movie is Memento
      if movie[0] == "Memento":
            # If the title is Memento, inform the user that the movie exists and break the loop
            print("Memento is in the movie library!")
            break


# range is capable of producing a series of integers according to some set pattern.
range(10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
range(3, 10) # 3, 4, 5, 6, 7, 8, 9
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(0, 10, 3)  # 0, 3, 6, 9
# you can't just print the return value of the range function
print(list(range(0,10,-1)))
numbers = list(range(10))             # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
immutable_numbers = tuple(range(10))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# range() return an iterable and you loop over it to access all the items
for number in range(10):
    print(number)

# if you're not using the variable in the loop you just use _ as a placeholder
for _ in range(10):
    print("Hello!")





