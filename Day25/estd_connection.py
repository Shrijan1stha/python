# psycopg2 (py Connector for Postgres) is the package to connect python witth postgres.


def estd_connection():
    import psycopg2
    conn = psycopg2.connect(
        database="myinfo",
        user="postgres",
        password="shrijan2886",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit = True
    print("Connection established successfully!!")
    cursor = conn.cursor()
    return cursor


# DATAGRIP