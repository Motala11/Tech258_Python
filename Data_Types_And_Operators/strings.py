# Strings

single_quotes = 'Look! Single quotes'
double_quotes = "Look! Double quotes"

print(single_quotes)
print(double_quotes)

# Generally prefer double quotes because ' can be used for other things

# String slicing
hw = ("Hello World!")

# Find out how many characters are in this string using an inbuilt method
print(len(hw))

# Target just the first character (H) using string indexing
print(hw[0])

# Target the last character
print(hw[11])

# Use negative indexing to get the second to last character
print(hw[-2])

# Bonus: Use string slicing to get just the first 3 characters
print(hw[:3])

# String methods
White_space = "Lot's of white space at the end                                    "
print(len(White_space))

# Remove white space but return string count
print(len(White_space.strip()))

example_string = "Here is some text with a lot of text"

# Count a substring within a string
print(example_string.count("text"))

# Make string lowercase
print(example_string.lower())

# Make string uppercase
print(example_string.upper())

# Make a string capitalised
print(example_string.capitalize())

# Replacing text
print(example_string.replace("with ", ","))

# Concatenation and Casting

a = "here "
b = "more "
c = "much more"

print(a + b +c)

x = 2
y= 5.4
z = "there is now a number 25.4 unless we put a space in!"

print(str(x) + " " + str(y) + " " + z)

# str(x) changes int to string. int(z) changes String to int

# F-Strings

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall.")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

# Using f-strings to format numbers

pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places
print(f"Pi to 3 decimal places: {pi:.3f}")

# Use an f-string to print pi to 5 decimal places
print(f"Pi to 3 decimal places: {pi:.5f}")

score = 16
max_score = 24

print(f"You scored {score/max_score:}") # Decimal
print(f"You scored {score/max_score:2%}") # Percentage
print(f"You scored {score/max_score:.2%}") # Percentage rounded to 2 places

# Ensure we are casting to the same type
name = input("Enter your name: ")
age = int(input("Enter your age: "))
dob = input("Enter your date of birth (DD-MM-YYYY): ")
address = input("Enter your address: ")
hobbies = input("Enter your hobbies: ")
thank_you = "Thank you for providing your information!"

print(f"Name:", name, "\nAge:", age, "\nDate of Birth:", dob, "\nAddress:", address, "\nHobbies: ", hobbies)
print(thank_you)


# Extend the capture further to grab details such as address (ensuring that a house number is correctly represented, hobbies, etc.) and respond to the user the details they have provided.