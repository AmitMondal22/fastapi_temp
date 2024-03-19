import mysql.connector
from dotenv import load_dotenv

load_dotenv()
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Amit@2022"
MYSQL_DB = "fast_api"

def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )