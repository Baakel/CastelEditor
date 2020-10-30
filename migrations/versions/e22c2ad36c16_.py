"""empty message

Revision ID: e22c2ad36c16
Revises: e0ce183e82b2
Create Date: 2020-10-08 12:32:33.972088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e22c2ad36c16'
down_revision = 'e0ce183e82b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assumptions', sa.Column('fundamental', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assumptions', 'fundamental')
    # ### end Alembic commands ###