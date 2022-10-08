from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_dw_partition_data

if __name__ == '__main__':
    spark = SparkSession.builder.appName("dw_sales_order") \
        .config("spark.jars", f'{Path.home()}/Documents/DE-training/driver/postgresql-42.5.0.jar') \
        .getOrCreate()

    df = spark.read.format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", "ods_sales_order") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .load()

    df = df.filter(col('event_date') == '2008-06-01') \
        .dropDuplicates(['sales_order_id', 'sales_order_detail_id'])

    if df.count() > 0:
        remove_dw_partition_data(df, 'sales_order', DATASET_SCHEMA.get('sales_order').get('partition_field'))

    df.show()
    df.write \
        .mode("append") \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", "dw_sales_order") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .save()
    spark.stop()
