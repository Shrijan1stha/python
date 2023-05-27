# Create a dictionary student with keys id, name, age, department. Take a input from the user,
#  which info(id, name, age or department) he wants to access and print the result. Handel the possible
#  exceptions.


a = {"id": 1, "name": "Jon", "age": 35, "department": "Accountant"}
key = input("Enter the info you want to get: ")
try:
    result = a[key]
except KeyError:
    print("Invalid key")
else:
    print(f"The {key} of the student is {result}")