from pathlib import Path

from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

from schema.dataset_schema import DATASET_SCHEMA


def to_lake(dataset, src_path, sink_path):
    builder = SparkSession.builder.appName("dataset") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    dataset_df = spark.read.schema(DATASET_SCHEMA.get(dataset).get('schema')).csv(
        src_path,
        header=True
    )
    dataset_df.show()
    dataset_df.write.partitionBy(DATASET_SCHEMA.get(dataset).get('partition_field')) \
        .format("delta") \
        .mode("overwrite") \
        .save(sink_path)

    spark.stop()


if __name__ == '__main__':
    # to_lake(
    #     'sales_order',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/raw/sales_order',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/sales_order',
    # )

    # to_lake(
    #     'address',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/raw/address',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/address',
    # )

    # to_lake(
    #     'customer_address',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/raw/customer_address',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/customer_address',
    # )

    # to_lake(
    #     'product',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/raw/product',
    #     f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product',
    # )

    to_lake(
        'product_category',
        f'{Path.home()}/batch-data-pipeline-exercise/data/raw/product_category',
        f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/product_category',
    )
