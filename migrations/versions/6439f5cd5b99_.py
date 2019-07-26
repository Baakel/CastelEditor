"""empty message

Revision ID: 6439f5cd5b99
Revises: 8ead3ea6a9c8
Create Date: 2019-07-16 16:24:21.835253

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6439f5cd5b99'
down_revision = '8ead3ea6a9c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actor_details', sa.Column('role_id', sa.Integer(), nullable=True))
    op.drop_constraint('actor_details_ibfk_3', 'actor_details', type_='foreignkey')
    op.create_foreign_key(None, 'actor_details', 'actors', ['role_id'], ['id'])
    op.drop_column('actor_details', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actor_details', sa.Column('role', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'actor_details', type_='foreignkey')
    op.create_foreign_key('actor_details_ibfk_3', 'actor_details', 'actors', ['role'], ['id'])
    op.drop_column('actor_details', 'role_id')
    # ### end Alembic commands ###
