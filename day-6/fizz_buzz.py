def fizzbuzz(num):
    if  num % 3 == 0 and num % 5 == 0:
        return 'Fizzbuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif  num % 5 == 0 :
        return 'Buzz'
    else :
        return num

print(fizzbuzz(15))

# 2
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
