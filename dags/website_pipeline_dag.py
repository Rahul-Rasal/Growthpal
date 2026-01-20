from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append("/path/to/src")

from crawler import crawl
from extractor import *
from transformer import *
from aggregator import *

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="website_data_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    default_args=default_args,
    catchup=False
) as dag:

    crawl_task = PythonOperator(
        task_id="crawl_websites",
        python_callable=crawl
    )

    extract_task = PythonOperator(
        task_id="extract_content",
        python_callable=lambda: None
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=lambda: None
    )

    aggregate_task = PythonOperator(
        task_id="aggregate_metrics",
        python_callable=lambda: None
    )

    crawl_task >> extract_task >> transform_task >> aggregate_task
