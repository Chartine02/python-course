def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)
print(list(cubed_numbers))

# map with two lists
def add(a, b):
    return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# map with lambda functions

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(lambda a, b: a + b, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# Conditional comprehensions
# numbers = [1, 56, 3, 5, 24, 19, 88, 37]
# even_numbers = [num for num in numbers if num % 2 == 0]

# filter function
def is_even(number):
    return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# use None to filter out falsy values
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2

