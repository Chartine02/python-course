
def get_sum(*numbers):
    print(sum(numbers))

get_sum(3,4,5,6,7,1)

# Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def pretty_print(*args, **kwargs):
    for n in args:
        print(f"Positional arg: {n}")

    print("Keyword arguments")
    for key, val in kwargs.items():
        print(f"{key}:{val}")

pretty_print(1,2,3,4,5,name="kal",age=8, height="4ft")

# Print the following dictionary using the format method and ** unpacking.
country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

print("{name} has {population} population, it's capital is {capital}, and {currency} is its currency".format(**country))

print(*range(1,21), sep="\n")

