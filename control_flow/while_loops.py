# While loops exercise

x = 0

# Create a while loop that loops while x is less than 10. Every time it loops, the value should be printed in an f-string and x should increment.
while x <10:
    print(f"x -> {x}")
    x += 1

# The code does not run when you comment out the assignment of x as x is not defined.

# If you do not increment x, the loop will run until your system crashes. This is because x will forever be 0.


# Ask user for their age

# age = input("What is your age? ")
# print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        age = int(age)
        if age <= 117:
            user_prompt = False
        else:
            print("Please enter an age less than or equal to 117.")
    else:
        print("You need to enter your age as digits.")
print(f"Your age is {age}")