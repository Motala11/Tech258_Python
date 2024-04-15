# Python standard library
import datetime
import os
import sys
import builtins
import requests


# The standard library consists of many modules and packages that are very useful, and were thus added to python by default

import random
import math


# print(random.random())
# print(random.randrange(1,12))

# Math demo

# num_float = 23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)
# print(f"Remainder from 1/5: {math.remainder(1, 5)}")

# os demo

# return current working directory
working_dir = os.getcwd()
print(f"Current working directory is: {working_dir}")

# get user
username = os.environ.get("Username") or os.environ.get("User")
print(f"Username is: {username}")

# cpu cores
cpu_cores = os.cpu_count()
print(f"CPU cores: {cpu_cores}")

# make directory
# os.mkdir("Test_dir")

# sys demo
print(f"Current path: {sys.path}")

# Print python version
print(sys.version)

# datetime demo
print(f"Today's date is: {datetime.datetime.today()}")

# Builtins demo
for name in dir(builtins):
    if name[0].islower():
        print(name)

# requests demo

request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc)
# print(request_bbc.content)