# 1
def exponentiated(base, exponent):
    return base ** exponent

def process_string(string):
    return string.strip().lower()

def process_data(data):
    name, nationality, age = data
    return {'name': name, "nationality": nationality, "age": age}

print(process_data(("Tom Hardy", "English", 42)))

def is_prime(n):
   for num in range(2, n):
       if n % num == 0:
           return False

   return True




