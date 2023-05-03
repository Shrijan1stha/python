### Arithmetic Operators

# Addition
a = 1
b = 2
print(a + b) # Here + is addition operator

# Subtraction
a = 2
b = 5
print(b - a) # Here - is a subtraction operator

#Multiplication
print(a * b) # Here * is used for multiplication

#Division
print(a / b) # Here / is used for division operation

#Exponent
print(a ** b) # This is 'a' raised to the power 'b'
# ** is used for exponential operation

#Remainder
print(a % 2) # Here a is 5. So remainder of 5/2 is 1

#Floor Division
print(a // 2) # // is an operator floor operator that terminates the decimal digits. Hence, it returns 2


#Relational Operators
a = 1
b = 1
print(a == b) # '==' is a comparision operator to check whether the values are equal or not. Here it gives true

a = 5
print(a > b) # it returns False
print(b > a) # it returns True

a = 2
b = 2
print(a >= b) # it gives True
print(a <= b) # it gives True

print(a != b) # it gives False


## Logical Operations

#And
print(True and True) # True
print(True and False) # Flase
print(False and True) # False
print(False and False) # False

#OR
print(True and True) # True
print(True and False) # True
print(False and True) # True
print(False and False) # False

#Not
print( not True) # False
print( not False) # Truse


## Identity Operators

# is and is not are the identity operators

a = 1
b = 1
# Here a and b both refers to the same object with value 1
print( a is b) # so it returns true

b = 123
print(a is b) # It returns False because b is another object with value 123
print(a is not b) # It gives True


## Membership Operator
ages = [21, 22, 23, 24]
print(21 in ages) # It give True
print(22 not in ages) # It give False

print(25 in ages) # It gives False
print(25 not in ages) # It gives True

name = "broadway"
print('b' in name) # It gives True

## Assignment Operators
a = 1 # "=" is the simplest assignment operator which assigns value from the RHS to the variable in LHS

a = a + 1 # This increase the value of a by 1
# But this logic can also be written as following
a += 1 # Here += is an assignment operator

a -= 1 # Here -= is an assignment operator


## Precedance and Associativity

# Precedance it the rule that determines the priority of operators in an operator.

# Associativity is the rule that determines the priority of operators if one or more operatoors have the same
# precedence

# Normally Associativity is from left to right. But for ** operator it is from right-left

print(2**3**2) # 3**2 is evaluated fist and result is raised by 2.