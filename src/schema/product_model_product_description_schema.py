from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

product_model_product_description_schema = StructType([
    StructField("ProductModelID", IntegerType(), True), StructField("ProductDescriptionID", IntegerType(), True),
    StructField("Culture", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

product_model_product_description_rename_schema = {
    'ProductModelID': 'product_model_id',
    'ProductDescriptionID': 'product_description_id',
    'Culture': 'culture',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
