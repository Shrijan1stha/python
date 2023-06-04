# WAP to create a students csv where the age of students is above 25.
import csv

students = [
    {"id": "1", "name" : "Arya", "age" : 43},
    {"id": "2", "name" : "Aanuk", "age" : 23},
    {"id": "3", "name" : "Jon", "age" : 31},
    {"id": "4", "name" : "Jane", "age" : 20},
    {"id": "5", "name" : "Krishna", "age" : 26},
    {"id": "5", "name" : "Eren", "age" : 21},
    {"id": "7", "name" : "John", "age" : 30},
    {"id": "8", "name" : "Nova", "age" : 31},
    {"id": "9", "name" : "Ram", "age" : 17},
    {"id": "10", "name" : "Jim", "age" : 19},
]

with open("task1.csv", "w") as cw:
    field_names = students[0].keys()
    csv_write = csv.DictWriter(cw, fieldnames=field_names)
    csv_write.writeheader()
    for student in students:
        if student["age"] > 25:
            csv_write.writerow(student)
