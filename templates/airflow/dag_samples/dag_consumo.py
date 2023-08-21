from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=60),
}

dag = DAG(
    'DAG_CONSUMO',
    default_args=default_args,
    description='Descricao do DAG',
    schedule_interval='*/5 * * * *',
)

coleta_dados = BashOperator(
    task_id='coleta_dados',
    bash_command='python3 /usr/local/airflow/scripts/ingestao_dados_olist.py',
    dag=dag,
)

coleta_dados