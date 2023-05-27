"""
From the given list of integer create a number whose digit are the elements of the list.
A = [4, 2, 3, 1, 2, 5]
Result = 423125
"""

a = [4, 2, 3, 1, 2, 5]
s = ""

for i in a:
    s += f"{i}"
print(s)


