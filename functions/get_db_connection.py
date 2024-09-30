import psycopg2
import os

URL = os.environ.get('SQL_KEY')

def get_db_connection():
    conn = psycopg2.connect(URL)
    return conn
