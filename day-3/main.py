# String concatenation
# To concatenate strings in Python we use + sign, but if the second element it a number it throws an exception
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: " + hourly_wage)
print("Hours worked: " + hours_worked)
# This will throw an exception
print("Hourly wage: " + 20)

# If you want to concatenate a string and a number, you can change the number to a string using str function
age = str(28)
# you can convert it again to an int
age = int("28")

# If we try to pass a string representation of a number with a decimal component, we’re going to get a TypeError.
hourly_wage = int("18.50")
# Instead of int, we’d need to call float here instead:
hourly_wage = float("18.50")
# float can also handle input without a decimal component. For example, if we pass in "20", we’re going to get the float 20.0 back.
# In addition to converting from strings to integers and floats, and vice versa, we can also convert between integers and floats using the same int and float. In this case, passing a float to int is going to work, but it’s going to “truncate” the float, essentially throwing away everything after the decimal point.

# String interpolation with the format method
"{} is {} years old!".format("John", 24)

output = "{} is {} years old, and {} works as a {}."
print(output.format("John", 24, "John", "web developer"))

output = "{0} is {1} years old, and {0} works as a {2}."

print(output.format("John", 24, "web developer"))
print(output.format(name="John", age=24, job="web developer"))

# String interpolation with f-strings
name = "John"
age = 24
f"{name} is {age} years old!"

# Basic string processing
"Hello, World!".lower()       # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"
# Trimming whitespaces
"  Hello, World!  ".strip()  # "Hello, World!"
# Processing many times
user_name = " ROLF SMITH ".strip().title()


