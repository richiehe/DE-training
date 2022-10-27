from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, String
from sqlalchemy.dialects.postgresql import INTEGER, DATE, FLOAT, TEXT, TIMESTAMP

Base = declarative_base()
metadata = Base.metadata


class OdsSalesOrder(Base):
    __tablename__ = 'sales_order'
    __table_args__ = {"schema": "ods"}

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
    __tablename__ = 'address'
    __table_args__ = {"schema": "ods"}

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


class OdsCustomerAddress(Base):
    __tablename__ = 'customer_address'
    __table_args__ = {"schema": "ods"}

    customer_id = Column(INTEGER, primary_key=True)
    address_id = Column(INTEGER, primary_key=True)
    address_type = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProduct(Base):
    __tablename__ = 'product'
    __table_args__ = {"schema": "ods"}

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
    __tablename__ = 'product_category'
    __table_args__ = {"schema": "ods"}

    product_category_id = Column(INTEGER, primary_key=True)
    parent_product_category_id = Column(String)
    name = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductDescription(Base):
    __tablename__ = 'product_description'
    __table_args__ = {"schema": "ods"}

    product_description_id = Column(INTEGER, primary_key=True)
    description = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductModel(Base):
    __tablename__ = 'product_model'
    __table_args__ = {"schema": "ods"}

    product_model_id = Column(INTEGER, primary_key=True)
    name = Column(String)
    catalog_description = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsProductModelProductDescription(Base):
    __tablename__ = 'product_model_product_description'
    __table_args__ = {"schema": "ods"}

    product_model_id = Column(INTEGER, primary_key=True)
    product_description_id = Column(INTEGER, primary_key=True)
    culture = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)


class OdsCustomer(Base):
    __tablename__ = 'customer'
    __table_args__ = {"schema": "ods"}

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


class DwSalesOrder(Base):
    __tablename__ = 'sales_order'
    __table_args__ = {"schema": "dw"}

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


class DwProduct(Base):
    __tablename__ = 'product'
    __table_args__ = {"schema": "dw"}

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
    is_valid = Column(Boolean)


class DwCustomerAddress(Base):
    __tablename__ = 'customer_address'
    __table_args__ = {"schema": "dw"}

    customer_id = Column(INTEGER, primary_key=True)
    address_id = Column(INTEGER, primary_key=True)
    address_type = Column(String)
    row_guid = Column(String)
    modified_date = Column(TIMESTAMP)
    processed_date = Column(DATE)
    is_valid = Column(Boolean)


class DwCustomer(Base):
    __tablename__ = 'customer'
    __table_args__ = {"schema": "dw"}

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
    is_valid = Column(Boolean)


class DwAddress(Base):
    __tablename__ = 'address'
    __table_args__ = {"schema": "dw"}

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
    is_valid = Column(Boolean)


class DmMonthlyCitySalesSummary(Base):
    __tablename__ = 'monthly_city_sales_summary'
    __table_args__ = {"schema": "dm"}

    order_year = Column(String, primary_key=True)
    order_month = Column(String, primary_key=True)
    city = Column(String, primary_key=True)
    state_province = Column(String)
    country_region = Column(String)
    total_due = Column(FLOAT)
    profit = Column(FLOAT)
    due_growth_rate = Column(FLOAT)


class DmProductProfitWeeklyTop10(Base):
    __tablename__ = 'product_profit_weekly_top10'
    __table_args__ = {"schema": "dm"}

    order_year = Column(String, primary_key=True)
    order_week_of_year = Column(String, primary_key=True)
    product_id = Column(INTEGER, primary_key=True)
    product_name = Column(String)
    color = Column(String)
    standard_cost = Column(FLOAT)
    list_price = Column(FLOAT)
    rank = Column(INTEGER)


class DmShippedOrderDurationTop10(Base):
    __tablename__ = 'shipped_order_duration_top10'
    __table_args__ = {"schema": "dm"}

    sales_order_id = Column(INTEGER, primary_key=True)
    sales_order_number = Column(String)
    ship_to_city = Column(String)
    ship_to_province = Column(String)
    ship_to_country_region = Column(String)
    ship_to_postal_code = Column(String)
    order_date = Column(DATE)
    modified_date = Column(TIMESTAMP)
    duration = Column(INTEGER)
    rank = Column(INTEGER)
