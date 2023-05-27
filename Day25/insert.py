from estd_connection import estd_connection

cursor = estd_connection()

id = input("Enter student id: ")
name = input("Enter student name: ")
age = int(input("Enter student age: "))

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}', '{name}', {age}) 
"""

cursor.execute(sql)
print("Student added successfully !!")
