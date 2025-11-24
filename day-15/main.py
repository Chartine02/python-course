# comprehension; usually this is how we transform an array to string to use title case
names = ["mary", "Richard", "Noah", "KATE"]
processed_names = []

for name in names:
    processed_names.append(name.title())

# list comprehension,
names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]  #Pretty cool! huh

employees = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)
people = [(name.title(), age) for name, age in zip(employees,ages)]
print(people)
# style note: if the comprehension is long, break it down into separate lines
people = [
    (name.title(), age)
    for name, age in zip(employees,ages)
]

# set comprehension, same as list comprehension but here returns a set
names = ["mary", "Richard", "Noah", "KATE"]
names ={name.title() for name in names}

# Dictionary comprehension
student_ids = (112343, 134555, 113826, 124888)
student_names = ("mary", "Richard", "Noah", "KATE")

students = {student_id: name.title() for student_id,name in zip(student_ids,student_names)}
print(students)

# comprehension scope
# a comprehension variable is only accessible inside the comprehension unlike for loops where you can access the variable
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = []

for name in names:
    names_lower.append(name.lower())

print(name)  # This refers to the name variable we defined in the loop

# and this is because behind the scenes these comprehension run as functions, and the variables are only accessible inside the function
names = ["Mary", "Richard", "Noah", "Kate"]
names_lower = [name.lower() for name in names]

print(name)  # NameError
