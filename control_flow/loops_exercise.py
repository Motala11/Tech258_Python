# Loops exercise

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {
        "name": "Bronson",
        "money": "$0.05"
    },
    2: {
        "name": "Masha",
        "money": "$3.66"
    },
    3: {
        "name": "Roscoe",
        "money": "$1.14"
    }
}

# Write a loop to print double each number in the "list_data" list
for num in list_data:
    print(num * 2)

# Write another loop that prints items inside  the "embedded_lists" list.
for sublist in embedded_lists:
    print(sublist)

# Create another loop inside the "embedded lists" for loop to list each individual item in each list
for sublist in embedded_lists:
    print(sublist)
    for item in sublist:
        print(item)

# Write a new loop on a new line. This one should loop through the dictionary "dict_data".
for key in dict_data:
    print(key)

# Write another loop, this time it should use the built-in dictionary method value() to print each value for each key inside the dictionary
for value in dict_data:
    print(dict_data[value])

# Create an embedded loop to extract and print the values within the dictionary of each item within that dictionary
for key in dict_data:
    print(dict_data[key]["name"])
    print(dict_data[key]["money"])

# Write another loop but this time it should only print the money values
for inner_dict in dict_data.values():
    print(inner_dict["money"])

# Write a loop that goes through the items in "list_data". Include a nested if statement inside the loop so that each loop will check the number it is currently on to see if:
# - if the number is less than 3, it prints 'less than 3'
# - if the number equals 3, it prints 'I found three'
# - if the number is greater than 3, it prints 'greater than 3'

for num in list_data:
    if num < 3:
        print("Less than 3.")
    elif num == 3:
        print("I found 3.")
    else:
        print("Greater than 3.")



