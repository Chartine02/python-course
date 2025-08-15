name = input("Please enter the employee's name: ").strip().title()
hourly_wage = input("What is their hourly wage? ")
worked_hours = input("How many hours did they work this week?: ")

total_earnings = float(hourly_wage) * float(worked_hours)

print(f"{name} earned ${total_earnings} this week")
