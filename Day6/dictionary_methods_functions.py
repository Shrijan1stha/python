student = {"name": "Jon", "age": 23}

print(all(student))  # Returns True if all the values in the iterable are Truthy. Here restult => True.
# This id like 'and' operation.

print(all([]))  # This is an exception because it gives True.

print(any(student)) # This gives True. any() returns True if any of the elements in an iterable is Truthy.
# This is like 'or' operation.

print(any([]))  # this gives False

result = sorted(student)  # It sorts the keys of the dictionary and returns a list.
print(result)  # Result => ["age", "name"]



# Dictionary Methods Condt...
student = {"name": "Jon", "age": 23}
print(student.items())  # It gives list like object  [("name", "Jon"), ("age", 23)]

print(student.keys())  # It gives list like object of dictionary keys
# Result => ["name", "age"]

print(student.values())  # It gives list like object of dictionary values
# Result => ["Jon", 23]


d = student.fromkeys([1, 2, 3], "Hello")
print(d)  # gives a new dictionary with keys of iterable with common value.
# Result => {1: "Hello", 2: "Hello", 3: "Hello"}


d = student.fromkeys([1, 2, 3])
print(d)  # {1: None, 2: None, 3: None}