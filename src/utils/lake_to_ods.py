from pathlib import Path

from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession, DataFrame

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_partition_data


def to_ods(dataset, src_path):
    builder = SparkSession.builder.appName(dataset) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.jars", f'{Path.home()}/batch-data-pipeline-exercise/driver/postgresql-42.5.0.jar')

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    dataset_df: DataFrame = spark.read.format("delta").load(src_path)
    for old_name, new_name in DATASET_SCHEMA.get(dataset).get('rename_schema').items():
        dataset_df = dataset_df.withColumnRenamed(old_name, new_name)

    if dataset_df.count() > 0:
        remove_partition_data(dataset_df, 'ods', dataset, DATASET_SCHEMA.get(dataset).get('partition_field'))

    dataset_df.show()
    dataset_df.write \
        .mode("append") \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", f"ods.{dataset}") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .save()
    spark.stop()


if __name__ == '__main__':
    to_ods('sales_order', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/sales_order')
    # to_ods('address', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/address')
    # to_ods('customer_address', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/customer_address')
    # to_ods('product', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product')
    # to_ods('product_category', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product_category')
    # to_ods('product_description', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product_description')
    # to_ods('product_model', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product_model')
    # to_ods('product_model_product_description', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product_model_product_description')
    # to_ods('customer', f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/customer')
