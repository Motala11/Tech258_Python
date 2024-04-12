# Functions

# DRY - Don't Repeat Yourself

# basic function

def print_something(name):
    print(f"Hello! My name is {name}")

print_something("Motala")

# function with args

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(1, 4))

def addition(int1 = 2, int2 = 2):
    return int1 + int2

print(addition())
print(addition(int2=15))

# Multiple arguments
def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6, 7)

# type hints
def division(denom: int, num: int) -> float:
    return denom / num

print(division(10/5))

