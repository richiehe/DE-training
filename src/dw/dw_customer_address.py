from pyspark.sql.functions import col, when

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_partition_data
from utils.spark_utils import init_spark_session, spark_read_from_db, spark_write_df_into_db

if __name__ == '__main__':
    source_dbtable = "ods_customer_address"
    target_dbtable = "dw_customer_address"

    spark = init_spark_session(target_dbtable)

    df = spark_read_from_db(spark, source_dbtable, col('processed_date') == '2022-09-19')

    df = df.dropDuplicates(['customer_id', 'address_id'])

    if df.count() > 0:
        remove_partition_data(df, 'dw', 'customer_address', DATASET_SCHEMA.get('customer_address').get('partition_field'))

    df = df.withColumn("is_valid", when(df.processed_date == '2022-09-19', True).otherwise(False))

    df.show()

    spark_write_df_into_db(df, target_dbtable)

    spark.stop()
