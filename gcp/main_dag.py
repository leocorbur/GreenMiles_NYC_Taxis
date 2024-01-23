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
    'main_dag',
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

    # TLC cs_to_bq
    tlc_task = DataProcPySparkOperator(
        task_id='tlc_task',
        job_name='tlc',
        main='gs://jobs_dataproc/tlc.py',
        region='us-central1',
        cluster_name='cluster-524f'
    )

    # Weather cs_to_bq
    weather_task = DataProcPySparkOperator(
        task_id = 'weather_task',
        job_name = 'weather',
        main = 'gs://jobs_dataproc/weather.py',
        region = 'us-central1',
        cluster_name='cluster-524f'
    )

    # Air Pollution cs_to_bq
    airPollution_task = DataProcPySparkOperator(
        task_id = 'airPollution_task',
        job_name = 'airPollution',
        main = 'gs://jobs_dataproc/airPollution.py',
        region = 'us-central1',
        cluster_name='cluster-524f'
    )

    # Fuel Consumption cs_to_bq
    fuelConsumption_task = DataProcPySparkOperator(
        task_id = 'fuelConsumption_task',
        job_name = 'fuelConsumption',
        main = 'gs://jobs_dataproc/fuelConsumption.py',
        region = 'us-central1',
        cluster_name='cluster-524f'
    )

    # Alternative Fuel Vehicles cs_to_bq
    altFuelVehicles_task = DataProcPySparkOperator(
        task_id = 'fuelVehicle_task',
        job_name = 'altFuelVehicles',
        main = 'gs://jobs_dataproc/altFuelVehicles.py',
        region = 'us-central1',
        cluster_name='cluster-524f'
    )

    # Car prices cs_to_bq
    carPrices_task = DataProcPySparkOperator(
        task_id = 'carPrices_task',
        job_name = 'carPrices',
        main = 'gs://jobs_dataproc/carPrices.py',
        region = 'us-central1',
        cluster_name='cluster-524f'
    )


    # DummyOperator para representar la tarea de finalización
    finish_task = DummyOperator(
        task_id='finish_task',
        dag=dag,
    )

    # Definir la secuencia de tareas
    start_task >> tlc_task
    tlc_task >> [weather_task, airPollution_task]
    [weather_task, airPollution_task] >> [fuelConsumption_task, altFuelVehicles_task, carPrices_task]
    [fuelConsumption_task, altFuelVehicles_task, carPrices_task] >> finish_task
