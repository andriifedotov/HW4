from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from oos_for_airflow import app

dag = DAG(
    'oos_dag',
    description='oos dag',
    schedule_interval='@daily',
    start_date=datetime(2021,2,23,1,0),
)

t1 = PythonOperator(
    task_id='oos_function',
    dag=dag,
    python_callable=app,
    op_kwargs={'date': '2021-02-02'}
)

t1