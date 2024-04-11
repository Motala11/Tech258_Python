# Mixed Lists

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)
print(type(mixture))

name = input("What is your name? ")
age = input("How old are you? ")
dob = input("What is your dob? ")
height = input("What is your height in cm? ")

user_details_list = [name, int(age), dob, float(height)]
print(user_details_list)
print("Hi " + user_details_list[0])
print(user_details_list[1])
print(user_details_list[2])
print(user_details_list[3])
