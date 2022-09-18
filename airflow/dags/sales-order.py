import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "airflow"}


with DAG(
    dag_id="sales_order",
    start_date=datetime.datetime(2022, 9, 12),
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
) as dag:

    sales_order_to_data_lake = BashOperator(
        task_id="sales_order_to_data_lake",
        bash_command="""
            python ~/batch-data-pipeline-exercise/src/sales_order_to_lake.py
        """
    )

    sales_order_to_data_ods = BashOperator(
        task_id="sales_order_to_data_ods",
        bash_command="""
            python ~/batch-data-pipeline-exercise/src/sales_order_to_ods.py
        """
    )

    sales_order_to_data_lake >> sales_order_to_data_ods
