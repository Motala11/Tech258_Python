# Bools and None

# Booleans can be: True or False

a = True
b = False

print(a == b) # False
print(a != b) # True

# False is ALWAYS 0
print(a >= b) # True
print(a <= b) # False

# Boolean methods

hi = "Hello World!"

print(hi.isalpha()) # Checks if string is alphanumeric hence it returns False
print(hi.islower()) # Checks if string is lowercase hence it returns False
print(hi.isupper()) # Checks if string is uppercase hence it returns False
print(hi.endswith("!")) # Checks if string ends in "!" hence it returns True
print(hi.startswith("H")) # Check if string starts with "H" hence it returns True

# What happens when you try to convert a string to a bool (using casting)?

# Always True unless the string is empty
print(bool("a")) # Returns True
print(bool("")) # Returns False

# Any number other than 0 returns True
print(bool(0)) # Returns False
print(bool(11)) # Returns True

# The value of None

# None is an object, it is essentially a placeholder

# None when converted to a bool is False
print(bool(None))

# This does not mean that None == False

x = None

print(x == False) # False
print(x is None) # True

print(type(x))