"""empty message

Revision ID: 37d611b81f3
Revises: 2ef67e8aa5c
Create Date: 2014-03-26 07:57:51.875704

"""

# revision identifiers, used by Alembic.
revision = '37d611b81f3'
down_revision = '2ef67e8aa5c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'nick_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('user', 'phone',
               existing_type=sa.VARCHAR(length=13),
               nullable=False)
    op.alter_column('user', 'real_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'real_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'phone',
               existing_type=sa.VARCHAR(length=13),
               nullable=True)
    op.alter_column('user', 'nick_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    ### end Alembic commands ###
