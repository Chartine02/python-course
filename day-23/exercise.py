# prime numbers
primes = []

# for dividend in range(2, 101):
#     for divisor in range(2, dividend):
#         if dividend % divisor == 0:
#             break
#     else:
#         primes.append(dividend)
#
# print(primes)


def get_primes(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        yield n

# 2

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)
names = (name.strip().title() for name in names)
print(names)