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
