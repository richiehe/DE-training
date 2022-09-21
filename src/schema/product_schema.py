from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, DateType, FloatType

product_schema = StructType([
    StructField("ProductID", IntegerType(), True), StructField("Name", StringType(), True),
    StructField("ProductNumber", StringType(), True), StructField("Color", StringType(), True),
    StructField("StandardCost", FloatType(), True), StructField("ListPrice", FloatType(), True),
    StructField("Size", StringType(), True), StructField("Weight", FloatType(), True),
    StructField("ProductCategoryID", IntegerType(), True), StructField("ProductModelID", IntegerType(), True),
    StructField("SellStartDate", TimestampType(), True), StructField("SellEndDate", TimestampType(), True),
    StructField("DiscontinuedDate", TimestampType(), True), StructField("ThumbNailPhoto", StringType(), True),
    StructField("ThumbnailPhotoFileName", StringType(), True), StructField("rowguid", StringType(), True),
    StructField("ModifiedDate", TimestampType(), True), StructField("processed_date", DateType(), True)
])

product_rename_schema = {
    'ProductID': 'product_id',
    'Name': 'name',
    'ProductNumber': 'product_number',
    'Color': 'color',
    'StandardCost': 'standard_cost',
    'ListPrice': 'list_price',
    'Size': 'size',
    'Weight': 'weight',
    'ProductCategoryID': 'product_category_id',
    'ProductModelID': 'product_model_id',
    'SellStartDate': 'sell_start_date',
    'SellEndDate': 'sell_end_date',
    'DiscontinuedDate': 'discontinued_date',
    'ThumbNailPhoto': 'thumbnail_photo',
    'ThumbnailPhotoFileName': 'thumbnail_photo_file_name',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'processed_date': 'processed_date'
}
