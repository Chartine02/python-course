print(1 + 2) # 3
print(3.4 + 11) # 14.4
print(8 + 4.0) # 12.0
#  if either of the operands for +/-/* is a float, the expression evaluates to a float.
# Examples
print(7 - 5) # 2
print(5 - 11.0) # -6.0
print(-4 - 9) # 13
print(4 * 7) # 28
print(2 * 29.0) # 58.0
print(8.2 * 34) # 278.799..

#  when performing division the result is always a float
print(5 / 6.5) # 0.7692307692307693
print(20 / 2) # 10.0
print(5.5 / 0.5) # 11.0

# Just like in normal mathematics, we can use parentheses to group operations, and these expressions will be given precedence in the order of evaluation.
print((4 - 5) * (5 + 3) / 2)

# Style note
# When we write binary operators (operators with two operands) like +, -, and *, we should put a space on either side of the operator.
print(1 / 11 + 4 - 3 / 2)

# However, it can sometimes be appropriate to forego this space to group operations together.
print(1/11 + 4 - 3/2)

# Exercises
# Print your age to the console.
print(21)
# Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
days_in_year = 365 * 27
weeks_in_year = 52 * 27
months_in_year = 12 * 27
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
print(3.14 * 5 * 5)
print(3.14 * 5  ** 2)
print(3.14 * pow(5,2))




