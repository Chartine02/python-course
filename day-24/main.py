# Exception hierarchy
# +-- LookupError
# |    +-- IndexError
# |    +-- KeyError

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError:
    print("Could not retrieve that value.")

# To be more specific we can also, when an exception if found py goes through the except clauses in order to see if there is a match
try:
    print(numbers[100])  # <- Out of range index
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")

#
person = {
    "name": "Phil",
    "city": "Budapest"
}

try:
    print(person["age"])  # <- Referencing an undefined key
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")

# Accessing the original exception, mostly for logging purposes
numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError as ex:
    print(f"Error: {ex}")

# nesting try blocks
def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}")
        else:
            return round(f_number)

with open("numbers.txt", "r") as numbers_file:
    numbers = [int(number) for number in numbers_file]




