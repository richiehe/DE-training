from pyspark.sql.functions import col

from schema.dataset_schema import DATASET_SCHEMA
from utils.db_utils import remove_partition_data
from utils.spark_utils import init_spark_session, spark_read_from_db, spark_write_df_into_db

if __name__ == '__main__':
    source_dbtable = "ods.sales_order"
    target_dbtable = "dw.sales_order"

    spark = init_spark_session(target_dbtable)

    df = spark_read_from_db(spark, source_dbtable, col('event_date') == '2008-06-01')

    df = df.dropDuplicates(['sales_order_id', 'sales_order_detail_id'])

    if df.count() > 0:
        remove_partition_data(df, 'dw', 'sales_order', DATASET_SCHEMA.get('sales_order').get('partition_field'))

    df.show()

    spark_write_df_into_db(df, target_dbtable)

    spark.stop()
