# poly = many
# morphism = forms

# For example we have a len() function which works in differentt forms


print(len([1, 2, 3]))  # It works for a list.
print(len((1, 2, 3)))  # It works for a tuple.
print(len({"1": 1, "2": 2}))  # It also works for a dictioonary.



# Function Overloading

def addition(a, b):
    return a + b

def addition(a, b, c):
    return a + b + c


print(addition(1, 2, 3))
# print(1, 2)  # This is not possible because function overloading is not possible in python.


def addition(a, b, c=0):
    return a + b +c

def addition(*args):  # *args le jati ota ni arguments lina pauxa.
    return sum(args)
print(addition(1, 2))
print(addition(1, 2, 3))
print(addition(1, 2, 3, 4))


# We can give the taste of function oerloading by using default parameter. But, it is not actually a
# function overloading.
print(addition(2, 3))
print(addition(2, 3, 4))



# Method Overloading

class Shape:

    def area(self, l):
        return l * l


    # Method overloading is also not possible in python. But, we can give its taste by using
    # default parameter.

    def area(self, l, b=None):
        if not b:
            return l * l
        return l * b


square = Shape()
print(square.area(4))

rectangle = Shape()
print(rectangle.area(4, 5))
