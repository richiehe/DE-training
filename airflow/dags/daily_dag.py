import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from ods.lake_to_ods import to_ods
from lake.source_to_lake import to_lake

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
        bash_command='echo Load raw data into data lake on {{ ds }}',
    )

    address_to_data_lake = PythonOperator(
        task_id="address_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            "src_path": "/data/raw/address/processed_date={{ ds }}/Address.csv",
            "sink_path": "/data/data_lake_bucket/address/",
            "dataset": "address",
        }
    )

    customer_to_data_lake = PythonOperator(
        task_id="customer_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/customer/processed_date={{ ds }}/Customer.csv",
            'sink_path': "/data/data_lake_bucket/customer/",
            'dataset': "customer",
        }
    )

    customer_address_to_data_lake = PythonOperator(
        task_id="customer_address_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/customer_address/processed_date={{ ds }}/CustomerAddress.csv",
            'sink_path': "/data/data_lake_bucket/customer_address/",
            'dataset': "customer_address",
        },
    )

    product_to_data_lake = PythonOperator(
        task_id="product_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/product/processed_date={{ ds }}/Product.csv",
            'sink_path': "/data/data_lake_bucket/product/",
            'dataset': "product",
        },
    )

    product_category_to_data_lake = PythonOperator(
        task_id="product_category_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/product_category/processed_date={{ ds }}/ProductCategory.csv",
            'sink_path': "/data/data_lake_bucket/product_category/",
            'dataset': "product_category",
        },
    )

    product_description_to_data_lake = PythonOperator(
        task_id="product_description_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/product_description/processed_date={{ ds }}/ProductDescription.csv",
            'sink_path': "/data/data_lake_bucket/product_description/",
            'dataset': "product_description",
        },
    )

    product_model_to_data_lake = PythonOperator(
        task_id="product_model_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/product_model/processed_date={{ ds }}/ProductModel.csv",
            'sink_path': "/data/data_lake_bucket/product_model/",
            'dataset': "product_model",
        },
    )

    product_model_product_description_to_data_lake = PythonOperator(
        task_id="product_model_product_description_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/product_model_product_description/processed_date={{ ds }}/ProductModelProductDescription.csv",
            'sink_path': "/data/data_lake_bucket/product_model_product_description/",
            'dataset': "product_model_product_description",
        },
    )

    sales_order_to_data_lake = PythonOperator(
        task_id="sales_order_to_data_lake",
        python_callable=to_lake,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/raw/sales_order/event_date={{ ds }}/SalesOrder.csv",
            'sink_path': "/data/data_lake_bucket/sales_order/",
            'dataset': "sales_order",
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

    address_to_ods = PythonOperator(
        task_id="address_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/address/processed_date={{ ds }}/",
            'dataset': 'address',
        },
    )

    customer_to_ods = PythonOperator(
        task_id="customer_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/customer/processed_date={{ ds }}/",
            'dataset': 'customer',
        },
    )

    customer_address_to_ods = PythonOperator(
        task_id="customer_address_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/customer_address/processed_date={{ ds }}/",
            'dataset': 'customer_address',
        },
    )

    product_to_ods = PythonOperator(
        task_id="product_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/product/processed_date={{ ds }}/",
            'dataset': 'customer_address',
        },
    )

    product_category_to_ods = PythonOperator(
        task_id="product_category_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/product_category/processed_date={{ ds }}/",
            'dataset': 'product_category',
        },
    )

    product_description_to_ods = PythonOperator(
        task_id="product_description_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/product_description/processed_date={{ ds }}/",
            'dataset': 'product_description',
        },
    )

    product_model_to_ods = PythonOperator(
        task_id="product_model_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/product_model/processed_date={{ ds }}/",
            'dataset': 'product_model',
        },
    )

    product_model_product_description_to_ods = PythonOperator(
        task_id="product_model_product_description_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/product_model_product_description/processed_date={{ ds }}/",
            'dataset': 'product_model_product_description',
        },
    )

    sales_order_to_ods = PythonOperator(
        task_id="sales_order_to_ods",
        python_callable=to_ods,
        provide_context=True,
        op_kwargs={
            'src_path': "/data/data_lake_bucket/sales_order/event_date={{ ds }}/",
            'dataset': 'sales_order',
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
        sales_order_to_ods,
    ]

    load_into_ods_completed = BashOperator(
        task_id="load_into_ods_completed",
        bash_command='echo data in lake on {{ ds }} has been loaded into ods',
    )

    daily_dag_start >> load_into_data_lake_tasks

    address_to_data_lake >> address_to_ods
    customer_to_data_lake >> customer_to_ods
    customer_address_to_data_lake >> customer_address_to_ods
    product_to_data_lake >> product_to_ods
    product_category_to_data_lake >> product_category_to_ods
    product_description_to_data_lake >> product_description_to_ods
    product_model_to_data_lake >> product_model_to_ods
    product_model_product_description_to_data_lake >> product_model_product_description_to_ods
    sales_order_to_data_lake >> sales_order_to_ods

    load_into_ods_tasks >> load_into_ods_completed
