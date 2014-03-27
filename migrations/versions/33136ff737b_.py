"""empty message

Revision ID: 33136ff737b
Revises: 37d611b81f3
Create Date: 2014-03-26 07:59:28.258015

"""

# revision identifiers, used by Alembic.
revision = '33136ff737b'
down_revision = '37d611b81f3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    ### end Alembic commands ###