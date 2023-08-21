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
    'DAG_INGESTAO_DADOS_MEDICOS',
    description='DAG que gera dados medicos no apache Kafka'
    default_args=default_args,
    schedule_interval='*/5 * * * *'
)

produzir_dados_kafka = BashOperator(
    task_id='PRODUZIR_DADOS_KAFKA',
    bash_command='python3 <coloque aqui o caminho do codigo>',
    dag=dag
)

gera_dados_kafka