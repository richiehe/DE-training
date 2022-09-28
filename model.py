from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, String
from sqlalchemy.dialects.postgresql import INTEGER, DATE, FLOAT, TEXT, TIMESTAMP

Base = declarative_base()
metadata = Base.metadata


class OdsSalesOrder(Base):
    __tablename__ = 'ods_sales_order'

    sales_order_id = Column(INTEGER)
    sales_order_detail_id = Column(INTEGER, primary_key=True)
    revision_number = Column(INTEGER)
    order_date = Column(DATE)
    due_date = Column(DATE)
    ship_date = Column(DATE)
    status = Column(INTEGER)
    online_order_flag = Column(Boolean)
    sales_order_number = Column(String)
    purchase_order_number = Column(String)
    account_number = Column(String)
    customer_id = Column(INTEGER)
    ship_to_address_id = Column(INTEGER)
    bill_to_address_id = Column(INTEGER)
    ship_method = Column(String)
    credit_card_approval_code = Column(String)
    sub_total = Column(FLOAT)
    tax_amt = Column(FLOAT)
    freight = Column(FLOAT)
    total_due = Column(FLOAT)
    comment = Column(TEXT)
    order_qty = Column(INTEGER)
    product_id = Column(INTEGER)
    unit_price = Column(FLOAT)
    unit_price_discount = Column(FLOAT)
    line_total = Column(FLOAT)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    event_date = Column(DATE)


class OdsAddress(Base):
    __tablename__ = 'ods_address'

    address_id = Column(INTEGER, primary_key=True)
    address_line1 = Column(String)
    address_line2 = Column(String)
    city = Column(String)
    state_province = Column(String)
    country_region = Column(String)
    postal_code = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsCustomrAddress(Base):
    __tablename__ = 'ods_customer_address'

    customer_id = Column(INTEGER, primary_key=True)
    address_id = Column(INTEGER, primary_key=True)
    address_type = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProduct(Base):
    __tablename__ = 'ods_product'

    product_id = Column(INTEGER, primary_key=True)
    name = Column(String)
    product_number = Column(String)
    color = Column(String)
    standard_cost = Column(FLOAT)
    list_price = Column(FLOAT)
    size = Column(String)
    weight = Column(FLOAT)
    product_category_id = Column(INTEGER)
    product_model_id = Column(INTEGER)
    sell_start_date = Column(TIMESTAMP)
    sell_end_date = Column(TIMESTAMP)
    discontinued_date = Column(TIMESTAMP)
    thumbnail_photo = Column(String)
    thumbnail_photo_file_name = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductCategory(Base):
    __tablename__ = 'ods_product_category'

    product_category_id = Column(INTEGER, primary_key=True)
    parent_product_category_id = Column(String)
    name = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductDescription(Base):
    __tablename__ = 'ods_product_description'

    product_description_id = Column(INTEGER, primary_key=True)
    description = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductModel(Base):
    __tablename__ = 'ods_product_model'

    product_model_id = Column(INTEGER, primary_key=True)
    name = Column(String)
    catalog_description = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductModelProductDescription(Base):
    __tablename__ = 'ods_product_model_product_description'

    product_model_id = Column(INTEGER, primary_key=True)
    product_description_id = Column(INTEGER, primary_key=True)
    culture = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsCustomer(Base):
    __tablename__ = 'ods_customer'

    customer_id = Column(INTEGER, primary_key=True)
    name_style = Column(Boolean)
    title = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    suffix = Column(String)
    company_name = Column(String)
    sales_person = Column(String)
    email_address = Column(String)
    phone = Column(String)
    password_hash = Column(String)
    password_salt = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class DWSalesOrder(Base):
    __tablename__ = 'dw_sales_order'

    sales_order_id = Column(INTEGER, primary_key=True)
    sales_order_detail_id = Column(INTEGER, primary_key=True)
    revision_number = Column(INTEGER)
    order_date = Column(DATE)
    due_date = Column(DATE)
    ship_date = Column(DATE)
    status = Column(INTEGER)
    online_order_flag = Column(Boolean)
    sales_order_number = Column(String)
    purchase_order_number = Column(String)
    account_number = Column(String)
    customer_id = Column(INTEGER)
    ship_to_address_id = Column(INTEGER)
    bill_to_address_id = Column(INTEGER)
    ship_method = Column(String)
    credit_card_approval_code = Column(String)
    sub_total = Column(FLOAT)
    tax_amt = Column(FLOAT)
    freight = Column(FLOAT)
    total_due = Column(FLOAT)
    comment = Column(TEXT)
    order_qty = Column(INTEGER)
    product_id = Column(INTEGER)
    unit_price = Column(FLOAT)
    unit_price_discount = Column(FLOAT)
    line_total = Column(FLOAT)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    event_date = Column(DATE)

