from schema.address_schema import address_schema, address_rename_schema
from schema.customer_address_schema import customer_address_schema, customer_address_rename_schema
from schema.product_category_schema import product_category_schema, product_category_rename_schema
from schema.product_schema import product_schema, product_rename_schema
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
    },
    'customer_address': {
        'schema': customer_address_schema,
        'rename_schema': customer_address_rename_schema,
        'partition_field': 'processed_date'
    },
    'product': {
        'schema': product_schema,
        'rename_schema': product_rename_schema,
        'partition_field': 'processed_date'
    },
    'product_category': {
        'schema': product_category_schema,
        'rename_schema': product_category_rename_schema,
        'partition_field': 'processed_date'
    }
}
