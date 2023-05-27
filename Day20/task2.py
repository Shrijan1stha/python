# Take one number and divide by another. Handel the possible exceptions

try:
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    print("Division of", a ,"and", b ,"is:", a / b)
except ValueError:
    print("Please, Enter the valid number")
except ZeroDivisionError:
    print("0 le divide na gar")
