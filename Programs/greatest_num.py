# WAP to input three number and find the greatest number among three.

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))

if a > b and a > c:
    print(a, " is greatest")
elif b > a and b > c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
