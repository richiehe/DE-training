import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "airflow"}

with DAG(
        dag_id="daily_dag",
        start_date=datetime.datetime(2022, 9, 12),
        schedule_interval="00 23 * * *",
        default_args=default_args,
        catchup=False,
) as dag:
    daily_dag_start = BashOperator(
        task_id='daily_dag_start',
        bash_command='echo Load raw data into data lake',
    )

    address_to_data_lake = BashOperator(
        task_id="address_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            "src_path": "/data/raw/address/processed_date={{ ds }}/Address.csv",
            "sink_path": "/data/data_lake_bucket/address/",
            "schema_key": "address",
        }
    )

    customer_to_data_lake = BashOperator(
        task_id="customer_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/customer/processed_date={{ ds }}/Customer.csv",
            'sink_path': "/data/data_lake_bucket/customer/",
            'schema_key': "customer",
        },
    )

    customer_address_to_data_lake = BashOperator(
        task_id="customer_address_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/customer_address/processed_date={{ ds }}/CustomerAddress.csv",
            'sink_path': "/data/data_lake_bucket/customer_address/",
            'schema_key': "customer_address",
        },
    )

    product_to_data_lake = BashOperator(
        task_id="product_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/product/processed_date={{ ds }}/Product.csv",
            'sink_path': "/data/data_lake_bucket/product/",
            'schema_key': "product",
        },
    )

    product_category_to_data_lake = BashOperator(
        task_id="product_category_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/product_category/processed_date={{ ds }}/ProductCategory.csv",
            'sink_path': "/data/data_lake_bucket/product_category/",
            'schema_key': "product_category",
        },
    )

    product_description_to_data_lake = BashOperator(
        task_id="product_description_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/product_description/processed_date={{ ds }}/ProductDescription.csv",
            'sink_path': "/data/data_lake_bucket/product_description/",
            'schema_key': "product_description",
        },
    )

    product_model_to_data_lake = BashOperator(
        task_id="product_model_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/product_model/processed_date={{ ds }}/ProductModel.csv",
            'sink_path': "/data/data_lake_bucket/product_model/",
            'schema_key': "product_model",
        },
    )

    product_model_product_description_to_data_lake = BashOperator(
        task_id="product_model_product_description_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/product_model_product_description/processed_date={{ ds }}/ProductModelProductDescription.csv",
            'sink_path': "/data/data_lake_bucket/product_model_product_description/",
            'schema_key': "product_model_product_description",
        },
    )

    sales_order_to_data_lake = BashOperator(
        task_id="sales_order_to_data_lake",
        bash_command="""
            python ~/Documents/DE-training/src/utils/source_to_lake.py
        """,
        params={
            'src_path': "/data/raw/sales_order/processed_date={{ ds }}/SalesOrder.csv",
            'sink_path': "/data/data_lake_bucket/sales_order/",
            'schema_key': "sales_order",
        },
    )

    load_into_data_lake_tasks = [
        address_to_data_lake,
        customer_to_data_lake,
        customer_address_to_data_lake,
        product_to_data_lake,
        product_category_to_data_lake,
        product_description_to_data_lake,
        product_model_to_data_lake,
        product_model_product_description_to_data_lake,
        sales_order_to_data_lake
    ]

    load_into_data_lake_completed = BashOperator(
        task_id='load_into_data_lake_completed',
        bash_command='echo raw data on {{ ds }} has been loaded into data lake',
    )

    address_to_ods = BashOperator(
        task_id="address_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/address/processed_date={{ ds }}/",
            'table_name': 'ods_address',
        },
    )

    customer_to_ods = BashOperator(
        task_id="customer_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/customer/processed_date={{ ds }}/",
            'table_name': 'ods_customer',
        },
    )

    customer_address_to_ods = BashOperator(
        task_id="customer_address_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/customer_address/processed_date={{ ds }}/",
            'table_name': 'ods_customer_address',
        },
    )

    product_to_ods = BashOperator(
        task_id="product_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/product/processed_date={{ ds }}/",
            'table_name': 'ods_customer_address',
        },
    )

    product_category_to_ods = BashOperator(
        task_id="product_category_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/product_category/processed_date={{ ds }}/",
            'table_name': 'ods_product_category',
        },
    )

    product_description_to_ods = BashOperator(
        task_id="product_description_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/product_description/processed_date={{ ds }}/",
            'table_name': 'ods_product_description',
        },
    )

    product_model_to_ods = BashOperator(
        task_id="product_model_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/product_model/processed_date={{ ds }}/",
            'table_name': 'ods_product_model',
        },
    )

    product_model_product_description_to_ods = BashOperator(
        task_id="product_model_product_description_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/product_model_product_description/processed_date={{ ds }}/",
            'table_name': 'ods_product_model_product_description',
        },
    )

    sales_order_to_data_ods = BashOperator(
        task_id="sales_order_to_ods",
        bash_command="""
            python ~/Documents/DE-training/src/lake_to_ods.py
        """,
        params={
            'src_path': "/data/data_lake_bucket/sales_order/processed_date={{ ds }}/",
            'table_name': 'ods_sales_order',
        },
    )

    load_into_ods_tasks = [
        address_to_ods,
        customer_to_ods,
        customer_address_to_ods,
        product_to_ods,
        product_category_to_ods,
        product_description_to_ods,
        product_model_to_ods,
        product_model_product_description_to_ods,
        sales_order_to_data_ods,
    ]

    load_into_ods_completed = BashOperator(
        task_id="load_into_ods_completed",
        bash_command='echo data in lake on {{ ds }} has been loaded into ods',
    )

    daily_dag_start >> load_into_data_lake_tasks >> load_into_data_lake_completed >> load_into_ods_tasks >> load_into_ods_completed
