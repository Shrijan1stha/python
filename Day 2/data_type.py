#### Mutable and immutable ####

# Mutable objects are those objects whose value can be changed even after its creation.

# Immutable objects are those objects whose value can't be changed once it is created.

# Integer, Float, Boolean, Tuple, Strings are immutable datatypes in python.
# List, Dictionary and Set are the mutable datatypes in python

a = (1, 2, 3) # Immutable Type
b = [1, 2, 3] # Mutable Type

b[1] = 5 # This is possible as list in a mutable type
print(b)
# a[1] = 5 # This is not possible