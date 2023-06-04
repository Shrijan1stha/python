"""
CSV = Comma Separated Values
way of storing the data in comma separated forms

id,name,age
1,Harry,23    => This is an example of CSV
"""

import csv
from Day25.estd_connection import estd_connection


with open("students.csv", "r") as cr:
    csv_reader = csv.reader(cr)  # This returns an iterator
    next(csv_reader)
    students = []
    # for each_line in csv_reader:  # Skipping 1st line from student.csv file
    #     print(each_line)


    for each_line in csv_reader: # name matra nikalne
        name = each_line[1]
        students.append(each_line[1])

        # Using comprehension
        # Students = [each_line[1] for each_line in students]
print(students)


# cav ko data table ma pathaune

def insert(student_id, name, age):
    cursor =estd_connection()
    sql = f"""
    INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{student_id}', '{name}', {age})
    """
    cursor.execute(sql)
    print("Data added successfully !!")



with open("students.csv", "r") as cr:
    csv_reader = csv.reader(cr)  # This returns an iterator
    next(csv_reader)

    # for each_line in csv_reader:  # Skipping 1st line from student.csv file
    #     print(each_line)


    for each_line in csv_reader:
        name = each_line[1]
        id = each_line[0]
        age = each_line[2]
        insert(id, name, age)