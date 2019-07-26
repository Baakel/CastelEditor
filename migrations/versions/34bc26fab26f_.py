"""empty message

Revision ID: 34bc26fab26f
Revises: 13fdb8bb23b7
Create Date: 2019-06-25 16:06:38.875009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bc26fab26f'
down_revision = '13fdb8bb23b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bb_mechanisms', sa.Column('against_actor', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bb_mechanisms', 'against_actor')
    # ### end Alembic commands ###
