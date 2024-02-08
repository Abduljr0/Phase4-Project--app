"""Foods

Revision ID: 094e5a0d70e3
Revises: dbe2fd49bddf
Create Date: 2024-02-08 23:43:50.810148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094e5a0d70e3'
down_revision = 'dbe2fd49bddf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('home_pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('price', sa.Float(precision=range(0, 30)), nullable=False))
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('home_pages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('price')
        batch_op.drop_column('category')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
