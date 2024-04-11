# Waiter helper exercise

# Greet the user
greet_customer = "Hello! Welcome to the restaurant."

# Print a list of starters
starters = {
    "Garlic bread": 4.99,
    "Calamari": 6.99,
    "Falafel": 4.99
}

# Take an input of the user for their starters
user_starters = input("What would you like to order for your starters? ")

# Print a list of mains
mains = {"Butterfly chicken": 12.99,
         "Steak": 18.99,
         "Chicken pasta": 11.99
         }

# Take an input of the user for their mains
user_mains = input("What would you like to order for your mains? ")

# Print a list of desserts
desserts = {"Cookie dough": 5.99,
            "Vanilla icecream": 4.99,
            "Chocolate sundae": 4.99}

# Take an input of the user for their dessert
user_dessert = input("What would you like to order for your dessert? ")

# Print all of the user's choices
customer_order_list = [user_starters, user_mains, user_dessert]
print(customer_order_list)

# Create a bill to total the order of the customer

user_starter_price = float

total_bill = starters.get(user_starters) + mains.get(user_mains) + desserts.get(user_dessert)
print(f"Your total bill is: £{total_bill:.2f}")

