import os

# Directory
directory = "test_dir"

# Parent directory YOU NEED TO USE FORWARD SLASH FOR PATHS AS BACKSLASH IS ESCAPE KEY FOR PYTHON
parent_directory = "E:/Documents-SG/Github/python_learning"

# Path
path = os.path.join(parent_directory, directory)

# File name
filename = "testfile.txt"

# Filepath
filepath = os.path.join(path, filename)

# Create the file
with open(filepath, "w") as file1:
    toFile = "Contents of the file go here"
    file1.write(toFile)
