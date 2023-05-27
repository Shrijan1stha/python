# Functions are the block of reusable code

# This is a function defination
def addition(a, b):
    return a + b


# These are function calls
addition(2, 3)
addition(6, 7)


# Return statement in a function

# If we don't return anything from a function then it returns 'None' by default.
# This is a function defination without any return and returns 'None'
def addition(a, b):
    print(a + b)

result = addition(2, 3)
print(result)  # Result => None

# This is a function defination with a return. Here, it returns sum of the parameters.
def addition(a, b):
    return a + b

result = addition(2, 3)
print(result)  # Result => 5


# Function Arguments
# Python function arguments are of three types:
# 1. Positional Arguments
# 2. Keyword / Default Arguments
# 3.Arbitrary Arguments


# Here a, b  and c are positional arguments. Positional arguments should be sent compulsorily during the
# function call.
def summ(a, b, c):
    return a + b + c

result = summ(1, 2, 3)


# Here b is a keyword / default parameter
def summ(a, b=2):
    return a + b

print(summ(2))  # It is not mandatory to send a default parameter during function call
print(summ(4, 5))  # Result => 9. Default agruments are only for fallbacks.
# Default values are overridden if a different value is sent durng the function call.