"""create_first_tables

Revision ID: 2834c30cda4a
Revises: 
Create Date: 2021-07-22 14:53:19.222295

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '2834c30cda4a'
down_revision = None
branch_labels = None
depends_on = None


def create_customer_table() -> None:
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.Text, nullable=False),
        sa.Column('last_name', sa.Text, nullable=False),
        sa.Column('email', sa.Text, nullable=False),
        sa.Column('created', sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column('modified', sa.TIMESTAMP, server_default=sa.func.now(), server_onupdate=sa.func.utc_timestamp())
    )


def upgrade() -> None:
    create_customer_table()


def downgrade() -> None:
    op.drop_table("customers")
