
# sets can only contain unique elements
# We do not initialize a set with {} because that's for defining an empty dictionary instead we use set()
# if you print an empty set it also prints set()

# you can not any mutable data type to a set

# Adding a single element to a set; use add method
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.add("potato")

print(vegetables)  # {'lettuce', 'broccoli', 'onion', 'potato', 'carrot'}

# Adding multiple elements; use update() method
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin"])

print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}

# Deleting items
# remove() which removes a single element in a list
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(["potato", "pumpkin"])

print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}
# If we try to remove an item which doesn't exist, we get a KeyError. If we don't want this KeyError to be raised, we can use another method called discard.

# pop() removes and returns the item that has been removed
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
random_vegetable = vegetables.pop()  # removes random item

print(vegetables)

# set operations
# union of two sets, it's more like update expect for it, it creates a new set while update modifies the existing one
letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# Intersection, returns a new set with items present in both sets
mod_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
mod_3 = {3, 6, 9, 12, 15, 18}

mod_6 = mod_2.intersection(mod_3)

print(mod_6)  # {18, 12, 6}

# Difference; unlike other sets methods here the order of the sets matters. Cause it returns a set with items present in the set you called the method on
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}

# symmetric difference
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.symmetric_difference(bundle_2))

# {'Cyberpunk 2077', 'Final Fanstay VII', 'Halo Infinite', 'Doom Eternal'}


# set operations with other collections
letters = {"a", "b", "c"}
numbers = [1, 2, 3]

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

# check if something is present in a collection
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)  # True
print(7 in numbers)  # False
