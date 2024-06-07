import psycopg2
from psycopg2 import OperationalError
import logging

sql_connect = {
    'host': 'localhost',
    'user': 'admin',
    'password': 'example',
    'port': '5432',
    'database': 'postgres'
}


def create_connection():
    try:
        conn = psycopg2.connect(**sql_connect)
        print("Connection successful")
        return conn
    except OperationalError as error:
        logging.error(error)
        raise RuntimeError('Connection failed')


if __name__ == '__main__':
    create_connection()
