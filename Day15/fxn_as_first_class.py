# functions are object.
# functions can be stored in data structures.
# functions can be passed ta another function.
# functions can be nested.


## Functions can be stored in a variable

def addition(a, b):
    return a + b

print(addition(2, 5))

add = addition
print(add(4, 7))


# Functions can be stored in data structure

data = [1, 2, add, lambda x, y: x + y, addition]
print(data)

