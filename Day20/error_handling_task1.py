### Task
# Take two number as input and add those numbers. Handel the possible exceptions.

try:
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
except ValueError:
    print("ValueError occurred. So, enter valid number.")
else:
    summ = a + b
    print(summ)
# finally:

#     print("executed")
