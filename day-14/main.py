# to read files we use open() function tha allows us to access data of a file
example_file = open('text.txt')
print(example_file.read())

write_file = open("write_example.txt", "w")
write_file.write("Welcome to the world, write_example.txt!")
write_file.close()

# to append more text, use method "a" cause "w" overwrites all the contents of the file
write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")
write_file.close()

# context manager, here we don't need to close the file everytime
with open("write_example.txt", "w") as write_file:
    write_file.write("Welcome to the world, write_example.txt!")

# csv
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

    irises.append({
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    })


