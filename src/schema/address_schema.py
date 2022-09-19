from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType

address_schema = StructType([
    StructField("AddressID", IntegerType(), True), StructField("AddressLine1", StringType(), True),
    StructField("AddressLine2", StringType(), True), StructField("City", StringType(), True),
    StructField("StateProvince", StringType(), True), StructField("CountryRegion", StringType(), True),
    StructField("PostalCode", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

address_rename_schema = {
    'AddressID': 'address_id',
    'AddressLine1': 'address_line1',
    'AddressLine2': 'address_line2',
    'City': 'city',
    'StateProvince': 'state_province',
    'CountryRegion': 'country_region',
    'PostalCode': 'postal_code',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
