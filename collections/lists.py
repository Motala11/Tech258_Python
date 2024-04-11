# Lists

# Collections are a way to store multiple pieces of data in one reference/object
# Lists are the most common/simple collection

# Lists are often known as arrays in other languages

#Create a shopping list
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

#Print your shopping list
print("This is your shopping list: \n" + str(shopping_list))

# Show the data type of your list
print("The data type of your shopping list is: {type(shopping_list)}")

# Show the first item in your list
print("The first item in your list is: " + shopping_list[0])

# Show the last item in your list
print("The last item in your list is: " + shopping_list[-1])

# Change the second item in your list
print("The second item currently is: " + shopping_list[1])
shopping_list[1] = "rice"
print("The second item now is :" + shopping_list[1])

# Show the length of the list, add an item and recheck the length
print("The length of the list currently is: ", len(shopping_list))
shopping_list.append("carrots")
print("The length of the list now is: ", len(shopping_list))

# Create a list of items you've forgotten and add them into your shopping list
forgotten_items = ["toffee", "coffee"]
shopping_list.extend(forgotten_items)

# Check this has been added to your shopping list
print("This is your current shopping list: \n" + str(shopping_list))

# Remove bananas from the list
shopping_list.remove("bananas")

# Remove the last item and check it has worked
shopping_list.pop()
print("This is your current shopping list: \n" + str(shopping_list))

# Add watermelon and check it has worked
shopping_list.append("watermelon")
print("This is your current shopping list: \n" + str(shopping_list))

# Create a new list and add it to your shopping list
extra_items = ["double cream", "lettuce"]
shopping_list.extend(extra_items)
print("This is your current shopping list: \n" + str(shopping_list))

# Remove bananas from your shopping list
shopping_list.remove("bananas")
print("This is your current shopping list: \n" + str(shopping_list))

# Remove the last item from your list
shopping_list.pop()
print("This is your current shopping list: \n" + str(shopping_list))

