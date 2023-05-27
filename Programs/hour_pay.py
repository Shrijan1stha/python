# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly
# rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45
# hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input
# to read a string and float() to convert the string to a number.


a = float(input("Enter hours:"))
b = float(input("Enter rate:"))

if a <= 40:
    print("He gets", a * b)
else:
    print("He gets", 40 * b + (a - 40)*b*1.5)

# ot = hour -40
# normal_pay = 40 * rate
# ot_pay = ot * rate * 1.5
# pay = normal_pay + ot_pay
#print("Received payment:" , pay)
