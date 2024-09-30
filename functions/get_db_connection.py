import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="7956",
        port="5432"
    )
    return conn
