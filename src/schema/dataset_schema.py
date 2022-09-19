from schema.address_schema import address_schema, address_rename_schema
from schema.sales_order_schema import sales_order_schema, sales_order_rename_schema

DATASET_SCHEMA = {
    'sales_order': {
        'schema': sales_order_schema,
        'rename_schema': sales_order_rename_schema,
        'partition_field': 'event_date'
    },
    'address': {
        'schema': address_schema,
        'rename_schema': address_rename_schema,
        'partition_field': 'processed_date'
    }
}
