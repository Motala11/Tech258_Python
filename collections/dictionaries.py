# Dictionaries

# key = value pairs
# key is the reference, value is the data storage mechanism you want (int, string, etc)

student1 = {
    "name": "Susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1["stream"])
print(student1["name"])
print(student1["completed_lesson_names"][0])

student1["completed_lessons"] = 3
print(student1["completed_lessons"])

student1["completed_lesson_names"].remove("collections")

# Getting the keys for a dictionary
print(student1.keys())

# Dictionary called story1
story1 = {
    "Start": "Po is a panda who works in his family's ramen shop, called 'Ping Dragon Warrior Noodles & Tofu",
    "Middle": "Po admires the Fantastic Five, he wishes to be one of them",
    "End": "Po slowly chases his dreams and becomes the dragon warrior to save his land"
}

# Print the story
print(story1)

# Print story type
print(type(story1))

# Print story key
print(story1.keys())

# Print story values
print(story1.values())

# Print just the start
print(story1["Start"])

# Print just the middle
print(story1["Middle"])

# Print just the end
print(story1["End"])

# Add a hero key and assign it with a value, check if it worked
story1["hero"] = "Po"
print(story1)

