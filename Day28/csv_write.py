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

with open("student.csv", "w") as cw: # cw is a file poinert
    field_names = students[0].keys()
    csv_writer = csv.DictWriter(cw, fieldnames=field_names)
    csv_writer.writeheader()
    for student in students:
        csv_writer.writerow(student)