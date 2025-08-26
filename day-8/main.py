# the while keyword, followed by some condition to test. If the condition evaluates to a truthy value, the loop will run one iteration, and then it will test the condition again.

user_number = input("Please enter a number: ")

while int(user_number) < 10:
    print("Your number was less than 10.")
    user_number = input("Please select another number: ")

print("Your number was at least 10.")

# The continue keyword
#  continue allows us to skip the remainder of the loop body for the current iteration.

for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

# else clause with loops
# => for loop
# Get a number to test from the user
dividend = int(input("Please enter a number: "))

# Grab numbers one at a time from the range sequence
for divisor in range(2, dividend):
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

# => while loop
# Get a number to test from the user, and set the initial divisor to 2
dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break

    # Increment the divisor for the next iteration
    divisor = divisor + 1
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

