numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

# converted into comprehension
squares = [number ** 2 for number in numbers]
print(squares)

movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movies = {key: value.title() for key, value in movie.items()}
print(movies)