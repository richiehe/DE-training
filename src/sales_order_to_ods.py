from pathlib import Path

from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession, DataFrame
from sqlalchemy import create_engine

COL_RENAME = {
    'SalesOrderID': 'sales_order_id',
    'SalesOrderDetailID': 'sales_order_detail_id',
    'RevisionNumber': 'revision_number',
    'OrderDate': 'order_date',
    'DueDate': 'due_date',
    'ShipDate': 'ship_date',
    'Status': 'status',
    'OnlineOrderFlag': 'online_order_flag',
    'SalesOrderNumber': 'sales_order_number',
    'PurchaseOrderNumber': 'purchase_order_number',
    'AccountNumber': 'account_number',
    'CustomerID': 'customer_id',
    'ShipToAddressID': 'ship_to_address_id',
    'BillToAddressID': 'bill_to_address_id',
    'ShipMethod': 'ship_method',
    'CreditCardApprovalCode': 'credit_card_approval_code',
    'SubTotal': 'sub_total',
    'TaxAmt': 'tax_amt',
    'Freight': 'freight',
    'TotalDue': 'total_due',
    'Comment': 'comment',
    'OrderQty': 'order_qty',
    'ProductID': 'product_id',
    'UnitPrice': 'unit_price',
    'UnitPriceDiscount': 'unit_price_discount',
    'LineTotal': 'line_total',
    'rowguid': 'row_guid',
    'ModifiedDate': 'modified_date',
    'date': 'date'
}


def remove_partition_data():
    event_date = ','.join(sales_order.rdd.map(lambda x: f"'{str(x.event_date)}'").distinct().collect())
    engine = create_engine('postgresql+psycopg2://dwh:dwh@localhost:5432/dwh')
    connection = engine.connect()
    my_query = f"DELETE FROM ods_sales_order WHERE event_date in ({event_date})"
    print(my_query)
    connection.execute(my_query)


if __name__ == '__main__':
    builder = SparkSession.builder.appName("sales_order") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.jars", f'{Path.home()}/batch-data-pipeline-exercise/driver/postgresql-42.5.0.jar')

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    sales_order: DataFrame = spark.read.format("delta").load(
        f'{Path.home()}/batch-data-pipeline-exercise/data/data_lake_bucket/sales-order'
    )
    for old_name, new_name in COL_RENAME.items():
        sales_order = sales_order.withColumnRenamed(old_name, new_name)

    remove_partition_data()

    sales_order.show()
    sales_order.write \
        .mode("append") \
        .format("jdbc") \
        .option("driver", "org.postgresql.Driver") \
        .option("url", "jdbc:postgresql://localhost:5432/dwh") \
        .option("dbtable", "ods_sales_order") \
        .option("user", "dwh") \
        .option("password", "dwh") \
        .save()
    spark.stop()
