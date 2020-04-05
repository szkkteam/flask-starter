"""Payment Order model updated

Revision ID: 98f50ac105ad
Revises: ec7dfa9ca712
Create Date: 2020-01-22 17:25:49.994736

"""
from alembic import op
import sqlalchemy as sa
import backend


# revision identifiers, used by Alembic.
revision = '98f50ac105ad'
down_revision = 'ec7dfa9ca712'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('download_cnt', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'download_cnt')
    # ### end Alembic commands ###