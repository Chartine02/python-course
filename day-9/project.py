card_number = (input("Enter a card number: ")).strip()

numbers = list(card_number)
checking_digit = numbers.pop()
numbers.reverse()

converted_numbers = []
for i, num in enumerate(numbers):
    num = int(num)
    if i % 2 == 0:
        n = (num * 2) - 9 if (num * 2) > 9 else num
        converted_numbers.append(n)
    else:
       converted_numbers.append(int(num))

converted_numbers.append(int(checking_digit))
total = sum(converted_numbers)

if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")