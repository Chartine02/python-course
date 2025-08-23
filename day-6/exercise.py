# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    print(f"{employee[0]} will be paid {employee[1] * employee[2]} at the end of the week")

#

total_wages = 0
for employee in employees:
    total_wages += employee[2]

average_wage = total_wages / len(employees)

for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]} earns more than average.")