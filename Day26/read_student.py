from Day25.estd_connection import estd_connection

def read(student_id):
    cursor = estd_connection()

    sql = f"""
        SELECT * FROM STUDENT WHERE ID = '{student_id}'
    """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False
