# List are the mutable datatype in python

# Empty list can be creataed using built-in list() function
a = list()  # This gives empty list 'a'
b = []  # Empty list can also be created in this way

c = [1, 2, 3]  # This is a non-empty list.
print(c)

# List are heterogenos data type. That means it can have the elements of different data types

d = [1, "Hello", [5, 6, 7], (1, 2)]
print(d)

# Accessing List elements
# List elements can be accessed with indexing and slicing

# List indexing starts from 0 for forward indexing and -1 for backward indexing

a = [1, "Hello", "World", 5.0, [4, 5, 6], 5]
print(a[0])  # This gives 1
print(a[-1]) # Negative index starts from -1. So, it gives 5.

print(a[4])  # It gives [4, 5, 6]
print(a[-5]) # It gives 'Hello'

print(a[4][1]) # It gives 5 from the nested list(list inside list).

# print(a[6]) # This gives list index out of range error (Index Error).
# print(a[-8]) # This also gives Index Error.

# We can assign item in any particular index of a list
a[2] = 10 # This changes value at 2nd index of the list to 10


# Slicing in list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:])  # This gives exactly the same list.

print(a[:6]) # This includes elements form 0 to 5.
# Result [0, 1, 2, 3, 4, 5]

print(a[0:6]) # This is same as above [:6]

print(a[5:]) # This includes elements form 5th index to the last.
# Result [5, 6, 7 , 8, 9, 10]

print(a[1:8]) # This givs [1, 2, 3, 4, 5, 6, 7].

print(a[1:6:2]) # It jumps 1 step for elements from 1 to 7


# Negative Slicing
print(a[:-4]) # This gives elements form 0 index to -5th index.

print(a[-5:]) # This gives elements form -5th index to the last element.

print(a[-6:-2]) # This gives elements form -6th to -3rd index [5, 6, 7, 8].

print(a[-6:-8]) # This gives []

print(a[-6:-2:2]) # It jumps 1 step for elements



## List operations


# Concenation with + operator

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a+b) # This concatenates two list
# Result [1, 2, 3, 4, 5, 6, 7, 8]


# Repetation with * operator (broadcast)
print(a*2) # It gives [1, 2, 3, 4, 1, 2, 3, 4]

# Membership Check
print(2 in a) # It gives True.
print(5 not in b) # It gives False.

# Methods are the functions which are compulsarily called by an object

sum() # This is a function

a = [1 ,2]
a.append(3) # This is method. {object le call garo vane method}

## List Methods
a = [1, 2, 3]
a.append("Hello")
print(a) # This give [1, 2, 3, "Hello"].

result = a.append(4) # This statement appends value 4 to the list a but it doesn't return anything(i.e. None)
print(a) # [1, 2, 3, "Hello", 4]
print(result) # This give None


a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(c) # None
print(a) # Result =? [1, 2, 3, 4, 5, 6]
# extend() method also returns a None type.

a.insert(1, "Hello World")
print(a) #Result => [1, "Hello World", 2, 3].

a.remove(3) # This removes 3 from the list.
print(a) # Result => [1, "Hello World", 2]
a.remove("Hello World")
print(a) # Result => [1, 2]

# But if we pass tthe elements not present in the list to the remove method then it raises error.