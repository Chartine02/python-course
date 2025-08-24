# join is used to join a collection of string
project_authors = ["Mike", "Sofia", "Helen"]

print(f"The people who worked on this project are: {', '.join(project_authors)}.")

# if you want to split a list of numbers first convert them to strings
numbers = [1, 2, 3, 4, 5]
stringified_numbers = []

for number in numbers:
    stringified_numbers.append(str(number))

print(', '.join(stringified_numbers)) # 1, 2, 3, 4, 5

# splitting string
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
numbers_list = user_numbers.split(",")

print(numbers_list) # ['1', '2', '3', '4', '5']

# We don’t always need to call split. If we just want to put every character as a different item in a list or tuple, we can just pass the string to the list or tuple function instead
sample_string = "Python"

print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')

# new line character
print("Super Special Mega Awesome Program\n\nBy Phillip Best")


# Slicing
original_string = "Python"
sliced_string = original_string[0:3]

print(sliced_string)  # Pyt

original_string = "Python"
sliced_string = original_string[3:]

print(sliced_string)  # hon

# len function returns the length of an obj
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5



