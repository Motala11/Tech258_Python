# Possible film ratings are "universal", "pg", "12", "12a", "15", "18"

film_rating = "UNIVERSAL"

# Use an if statement to check for universal rating

# If statement goes here
if film_rating.lower() == "universal":
    print("All age groups can watch this film")
# Check if the film rating is "pg"
# ELIF statment goes here
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
# Check if the film rating is "12" or "12a"
# ELIF statement goes here
elif film_rating.lower() == "12" or "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# Check if the film rating is "15"
# ELIF statement goes here
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
# Check if the film rating is "18"
# ELIF statement goes here
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
# ELSE statement goes here
    print("This is not a correct rating, please use 'universal', 'pg', '12', '12a', '15', '18'. ")