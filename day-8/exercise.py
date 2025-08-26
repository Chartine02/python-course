import random

# Assignment expression
while (user_input := input('Enter q or p: ')) != 'q':
    if user_input == 'p':
        print("Hello!")

# Guessing game
number = random.randint(1,100)
# answer = input("choose a number between 1 and 100")

while (answer := 
int(input("choose a number between 1 and 100"))) != number:
    if answer > number:
        print('Too high')
    else:
        print("Too low")

print("Your guess was right", number)
    



for char in "Python":
    if char == "o":
        continue

    print(char)


# prime numbers
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(dividend)

print(primes)




