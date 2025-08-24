# extract the names, and then assign each name to a different variable
user_data = input("Please enter your name and username: ").split(" ")
name = user_data[0]
username = user_data[1]

print(f"name: {name} username: {username}")

#  Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5
numbers = [1, 2, 3, 4, 5]
stringified_numbers = []
for num in numbers:
    stringified_numbers.append(str(num))

print(" | ".join(stringified_numbers))

#
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

new_quotes = []

for quote in quotes:
    # new_quotes.append(quote[1:len(quote) - 1])
    new_quotes.append(quote.strip("'"))
    # new_quotes.append(quote[1:-1])


print(new_quotes)

# print len

word = input("Enter anything:").strip()
print(len(word))

