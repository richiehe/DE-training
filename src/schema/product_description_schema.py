from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

product_description_schema = StructType([
    StructField("ProductDescriptionID", IntegerType(), True), StructField("Description", StringType(), True),
    StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

product_description_rename_schema = {
    'ProductDescriptionID': 'product_description_id',
    'Description': 'description',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
