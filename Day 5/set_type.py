# An empty set can be created in python with a built-in function set().
# Sets are the mutable datatypes in python but the elements of the set must be immutable.
# Sets are unordered datatype i.e. {1, 2} and {2, 1} are same.

s = set()  # Creating an empty set
print(s)

s = {2, 4, 6, 6}  # A non-empty set.
print(s)
s = {1, 2, 2, 3, 4, 4}
print(s)  # It gives {1, 2, 3, 4} because set elements are unique and non-repeated.

s = {[1, 2, 3], 4}
print(s)  # This is not possible in set because all the elements must be immutable in set but, it has a list.



# Adding elements in a set
s = {1, 2, 3}
a.add(4)  # It adds an element to a random positioon in a set
print(s)

s.update([5, 6, 7])  # We can use update() method to update a set. Update method takes iterable/sequence
# as a parameter.

print(s)  # Result => {1, 2, 3, 5, 6, 7}


# Removing elements in a set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s.remove(8)  # remove() method takes value (not index) as a parameter.
print(s)  # Result => {1, 2, 3, 4, 5, 6, 7, 9, 10}

s.discard(5)
print(s)  # Result => {1, 2, 3, 4, 6, 7, 9, 10}

# The difference in discard() and remove() method is. remove() raises an error if the value to be removed is
# not present in the set. But, the discard() method returns None if the value to be removed is not present in
# the set.

s.pop()  # It pops out an element from a random position in a set.
print(s)