from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator

# Default arguments for DAG
default_args = {
    'owner': 'yeshwanth',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['yeshwanth.yedla@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='yeshwanth_employee_etl_dag',
    default_args=default_args,
    description='ETL DAG to extract employee data and trigger Data Fusion pipeline',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Task 1: Run the local Python script to extract data
    extract_employee_data = BashOperator(
        task_id='extract_employee_data',
        bash_command='python /home/airflow/gcs/dags/scripts/yeshwanth_extract_employee_data.py',
    )

    # Task 2: Start Data Fusion pipeline
    trigger_datafusion_pipeline = CloudDataFusionStartPipelineOperator(
        task_id='trigger_datafusion_pipeline',
        location='us-central1',
        pipeline_name='yeshwanth-etl-pipeline',
        instance_name='datafusion-dev',
    )

    # Set task dependencies
    extract_employee_data >> trigger_datafusion_pipeline
