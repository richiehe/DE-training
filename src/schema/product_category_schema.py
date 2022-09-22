from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

product_category_schema = StructType([
    StructField("ProductCategoryID", IntegerType(), True), StructField("ParentProductCategoryID", IntegerType(), True),
    StructField("Name", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

product_category_rename_schema = {
    'ProductCategoryID': 'product_category_id',
    'ParentProductCategoryID': 'parent_product_category_id',
    'Name': 'name',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
