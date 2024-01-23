import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.contrib.operators.dataproc_operator import DataProcPySparkOperator
from datetime import datetime, timedelta

# Configuración predeterminada del DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': airflow.utils.dates.days_ago(1)
}

# Crear el DAG
with DAG(
    'transform_and_load_parquet',
    default_args=default_args,
    description='DAG para transformar y cargar datos en BigQuery',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    # Definir operadores
    start_task = DummyOperator(
        task_id='start_task',
        dag=dag,
    )

    # Operador para ejecutar un script de eliminación de duplicados
    remove_duplicates = DataProcPySparkOperator(
        task_id='remove_duplicates',
        job_name='transform_parquet_job',
        main='gs://jobs_dataproc/tlc_rm_dup_and_col_MULTIFILES.py',
        region='us-central1',
        cluster_name='cluster-524f'
    )

    # Operador para ejecutar un script de limpieza de nulos
    clean_nulls = DataProcPySparkOperator(
        task_id='clean_nulls',
        job_name='transform_parquet_job',
        main='gs://jobs_dataproc/tlc_rm_nan_MULTIFILES.py',
        region='us-central1',
        cluster_name='cluster-524f'
    )

    # Operador para cargar el archivo en BigQuery
    load_task = DataProcPySparkOperator(
        task_id='load_task',
        job_name='transform_parquet_job',
        main='gs://jobs_dataproc/load_to_bq_MULTIFILES.py',
        region='us-central1',
        cluster_name='cluster-524f'
    )

    # DummyOperator para representar la tarea de finalización
    finish_task = DummyOperator(
        task_id='finish_task',
        dag=dag,
    )

    # Definir la secuencia de tareas
    start_task >> remove_duplicates >> clean_nulls >> load_task >> finish_task