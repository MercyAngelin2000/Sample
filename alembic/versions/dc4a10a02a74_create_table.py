"""create table

Revision ID: dc4a10a02a74
Revises: 
Create Date: 2022-09-16 18:01:05.749318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc4a10a02a74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post',sa.Column('id',sa.Integer(),nullable = False,primary_key=True))


def downgrade() -> None:
    op.drop_column("post","id")
