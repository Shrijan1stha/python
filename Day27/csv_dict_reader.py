import csv
from Day25.estd_connection import estd_connection

def insert(student_id, name, age):
    cursor =estd_connection()
    sql = f"""
    INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{student_id}', '{name}', {age})
    """
    cursor.execute(sql)
    print("Data added successfully !!")

with open("students.csv" ) as cr:
    csv_reader = csv.DictReader(cr)
    for data in csv_reader:
        insert(data['id'], data['name'], data['age'])
