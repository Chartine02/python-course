# first class functions, are functions that can be treated as any other variable in a programming language
# Assigning functions to variables
def add(a, b):
    print(a + b)

adder = add
del add

adder(5, 4)   # 9
print(adder)  # <function add at 0x7f03780ae1f0>

# Functions as arguments
def get_grade_average(student):
    return student["grade_average"]

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=get_grade_average)
sorted_students = (sorted(students, key=get_grade_average, reverse=True))
print(valedictorian)

# Returning functions from other functions
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

operations = {
    "a": add,
    "s": subtract,
    "m": multiply,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("Invalid selection")

# Lambda expressions
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)

