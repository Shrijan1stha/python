from Day25.estd_connection import estd_connection



def update(id, to_change, changed_value):
    cursor = estd_connection()

    sql = f"""
    UPDATE STUDENT SET {to_change} = '{changed_value}' WHERE ID = '{id}'
    """

    cursor.execute(sql)
    print("Student updated successfully !!")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False