from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'start_date': datetime.now(),
    'catchup': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'DAG_CONSUMO_DADOS_MEDCIOS',
    description='DAG que consome dados medicos no apache Kafka'
    default_args=default_args,
    schedule_interval='*/10 * * * *'
)

consumir_dados_kafka = BashOperator(
    task_id='CONSUMIR_DADOS_KAFKA',
    bash_command='python3 <coloque aqui o caminho do codigo>',
    dag=dag
)

consumir_dados_kafka