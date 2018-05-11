"""empty message

Revision ID: 0e665e24d572
Revises: c7dd39933503
Create Date: 2018-05-11 16:50:21.487458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e665e24d572'
down_revision = 'c7dd39933503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed_on')
    # ### end Alembic commands ###