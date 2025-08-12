# creating a string in python you just have to wrap it into quotations whether single or double
print("Hello, world!")

# Variable names can include letters, numbers, and underscore (_) characters.
# Variable names can’t start with a number, though starting with an underscore is allowed.
# Variable names are case sensitive, but can be in any case.

# In Python, you have to define variables before using them this is because python code runs from top to bottom, and there is no hoisting
# print(hourly_wage * hours_worked)
# hourly_wage = 20.00
# hours_worked = 40

# use input() function to get values from the users, you add a prompt by adding a string when you call the function
input("Please enter your name: ")

# Exercises
# Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("What is your name: ")
age = input("How old are you? ")
print(name, age)

# Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.
color = "black"
color = "gray"
print(color)

#fix the issues in the code
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: ")
print(hourly_wage)

print("Hours worked: ")
print(hours_worked)




