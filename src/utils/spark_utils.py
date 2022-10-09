from pathlib import Path
from typing import Union

from pyspark.sql import SparkSession, Column, DataFrame


def init_spark_session(dataset: str) -> SparkSession:
    spark = SparkSession.builder.appName(dataset) \
        .config("spark.jars", f'{Path.home()}/Documents/DE-training/driver/postgresql-42.5.0.jar') \
        .getOrCreate()

    return spark


def spark_read_from_db(spark: SparkSession, dbtable_name: str, filter: Union[Column, str] = None) -> DataFrame:
    df = spark.read.format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", dbtable_name) \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .load()

    return df if filter is None else df.where(filter)


def spark_write_df_into_db(df: DataFrame, dbtable_name: str):
    df.write \
        .mode("append") \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", dbtable_name) \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .save()
