from dotenv import load_dotenv
import sys, os, psycopg2


load_dotenv()

try:
    conection = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        port = os.getenv('DB_PORT'),
        database = os.getenv('DB_DATABASE'),
        user = os.getenv('DB_USERNAME'),
        password = os.getenv('DB_PASSWORD')
    )
    print('Database is Connected!')

except psycopg2.Error as e:
    raise Exception(f"Error while connecting to database: {e}")
