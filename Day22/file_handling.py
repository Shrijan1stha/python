# opening files in different modes:
# 1. r => Read Mode
# 2. w => Write Mode
# 3. a => Append mode
# 4. x = Exclusive Write Mode
# 5. b => Binary Mode(rb, wb, r+b, w+b)
# 6. r+ => Read and Write Mode
# 7. w+ => Weite and Read Mode
# 8. a + => Append and Read Mode

filename = "info.txt"
#

# Write Mode

# fp = open(filename, "w")
# fp.write("Hello  World")
# fp.close()
#
#
# Read Mode

# fp = open(filename, "r")
# data = fp.read()
# print(data)
# fp.close()



# Write and Read Mode
fp = open(filename, "w+")
fp.write("Python is a high level language")
fp.seek(0)  # Moves the file cursor to the very first location in a file.
date = fp.read()
print(date)
fp.close()


# Append Mode
# fp = open(filename, "a")
# fp.write("\nI'm learning python")
# fp.close()


# Exclusive Mode
# fp = open(filename, "x")
# fp.write("Hello World")
# fp.close()



# Context Manager
filename = "message.txt"
with open(filename, "w+") as fp:
    fp.write("Hello World")
    fp.seek(0)
    data = fp.read()
    print(data)


with open(filename, "a") as fp:
    fp.write("\nHi")
    # fp.seek(0)


import test1 as t  # Directly importing a module
from test1 import addition  # Importing function from a module
from Day20 import Factorial_task
Factorial_task.factorial()

from Day20.recurssion_fxn import message

from Day20 import recurssion_fxn
recurssion_fxn.message()
