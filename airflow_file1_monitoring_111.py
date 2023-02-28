import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator
from datetime import timedelta
BUCKET_NAME="bucket909014"

default_args={
        'depends_on_past': False,
        #'email': ['arun@gamil.com,teja@gamil,ravi@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 5,
        'retry_delay': timedelta(minutes=1)
}
dag = DAG(
    'airflow_file1_monitoring',
    default_args=default_args,
    description='liveness monitoring dag',
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=1)
)

gcs_bucket_create_acl_entry_task = GCSBucketCreateBucketOperator(
    bucket=BUCKET_NAME,
    entity=GCS_ACL_ENTITY,
    role=GCS_ACL_BUCKET_ROLE,
    task_id="gcs_bucket_create_acl_entry_task",
    dag=dag
    )

create_dataset = BigQueryCreateEmptyDatasetOperator(
    task_id="create_dataset", dataset_id=DATASET_NAME,
    dag=dag)

    
    