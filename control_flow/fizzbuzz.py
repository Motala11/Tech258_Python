# Write a program that prints the numbers from 1 to 100.
# For multiples of 3, print "Fizz"
# For multiples of 5, print "buzz"
# For numbers which are multiples of both, print "FizzBuzz"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
