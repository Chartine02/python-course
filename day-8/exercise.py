import random

# Assignment expression
while (user_input := input('Enter q or p: ')) != 'q':
    if user_input == 'p':
        print("Hello!")

# Guessing game
number = random.randint(1,100)
answer = input("choose a number between 1 and 100")






