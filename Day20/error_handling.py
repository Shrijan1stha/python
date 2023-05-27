# In python (or in any other language) there are three types of error.
# 1. Syntax error
# 2. Logical error
# 3. Exceptions / Runtime error.

try:
    num = int(input("Enter a number:"))
except (ValueError, TypeError):
    print("Please enter valid number")
except IndexError:
    print("Index Error")
except ValueError:
    print("Value Error")
else:
    x = num
    y = num
    summ = x + y
    print(summ)
finally:
    print("Finally executed")

# try:
#     fp = open("student.txt", "w")
#     print(fp)
#     a = 2
#     print(a)
# except:
#     print("Exception occured")
# finally:
#     fp.close()


