a = "Hello World"
print(len(a))  # Returns the length of a sequence / iterable

print(bool(a))  # here 'a' is non-empty string which is truthy. So, it gives True

print(a[slice(1, 5)])  # Slice() function can be used in the string slicing. First parameter is start an
# second is stop.
# slice(start, stop, step) # step can also be provided as the third parameter.

print(type(a))  # This returns type of the object inside the function. Here it is string.
