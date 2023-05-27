from Day25.estd_connection import estd_connection

cursor = estd_connection()

def create():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    sql = f"""
        INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}', '{name}', {age})
    """

    cursor.execute(sql)
    print("Student added successfully !!")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False
