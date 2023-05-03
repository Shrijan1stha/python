# String formatting using %

m = "Hello I'm %s. I'm %d years old" %("Jon", 45)
print(m)

m = "I have Rs. %.2f" %(45.256122)
print(m)


# String formatting using format() method
m = "Hello I'm {}" .format("Jon")
print(m)

m = "I'm {age} years old" .format(age=30)
print(m)


m = "I have {0}, {1} and {2}" .format("pen", "pencil", "copy")
print(m) # Result => I have pen, pencil and copy.

m = "I have {1}, {0} and {2}" .format("pen", "pencil", "copy")
print(m) # Result => I have pencil, pen and copy.

# If you don't give index and have multiple placeholders then the values are taken in order
m = "I have {}, {}, {}" .format("pen", "pencil", "copy")
print(m)  # Result => I have pen, pencil and copy.