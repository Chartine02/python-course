# generators

# the difference between a generator and a normal function is the keyword yield

def first_hundred():
    for number in range(1, 101):
        yield number

g = first_hundred()
print(g) # a generator object will be printed

# Since it's like other iterators we can access its values using next()
def first_hundred():
    for number in range(1, 101):
        yield number

g = first_hundred()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

# yield keyword
# we can think of yield as a non-terminating return

def first_hundred():
    print("First value requested\n")

    for number in range(1, 101):
        print("Starting new iteration")
        yield number
        print("Ending this iteration\n")

g = first_hundred()

print(next(g))
print(next(g))

# Generator expressions, the difference between these the comprehension is that here we use normal brackets rather than square brackets
squares = (number ** 2 for number in range(1, 11))
print(squares)

# Style note
# One nice thing about generator expressions is that we can forego the parentheses when we use the generator expression as the sole argument in a function or method.

total = sum(number ** 2  for number in  range(1,  11))
print(total)  # 385



