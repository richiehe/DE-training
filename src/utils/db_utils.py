from sqlalchemy import create_engine


def remove_ods_partition_data(df, dataset, partition_field):
    partition = ','.join(df.rdd.map(lambda x: f"'{str(x[partition_field])}'").distinct().collect())
    engine = create_engine('postgresql+psycopg2://dwh:dwh@localhost:5432/dwh')
    connection = engine.connect()
    print('partition: ', partition)
    query = f"DELETE FROM ods_{dataset} WHERE {partition_field} in ({partition})"
    print(query)
    connection.execute(query)


def remove_dw_partition_data(df, dataset, partition_field):
    partition = ','.join(df.rdd.map(lambda x: f"'{str(x[partition_field])}'").distinct().collect())
    engine = create_engine('postgresql+psycopg2://dwh:dwh@localhost:5432/dwh')
    connection = engine.connect()
    print('partition: ', partition)
    query = f"DELETE FROM dw_{dataset} WHERE {partition_field} in ({partition})"
    print(query)
    connection.execute(query)
