from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, \
    DateType, BooleanType, FloatType, TimestampType
from pathlib import Path


SCHEMA = StructType(
    [StructField("SalesOrderID", IntegerType(), True), StructField("SalesOrderDetailID", IntegerType(), True),
     StructField("RevisionNumber", IntegerType(), True), StructField("OrderDate", DateType(), True),
     StructField("DueDate", DateType(), True), StructField("ShipDate", DateType(), True),
     StructField("Status", IntegerType(), True), StructField("OnlineOrderFlag", BooleanType(), True),
     StructField("SalesOrderNumber", StringType(), True), StructField("PurchaseOrderNumber", StringType(), True),
     StructField("AccountNumber", StringType(), True), StructField("CustomerID", IntegerType(), True),
     StructField("ShipToAddressID", IntegerType(), True), StructField("BillToAddressID", IntegerType(), True),
     StructField("ShipMethod", StringType(), True), StructField("CreditCardApprovalCode", StringType(), True),
     StructField("SubTotal", FloatType(), True), StructField("TaxAmt", FloatType(), True),
     StructField("Freight", FloatType(), True), StructField("TotalDue", FloatType(), True),
     StructField("Comment", StringType(), True), StructField("OrderQty", IntegerType(), True),
     StructField("ProductID", IntegerType(), True), StructField("UnitPrice", FloatType(), True),
     StructField("UnitPriceDiscount", FloatType(), True), StructField("LineTotal", FloatType(), True),
     StructField("rowguid", StringType(), True), StructField("ModifiedDate", TimestampType(), True)])

if __name__ == '__main__':
    builder = SparkSession.builder.appName("sales_order") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    sales_order = spark.read.schema(SCHEMA).csv(
        f'{Path.home()}/batch-data-pipeline-exercise/data/raw/sales_order.csv',
        header=True
    )
    sales_order = sales_order.withColumn('event_date', to_date('ModifiedDate'))
    sales_order.show()
    sales_order.write.partitionBy('event_date') \
        .format("delta") \
        .mode("overwrite") \
        .save(f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/sales-order')

    spark.stop()
