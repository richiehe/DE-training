from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType, BooleanType

customer_schema = StructType([
    StructField("CustomerID", IntegerType(), True), StructField("NameStyle", BooleanType(), True),
    StructField("Title", StringType(), True), StructField("FirstName", StringType(), True),
    StructField("MiddleName", StringType(), True), StructField("LastName", StringType(), True),
    StructField("Suffix", StringType(), True), StructField("CompanyName", StringType(), True),
    StructField("SalesPerson", StringType(), True), StructField("EmailAddress", StringType(), True),
    StructField("Phone", StringType(), True), StructField("PasswordHash", StringType(), True),
    StructField("PasswordSalt", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

customer_rename_schema = {
    'CustomerID': 'customer_id',
    'NameStyle': 'name_style',
    'Title': 'title',
    'FirstName': 'first_name',
    'MiddleName': 'middle_name',
    'LastName': 'last_name',
    'Suffix': 'suffix',
    'CompanyName': 'company_name',
    'SalesPerson': 'sales_person',
    'EmailAddress': 'email_address',
    'Phone': 'phone',
    'PasswordHash': 'password_hash',
    'PasswordSalt': 'password_salt',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
