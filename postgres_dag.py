from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from postgres import read_from_db

dag = DAG(
    'postgres_dag',
    description='postgres dag',
    schedule_interval='@daily',
    start_date=datetime(2021,2,23,1,0),
)

t1 = PythonOperator(
    task_id='oos_function',
    dag=dag,
    python_callable=read_from_db,
)

t1