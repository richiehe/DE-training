"""ods_product

Revision ID: 22e7204550f1
Revises: 849efaf4553c
Create Date: 2022-10-27 19:25:50.616236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '22e7204550f1'
down_revision = '849efaf4553c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('product_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('product_number', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('standard_cost', sa.FLOAT(), nullable=True),
    sa.Column('list_price', sa.FLOAT(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('weight', sa.FLOAT(), nullable=True),
    sa.Column('product_category_id', sa.INTEGER(), nullable=True),
    sa.Column('product_model_id', sa.INTEGER(), nullable=True),
    sa.Column('sell_start_date', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('sell_end_date', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('discontinued_date', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('thumbnail_photo', sa.String(), nullable=True),
    sa.Column('thumbnail_photo_file_name', sa.String(), nullable=True),
    sa.Column('row_guid', sa.String(), nullable=True),
    sa.Column('modified_date', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('processed_date', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('product_id'),
    schema='ods'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product', schema='ods')
    # ### end Alembic commands ###