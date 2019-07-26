"""empty message

Revision ID: 692ee18830d4
Revises: deaf8d411863
Create Date: 2019-06-25 17:55:08.547383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '692ee18830d4'
down_revision = 'deaf8d411863'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aktoren',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aktoren')
    # ### end Alembic commands ###
