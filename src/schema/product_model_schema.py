from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

product_model_schema = StructType([
    StructField("ProductModelID", IntegerType(), True), StructField("Name", StringType(), True),
    StructField("CatalogDescription", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

product_model_rename_schema = {
    'ProductModelID': 'product_model_id',
    'Name': 'name',
    'CatalogDescription': 'catalog_description',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
