from operator import methodcaller
# Iterators
# Properties of iterators
# 1. They are lazy, Being lazy comes with some significant memory benefits, because we only have to keep the most recent value in memory


words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

# we can't determine the length of a_words until we actually performing the filtering operation.
# However, filter is going to wait until we ask it for values to calculate anything.

# 2. Iterator values are consumed

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

for word in a_words:
    print('loop 1')
    print(word)

for word in a_words:
    print('loop 2')
    print(word)

# What we would usually expect here is for the names to print twice, but that's not what happens.

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

for word in a_words:
    print(word)

a_words = list(a_words)
print(a_words)  # []
# we get an empty list cause the values have been provided to us, and they can't be given

# Changes to mutable collections can affect an iterator
# from operator import methodcaller
words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

words.append("apple")

for word in a_words:
    print(word) #anaconda anime addition apple

# Manual iteration with the next function

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

print(next(a_words))  # "anaconda"
print(next(a_words))  # "anime"

# what's a practical use-case for this?
irises = []

with open("iris.csv", "r") as iris_file:
    # instead of using iris_file.readlines()
    headers = next(iris_file).strip().split(",")

    for row in iris_file:
        iris = row.strip().split(",")
        iris_dict = dict(zip(headers, iris))

        irises.append(iris_dict)


# The StopIteration exception
# It is handled for us when we use for loop or destruction but not handled when doing manual iteration
from operator import methodcaller

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

print(next(a_words))  # "anaconda"
print(next(a_words))  # "anime"
print(next(a_words))  # "addition"

print(next(a_words))  # StopIteration



