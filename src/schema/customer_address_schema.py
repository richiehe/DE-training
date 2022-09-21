from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

customer_address_schema = StructType([
    StructField("CustomerID", IntegerType(), True), StructField("AddressID", IntegerType(), True),
    StructField("AddressType", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

customer_address_rename_schema = {
    'CustomerID': 'customer_id',
    'AddressID': 'address_id',
    'AddressType': 'address_type',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
