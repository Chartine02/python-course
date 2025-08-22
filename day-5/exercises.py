# Try to approximate the behaviour of the is operator using ==.
a = [1,2,3]
b = [1,2,3]

print(id(a) == id(b))

# Try to use the is operator or the id function to investigate
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

nmbers = [1, 2, 3, 4]
nmbers.append(5)

print(nmbers is new_numbers)

# Tell the user whether the number is positive, negative, or zero
num = int(input('Enter a number:'))

if num < 0 :
    print("You entered a negative number")
else:
    print("You entered a positive number")

# determine whether an employee is owed any overtime

employee_name = input("Enter the employee's name: ")
hours_worked = float(input(f"How many hours did {employee_name} work this week? "))
hourly_wage = float(input(f"What is {employee_name}'s hourly wage? "))

if hours_worked > 40:
    regular_pay = 40 * hourly_wage
    overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
    owed_pay = int(regular_pay + overtime_pay)
else:
    owed_pay = int(hours_worked * hourly_wage)

print(f"{employee_name} is owed ${owed_pay}.")
