# Sets and Frozen sets

# Create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED

# Add an element
fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
fruits.add("banana")
print(fruits) # There can be no duplicates in sets

# Convert list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a | set_b)
print(set_a - set_b) # Shows what is in set A but not set B

# Frozen set --> IMMUTABLE SET

frozen_set = frozenset(["hello", "world"])
print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)