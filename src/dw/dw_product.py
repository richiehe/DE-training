from pyspark.sql.functions import col, when

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_partition_data
from utils.spark_utils import init_spark_session, spark_read_from_db, spark_write_df_into_db

if __name__ == '__main__':
    source_dbtable = "ods_product"
    target_dbtable = "dw.dw_product"
    spark = init_spark_session(target_dbtable)

    df = spark_read_from_db(spark, source_dbtable, col('processed_date') == '2022-09-19')

    df = df.dropDuplicates(['product_id'])

    if df.count() > 0:
        remove_partition_data(df, 'dw', 'product', DATASET_SCHEMA.get('product').get('product'))

    df = df.withColumn("is_valid", when(df.processed_date == '2022-09-19', True).otherwise(False))

    df.show()

    spark_write_df_into_db(df, target_dbtable)

    spark.stop()
