# import fractions
from fractions import Fraction
import random

print(Fraction(2.25))
print(random.randint(1,100))

def get_user_num():
    num = int(input('Choose a random number between 1 and 10:'))
    return num

def guess_num():
    response = get_user_num()
    random_number = random.randint(1,10)
    print(f'random number: {random_number}')
    while response != random_number:
        if response > random_number:
            print('Your guess was too high')
            response = get_user_num()
        else:
            print('your guess was too low')
            response = get_user_num()
    print('Kudos!! You have guessed the right number')

guess_num()