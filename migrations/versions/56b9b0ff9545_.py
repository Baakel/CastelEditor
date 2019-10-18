"""empty message

Revision ID: 56b9b0ff9545
Revises: 573d4df2a35f
Create Date: 2019-10-14 15:47:55.745768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b9b0ff9545'
down_revision = '573d4df2a35f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bb_mechanisms', sa.Column('extra_asset', sa.String(length=280), nullable=True))
    op.add_column('bb_mechanisms', sa.Column('extra_functional_requirement', sa.String(length=280), nullable=True))
    op.add_column('bb_mechanisms', sa.Column('extra_softgoal', sa.String(length=280), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bb_mechanisms', 'extra_softgoal')
    op.drop_column('bb_mechanisms', 'extra_functional_requirement')
    op.drop_column('bb_mechanisms', 'extra_asset')
    # ### end Alembic commands ###
