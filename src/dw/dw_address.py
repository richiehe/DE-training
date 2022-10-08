from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_dw_partition_data

if __name__ == '__main__':
    spark = SparkSession.builder.appName("dw_address") \
        .config("spark.jars", f'{Path.home()}/DE-training/driver/postgresql-42.5.0.jar') \
        .getOrCreate()

    df = spark.read.format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", "ods_address") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .load()

    df = df.filter(col('processed_date') == '2022-09-19') \
        .dropDuplicates(['address_id'])

    if df.count() > 0:
        remove_dw_partition_data(df, 'address', DATASET_SCHEMA.get('address').get('partition_field'))

    df = df.withColumn("is_valid", when(df.processed_date == '2022-09-19', True).otherwise(False))

    df.show()
    df.write \
        .mode("append") \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", "dw_address") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .save()
    spark.stop()
