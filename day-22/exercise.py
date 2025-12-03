from itertools import cycle

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

summation = map(lambda x: sum(x), numbers)

first_sum = next(summation)
second_sum = next(summation)

print(first_sum, second_sum)

# 2.
iteration = cycle(["Ann", "Kan", "Kel"])
days = cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

def cycle():
    for i in range(31):
        print(f"{next(iteration)} will close on day {next(days)}")


cycle()