from Day25.estd_connection import estd_connection




def delete(id):
    cursor = estd_connection()

    if id == 'a':
        sql = """
            DELETE FROM STUDENT
        """
        cursor.execute(sql)
        print("All data deleted successfully !!")

    else:
        sql = f"""
        DELETE FROM STUDENT WHERE ID = '{id}'
        """
        cursor.execute(sql)
        print("Student deleted successfully !!")

    choice = input("Wish to continue (y/n)? ")
    return True if choice.lower() == 'y' else False
