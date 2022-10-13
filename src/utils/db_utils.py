from sqlalchemy import create_engine


def remove_partition_data(df, layer, dataset, partition_field):
    partition = ','.join(df.rdd.map(lambda x: f"'{str(x[partition_field])}'").distinct().collect())
    engine = create_engine('postgresql+psycopg2://dwh:dwh@localhost:5432/dwh')
    connection = engine.connect()
    print('partition: ', partition)
    query = f"DELETE FROM {layer}.{dataset} WHERE {partition_field} in ({partition})"
    print(query)
    connection.execute(query)
