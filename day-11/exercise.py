# 1) Create an empty set and assign it to a variable.
animals = set()
# 2) Add three items to your empty set using either several add calls, or a single call to update.
animals.update(["dog", "cat", "hen"])
# Create a second set which includes at least one common element with the first set.
wild_animals = {"dog", "lion", "tiger"}
# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
animals_intersection = animals.intersection(wild_animals)
print(animals_intersection)
animals_union = animals.union(wild_animals)
print(animals_union)
animals_symmetric_difference = animals.symmetric_difference(wild_animals)
print(animals_symmetric_difference)

# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

numbers = range(5, 11)
num = input("Enter any number: ")
if num in numbers:
    print(num, "is in the list")
else:
    if num < numbers[0]:
        print("Your number is too low")
    else:
        print("Your number is too high")