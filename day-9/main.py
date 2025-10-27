# unpacking == destructuring
movie = ("12 Angry Men", "Sidney Lumet", 1957)

title, director, year = movie

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

for title, director, year in movies:
    print(f"{title} ({year}), by {director}")

# Enumeration
# enumerate function returns the index(you can specify the start if you don't want to start from 0) and current item
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

for counter, movie in enumerate(movies, start=1):
    print(f"{counter}. {movie[0]} ({movie[2]}), by {movie[1]}")

movies = [ ... ]

# unpacking and enumuration
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")

# zip: combines two lists
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)
# ("Paul", "Fluffy"), ("Andrea", "Bubbles"), ("Marta", "Captain Catsworth")

# zip in loops
for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}")

# A caveat for using zip and enumerate: If not converted to a non-iterator(list/tuple) they return an iterator which can only be looped over once
movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)
# The solution would be: movies = list(zip(movie_titles, movie_directors))

for title, director in movies:
    print(f"{title} by {director}.")

movie_list = list(movies)
print(len(movie_list))




