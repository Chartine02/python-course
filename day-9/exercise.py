# 1.
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, specie in main_characters:
    print(f"{character} is a {specie.lower()} voiced by {actor}.")

# 2.
name, student_id, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

# 3.
letters = ["a", "b", "c"]
numbers = [1, 2]

print(list(zip(letters, numbers)))


