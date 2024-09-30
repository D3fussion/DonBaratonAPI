import psycopg2


URL = os.environ.get('SQL_KEY')

def get_db_connection():
    conn = psycopg2.connect(URL)
    return conn
