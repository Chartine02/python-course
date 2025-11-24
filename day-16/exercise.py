
#
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

sorted_students = sorted(students, key=lambda student: student["grade_average"])
print(sorted_students)

# convert to lambda
def exponentiate(base, exponent):
    return base ** exponent
exp = lambda base, exponent: base ** exponent
print(exp)

