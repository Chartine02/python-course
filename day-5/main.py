# Booleans
print(True)   # True
print(False)  # False

# Falsy values: 0, 0.0, empty string, False, None, empty list, empty tuple
# Everything else is a truthy values, except the types you define to be falsy under certain circumstances

# Comparison operators
print(5 < 10)     # True
print(5 > 10)     # False
print(10 > 10)    # False
print("A" < "a")  # True
# The ASCII code for A is 65, while a is 97

print(10 > 10)   # False
print(10 >= 10)  # True

print(0 == "0")                # False
print(0 == 0)                  # True
print(7 == 7.0)                # True
print("Hello" == "Hello!")     # False
print([1, 2, 3] == [1, 2, 3])  # True

print(0 != "0")         # True
print(0 != 0)           # False
print("Hello" != "Hi")  # True


# == is different from `is` and != is different from is not
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

# We can use a function called id to find out where something is being stored, represented as a long series of numbers.
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944
print(a == b)  # True
print(a is b)  # False
# is will compare the values and their memory addresses

a = [1, 2, 3]
b = a

print(id(a))  # 139685763327296
print(id(b))  # 139685763327296

print(a == b)  # True
print(a is b)  # True

# It's important to note that, in some complex cases, is will yield False when we compare two things that seemingly occupy the same memory address. In other words, there are cases were two items seem have the same id, but is nonetheless indicates that the objects are not one and the same.

# Order of operations: comparisons take less precedence to arithmetica operators
5 + 4 < 3 * 2 # False

# Conditional statement
age = int(input("How old are you? "))

if age < 18:
      print("Sorry, we can't serve you.")

# Truthy values and conditional statements
name = input("Please enter your name: ")

if name:  # Checks the truth value of name by calling bool
      print(f"You entered {name}")
else:
      print("You didn't type anything")



