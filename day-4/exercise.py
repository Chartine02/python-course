movies = [("Breaking Bad", "Walt White", 2006, "$500")]


name = input("Insert the movie title: ")
director = input("Insert the movie director: ")
year = input("Insert the movie release year: ")
budget = input("Insert the movie budget: ")

new_movie = (name, director,int(year), budget)
print(f"{new_movie[0]} {new_movie[2]}")
movies.append(new_movie)

print(movies)

del movies[0]

print(movies)
