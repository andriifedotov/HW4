import os

import psycopg2

pg_creds = {
    'host': '192.168.0.101'
    , 'port': '5432'
    , 'database': 'dshop'
    , 'user': 'pguser'
    , 'password': 'secret'
}


def read_from_db():
    tables = ['aisles', 'clients', 'departments', 'orders', 'products']
    for table in tables:

        with psycopg2.connect(**pg_creds) as pg_connection:
            cursor = pg_connection.cursor()
            with open(file=os.path.join('.', 'data', f'{table}.csv'), mode='w') as csv_file:
                cursor.copy_expert(f'COPY public.{table} TO STDOUT WITH HEADER CSV', csv_file)


if __name__ == '__main__':
     read_from_db()
