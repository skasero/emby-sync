"""empty message

Revision ID: 9a11cbf67070
Revises: 8a9f881d8515
Create Date: 2021-01-18 14:53:17.935796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a11cbf67070'
down_revision = '8a9f881d8515'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('loading', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session', 'loading')
    # ### end Alembic commands ###