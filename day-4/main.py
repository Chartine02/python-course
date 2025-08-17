# lists are containers for other values
names = ["John", "Alice", "Sarah", "George"]

movie_titles = [
    "Eternal Sunshine of the Spotless Mind",
    "Memento",
    "Requiem for a Dream"
]
# we can mix whatever types of value we want in a list, you don’t have to have just strings, or just integers.
friend_details = ["John", 27, "Web Developer"]

# Accessing values in a list
names = ["John", "Alice", "Sarah", "George"]

print(names[2])  # Sarah
print(names[-1])  # George

# Adding new items to a list
names.append("Simon")
print(names[-1])  # Simon

# we can also use + to add an item to a list, in this case both operands must be lists
# The approach is also somewhat different, as we have to perform an assignment as part of the operation. This can sometimes be handy, because it doesn’t modify the original list, as the operation yields a new list instead. append, on the other hand, modifies the existing list.
names = names + ["Simon"]
print(names[-1])  # Simon

# To add multiple items to a list we use extend
names.extend(["Nina", "Kaan"])

# To add items in the middle we use insert, which takes two args the starting index and the item to insert
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)
print(numbers)  # [1, 2, 3, 4, 5]

# If you provide an index that is not present, the element is added to the end of the list
numbers = [1, 2, 4, 5]
numbers.insert(7, 3)
print(numbers)  # [1, 2, 4, 5, 3]

# Removing elements from a list
names = ["John", "Sarah", "Alice", "John"]
names.remove("John")
print(names)  # ['Sarah', 'Alice', 'John']

# del can be used to delete anything we want, including a whole list, but if we use a subscription expression, we can use it to remove an item at a specific index.
names = ["John", "Sarah", "Alice", "Mike"]
del names[0]
print(names)  # ['Sarah', 'Alice', 'Mike']

# By default pop is going to remove the last item in the list, but we can optionally pass in an index as an argument to remove a different item instead.

names = ["John", "Sarah", "Alice", "Mike"]
names.pop()
print(names)  # ['John', 'Sarah', 'Alice']

names.pop(1)
print(names)  # ['John', 'Alice']

# pop returns the removed element, which can be stored for future use
names = ["John", "Sarah", "Alice", "Mike"]
last_in_line = names.pop()
print(names)         # ['John', 'Sarah', 'Alice']
print(last_in_line)  # Mike

# to remove everything from a list use clear()
names = ["John", "Sarah", "Alice", "John"]
names.clear()

print(names)  # []

