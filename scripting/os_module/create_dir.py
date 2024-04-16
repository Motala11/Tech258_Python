import os

# Directory
directory = "test_dir"

# Parent directory YOU NEED TO USE FORWARD SLASH FOR PATHS AS BACKSLASH IS ESCAPE KEY FOR PYTHON
parent_directory = "E:/Documents-SG/Github/python_learning"

# Path
path = os.path.join(parent_directory, directory)

# Create Dir
os.mkdir(path)