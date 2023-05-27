##### Iteration in dictionary
student = {"name": "Jon", "age": 45, "department": "CS"}

for key in student:
    print(key)  # This gives keys of the dictionary 'name', 'age', 'department'


values = student.values()
for value in values:
    print(value)  # This gives values of the dictionary "Jon", 45, "CS"

### OR

for value in student.values():
    print(value)  # This also gives values of the dictionary "Jon", 45, "CS"

for key in student.keys():
    print(key)  # This also gives keys of the dictionary 'name', 'age', 'department'

for i in student.items():
    print(i)  # This also gives key-value pari of the dictionary ('name','Jon'), ('age',45),
# ('department','CS')

for key, value in student.items():
    print(key)
    print(value)
